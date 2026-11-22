"""Structural regression tests; these do not run an agent behavioral harness."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_validator", ROOT / "scripts/validate.py")
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
VALID = "---\nname: testomancer\ndescription: Testing guidance\n---\n# Testing\nUse existing tests.\n"


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        # tempfile honors TMPDIR; explicit dir keeps host scratch policy visible.
        self.tmp = tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR"))
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.package = self.root / "testomancer"
        self.package.mkdir()
        self.skill = self.package / "SKILL.md"
        self.skill.write_text(VALID, encoding="utf-8")

    def write(self, text):
        self.skill.write_text(text, encoding="utf-8")

    def assert_invalid(self, fragment):
        errors = validator.validate(self.root)
        self.assertTrue(errors, "validator must not silently pass malformed input")
        self.assertIn(fragment, "\n".join(errors))

    def test_valid_minimal_fixture(self):
        self.assertEqual([], validator.validate(self.root))

    def test_actual_package(self):
        self.assertEqual([], validator.validate(ROOT))

    def test_empty_skill_is_not_success(self):
        self.write("")
        self.assert_invalid("frontmatter")
        self.write(VALID.split("# Testing")[0])
        self.assert_invalid("body")
        self.write(VALID.split("# Testing")[0] + "```\nexample\n```\n")
        self.assert_invalid("body")

    def test_missing_required_file_and_folder(self):
        self.skill.unlink()
        self.assert_invalid("missing required regular file")
        self.package.rmdir()
        self.assert_invalid("missing required directory")

    def test_missing_and_empty_metadata_fields(self):
        for change in ("name: testomancer\n", "description: Testing guidance\n"):
            with self.subTest(change=change):
                self.write(VALID.replace(change, ""))
                self.assert_invalid("required field")
        self.write(VALID.replace("Testing guidance", '""'))
        self.assert_invalid("required field")

    def test_unsupported_metadata_shapes(self):
        for field in ("tags: [testing]", "metadata: {}", "metadata:\n  score: 3",
                      "metadata:\n  nested:\n    value: nope", "metadata:",
                      "description: |\n  multiline", "description: >\n  multiline"):
            with self.subTest(field=field):
                base = VALID.replace("description: Testing guidance\n", "") if field.startswith("description:") else VALID
                self.write(base.replace("---\n# Testing", field + "\n---\n# Testing"))
                self.assertTrue(validator.validate(self.root))

    def test_optional_string_map_and_quoted_values(self):
        extra = ('license: MIT\ncompatibility: "Python 3.11+"\nallowed-tools: Read Bash\n'
                 'metadata:\n  version: "1.0"\n  author: \'It\'\'s us\'\n')
        self.write(VALID.replace("---\n# Testing", extra + "---\n# Testing"))
        self.assertEqual([], validator.validate(self.root))

    def test_duplicate_and_unknown_fields(self):
        for extra in ("name: testomancer", "unknown: value", "metadata:\n  a: one\n  a: two"):
            with self.subTest(extra=extra):
                self.write(VALID.replace("---\n# Testing", extra + "\n---\n# Testing"))
                self.assertTrue(validator.validate(self.root))

    def test_name_must_match_folder_and_format(self):
        for name in ("other-skill", "Testomancer", "bad--name", "x" * 65):
            with self.subTest(name=name):
                self.write(VALID.replace("name: testomancer", f"name: {name}"))
                self.assertTrue(validator.validate(self.root))

    def test_links_relative_to_source_and_encoded_spaces(self):
        refs = self.package / "references"
        refs.mkdir()
        (refs / "a b.md").write_text("[home](../SKILL.md#testing)\n", encoding="utf-8")
        self.write(VALID + "[guide](references/a%20b.md#section)\n[angle](<references/a b.md>)\n"
                   "[defined][ref]\n[ref]: references/a%20b.md 'Title'\n")
        self.assertEqual([], validator.validate(self.root))

    def test_broken_inline_image_and_reference_links(self):
        for link in ("[bad](missing.md)", "![image](missing.png)", "[ref]: missing.md"):
            with self.subTest(link=link):
                self.write(VALID + link)
                self.assert_invalid("broken local path")

    def test_reference_paths_in_backticks(self):
        self.write(VALID + "Read `references/missing.md`.\n")
        self.assert_invalid("broken local path")
        (self.package / "references").mkdir()
        (self.package / "references/guide.md").write_text("# Guide\n", encoding="utf-8")
        self.write(VALID + "Read `references/guide.md`.\n")
        self.assertEqual([], validator.validate(self.root))

    def test_external_anchors_fences_and_template_examples_ignored(self):
        self.write(VALID + "\n".join((
            "[web](https://example.invalid/missing)", "[mail](mailto:a@example.invalid)",
            "[anchor](#not-checked)", "[web](//example.invalid/x)",
            "```markdown", "[bad](missing.md)", "`references/missing.md`", "```",
            "~~~~", "[bad](missing.md)", "~~~", "~~~~", "    [bad](missing.md)",
            "`[bad](missing.md)`", "`references/<project>.md`", "`references/{name}.md`",
            "`tests/example_test.py`", "`unit_tests.md`")))
        self.assertEqual([], validator.validate(self.root))

    def test_path_traversal_and_absolute_paths(self):
        (self.root / "outside.md").write_text("exists", encoding="utf-8")
        for target in ("../outside.md", "%2e%2e/outside.md", "/etc/hosts", "references/../../outside.md"):
            with self.subTest(target=target):
                self.write(VALID + f"[bad]({target})")
                self.assertTrue(validator.validate(self.root))

    def test_symlink_file_directory_and_package_rejected(self):
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "file.md").write_text("# Outside", encoding="utf-8")
        for name, target in (("linked.md", outside / "file.md"), ("linked", outside)):
            with self.subTest(name=name):
                link = self.package / name
                link.symlink_to(target)
                self.assert_invalid("symlinks are not allowed")
                link.unlink()
        self.skill.unlink()
        self.package.rmdir()
        self.package.symlink_to(outside, target_is_directory=True)
        self.assert_invalid("symlinks are not allowed")

    def test_internal_and_dangling_symlinks_rejected(self):
        link = self.package / "linked.md"
        for target in (self.skill, self.package / "does-not-exist.md"):
            with self.subTest(target=target):
                link.symlink_to(target)
                self.assert_invalid("symlinks are not allowed")
                link.unlink()

    def test_every_packaged_markdown_file_is_checked(self):
        refs = self.package / "references"
        refs.mkdir()
        (refs / "unlinked.md").write_text("[bad](missing.md)", encoding="utf-8")
        self.assert_invalid("broken local path")

    def test_missing_delimiter_rejected(self):
        self.write("---\nname: testomancer\ndescription: Testing guidance\n")
        self.assert_invalid("missing closing")

    def test_encoded_absolute_and_backslash_paths_rejected(self):
        for target in ("%2Fetc%2Fhosts", "..%5Coutside.md", "bad%00.md"):
            with self.subTest(target=target):
                self.write(VALID + f"[bad]({target})")
                self.assert_invalid("absolute or invalid local path")

    def test_invalid_utf8_rejected(self):
        self.skill.write_bytes(b"\xff")
        self.assert_invalid("cannot read UTF-8")

    def test_cli_rejects_then_accepts_repaired_fixture(self):
        # An actual process failure before repair, not an assertion of an error mock.
        self.write(VALID + "[guide](references/missing.md)\n")
        command = [sys.executable, str(ROOT / "scripts/validate.py"), "--root", str(self.root)]
        before = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(1, before.returncode)
        self.assertIn("broken local path", before.stderr)
        (self.package / "references").mkdir()
        (self.package / "references/missing.md").write_text("# Guide\n", encoding="utf-8")
        after = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(0, after.returncode, after.stderr)
        self.assertIn("Validated testomancer", after.stdout)


class EvalFixtureTests(unittest.TestCase):
    def test_eight_manual_cases_have_required_fields(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        self.assertEqual(8, len(cases))
        self.assertEqual(8, len({case["id"] for case in cases}))
        for case in cases:
            with self.subTest(case=case["id"]):
                for field in ("prompt", "context", "expected", "forbidden"):
                    self.assertTrue(case[field])
                self.assertIsInstance(case["expected"], list)
                self.assertIsInstance(case["forbidden"], list)


if __name__ == "__main__":
    unittest.main()

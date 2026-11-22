# Structural validator

Run from the repository root (Python 3.10+, standard library only):

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

`--root PATH` selects a repository root containing the canonical `testomancer/`
folder, including for temporary test fixtures. Missing folders, missing or empty
`SKILL.md`, malformed metadata, and unresolved local paths fail with exit code 1.
Exit code 0 means structural validation only, not tested agent behavior.

## Supported frontmatter subset

This intentionally is **not a general YAML parser**. A UTF-8 `SKILL.md` starts with
an exact `---` line and ends frontmatter with another exact `---` line. Supported:

- Required nonempty string fields: `name`, `description`.
- Optional string fields: `license`, `compatibility`, `allowed-tools`.
- Optional `metadata:` followed by a nonempty flat map of two-space-indented
  alphanumeric/underscore/hyphen keys to string values. Numeric-looking versions
  must be quoted, for example `version: "1.0"`.
- Single-line plain strings, single-quoted strings with doubled apostrophes, or
  double-quoted strings using JSON escapes. Blank lines and full-line comments
  are accepted. Quote strings containing `: ` or ` #`.
- Unique keys only. `name` must match folder `testomancer`, be lowercase kebab-case,
  and at most 64 characters. Description max 1024; compatibility max 500.

Unsupported forms are rejected clearly: block/folded scalars, flow collections,
arrays, aliases, anchors, tags, nested mappings, inline comments, duplicate or
unknown top-level fields (including top-level `tags`). Put nonstandard string
annotations in `metadata`, not new top-level fields. Required metadata here means
`name` and `description`; the `metadata` map itself is optional. No arbitrary
reference-file inventory is hardcoded: `SKILL.md` is required and every explicit
local reference must exist. This permits a minimal self-contained skill.

## Paths and Markdown

The entire skill folder is inspected. Symlinks are rejected, including internal
ones and the package folder itself; directory links are never followed. Local
links must stay within the resolved package boundary. Absolute local paths,
backslashes, NULs, broken targets, and URL-encoded traversal escapes fail.

All UTF-8 `.md` files in the package are checked. Supported links are inline links
and images, link-reference definitions, angle-bracket destinations, URL-encoded
paths, and common single-level balanced parentheses in bare destinations.
Destinations are relative to the source Markdown file. URLs with a scheme,
protocol-relative URLs, and anchor-only links are ignored. Query/fragment suffixes
are removed before filesystem lookup; anchor existence is not checked. Definition
targets are checked even if unused; undefined reference labels are not checked.
Fenced backtick/tilde blocks and four-space/tab-indented code lines are ignored.
Inline code is not interpreted as Markdown links.

Additionally, backticked literal paths beginning `references/`, `scripts/`, or
`assets/` are resolved from the skill root. Only literal characters (letters,
digits, underscores, dots, slashes, hyphens, spaces) qualify: placeholder paths
like `references/<project>.md` and `references/{name}.md` are ignored. Bare
filenames or arbitrary example test paths are not inferred as package references.
Use actual Markdown links for paths outside these literal conventions.

This is a deliberately small Markdown subset, not CommonMark conformance. Complex
nested link labels/destinations, HTML links, blockquoted fences, dynamically
constructed paths, and runtime filesystem races are out of scope. The check is
not a security sandbox or a content/policy-quality evaluator. It imposes no
numeric test ratios or subjective prose/policy regex requirements.

## Test and evaluation boundaries

Tests use `TemporaryDirectory` under host `TMPDIR` when supplied. A CLI regression
actually runs a broken-link fixture (exit 1), repairs it, then runs the same CLI
(exit 0). Additional tests cover the actual package, minimal fixtures, metadata,
links, traversal, and symlink rejection. `evals/cases.json` is shape-checked only;
manual behavioral execution and evidence recording are described in
`evals/rubric.md`.

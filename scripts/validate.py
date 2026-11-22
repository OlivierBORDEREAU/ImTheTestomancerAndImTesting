#!/usr/bin/env python3
"""Validate the canonical skill without third-party dependencies.

See scripts/README.md for the intentionally constrained frontmatter/Markdown
subset. This is a structural package check, not a behavioral evaluation.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

FIELDS = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def scalar(value: str) -> str:
    """Read one explicit string, not arbitrary YAML."""
    value = value.strip()
    if not value:
        raise ValueError("expected a nonempty string scalar")
    if value.startswith('"'):
        try:
            result = json.loads(value)
        except ValueError as exc:
            raise ValueError("double-quoted strings must use JSON escapes") from exc
        if not isinstance(result, str):
            raise ValueError("expected a string")
        return result
    if value.startswith("'"):
        if not re.fullmatch(r"'(?:[^']|'')*'", value):
            raise ValueError("invalid single-quoted string")
        return value[1:-1].replace("''", "'")
    if (value[0] in "|>{[&*!%@`" or re.search(r"\s#|:\s", value)
            or value.lower() in {"true", "false", "null", "~"}
            or re.fullmatch(r"[-+]?\d+(?:\.\d+)?", value)):
        raise ValueError("unsupported YAML value; use a quoted string (see scripts/README.md)")
    return value


def frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with --- frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing closing --- frontmatter delimiter") from exc
    data: dict = {}
    in_metadata = False
    for number, line in enumerate(lines[1:end], 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  ") and not line.startswith("   ") and in_metadata:
            match = re.fullmatch(r"  ([A-Za-z0-9_-]+):\s*(.*)", line)
            if not match:
                raise ValueError(f"line {number}: metadata must be a flat string map")
            key, value = match.groups()
            if key in data["metadata"]:
                raise ValueError(f"line {number}: duplicate metadata key {key}")
            data["metadata"][key] = scalar(value)
            continue
        match = re.fullmatch(r"([a-z][a-z-]*):\s*(.*)", line)
        if not match:
            raise ValueError(f"line {number}: unsupported frontmatter syntax")
        key, value = match.groups()
        if key not in FIELDS:
            raise ValueError(f"line {number}: unsupported field {key}")
        if key in data:
            raise ValueError(f"line {number}: duplicate field {key}")
        in_metadata = key == "metadata"
        if in_metadata:
            if value:
                raise ValueError("metadata must be an indented flat string map")
            data[key] = {}
        else:
            data[key] = scalar(value)
    for key in ("name", "description"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"missing or empty required field: {key}")
    if "metadata" in data and not data["metadata"]:
        raise ValueError("metadata must contain at least one string entry")
    if len(data["name"]) > 64 or not NAME.fullmatch(data["name"]):
        raise ValueError("name must be lowercase kebab-case, at most 64 characters")
    if len(data["description"]) > 1024:
        raise ValueError("description exceeds 1024 characters")
    if "compatibility" in data and len(data["compatibility"]) > 500:
        raise ValueError("compatibility exceeds 500 characters")
    return data, "\n".join(lines[end + 1:])


def without_fences(text: str) -> str:
    result = []
    fence = None
    for line in text.splitlines():
        if fence:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(fence[1]) + r",}\s*", line):
                fence = None
            continue
        opening = re.match(r" {0,3}(`{3,}|~{3,})", line)
        if opening:
            mark = opening.group(1)
            fence = (mark[0], len(mark))
        elif not line.startswith(("    ", "\t")):
            result.append(line)
    return "\n".join(result)


def destinations(text: str):
    """Extract inline/definition links plus explicit package-root code paths."""
    text = without_fences(text)
    # Code spans are not Markdown links. Only explicit package folders count.
    for match in re.finditer(r"(`+)(.+?)\1", text):
        path = match.group(2)
        if re.fullmatch(r"(?:references|scripts|assets)/[A-Za-z0-9_./ -]+", path):
            yield path, True
    prose = re.sub(r"(`+)(.+?)\1", "", text)
    # Angle destinations permit spaces; bare destinations permit balanced parens.
    pattern = r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s()]*(?:\([^()]*\)[^\s()]*)*))"
    for match in re.finditer(pattern, prose):
        yield match.group(1) or match.group(2), False
    for match in re.finditer(r"^ {0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))", prose, re.M):
        yield match.group(1) or match.group(2), False


def validate(root: Path) -> list[str]:
    errors = []
    # Never resolve the root before checking its symlink identity.
    package = root.absolute() / "testomancer"
    if package.is_symlink():
        return ["testomancer: packaged artifact symlinks are not allowed"]
    if not package.is_dir():
        return ["missing required directory: testomancer"]
    boundary = package.resolve()
    files = []
    for directory, dirs, names in os.walk(package, followlinks=False):
        for name in dirs + names:
            path = Path(directory) / name
            if path.is_symlink():
                errors.append(f"{path.relative_to(package)}: packaged artifact symlinks are not allowed")
            elif path.is_file():
                files.append(path)
    skill = package / "SKILL.md"
    if not skill.is_file() or skill.is_symlink():
        errors.append("missing required regular file: testomancer/SKILL.md")
        return errors
    bodies = {}
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        try:
            bodies[path] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(package)}: cannot read UTF-8: {exc}")
    if skill in bodies:
        try:
            data, bodies[skill] = frontmatter(bodies[skill])
            if data["name"] != package.name:
                errors.append("SKILL.md: name must match containing folder testomancer")
            if not without_fences(bodies[skill]).strip():
                errors.append("SKILL.md: skill body must not be empty or code-only")
        except ValueError as exc:
            errors.append(f"SKILL.md: {exc}")
    for source, text in bodies.items():
        for target, package_relative in destinations(text):
            try:
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                decoded = unquote(url.path)
                if "\\" in decoded or "\x00" in decoded or decoded.startswith("/"):
                    raise ValueError("absolute or invalid local path")
                base = package if package_relative else source.parent
                resolved = (base / decoded).resolve()
                if not resolved.is_relative_to(boundary):
                    raise ValueError("local path escapes packaged skill")
                if not resolved.exists():
                    raise ValueError("broken local path")
            except (ValueError, OSError, RuntimeError) as exc:
                errors.append(f"{source.relative_to(package)}: {target!r}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository root containing testomancer/")
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1
    print("Validated testomancer: frontmatter, package paths, and local Markdown links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

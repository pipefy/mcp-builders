#!/usr/bin/env python3
"""Validate MCP Builders submissions.

Usage:
    python3 scripts/validate_submission.py                       # every submission
    python3 scripts/validate_submission.py submissions/ana/foo   # one submission

Exits 1 when a submission has an error, 0 otherwise. Warnings never fail the run.

The checks here are deliberately structural. Nothing verifies that an MCP tool
name is spelled correctly, because a submission from someone who does not write
code should not be blocked by a typo a reviewer can fix in a comment.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SUBMISSIONS_DIR = REPO_ROOT / "submissions"

REQUIRED_FILES = ("SKILL.md", "EVIDENCE.md")
REQUIRED_KEYS = ("name", "description", "tags")
REQUIRED_SECTIONS = (
    "When to use",
    "Prerequisites",
    "Tools needed",
    "Steps",
    "Success criteria",
    "Failure modes",
)

LINE_WARN_THRESHOLD = 500
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEADING_PATTERN = re.compile(r"^#{2,3}\s+(.+?)\s*$", re.MULTILINE)

PLACEHOLDER_HINTS = ("<", "your_", "your-", "xxx", "***", "...", "example", "placeholder")
SECRET_PATTERNS = (
    (re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\."), "looks like a JWT"),
    (re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{20,}", re.IGNORECASE), "looks like a bearer token"),
    (
        re.compile(
            r"(?i)\b(authorization|token|api[_-]?key|secret|password|client[_-]?secret)\b\s*[:=]\s*"
            r"[\"']?([^\s\"'<>]{12,})"
        ),
        "looks like a hardcoded credential",
    ),
)


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    """Return (keys, error). Values are raw strings; only presence is checked."""
    if not text.startswith("---"):
        return None, "the file does not start with a YAML frontmatter block (---)"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "the frontmatter block is never closed with ---"
    block = text[3:end]

    try:
        import yaml  # type: ignore[import-untyped]
    except ImportError:
        keys: dict[str, str] = {}
        for line in block.splitlines():
            match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
            if match:
                keys[match.group(1)] = match.group(2).strip()
        return keys, None

    try:
        loaded = yaml.safe_load(block)
    except yaml.YAMLError as exc:
        return None, f"the frontmatter is not valid YAML: {exc}"
    if not isinstance(loaded, dict):
        return None, "the frontmatter is not a set of key/value pairs"
    return {str(k): str(v) for k, v in loaded.items()}, None


def check(folder: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        relative = folder.resolve().relative_to(SUBMISSIONS_DIR)
    except ValueError:
        return ([f"{folder} is not inside submissions/"], warnings)

    parts = relative.parts
    if len(parts) != 2:
        errors.append(
            f"expected submissions/<github-handle>/<skill-name>/, got submissions/{relative}"
        )
        return errors, warnings
    handle, skill_name = parts

    if not NAME_PATTERN.match(handle):
        errors.append(f"'{handle}' must be your GitHub handle in lowercase kebab-case")
    if not NAME_PATTERN.match(skill_name):
        errors.append(f"'{skill_name}' must be lowercase kebab-case, for example invoice-approval-flow")

    for filename in REQUIRED_FILES:
        if not (folder / filename).is_file():
            errors.append(f"{filename} is missing")
    if errors:
        return errors, warnings

    skill_text = (folder / "SKILL.md").read_text(encoding="utf-8")

    keys, frontmatter_error = parse_frontmatter(skill_text)
    if frontmatter_error:
        errors.append(f"SKILL.md: {frontmatter_error}")
    else:
        assert keys is not None
        for key in REQUIRED_KEYS:
            if not keys.get(key):
                errors.append(f"SKILL.md: frontmatter is missing '{key}'")
        declared = keys.get("name", "")
        if declared and declared != skill_name:
            errors.append(
                f"SKILL.md: frontmatter name '{declared}' does not match the folder name '{skill_name}'"
            )

    headings = [h.strip().lower() for h in HEADING_PATTERN.findall(skill_text)]
    for section in REQUIRED_SECTIONS:
        if not any(h.startswith(section.lower()) for h in headings):
            errors.append(f"SKILL.md: the '{section}' section is missing")

    line_count = len(skill_text.splitlines())
    if line_count > LINE_WARN_THRESHOLD:
        warnings.append(
            f"SKILL.md is {line_count} lines. Over {LINE_WARN_THRESHOLD} is allowed, "
            "but a reviewer will ask whether it can be split."
        )

    for path in sorted(folder.rglob("*.md")):
        content = path.read_text(encoding="utf-8", errors="replace")
        for pattern, label in SECRET_PATTERNS:
            for match in pattern.finditer(content):
                snippet = match.group(0)
                if any(hint in snippet.lower() for hint in PLACEHOLDER_HINTS):
                    continue
                line_no = content[: match.start()].count("\n") + 1
                errors.append(
                    f"{path.relative_to(folder)}:{line_no}: {label}. "
                    "Replace it with a placeholder such as <token>."
                )

    return errors, warnings


def main(argv: list[str]) -> int:
    if argv:
        folders = [Path(arg) for arg in argv]
    elif SUBMISSIONS_DIR.is_dir():
        folders = sorted(p for p in SUBMISSIONS_DIR.glob("*/*") if p.is_dir())
    else:
        folders = []

    if not folders:
        print("No submissions to validate.")
        return 0

    failed = 0
    for folder in folders:
        errors, warnings = check(folder)
        label = folder.resolve().relative_to(REPO_ROOT)
        if errors:
            failed += 1
            print(f"FAIL {label}")
            for message in errors:
                print(f"     {message}")
        else:
            print(f"OK   {label}")
        for message in warnings:
            print(f"WARN {label}: {message}")

    print()
    print(f"{len(folders) - failed} passed, {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

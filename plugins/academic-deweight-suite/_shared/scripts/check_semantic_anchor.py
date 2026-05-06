#!/usr/bin/env python3
"""Validate Semantic Anchor and Integrity Snapshot shape.

This script checks fields and drift-sensitive metadata only. It does not judge
academic style or claim quality.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


SNAPSHOT_FIELDS = ["terms", "citations", "numbers", "equations", "labels"]
ANCHOR_FIELDS = [
    "section",
    "status",
    "writing_function",
    "core_claim",
    "evidence_or_basis",
    "information_focus",
    "reader_takeaway",
    "context_dependency",
    "immutable_tokens",
    "claim_polarity",
    "evidence_strength",
    "format_exempt_reason",
]
VALID_STATUS = {"normal", "format-exempt"}
VALID_POLARITY = {"positive", "negative", "mixed", "neutral", "not_applicable"}
VALID_STRENGTH = {"strong", "moderate", "weak", "descriptive", "not_applicable"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def field_value(block: str, field: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*(.*)$", block)
    if not match:
        return None
    return match.group(1).strip()


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_semantic_anchor.py <semantic-anchor.md>")

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")

    for field in SNAPSHOT_FIELDS:
        if field_value(text, field) in (None, ""):
            fail(f"missing Integrity Snapshot field: {field}")

    starts = list(re.finditer(r"(?m)^paragraph_id:\s*(P\d{3,})\s*$", text))
    if not starts:
        fail("missing paragraph_id blocks")

    seen: set[str] = set()
    for index, start in enumerate(starts):
        paragraph_id = start.group(1)
        if paragraph_id in seen:
            fail(f"duplicate paragraph_id: {paragraph_id}")
        seen.add(paragraph_id)

        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[start.start() : end]
        for field in ANCHOR_FIELDS:
            value = field_value(block, field)
            if value in (None, ""):
                fail(f"{paragraph_id}: missing field {field}")

        status = field_value(block, "status")
        if status not in VALID_STATUS:
            fail(f"{paragraph_id}: invalid status {status}")

        polarity = field_value(block, "claim_polarity")
        if polarity not in VALID_POLARITY:
            fail(f"{paragraph_id}: invalid claim_polarity {polarity}")

        strength = field_value(block, "evidence_strength")
        if strength not in VALID_STRENGTH:
            fail(f"{paragraph_id}: invalid evidence_strength {strength}")

        exempt_reason = field_value(block, "format_exempt_reason")
        if status == "format-exempt" and exempt_reason in {"", "none", "not_applicable"}:
            fail(f"{paragraph_id}: format-exempt requires format_exempt_reason")

    print(f"PASS: {path} ({len(seen)} paragraph anchors)")


if __name__ == "__main__":
    main()

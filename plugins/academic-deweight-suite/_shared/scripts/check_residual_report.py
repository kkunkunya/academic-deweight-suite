#!/usr/bin/env python3
"""Validate Residual AI Gate report fields and deterministic verdict rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "original_hit_modes",
    "remaining_hit_modes",
    "new_hit_modes",
    "max_remaining_severity",
    "max_new_severity",
    "semantic_anchor_match",
    "immutable_token_match",
    "claim_polarity_match",
    "evidence_strength_match",
    "verdict",
    "reason",
    "next_action",
]
MATCH_VALUES = {"pass", "fail", "uncertain"}
VERDICTS = {"pass", "revise", "blocked"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def field_value(block: str, field: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(field)}:\s*(.*)$", block)
    if not match:
        return None
    return match.group(1).strip()


def severity(block: str, field: str, paragraph_id: str) -> int:
    value = field_value(block, field)
    if value not in {"0", "1", "2", "3"}:
        fail(f"{paragraph_id}: invalid {field} {value}")
    return int(value)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_residual_report.py <residual-report.md>")

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    starts = list(re.finditer(r"(?m)^paragraph_id:\s*(P\d{3,})\s*$", text))
    if not starts:
        fail("missing paragraph_id blocks")

    for index, start in enumerate(starts):
        paragraph_id = start.group(1)
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[start.start() : end]

        for field in REQUIRED_FIELDS:
            value = field_value(block, field)
            if value in (None, ""):
                fail(f"{paragraph_id}: missing field {field}")

        for field in [
            "semantic_anchor_match",
            "immutable_token_match",
            "claim_polarity_match",
            "evidence_strength_match",
        ]:
            value = field_value(block, field)
            if value not in MATCH_VALUES:
                fail(f"{paragraph_id}: invalid {field} {value}")

        verdict = field_value(block, "verdict")
        if verdict not in VERDICTS:
            fail(f"{paragraph_id}: invalid verdict {verdict}")

        remaining = severity(block, "max_remaining_severity", paragraph_id)
        new = severity(block, "max_new_severity", paragraph_id)
        semantic = field_value(block, "semantic_anchor_match")
        tokens = field_value(block, "immutable_token_match")
        polarity = field_value(block, "claim_polarity_match")
        strength = field_value(block, "evidence_strength_match")

        if tokens in {"fail", "uncertain"} and verdict != "blocked":
            fail(f"{paragraph_id}: token drift requires blocked verdict")
        if semantic in {"fail", "uncertain"} and verdict != "blocked":
            fail(f"{paragraph_id}: semantic drift requires blocked verdict")
        if polarity == "fail" and verdict != "blocked":
            fail(f"{paragraph_id}: claim polarity drift requires blocked verdict")
        if strength == "fail" and verdict != "blocked":
            fail(f"{paragraph_id}: evidence strength drift requires blocked verdict")
        if verdict == "pass" and (remaining >= 2 or new >= 2):
            fail(f"{paragraph_id}: severity >=2 cannot pass")

    print(f"PASS: {path} ({len(starts)} residual rows)")


if __name__ == "__main__":
    main()

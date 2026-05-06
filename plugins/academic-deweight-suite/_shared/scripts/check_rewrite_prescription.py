#!/usr/bin/env python3
"""Validate anchor-bound rewrite prescription fields."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_TOP = [
    "paragraph_id",
    "semantic_anchor_ref",
    "writing_function",
    "hit_modes",
    "source_anchor_origin",
    "quote_exact",
    "source_locator",
    "source_decision",
    "observed_human_move",
    "why_this_quote_fits_user_paragraph",
    "transferable_structure",
    "non_transferable_surface",
    "adaptation_plan",
    "delete",
    "keep",
    "restructure_as",
    "evidence_boundary",
    "sentence_rhythm",
    "citation_number_policy",
    "verification_focus",
]
REQUIRED_CARD_FIELDS = ["a_code_cards", "function_cards", "paper_practice_cards"]
REQUIRED_EVIDENCE_FIELDS = [
    "quote_exact",
    "source_locator",
    "source_decision",
    "observed_human_move",
    "why_this_quote_fits_user_paragraph",
    "transferable_structure",
    "non_transferable_surface",
    "adaptation_plan",
]
REQUIRED_FORBIDDEN = {
    "no new fact",
    "no claim upgrade",
    "no citation or number drift",
    "no OCR/MinerU noise copying",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def field_value(block: str, field: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(field)}:\s*(.*)$", block)
    if not match:
        return None
    return match.group(1).strip()


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_rewrite_prescription.py <rewrite-prescription.md>")

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")

    starts = list(re.finditer(r"(?m)^paragraph_id:\s*(P\d{3,})\s*$", text))
    if not starts:
        fail("missing paragraph_id blocks")

    for index, start in enumerate(starts):
        paragraph_id = start.group(1)
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[start.start() : end]

        for field in REQUIRED_TOP:
            value = field_value(block, field)
            if value in (None, ""):
                fail(f"{paragraph_id}: missing field {field}")
        for field in REQUIRED_CARD_FIELDS:
            value = field_value(block, field)
            if value in (None, ""):
                fail(f"{paragraph_id}: missing human_anchor field {field}")
        for field in REQUIRED_EVIDENCE_FIELDS:
            value = field_value(block, field)
            if value in (None, ""):
                fail(f"{paragraph_id}: missing human_anchor_evidence field {field}")

        hit_modes = field_value(block, "hit_modes") or ""
        if not re.search(r"\bA(?:[1-9]|[1-3]\d)\b", hit_modes):
            fail(f"{paragraph_id}: hit_modes must contain A-codes")

        card_refs = " ".join(field_value(block, field) or "" for field in REQUIRED_CARD_FIELDS)
        if "human-writing-practice-cards" not in card_refs and "实践卡矩阵" not in card_refs and "实践卡" not in card_refs:
            fail(f"{paragraph_id}: no recognizable practice-card reference")

        source_decision = field_value(block, "source_decision") or ""
        if source_decision not in {"runtime_card", "curated_anchor", "keep"}:
            fail(f"{paragraph_id}: source_decision must be runtime_card, curated_anchor, or keep")

        quote_exact = field_value(block, "quote_exact") or ""
        if len(quote_exact) < 20:
            fail(f"{paragraph_id}: quote_exact too short to provide real source context")

        forbidden_items = {
            item.strip()
            for item in re.findall(r"(?m)^\s*-\s*(.+?)\s*$", block)
            if item.strip().startswith("no ")
        }
        missing_forbidden = REQUIRED_FORBIDDEN - forbidden_items
        if missing_forbidden:
            fail(f"{paragraph_id}: missing forbidden items: {', '.join(sorted(missing_forbidden))}")

    print(f"PASS: {path} ({len(starts)} prescription blocks)")


if __name__ == "__main__":
    main()

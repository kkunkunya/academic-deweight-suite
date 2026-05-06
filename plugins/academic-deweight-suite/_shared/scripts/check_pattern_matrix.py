#!/usr/bin/env python3
"""Validate Pattern Coverage Matrix shape and paragraph coverage."""

from __future__ import annotations

import re
import sys
from pathlib import Path


VALID_STATUS = {"clean", "suspect", "format-exempt"}
VALID_CONFIDENCE = {"high", "medium", "low", "uncertain"}
VALID_GROUP_STATUS = {"hit", "not_seen", "uncertain"}
REQUIRED_GROUPS = {
    "空话包装型",
    "机械对称型",
    "技术散文模板型",
    "论证过度闭合型",
    "教科书/贴源型",
    "作者性缺席型",
    "混写与新式精修型",
}
VALID_MOTHER = {"A30", "A33", "A35", "A37", "none", "uncertain"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def normalize(cell: str) -> str:
    return cell.strip().strip("`").strip()


def parse_tables(text: str) -> list[tuple[list[str], list[dict[str, str]]]]:
    lines = text.splitlines()
    tables: list[tuple[list[str], list[dict[str, str]]]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            headers = [normalize(part) for part in line.strip().strip("|").split("|")]
            rows: list[dict[str, str]] = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                parts = [normalize(part) for part in lines[i].strip().strip("|").split("|")]
                if len(parts) == len(headers):
                    rows.append(dict(zip(headers, parts)))
                i += 1
            tables.append((headers, rows))
        else:
            i += 1
    return tables


def find_table(tables: list[tuple[list[str], list[dict[str, str]]]], required: set[str]) -> list[dict[str, str]]:
    for headers, rows in tables:
        if required.issubset(set(headers)):
            return rows
    fail(f"missing table with columns: {', '.join(sorted(required))}")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_pattern_matrix.py <pattern-matrix.md>")

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    tables = parse_tables(text)

    paragraph_rows = find_table(
        tables,
        {"paragraph_id", "section", "status", "A_codes", "evidence_sentence", "reason", "severity", "confidence"},
    )
    seen: set[str] = set()
    for row in paragraph_rows:
        paragraph_id = row["paragraph_id"]
        if not re.fullmatch(r"P\d{3,}", paragraph_id):
            fail(f"invalid paragraph_id: {paragraph_id}")
        if paragraph_id in seen:
            fail(f"duplicate paragraph row: {paragraph_id}")
        seen.add(paragraph_id)

        status = row["status"]
        if status not in VALID_STATUS:
            fail(f"{paragraph_id}: invalid status {status}")
        if row["confidence"] not in VALID_CONFIDENCE:
            fail(f"{paragraph_id}: invalid confidence {row['confidence']}")
        if row["severity"] not in {"0", "1", "2", "3"}:
            fail(f"{paragraph_id}: invalid severity {row['severity']}")

        a_codes = row["A_codes"]
        evidence = row["evidence_sentence"]
        reason = row["reason"]
        if status == "suspect":
            if not re.search(r"\bA(?:[1-9]|[1-3]\d)\b", a_codes):
                fail(f"{paragraph_id}: suspect row missing A-code")
            if evidence in {"", "none"}:
                fail(f"{paragraph_id}: suspect row missing evidence_sentence")
        elif reason in {"", "none"}:
            fail(f"{paragraph_id}: {status} row missing reason")

    group_rows = find_table(tables, {"group", "A-codes", "status"})
    groups = {row["group"]: row["status"] for row in group_rows}
    missing_groups = REQUIRED_GROUPS - set(groups)
    if missing_groups:
        fail(f"missing diagnostic groups: {', '.join(sorted(missing_groups))}")
    for group, status in groups.items():
        if group in REQUIRED_GROUPS and status not in VALID_GROUP_STATUS:
            fail(f"{group}: invalid status {status}")

    mother_rows = find_table(tables, {"section", "paragraphs", "mother_skeleton", "why_this_skeleton", "counter_evidence", "targeted_rescan_needed"})
    for row in mother_rows:
        mother = row["mother_skeleton"]
        if mother not in VALID_MOTHER:
            fail(f"{row['section']}: invalid mother_skeleton {mother}")
        if mother == "uncertain" and row["targeted_rescan_needed"] != "yes":
            fail(f"{row['section']}: uncertain mother_skeleton requires targeted_rescan_needed=yes")

    print(f"PASS: {path} ({len(seen)} paragraph rows, {len(mother_rows)} section rows)")


if __name__ == "__main__":
    main()

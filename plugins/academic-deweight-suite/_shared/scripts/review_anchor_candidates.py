#!/usr/bin/env python3
"""Prepare and audit human review decisions for academic deweight anchors.

The script only performs deterministic checks: schema setup, pending-row sync,
candidate export, decision import, and mechanical noise flags. It does not
judge whether prose has human flavor.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


DECISIONS = {"pending", "keep", "reject", "needs_source_check", "negative_style_only"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def ensure_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS anchor_review_decisions (
          id INTEGER PRIMARY KEY,
          source_table TEXT NOT NULL,
          source_id INTEGER NOT NULL,
          source_slug TEXT NOT NULL,
          batch TEXT NOT NULL,
          decision TEXT NOT NULL DEFAULT 'pending',
          reviewer TEXT,
          reviewed_at TEXT,
          human_quality_notes TEXT NOT NULL DEFAULT '',
          reject_reasons TEXT NOT NULL DEFAULT '',
          flags TEXT NOT NULL DEFAULT '',
          UNIQUE(source_table, source_id)
        );
        CREATE INDEX IF NOT EXISTS idx_anchor_review_source
          ON anchor_review_decisions(source_table, source_id);
        CREATE INDEX IF NOT EXISTS idx_anchor_review_batch_decision
          ON anchor_review_decisions(batch, decision);
        """
    )


def batch_like(batch: str) -> str:
    return f"{batch}-%"


def iter_candidates(conn: sqlite3.Connection, batch: str) -> Iterable[sqlite3.Row]:
    queries = [
        (
            "pattern_examples",
            """
            SELECT 'pattern_examples' AS source_table, p.id AS source_id, d.slug AS source_slug,
                   p.pattern_code AS pattern_code, p.writing_function AS writing_function,
                   p.source_locator AS locator, p.quote AS quote, p.structure AS structure,
                   p.reuse_rule AS reuse_rule, p.boundary AS boundary
            FROM pattern_examples p
            JOIN source_documents d ON d.id = p.document_id
            WHERE d.slug LIKE ?
            """,
        ),
        (
            "practice_excerpts",
            """
            SELECT 'practice_excerpts' AS source_table, p.id AS source_id, d.slug AS source_slug,
                   p.anti_ai_modes AS pattern_code, p.writing_function AS writing_function,
                   p.source_locator AS locator, p.quote AS quote, p.structure AS structure,
                   p.reuse_rule AS reuse_rule, '' AS boundary
            FROM practice_excerpts p
            JOIN source_documents d ON d.id = p.document_id
            WHERE d.slug LIKE ?
            """,
        ),
        (
            "card_entries",
            """
            SELECT 'card_entries' AS source_table, c.id AS source_id, d.slug AS source_slug,
                   c.anti_ai_modes AS pattern_code, c.writing_function AS writing_function,
                   c.card_id AS locator, c.quote AS quote, c.structure AS structure,
                   c.reuse_rule AS reuse_rule, c.boundary AS boundary
            FROM card_entries c
            JOIN source_documents d ON d.id = c.document_id
            WHERE d.slug LIKE ?
            """,
        ),
    ]
    for _name, sql in queries:
        yield from conn.execute(sql, (batch_like(batch),))


def flag_quote(row: sqlite3.Row) -> list[str]:
    quote = " ".join(str(row["quote"] or "").split())
    locator = str(row["locator"] or "")
    flags: list[str] = []
    if len(quote) < 180:
        flags.append("too_short")
    if len(quote) > 1600:
        flags.append("too_long")
    if re.search(r"\blines (\d+)-\1\b", locator) and len(quote) > 700:
        flags.append("single_line_long_block")
    if len(re.findall(r"\[[0-9,\s]+\]|\([A-Z][A-Za-z-]+ et al\.,? \d{4}\)", quote)) >= 6:
        flags.append("reference_dense")
    if quote.count("|") >= 6 or quote.count("$") >= 6:
        flags.append("table_or_formula_noise")
    generic_cues = [
        "has attracted increasing attention",
        "has gained significant attention",
        "plays an important role",
        "in recent years",
        "comprehensive overview",
        "strengthen",
        "improve",
        "promote",
        "enhance",
        "加强",
        "完善",
        "推动",
        "强化",
        "具有重要意义",
        "近年来",
    ]
    cue_hits = [cue for cue in generic_cues if cue.lower() in quote.lower()]
    if len(cue_hits) >= 2:
        flags.append("generic_template_cues")
    return flags


def sync_pending(conn: sqlite3.Connection, batch: str) -> int:
    count = 0
    for row in iter_candidates(conn, batch):
        flags = ",".join(flag_quote(row))
        conn.execute(
            """
            INSERT INTO anchor_review_decisions
              (source_table, source_id, source_slug, batch, decision, flags)
            VALUES (?, ?, ?, ?, 'pending', ?)
            ON CONFLICT(source_table, source_id) DO UPDATE SET
              source_slug=excluded.source_slug,
              batch=excluded.batch,
              flags=excluded.flags
            """,
            (row["source_table"], row["source_id"], row["source_slug"], batch, flags),
        )
        count += 1
    conn.commit()
    return count


def export_jsonl(conn: sqlite3.Connection, batch: str, output: Path, limit: int) -> int:
    sql = """
    SELECT r.source_table, r.source_id, r.source_slug, r.batch, r.decision,
           r.flags, r.human_quality_notes, r.reject_reasons,
           COALESCE(p.pattern_code, pe.anti_ai_modes, c.anti_ai_modes, '') AS pattern_code,
           COALESCE(p.writing_function, pe.writing_function, c.writing_function, '') AS writing_function,
           COALESCE(p.source_locator, pe.source_locator, c.card_id, '') AS locator,
           COALESCE(p.quote, pe.quote, c.quote, '') AS quote,
           COALESCE(p.structure, pe.structure, c.structure, '') AS structure,
           COALESCE(p.reuse_rule, pe.reuse_rule, c.reuse_rule, '') AS reuse_rule
    FROM anchor_review_decisions r
    LEFT JOIN pattern_examples p ON r.source_table='pattern_examples' AND p.id=r.source_id
    LEFT JOIN practice_excerpts pe ON r.source_table='practice_excerpts' AND pe.id=r.source_id
    LEFT JOIN card_entries c ON r.source_table='card_entries' AND c.id=r.source_id
    WHERE r.batch=?
    ORDER BY r.decision, r.flags DESC, r.source_slug, r.source_table, r.source_id
    LIMIT ?
    """
    rows = conn.execute(sql, (batch, limit)).fetchall()
    with output.open("w", encoding="utf-8") as f:
        for row in rows:
            item = dict(row)
            item["quote_preview"] = " ".join(str(item.pop("quote") or "").split())[:500]
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    return len(rows)


def apply_decisions(conn: sqlite3.Connection, path: Path) -> int:
    changed = 0
    now = datetime.now(timezone.utc).isoformat()
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            decision = item.get("decision")
            if decision not in DECISIONS:
                fail(f"{path}:{line_no} invalid decision: {decision}")
            if "source_table" not in item or "source_id" not in item:
                fail(f"{path}:{line_no} missing source_table/source_id")
            conn.execute(
                """
                UPDATE anchor_review_decisions
                SET decision=?, reviewer=?, reviewed_at=?, human_quality_notes=?, reject_reasons=?
                WHERE source_table=? AND source_id=?
                """,
                (
                    decision,
                    item.get("reviewer", "curator"),
                    item.get("reviewed_at", now),
                    item.get("human_quality_notes", ""),
                    item.get("reject_reasons", ""),
                    item["source_table"],
                    item["source_id"],
                ),
            )
            changed += 1
    conn.commit()
    return changed


def print_summary(conn: sqlite3.Connection, batch: str) -> None:
    rows = conn.execute(
        """
        SELECT decision, COUNT(*) AS n
        FROM anchor_review_decisions
        WHERE batch=?
        GROUP BY decision
        ORDER BY decision
        """,
        (batch,),
    ).fetchall()
    flag_rows = conn.execute(
        """
        SELECT flags, COUNT(*) AS n
        FROM anchor_review_decisions
        WHERE batch=? AND flags <> ''
        GROUP BY flags
        ORDER BY n DESC, flags
        LIMIT 12
        """,
        (batch,),
    ).fetchall()
    print("REVIEW_SUMMARY")
    for row in rows:
        print(f"{row['decision']}|{row['n']}")
    print("FLAG_SUMMARY")
    for row in flag_rows:
        print(f"{row['flags']}|{row['n']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("db", type=Path)
    parser.add_argument("--batch", default="corpus-20260505")
    parser.add_argument("--sync-pending", action="store_true")
    parser.add_argument("--export", type=Path)
    parser.add_argument("--apply", dest="apply_path", type=Path)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--limit", type=int, default=500)
    args = parser.parse_args()

    if not args.db.exists():
        fail(f"missing database: {args.db}")
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    ensure_schema(conn)

    if args.sync_pending:
        print(f"SYNCED_PENDING={sync_pending(conn, args.batch)}")
    if args.apply_path:
        print(f"APPLIED_DECISIONS={apply_decisions(conn, args.apply_path)}")
    if args.export:
        print(f"EXPORTED={export_jsonl(conn, args.batch, args.export, args.limit)} path={args.export}")
    if args.summary:
        print_summary(conn, args.batch)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate the academic deweight anchor SQLite database."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


REQUIRED_TABLES = {
    "metadata",
    "source_documents",
    "source_sections",
    "source_segments",
    "pattern_examples",
    "practice_excerpts",
    "card_entries",
    "anchor_fts",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def count(conn: sqlite3.Connection, table: str, where: str = "", params: tuple[object, ...] = ()) -> int:
    suffix = f" WHERE {where}" if where else ""
    return int(conn.execute(f"SELECT COUNT(*) FROM {table}{suffix}", params).fetchone()[0])


def metadata_value(conn: sqlite3.Connection, key: str) -> str:
    row = conn.execute("SELECT value FROM metadata WHERE key=?", (key,)).fetchone()
    return str(row[0]) if row else ""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("db", type=Path)
    args = parser.parse_args()

    if not args.db.exists():
        fail(f"missing database: {args.db}")

    conn = sqlite3.connect(args.db)
    tables = {row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type IN ('table', 'virtual table')")}
    missing = REQUIRED_TABLES - tables
    if missing:
        fail("missing tables: " + ", ".join(sorted(missing)))

    public_safe = metadata_value(conn, "public_safe").lower() == "true"
    cards = count(conn, "card_entries")

    if public_safe:
        if cards < 20:
            fail(f"runtime card entry count too low: {cards}")
        local_paths = count(
            conn,
            "source_documents",
            "source_path LIKE '/Users/%' OR source_path LIKE '/Volumes/%'",
        )
        if local_paths:
            fail(f"portable DB contains local absolute source paths: {local_paths}")
        print(f"PASS: {args.db} tables={len(tables)} public_safe=true card_entries={cards}")
        return

    hu_docs = count(conn, "source_documents", "slug LIKE ?", ("%huyuxiao-phd%",))
    if hu_docs < 2:
        fail("expected Hu fulltext and curated anchor documents")

    hu_segments = count(
        conn,
        "source_segments",
        "document_id IN (SELECT id FROM source_documents WHERE slug = 'huyuxiao-phd-fulltext')",
    )
    if hu_segments < 100:
        fail(f"Hu fulltext segment count too low: {hu_segments}")

    a_patterns = count(
        conn,
        "pattern_examples",
        "document_id IN (SELECT id FROM source_documents WHERE slug = 'huyuxiao-phd-curated-anchor') AND pattern_code LIKE 'A%'",
    )
    if a_patterns < 39:
        fail(f"Hu A-code pattern count too low: {a_patterns}")

    excerpts = count(
        conn,
        "practice_excerpts",
        "document_id IN (SELECT id FROM source_documents WHERE slug = 'huyuxiao-phd-curated-anchor')",
    )
    if excerpts < 20:
        fail(f"Hu practice excerpt count too low: {excerpts}")

    if cards < 20:
        fail(f"runtime card entry count too low: {cards}")

    print(
        f"PASS: {args.db} tables={len(tables)} hu_docs={hu_docs} "
        f"hu_segments={hu_segments} hu_a_patterns={a_patterns} "
        f"hu_excerpts={excerpts} card_entries={cards}"
    )


if __name__ == "__main__":
    main()

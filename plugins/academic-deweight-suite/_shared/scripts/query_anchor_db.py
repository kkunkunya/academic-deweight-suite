#!/usr/bin/env python3
"""Query the academic deweight anchor SQLite database."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


def like(value: str) -> str:
    return f"%{value}%"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("db", type=Path)
    parser.add_argument("--source", default="", help="Filter by source slug fragment, e.g. huyuxiao-phd")
    parser.add_argument("--a-code", default="", help="Filter by A-code, e.g. A31")
    parser.add_argument("--writing-function", default="", help="Filter by writing function text")
    parser.add_argument("--q", default="", help="Full text search query")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    clauses = []
    params: list[object] = []

    if args.source:
        clauses.append("d.slug LIKE ?")
        params.append(like(args.source))
    if args.a_code:
        clauses.append("p.pattern_code LIKE ?")
        params.append(like(args.a_code))
    if args.writing_function:
        clauses.append("p.writing_function LIKE ?")
        params.append(like(args.writing_function))
    if args.q:
        clauses.append("(p.quote LIKE ? OR p.structure LIKE ? OR p.reuse_rule LIKE ?)")
        params.extend([like(args.q), like(args.q), like(args.q)])

    where = "WHERE " + " AND ".join(clauses) if clauses else ""
    pattern_rows = conn.execute(
        f"""
        SELECT
          d.slug,
          'pattern_examples' AS source_table,
          p.pattern_code,
          p.pattern_name,
          p.source_locator,
          p.quote,
          p.writing_function,
          p.reuse_rule,
          p.boundary
        FROM pattern_examples p
        JOIN source_documents d ON d.id = p.document_id
        {where}
        ORDER BY p.pattern_code, p.id
        LIMIT ?
        """,
        [*params, args.limit],
    ).fetchall()

    practice_rows = conn.execute(
        """
        SELECT
          d.slug,
          'practice_excerpts' AS source_table,
          '' AS pattern_code,
          'practice excerpt' AS pattern_name,
          p.source_locator,
          p.quote,
          p.writing_function,
          p.reuse_rule,
          '' AS boundary
        FROM practice_excerpts p
        JOIN source_documents d ON d.id = p.document_id
        WHERE (? = '' OR d.slug LIKE ?)
          AND (? = '' OR p.anti_ai_modes LIKE ?)
          AND (? = '' OR p.writing_function LIKE ?)
          AND (? = '' OR p.quote LIKE ? OR p.structure LIKE ? OR p.reuse_rule LIKE ?)
        ORDER BY p.id
        LIMIT ?
        """,
        [
            args.source,
            like(args.source),
            args.a_code,
            like(args.a_code),
            args.writing_function,
            like(args.writing_function),
            args.q,
            like(args.q),
            like(args.q),
            like(args.q),
            args.limit,
        ],
    ).fetchall()

    rows = [*pattern_rows, *practice_rows][: args.limit]

    if len(rows) < args.limit and (args.q or args.writing_function or args.a_code):
        card_rows = conn.execute(
            """
            SELECT
              d.slug,
              'card_entries' AS source_table,
              c.anti_ai_modes AS pattern_code,
              c.card_id AS pattern_name,
              c.discipline AS source_locator,
              c.quote,
              c.writing_function,
              c.reuse_rule,
              c.boundary
            FROM card_entries c
            JOIN source_documents d ON d.id = c.document_id
            WHERE (? = '' OR d.slug LIKE ?)
              AND (? = '' OR c.anti_ai_modes LIKE ?)
              AND (? = '' OR c.writing_function LIKE ?)
              AND (? = '' OR c.quote LIKE ? OR c.structure LIKE ? OR c.reuse_rule LIKE ?)
            LIMIT ?
            """,
            [
                args.source,
                like(args.source),
                args.a_code,
                like(args.a_code),
                args.writing_function,
                like(args.writing_function),
                args.q,
                like(args.q),
                like(args.q),
                like(args.q),
                args.limit,
            ],
        ).fetchall()
        rows = [*rows, *card_rows][: args.limit]

    for index, row in enumerate(rows, start=1):
        print(f"[{index}] {row['source_table']} {row['slug']} {row['pattern_code']} {row['pattern_name']} @ {row['source_locator']}")
        print(f"quote: {row['quote']}")
        print(f"function: {row['writing_function']}")
        print(f"reuse: {row['reuse_rule']}")
        print(f"boundary: {row['boundary']}")
        print()

    print(f"RESULT_COUNT={len(rows)}")


if __name__ == "__main__":
    main()

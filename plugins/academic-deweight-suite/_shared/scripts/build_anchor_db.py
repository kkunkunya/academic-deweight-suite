#!/usr/bin/env python3
"""Build the portable academic deweight anchor SQLite database."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_HU_FULL = None
DEFAULT_HU_ANCHOR = None
PLUGIN_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class Document:
    id: int
    slug: str
    path: Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def source_path_for_db(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PLUGIN_ROOT))
    except ValueError:
        return f"<LOCAL_SOURCE>/{path.name}"


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA foreign_keys = ON;

        DROP TABLE IF EXISTS metadata;
        DROP TABLE IF EXISTS source_documents;
        DROP TABLE IF EXISTS source_sections;
        DROP TABLE IF EXISTS source_segments;
        DROP TABLE IF EXISTS pattern_examples;
        DROP TABLE IF EXISTS practice_excerpts;
        DROP TABLE IF EXISTS card_entries;
        DROP TABLE IF EXISTS anchor_fts;

        CREATE TABLE metadata (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        );

        CREATE TABLE source_documents (
          id INTEGER PRIMARY KEY,
          slug TEXT NOT NULL UNIQUE,
          title TEXT NOT NULL,
          source_path TEXT NOT NULL,
          source_type TEXT NOT NULL,
          origin_kind TEXT NOT NULL,
          sha256 TEXT NOT NULL,
          line_count INTEGER NOT NULL,
          char_count INTEGER NOT NULL
        );

        CREATE TABLE source_sections (
          id INTEGER PRIMARY KEY,
          document_id INTEGER NOT NULL REFERENCES source_documents(id) ON DELETE CASCADE,
          level INTEGER NOT NULL,
          heading TEXT NOT NULL,
          start_line INTEGER NOT NULL,
          end_line INTEGER NOT NULL
        );

        CREATE TABLE source_segments (
          id INTEGER PRIMARY KEY,
          document_id INTEGER NOT NULL REFERENCES source_documents(id) ON DELETE CASCADE,
          section_id INTEGER REFERENCES source_sections(id) ON DELETE SET NULL,
          segment_no INTEGER NOT NULL,
          start_line INTEGER NOT NULL,
          end_line INTEGER NOT NULL,
          section_heading TEXT NOT NULL,
          text TEXT NOT NULL,
          segment_kind TEXT NOT NULL
        );

        CREATE TABLE pattern_examples (
          id INTEGER PRIMARY KEY,
          document_id INTEGER NOT NULL REFERENCES source_documents(id) ON DELETE CASCADE,
          pattern_code TEXT NOT NULL,
          pattern_name TEXT NOT NULL,
          source_locator TEXT NOT NULL,
          quote TEXT NOT NULL,
          writing_function TEXT NOT NULL,
          structure TEXT NOT NULL,
          reuse_rule TEXT NOT NULL,
          boundary TEXT NOT NULL,
          source_origin TEXT NOT NULL
        );

        CREATE TABLE practice_excerpts (
          id INTEGER PRIMARY KEY,
          document_id INTEGER NOT NULL REFERENCES source_documents(id) ON DELETE CASCADE,
          source_locator TEXT NOT NULL,
          quote TEXT NOT NULL,
          writing_function TEXT NOT NULL,
          structure TEXT NOT NULL,
          reuse_rule TEXT NOT NULL,
          anti_ai_modes TEXT NOT NULL
        );

        CREATE TABLE card_entries (
          id INTEGER PRIMARY KEY,
          document_id INTEGER NOT NULL REFERENCES source_documents(id) ON DELETE CASCADE,
          card_id TEXT NOT NULL,
          discipline TEXT NOT NULL,
          language TEXT NOT NULL,
          writing_function TEXT NOT NULL,
          quote TEXT NOT NULL,
          structure TEXT NOT NULL,
          reuse_rule TEXT NOT NULL,
          boundary TEXT NOT NULL,
          anti_ai_modes TEXT NOT NULL
        );

        CREATE VIRTUAL TABLE anchor_fts USING fts5(
          source_table,
          source_id UNINDEXED,
          source_slug UNINDEXED,
          pattern_code,
          writing_function,
          quote,
          structure,
          reuse_rule,
          boundary,
          content
        );

        CREATE INDEX idx_segments_document ON source_segments(document_id);
        CREATE INDEX idx_segments_section ON source_segments(section_heading);
        CREATE INDEX idx_pattern_code ON pattern_examples(pattern_code);
        CREATE INDEX idx_practice_function ON practice_excerpts(writing_function);
        CREATE INDEX idx_card_function ON card_entries(writing_function);
        """
    )


def insert_document(
    conn: sqlite3.Connection,
    slug: str,
    title: str,
    path: Path,
    source_type: str,
    origin_kind: str,
) -> Document:
    text = read_text(path)
    lines = text.splitlines()
    cur = conn.execute(
        """
        INSERT INTO source_documents
          (slug, title, source_path, source_type, origin_kind, sha256, line_count, char_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (slug, title, source_path_for_db(path), source_type, origin_kind, sha256_text(text), len(lines), len(text)),
    )
    return Document(id=int(cur.lastrowid), slug=slug, path=path)


def heading_level(line: str) -> int | None:
    match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
    if not match:
        return None
    return len(match.group(1))


def parse_sections(conn: sqlite3.Connection, doc: Document, text: str) -> list[dict[str, object]]:
    lines = text.splitlines()
    headings: list[dict[str, object]] = []
    for index, line in enumerate(lines, start=1):
        level = heading_level(line)
        if level is None:
            continue
        heading = re.sub(r"^#{1,6}\s+", "", line).strip()
        headings.append({"level": level, "heading": heading, "start_line": index, "end_line": len(lines), "id": None})
    for i, item in enumerate(headings):
        if i + 1 < len(headings):
            item["end_line"] = int(headings[i + 1]["start_line"]) - 1
        cur = conn.execute(
            """
            INSERT INTO source_sections (document_id, level, heading, start_line, end_line)
            VALUES (?, ?, ?, ?, ?)
            """,
            (doc.id, item["level"], item["heading"], item["start_line"], item["end_line"]),
        )
        item["id"] = int(cur.lastrowid)
    return headings


def section_for_line(sections: list[dict[str, object]], line_no: int) -> tuple[int | None, str]:
    current_id: int | None = None
    current_heading = ""
    for section in sections:
        if int(section["start_line"]) <= line_no <= int(section["end_line"]):
            current_id = int(section["id"])
            current_heading = str(section["heading"])
    return current_id, current_heading


def segment_kind(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("#"):
        return "heading"
    if "<table" in stripped.lower() or stripped.startswith("|"):
        return "table"
    if "$" in stripped and len(stripped) < 500:
        return "formula_like"
    if re.search(r"(学位申请人|指导教师|论文类型|KEY WORDS|TYPE OF DISSERTATION)", stripped):
        return "metadata"
    return "paragraph"


def insert_fulltext_segments(conn: sqlite3.Connection, doc: Document, text: str) -> int:
    sections = parse_sections(conn, doc, text)
    lines = text.splitlines()
    count = 0
    block: list[tuple[int, str]] = []

    def flush() -> None:
        nonlocal count, block
        if not block:
            return
        start = block[0][0]
        end = block[-1][0]
        raw = "\n".join(line for _, line in block).strip()
        if not raw:
            block = []
            return
        section_id, section_heading = section_for_line(sections, start)
        count += 1
        conn.execute(
            """
            INSERT INTO source_segments
              (document_id, section_id, segment_no, start_line, end_line, section_heading, text, segment_kind)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (doc.id, section_id, count, start, end, section_heading, raw, segment_kind(raw)),
        )
        block = []

    for index, line in enumerate(lines, start=1):
        if line.strip():
            block.append((index, line))
        else:
            flush()
    flush()
    return count


def parse_markdown_table(text: str, required_headers: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip().startswith("|") or i + 1 >= len(lines):
            i += 1
            continue
        if not re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            i += 1
            continue
        headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not set(required_headers).issubset(headers):
            i += 1
            continue
        i += 2
        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
            if len(cells) == len(headers):
                rows.append(dict(zip(headers, cells)))
            i += 1
    return rows


def insert_hu_curated_examples(conn: sqlite3.Connection, doc: Document, anchor_text: str) -> tuple[int, int]:
    pattern_rows = parse_markdown_table(anchor_text, ["模式", "真人写法锚点", "本文证据", "改写时怎么学"])
    pattern_count = 0
    for row in pattern_rows:
        mode = row["模式"]
        match = re.match(r"(A\d+)\s*(.*)", mode)
        if not match:
            continue
        code, name = match.group(1), match.group(2).strip()
        conn.execute(
            """
            INSERT INTO pattern_examples
              (document_id, pattern_code, pattern_name, source_locator, quote, writing_function, structure, reuse_rule, boundary, source_origin)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                doc.id,
                code,
                name or mode,
                row["本文证据"],
                row["真人写法锚点"],
                "A-code counterexample",
                row["真人写法锚点"],
                row["改写时怎么学"],
                "Use as structure/action only; do not copy source phrasing or MinerU noise.",
                str(doc.path),
            ),
        )
        pattern_count += 1

    excerpt_rows = parse_markdown_table(anchor_text, ["行号", "原文摘录", "适用场景", "实践要点"])
    excerpt_count = 0
    for row in excerpt_rows:
        conn.execute(
            """
            INSERT INTO practice_excerpts
              (document_id, source_locator, quote, writing_function, structure, reuse_rule, anti_ai_modes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                doc.id,
                row["行号"],
                row["原文摘录"].strip("“”\""),
                row["适用场景"],
                row["实践要点"],
                row["实践要点"],
                "",
            ),
        )
        excerpt_count += 1

    group_pattern = re.compile(
        r"###\s+3\.(\d+)\s+(.+?)\n\n- 对抗模式：(.+?)。\n- 本文锚点：(.+?)。\n- 写法原则：(.+?)(?=\n\n###|\n\n##)",
        re.S,
    )
    for match in group_pattern.finditer(anchor_text):
        group_name = match.group(2).strip()
        modes = match.group(3).strip()
        evidence = normalize_space(match.group(4))
        rule = normalize_space(match.group(5))
        conn.execute(
            """
            INSERT INTO pattern_examples
              (document_id, pattern_code, pattern_name, source_locator, quote, writing_function, structure, reuse_rule, boundary, source_origin)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                doc.id,
                f"GROUP:{match.group(1)}",
                group_name,
                modes,
                evidence,
                "seven diagnostic group counterexample",
                evidence,
                rule,
                "Use group rows for routing and retrieval, not as a paragraph-level verifier.",
                str(doc.path),
            ),
        )
        pattern_count += 1

    return pattern_count, excerpt_count


def parse_card_blocks(text: str) -> list[dict[str, str]]:
    fields = [
        "source",
        "location",
        "language",
        "writing_function",
        "quote",
        "structure",
        "anti_ai_modes",
        "reuse_rule",
        "boundary",
    ]
    lines = text.splitlines()
    blocks: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for line in lines:
        match = re.match(r"^\s*-?\s*([a-zA-Z_]+):\s*(.+?)\s*$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        if key == "source" and current:
            blocks.append(current)
            current = {}
        if key in fields:
            current[key] = value.strip("`")
    if current:
        blocks.append(current)
    return [block for block in blocks if "writing_function" in block or "quote" in block]


def insert_practice_cards(conn: sqlite3.Connection, cards_root: Path) -> int:
    if not cards_root.exists():
        return 0
    count = 0
    for path in sorted(cards_root.glob("*/*.md")):
        if path.name == "DOMAIN_SUMMARY.md":
            source_type = "domain_summary"
        else:
            source_type = "practice_card"
        title = path.stem
        doc = insert_document(conn, f"card-{path.parent.name}-{path.stem}", title, path, source_type, "runtime_plugin")
        if source_type != "practice_card":
            continue
        blocks = parse_card_blocks(read_text(path))
        for index, block in enumerate(blocks, start=1):
            conn.execute(
                """
                INSERT INTO card_entries
                  (document_id, card_id, discipline, language, writing_function, quote, structure, reuse_rule, boundary, anti_ai_modes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    doc.id,
                    f"{path.stem}-{index:03d}",
                    path.parent.name,
                    block.get("language", ""),
                    block.get("writing_function", ""),
                    block.get("quote", ""),
                    block.get("structure", ""),
                    block.get("reuse_rule", ""),
                    block.get("boundary", ""),
                    block.get("anti_ai_modes", ""),
                ),
            )
            count += 1
    return count


def rebuild_fts(conn: sqlite3.Connection) -> None:
    for table, columns in {
        "pattern_examples": "id, pattern_code, writing_function, quote, structure, reuse_rule, boundary",
        "practice_excerpts": "id, '' AS pattern_code, writing_function, quote, structure, reuse_rule, '' AS boundary",
        "card_entries": "id, anti_ai_modes AS pattern_code, writing_function, quote, structure, reuse_rule, boundary",
    }.items():
        for row in conn.execute(f"SELECT {columns} FROM {table}"):
            source_id, pattern_code, writing_function, quote, structure, reuse_rule, boundary = row
            source_slug = table
            content = " ".join(str(part) for part in row[1:] if part)
            conn.execute(
                """
                INSERT INTO anchor_fts
                  (source_table, source_id, source_slug, pattern_code, writing_function, quote, structure, reuse_rule, boundary, content)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (table, source_id, source_slug, pattern_code, writing_function, quote, structure, reuse_rule, boundary, content),
            )


def write_metadata(conn: sqlite3.Connection, items: dict[str, object]) -> None:
    for key, value in items.items():
        conn.execute(
            "INSERT INTO metadata (key, value) VALUES (?, ?)",
            (key, str(value)),
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cards-root", type=Path, default=Path(__file__).resolve().parents[1] / "references" / "human-writing-practice-cards")
    parser.add_argument("--hu-full", type=Path, default=DEFAULT_HU_FULL, help="Local full-text Markdown source; not shipped in this public repo.")
    parser.add_argument("--hu-anchor", type=Path, default=DEFAULT_HU_ANCHOR, help="Local curated anchor Markdown source; not shipped in this public repo.")
    parser.add_argument("--cards-only", action="store_true", help="Build a smaller DB from bundled runtime practice cards only.")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.out.exists():
        args.out.unlink()

    conn = sqlite3.connect(args.out)
    create_schema(conn)

    if args.cards_only:
        card_entries = insert_practice_cards(conn, args.cards_root)
        rebuild_fts(conn)
        write_metadata(
            conn,
            {
                "built_at": datetime.now(timezone.utc).isoformat(),
                "builder": Path(__file__).name,
                "cards_only": "true",
                "build_mode": "cards_only",
                "runtime_card_entries": card_entries,
                "source_policy": "Cards-only DB includes bundled practice-card entries only.",
            },
        )
        conn.commit()
        conn.close()
        print(f"PASS: built cards-only {args.out} with runtime_card_entries={card_entries}")
        return

    if args.hu_full is None or args.hu_anchor is None:
        raise SystemExit("--hu-full and --hu-anchor are required. Public package does not ship local corpus sources.")

    missing = [path for path in [args.hu_full, args.hu_anchor] if not path.exists()]
    if missing:
        raise SystemExit("missing required source: " + ", ".join(str(path) for path in missing))

    hu_full_doc = insert_document(
        conn,
        "huyuxiao-phd-fulltext",
        "胡钰骁博士论文全文",
        args.hu_full,
        "thesis_fulltext",
        "external_fulltext",
    )
    hu_segments = insert_fulltext_segments(conn, hu_full_doc, read_text(args.hu_full))

    hu_anchor_doc = insert_document(
        conn,
        "huyuxiao-phd-curated-anchor",
        "真实写作锚点：胡钰骁博士论文",
        args.hu_anchor,
        "curated_anchor_note",
        "legacy_local",
    )
    hu_patterns, hu_excerpts = insert_hu_curated_examples(conn, hu_anchor_doc, read_text(args.hu_anchor))

    card_entries = insert_practice_cards(conn, args.cards_root)
    rebuild_fts(conn)
    write_metadata(
        conn,
        {
            "built_at": datetime.now(timezone.utc).isoformat(),
            "builder": Path(__file__).name,
            "hu_full_segments": hu_segments,
            "hu_pattern_examples": hu_patterns,
            "hu_practice_excerpts": hu_excerpts,
            "runtime_card_entries": card_entries,
        },
    )
    conn.commit()
    conn.close()

    print(
        "PASS: built "
        f"{args.out} with hu_segments={hu_segments}, hu_pattern_examples={hu_patterns}, "
        f"hu_practice_excerpts={hu_excerpts}, runtime_card_entries={card_entries}"
    )


if __name__ == "__main__":
    main()

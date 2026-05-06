# Anchor Database Schema

The anchor database packages real academic writing references into a portable SQLite asset:

```text
_shared/assets/academic_deweight_anchors.sqlite
```

It is built by:

```text
_shared/scripts/build_anchor_db.py
```

The database is a retrieval layer. It does not judge prose quality, decide AIGC probability, or generate rewrites. It returns candidate anchors that still must pass:

```text
human-anchor-bind -> rewrite-prescription -> verify-gate
```

## Source Policy

The database stores both source provenance and extracted examples.

Current local build inputs:

- Runtime practice cards: `_shared/references/human-writing-practice-cards/`
- Optional user-provided thesis full text, passed to `build_anchor_db.py --hu-full`
- Optional user-provided curated anchor note, passed to `build_anchor_db.py --hu-anchor`
- Optional user-provided corpus batches kept outside Git

The source path is stored for traceability. The full text and curated examples are stored inside SQLite so the asset remains portable after build.

## Tables

### metadata

Key-value build metadata.

| column | type | rule |
|---|---|---|
| `key` | text primary key | metadata key |
| `value` | text | metadata value |

### source_documents

One row per source document or card file.

| column | type | rule |
|---|---|---|
| `id` | integer primary key | internal id |
| `slug` | text unique | stable identifier |
| `title` | text | human-readable title |
| `source_path` | text | original source path |
| `source_type` | text | `thesis_fulltext`, `curated_anchor_note`, `practice_card`, `practice_matrix`, `domain_summary` |
| `origin_kind` | text | `runtime_plugin`, `legacy_local`, or `external_fulltext` |
| `sha256` | text | source file checksum |
| `line_count` | integer | source lines |
| `char_count` | integer | source characters |

### source_sections

Markdown heading map for source documents.

| column | type | rule |
|---|---|---|
| `id` | integer primary key | internal id |
| `document_id` | integer | `source_documents.id` |
| `level` | integer | heading level |
| `heading` | text | heading text |
| `start_line` | integer | first line |
| `end_line` | integer | last line before next heading |

### source_segments

All non-empty full-text blocks. For Hu thesis, this stores the whole paper as retrievable paragraph-like segments.

| column | type | rule |
|---|---|---|
| `id` | integer primary key | internal id |
| `document_id` | integer | `source_documents.id` |
| `section_id` | integer | nullable section id |
| `segment_no` | integer | stable order in document |
| `start_line` | integer | source start line |
| `end_line` | integer | source end line |
| `section_heading` | text | nearest heading |
| `text` | text | original segment text |
| `segment_kind` | text | `heading`, `paragraph`, `table`, `formula_like`, `metadata` |

### pattern_examples

Curated examples keyed by A-code or diagnostic group.

| column | type | rule |
|---|---|---|
| `id` | integer primary key | internal id |
| `document_id` | integer | source document |
| `pattern_code` | text | `A1`-`A39` or `GROUP:*` |
| `pattern_name` | text | pattern label |
| `source_locator` | text | line number or section reference |
| `quote` | text | short source quote |
| `writing_function` | text | paragraph/function label |
| `structure` | text | transferable structure move |
| `reuse_rule` | text | how to imitate safely |
| `boundary` | text | when not to reuse |
| `source_origin` | text | source artifact used |

### practice_excerpts

Curated excerpts not necessarily tied to one A-code.

| column | type | rule |
|---|---|---|
| `id` | integer primary key | internal id |
| `document_id` | integer | source document |
| `source_locator` | text | line number, range, or section |
| `quote` | text | short source quote |
| `writing_function` | text | use case |
| `structure` | text | practice point |
| `reuse_rule` | text | transfer instruction |
| `anti_ai_modes` | text | comma-separated A-codes if known |

### card_entries

Parsed entries from runtime practice cards.

| column | type | rule |
|---|---|---|
| `id` | integer primary key | internal id |
| `document_id` | integer | card file id |
| `card_id` | text | file stem plus local index |
| `discipline` | text | parent folder |
| `language` | text | source language |
| `writing_function` | text | card function |
| `quote` | text | short quote |
| `structure` | text | structure move |
| `reuse_rule` | text | reuse rule |
| `boundary` | text | boundary |
| `anti_ai_modes` | text | A-code list text |

### anchor_fts

SQLite FTS5 table over searchable anchor text. Query scripts use this table first and fall back to `LIKE` if FTS5 is unavailable.

### anchor_review_decisions

Curator decisions for mechanically extracted corpus candidates. Scripts may create pending rows, but only a human curator may mark `keep`.

| column | type | rule |
|---|---|---|
| `id` | integer primary key | internal id |
| `source_table` | text | `pattern_examples`, `practice_excerpts`, or `card_entries` |
| `source_id` | integer | row id in `source_table` |
| `source_slug` | text | source document slug |
| `batch` | text | corpus batch, for example `corpus-20260505` |
| `decision` | text | `pending`, `keep`, `reject`, `needs_source_check`, or `negative_style_only` |
| `reviewer` | text | reviewer id or name |
| `reviewed_at` | text | ISO timestamp |
| `human_quality_notes` | text | why this is strong enough to keep |
| `reject_reasons` | text | why it was rejected or blocked |
| `flags` | text | deterministic script flags such as `too_long` or `generic_template_cues` |

### negative_candidate

Style-only counterexamples that must not be used as positive rewrite anchors.

| column | type | rule |
|---|---|---|
| `candidate_id` | text unique | stable candidate id |
| `batch` | text | corpus batch |
| `title` | text | source title |
| `observable_signals_json` | text | JSON array of style signals |
| `why_useful_as_negative_anchor` | text | counterexample use |
| `ai_judgement` | text | must remain `no, style-only` unless a real verifier artifact exists |

## Required Verifiers

```bash
python3 _shared/scripts/check_anchor_db.py _shared/assets/academic_deweight_anchors.sqlite
python3 _shared/scripts/query_anchor_db.py _shared/assets/academic_deweight_anchors.sqlite --source huyuxiao-phd --a-code A31 --limit 5
python3 _shared/scripts/review_anchor_candidates.py _shared/assets/academic_deweight_anchors.sqlite --sync-pending --batch corpus-20260505 --summary
```

# Real Example Index

This index separates real source material from schema-only templates.

## Available Real Practice-Card Library

Runtime cards are available under:

```text
plugins/academic-deweight-suite/_shared/references/human-writing-practice-cards/
```

Legacy source copy is available under:

```text
Local human-writing anchor library path is user-provided and not shipped in this public package.
```

Current library shape observed in this workspace:

- 28 paper practice cards across 6 discipline folders.
- 6 `DOMAIN_SUMMARY.md` files.
- Global A-code matrix: `00_A1-A39_实践卡矩阵.md`.
- Global writing-function matrix: `00_写作功能_实践卡矩阵.md`.
- Card entries use real-paper source/location/language/writing-function/quote/structure/anti-AI-mode/reuse/boundary fields.

Use these as human-writing references. Do not treat them as proof that a target rewrite passed verification.

## Portable SQL Asset

The portable SQLite asset is:

```text
plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

It is built from:

- runtime practice cards under `plugins/academic-deweight-suite/_shared/references/human-writing-practice-cards/`
- Hu Yuxiao thesis full text, if the user provides a local Markdown path
- the curated Hu Yuxiao anchor note, if the user provides a local Markdown path

Current verified DB contents:

- Hu thesis full text: 1303 stored segments.
- Hu curated pattern examples: 46 rows, including A1-A39 plus seven diagnostic groups.
- Hu curated practice excerpts: 40 rows.
- Runtime practice-card entries: 263 rows.

Rebuild and query:

```bash
python3 plugins/academic-deweight-suite/_shared/scripts/build_anchor_db.py --out plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
python3 plugins/academic-deweight-suite/_shared/scripts/check_anchor_db.py plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
python3 plugins/academic-deweight-suite/_shared/scripts/query_anchor_db.py plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite --source huyuxiao-phd --a-code A31 --limit 5
```

## Missing Complete Workflow Examples

The requested real workflow material path was checked:

```text
User-provided local deweighting workspace, not included in this public package.
```

It is not present in the current filesystem state. Therefore the suite must report:

```text
missing-real-workflow-example
```

when asked for a complete example containing original paragraph, Pattern Coverage Matrix, rewrite prescription, rewritten paragraph, and Residual AI Gate output.

The repository-local `knowledge/runs/` path is also absent in the current filesystem state.

## Schema-Only Templates

The following are schema fixtures, not real user cases:

- `templates/semantic-anchor-template.md`
- `templates/pattern-coverage-matrix-template.md`
- `templates/rewrite-prescription-template.md`
- `templates/residual-report-template.md`

Use them to validate field shape only.

## Future Retrieval Layer

A SQLite or DuckDB index is a good next layer for matching suspect paragraphs to practice cards. The first useful schema would index:

- `card_id`
- `source_path`
- `discipline`
- `language`
- `writing_function`
- `anti_ai_modes`
- `structure`
- `reuse_rule`
- `boundary`
- short quote text

The database should retrieve candidate cards; it must not decide prose quality or write rewrites by itself.

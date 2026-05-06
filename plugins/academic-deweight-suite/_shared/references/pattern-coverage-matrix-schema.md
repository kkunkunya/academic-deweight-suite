# Pattern Coverage Matrix Schema

Use this schema after `deweight-coverage-scan`. The matrix is a coverage artifact, not a rewrite plan.

## Paragraph Status Table

Required columns:

| column | rule |
|---|---|
| `paragraph_id` | stable `Pxxx`; appears exactly once |
| `section` | local section or chapter label |
| `status` | `clean`, `suspect`, or `format-exempt` |
| `A_codes` | comma-separated `A1`-`A39`; required for `suspect`, empty or `none` otherwise |
| `evidence_sentence` | exact short source span or phrase for `suspect` |
| `reason` | why clean, suspect, or exempt |
| `severity` | `0`, `1`, `2`, or `3` |
| `confidence` | `high`, `medium`, `low`, or `uncertain` |

Rules:

- Every paragraph in the input must have one row.
- `suspect` rows require at least one A-code and evidence.
- `clean` rows require a reason for no rewrite.
- `format-exempt` rows require a reason such as formula, table, reference list, metadata, pseudo-code, or figure caption.
- `uncertain` rows require targeted rescan or blocked return before rewrite.

## Pattern Coverage Matrix

Required columns:

| section | paragraphs | dominant_group | mother_skeleton | A-codes | count | density | confidence | examples |
|---|---|---|---|---|---:|---:|---|---|

Allowed `mother_skeleton` values:

```text
A30 | A33 | A35 | A37 | none | uncertain
```

## Seven Diagnostic Groups

Every report must include all seven groups and mark each one `hit`, `not_seen`, or `uncertain`.

| group | A-codes | status |
|---|---|---|
| 空话包装型 | A1-A6, A8-A10, A14 | hit/not_seen/uncertain |
| 机械对称型 | A7, A11-A13, A15-A18, A20-A23, A26, A29 | hit/not_seen/uncertain |
| 技术散文模板型 | A24-A27 | hit/not_seen/uncertain |
| 论证过度闭合型 | A19, A30, A32, A33 | hit/not_seen/uncertain |
| 教科书/贴源型 | A3, A31, A35 | hit/not_seen/uncertain |
| 作者性缺席型 | A16, A36 | hit/not_seen/uncertain |
| 混写与新式精修型 | A34, A37, A38, A39 | hit/not_seen/uncertain |

## Section Mother-Skeleton Table

Required columns:

| section | paragraphs | mother_skeleton | why_this_skeleton | counter_evidence | targeted_rescan_needed |
|---|---|---|---|---|---|

If `mother_skeleton` is `uncertain`, `targeted_rescan_needed` must be `yes`.

## Template

Use `templates/pattern-coverage-matrix-template.md` as a copyable blank/fixture.

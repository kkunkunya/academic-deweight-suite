# Pattern Coverage Matrix Template

## Paragraph Status Table

| paragraph_id | section | status | A_codes | evidence_sentence | reason | severity | confidence |
|---|---|---|---|---|---|---:|---|
| P001 | Method | suspect | A31,A36 | "This dimension provides a comprehensive framework" | textbook explanation and thin author choice | 2 | high |
| P002 | References | format-exempt | none | none | reference list | 0 | high |

## Pattern Coverage Matrix

| section | paragraphs | dominant_group | mother_skeleton | A-codes | count | density | confidence | examples |
|---|---|---|---|---|---:|---:|---|---|
| Method | P001 | 教科书/贴源型 | A35 | A31,A36 | 1 | 1.00 | high | P001 |
| References | P002 | none | none | none | 0 | 0.00 | high | P002 |

## Seven Diagnostic Groups

| group | A-codes | status |
|---|---|---|
| 空话包装型 | A1-A6, A8-A10, A14 | not_seen |
| 机械对称型 | A7, A11-A13, A15-A18, A20-A23, A26, A29 | not_seen |
| 技术散文模板型 | A24-A27 | not_seen |
| 论证过度闭合型 | A19, A30, A32, A33 | not_seen |
| 教科书/贴源型 | A3, A31, A35 | hit |
| 作者性缺席型 | A16, A36 | hit |
| 混写与新式精修型 | A34, A37, A38, A39 | not_seen |

## Section Mother-Skeleton Table

| section | paragraphs | mother_skeleton | why_this_skeleton | counter_evidence | targeted_rescan_needed |
|---|---|---|---|---|---|
| Method | P001 | A35 | The paragraph follows source explanation order more than author choice. | It still contains one local variable choice. | no |
| References | P002 | none | Exempt reference list. | none | no |

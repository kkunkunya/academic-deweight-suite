---
name: deweight-coverage-scan
description: 学术降重的全量 AI 模式扫描门。长文必须启用 subagent 并行隔离扫描，生成 Pattern Coverage Matrix，确保每段都有 clean/suspect/format-exempt 状态和 A-code 证据。触发关键词：长文扫描、模式门控、Pattern Coverage Matrix、A-code 扫描、反漏检、母骨架诊断、subagent 并行扫描。
---

# Deweight Coverage Scan

## Purpose

把“感觉像 AI”变成可定位、可统计、可复查的模式证据。识别阶段追求 recall：宁可多报 `uncertain`，不能漏扫。

## Runtime References

- Pattern catalog: `../../_shared/references/pattern-catalog.md`
- Long document protocol: `../../_shared/references/long-document-coverage-protocol.md`
- Pattern Coverage Matrix schema: `../../_shared/references/pattern-coverage-matrix-schema.md`
- Copyable template: `../../_shared/references/templates/pattern-coverage-matrix-template.md`
- Deterministic check: `../../_shared/scripts/check_pattern_matrix.py`

## Mandatory Subagent Policy

For long documents, chapter-level scans, or any input with 12+ paragraphs:

- Must use isolated subagents when the runtime supports subagents.
- Required roles:
  - `Local Scanner`
  - `Section Diagnostician`
  - `Global Aggregator`
  - `Anti-Miss Reviewer`
- If subagents are unavailable, return:

```text
blocked: needs_subagent_runtime
```

Do not silently run single-context long-document scanning unless the user explicitly permits serial fallback.

## Role Contracts

### Local Scanner

Input: 3-5 paragraphs plus one-paragraph overlap on both sides.

Output per paragraph:

```text
paragraph_id:
status: clean | suspect | format-exempt
A_codes:
evidence_sentence:
reason:
severity: 0 | 1 | 2 | 3
confidence: high | medium | low | uncertain
```

Local Scanner must not judge the whole document.

### Section Diagnostician

Input: section outline, local scanner outputs, representative paragraphs.

Required judgment:

```text
mother_skeleton: A30 | A33 | A35 | A37 | none | uncertain
why_this_skeleton:
counter_evidence:
minimal_surgery:
targeted_rescan_needed:
```

### Global Aggregator

Input: all local and section outputs.

Output:

- Pattern Coverage Matrix.
- seven-group coverage table.
- high-risk zones.
- missing paragraph list.

### Anti-Miss Reviewer

Input: matrix, high-risk zones, representative paragraphs.

Task:

- Do not rewrite.
- Do not summarize.
- Only challenge omissions, mislabels, and overconfidence.

## Pattern Coverage Matrix

Every scan must include:

```text
| section | paragraphs | dominant_group | mother_skeleton | A-codes | count | density | confidence | examples |
```

Rules:

- Every paragraph must be represented exactly once in final coverage.
- Each paragraph status must be `clean`, `suspect`, or `format-exempt`.
- Every `suspect` paragraph must have A-code evidence.
- Every `clean` paragraph must state why no rewrite is needed.
- All seven diagnostic groups must be marked `hit | not_seen | uncertain`.
- Every section must answer A30/A33/A35/A37 mother-skeleton status.
- `uncertain` requires targeted rescan or a blocked return.
- The final artifact must include the paragraph status table, seven-group table, and section mother-skeleton table defined in `pattern-coverage-matrix-schema.md`.

## Diagnostic Groups

- 空话包装型：A1-A6, A8-A10, A14
- 机械对称型：A7, A11-A13, A15-A18, A20-A23, A26, A29
- 技术散文模板型：A24-A27
- 论证过度闭合型：A19, A30, A32, A33
- 教科书/贴源型：A3, A31, A35
- 作者性缺席型：A16, A36
- 混写与新式精修型：A34, A37, A38, A39

## Failure Conditions

- Missing paragraph IDs.
- Missing overlap for local shards.
- Any paragraph omitted from final matrix.
- Any `suspect` without evidence sentence.
- Any section missing mother-skeleton judgment.
- Anti-Miss Reviewer finds unresolved omissions.

Before handoff to binding, the artifact should pass:

```bash
python3 ../../_shared/scripts/check_pattern_matrix.py <pattern-matrix.md>
```

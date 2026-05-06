---
name: deweight-intake-anchor
description: 学术降重的输入锚定门。用于生成 Integrity Snapshot 与 Semantic Anchor，锁定术语、引用、数字、公式、核心命题、段落功能和上下文依赖。触发关键词：文意锚定、Integrity Snapshot、Semantic Anchor、降重前锚定、不可变 token。
---

# Deweight Intake Anchor

## Purpose

在任何扫描或改写前，先锁定不可变事实和文意。后续步骤只能改“怎么说”，不能改“说什么”和“为什么说”。

## Runtime References

- Workflow contract: `../../_shared/references/deweight-workflow-contract.md`
- Semantic Anchor schema: `../../_shared/references/semantic-anchor-schema.md`
- Copyable template: `../../_shared/references/templates/semantic-anchor-template.md`
- Deterministic check: `../../_shared/scripts/check_semantic_anchor.py`

## Required Outputs

### Integrity Snapshot

Record all immutable tokens:

- terms and named methods.
- citations, citation keys, years, author names, page numbers.
- numbers, units, percentages, p values, sample sizes.
- equations, symbols, variable names, code identifiers, paths.
- table/figure labels.

### Semantic Anchor

For each paragraph:

```text
paragraph_id: P001
section:
status: normal | format-exempt
writing_function:
core_claim:
evidence_or_basis:
information_focus:
reader_takeaway:
context_dependency:
immutable_tokens:
claim_polarity:
evidence_strength:
format_exempt_reason:
```

## Gates

- No paragraph may enter scan/rewrite without a `Pxxx` ID.
- If citation truth or numeric meaning is uncertain, mark `blocked: needs_source_check`.
- If a paragraph is a formula table, pseudo-code block, reference list, or pure metadata, mark it `format-exempt` and explain why.

## Output Style

Return structured Markdown tables or YAML-like blocks. Do not rewrite text in this skill.

Before handing off to scan or rewrite, the artifact should pass:

```bash
python3 ../../_shared/scripts/check_semantic_anchor.py <semantic-anchor.md>
```

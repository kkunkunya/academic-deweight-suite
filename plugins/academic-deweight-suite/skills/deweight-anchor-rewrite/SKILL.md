---
name: deweight-anchor-rewrite
description: 学术降重的锚点约束改写门。只根据 Semantic Anchor、Pattern Coverage Matrix 和真人实践卡绑定处方改写 suspect 段；无绑定不改写。触发关键词：按锚点改写、处方式改写、anchor-bound rewrite、去 AI 改写、论文段落改写。
---

# Deweight Anchor Rewrite

## Purpose

改写目标是降低 AI 模式残留，不是润色成统一顺滑风格。所有改写必须追溯到：

```text
paragraph_id -> hit_modes -> practice_cards -> rewrite_recipe
```

## Required Inputs

- Original paragraph text.
- Semantic Anchor.
- Human Anchor Binding prescription.
- Rewrite Prescription following `../../_shared/references/rewrite-prescription-rubric.md`.
- Integrity Snapshot for immutable token restore.

## Hard Gate

If a suspect paragraph has no valid human-anchor binding, return:

```text
blocked: missing_human_anchor_binding
```

Do not rewrite.

If the binding has no `human_anchor_evidence.quote_exact`, return:

```text
blocked: missing_human_quote_evidence
```

## Rewrite Rules

- Preserve language of the input.
- Preserve claim polarity and evidence strength.
- Preserve citation keys, author/year mentions, numbers, units, formulas, table/figure labels.
- Change structure before vocabulary.
- Read `human_anchor_evidence.quote_exact` before rewriting; imitate the quoted author's writing move, not the surface wording.
- Use `observed_human_move`, `transferable_structure`, and `adaptation_plan` as the concrete operation.
- Do not copy `quote_exact` wording, examples, entities, data, or topic-specific phrasing into the user's rewrite.
- Do not copy OCR/MinerU noise from practice cards.
- Do not add first-person experience, new examples, new data, or fabricated sources.
- Do not use SQL/database retrieval results as authority by themselves; retrieved cards are candidates and still need real practice-card binding.

## Output Contract

For each changed paragraph:

```text
paragraph_id:
before_modes:
practice_cards_used:
human_quote_used:
human_move_transferred:
rewrite_recipe_applied:
rewritten_text:
integrity_notes:
```

If `report=rewrite_only`, output only the final rewritten text after verification.

The rewrite prescription consumed by this skill should pass:

```bash
python3 ../../_shared/scripts/check_rewrite_prescription.py <rewrite-prescription.md>
```

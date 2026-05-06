---
name: deweight-human-anchor-bind
description: 学术降重的真人写作实践绑定门。用于把每个 suspect 段落绑定到 A-code、写作功能和具体真人实践卡，生成可执行改写处方。触发关键词：真人写法锚点、实践卡绑定、anchor binding、rewrite prescription、A-code 锚点。
---

# Deweight Human Anchor Bind

## Purpose

防止模型从零凭感觉改写。每个待改段落必须先绑定真人写作实践卡。

## Runtime Sources

- A-code matrix: `../../_shared/references/human-writing-practice-cards/00_A1-A39_实践卡矩阵.md`
- Function matrix: `../../_shared/references/human-writing-practice-cards/00_写作功能_实践卡矩阵.md`
- Paper practice cards: `../../_shared/references/human-writing-practice-cards/*/*.md`
- Rewrite prescription rubric: `../../_shared/references/rewrite-prescription-rubric.md`
- Real example index: `../../_shared/references/real-example-index.md`
- Anchor DB schema: `../../_shared/references/anchor-db-schema.md`
- Anchor curation review gate: `../../_shared/references/anchor-curation-review-gate.md`
- Portable anchor DB: `../../_shared/assets/academic_deweight_anchors.sqlite`
- Anchor DB query script: `../../_shared/scripts/query_anchor_db.py`
- Anchor review helper: `../../_shared/scripts/review_anchor_candidates.py`
- Copyable template: `../../_shared/references/templates/rewrite-prescription-template.md`
- Deterministic check: `../../_shared/scripts/check_rewrite_prescription.py`

## Required Input

- Semantic Anchor from `deweight-intake-anchor`.
- Pattern Coverage Matrix from `deweight-coverage-scan`.
- Original paragraph text for suspect paragraphs only.

## Binding Contract

For each suspect paragraph:

```text
paragraph_id:
semantic_anchor:
writing_function:
hit_modes:
human_anchor:
  a_code_cards:
  function_cards:
  paper_practice_cards:
  source_anchor_origin:
human_anchor_evidence:
  quote_exact:
  source_locator:
  source_decision:
  observed_human_move:
  why_this_quote_fits_user_paragraph:
  transferable_structure:
  non_transferable_surface:
  adaptation_plan:
rewrite_operation:
  delete:
  keep:
  restructure_as:
  evidence_boundary:
  sentence_rhythm:
  citation_number_policy:
forbidden:
  - no new fact
  - no claim upgrade
  - no citation or number drift
  - no OCR/MinerU noise copying
verification_focus:
```

## Practice Card Requirements

A valid practice card must include:

- `source`
- `location`
- `language`
- `writing_function`
- `quote` or `quote_short`
- `structure` or `structure_skeleton`
- `anti_ai_modes`
- `reuse_rule` or `rewrite_recipe`
- `boundary`

Runtime cards currently use the real-paper card fields documented in `real-example-index.md`; do not require nonexistent fields if an equivalent field is present.

## Corpus Review Gate

Portable DB entries with `source_slug` beginning `corpus-` are mechanically extracted candidates until a curator reviews them. Before binding one of these entries as `human_anchor`, check `anchor-curation-review-gate.md` and require an `anchor_review_decisions` row with:

```text
decision: keep
```

If the candidate is unreviewed, pending, rejected, or marked `needs_source_check`, return:

```text
blocked: unreviewed_human_anchor
paragraph_id:
candidate_anchor:
required_action: curator review must mark decision=keep before rewrite binding
```

`negative_candidate` rows are counterexamples only. They preserve `ai_judgement="no, style-only"` and must never be used as positive practice cards.

## Human Quote Evidence Gate

Binding must put the real human source wording into the prescription context. Do not bind from an abstract label alone.

For every bound suspect paragraph, include:

- `quote_exact`: the original human source excerpt that the model should read before rewriting.
- `source_locator`: file/card/DB locator for the quote.
- `source_decision`: `runtime_card`, `curated_anchor`, or `keep` for reviewed corpus anchors.
- `observed_human_move`: what the quoted author actually does in the paragraph.
- `why_this_quote_fits_user_paragraph`: why the user's paragraph has the same writing problem.
- `transferable_structure`: the writing move to imitate.
- `non_transferable_surface`: words, entities, data, examples, and topic-specific phrasing that must not be copied.
- `adaptation_plan`: how to move from the user's facts to a rewritten paragraph.

This is not optional analysis. It is the context bridge that prevents "A-code template rewriting". If no real quote can be shown, return:

```text
blocked: missing_human_quote_evidence
paragraph_id:
needed_quote:
```

If no suitable card exists, return:

```text
blocked: missing_human_anchor
paragraph_id:
needed_anchor:
```

Do not invent a card during rewrite.

Before handoff to rewrite, the prescription should pass:

```bash
python3 ../../_shared/scripts/check_rewrite_prescription.py <rewrite-prescription.md>
```

For newly ingested corpus batches, initialize review rows before using candidates:

```bash
python3 ../../_shared/scripts/review_anchor_candidates.py ../../_shared/assets/academic_deweight_anchors.sqlite --sync-pending --batch corpus-20260505 --summary
```

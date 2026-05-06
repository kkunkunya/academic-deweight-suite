# Rewrite Prescription Rubric

The rewrite prescription is produced by `deweight-human-anchor-bind` and consumed by `deweight-anchor-rewrite`. It turns human practice-card evidence into an operation plan without copying the card.

## Required Fields

```text
paragraph_id:
semantic_anchor_ref:
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

## Binding Rules

- `hit_modes` must cite A-codes from the coverage matrix.
- `paper_practice_cards` must point to existing real cards under `human-writing-practice-cards/`.
- `source_anchor_origin` must say whether the card is from `_shared` runtime cards or legacy source material.
- `human_anchor_evidence.quote_exact` must contain the real human source wording used as rewrite context.
- `source_decision` must be `runtime_card`, `curated_anchor`, or `keep`; corpus rows require `keep`.
- If no suitable card exists, return `blocked: missing_human_anchor`.
- Do not invent practice cards inside a rewrite prescription.

## Operation Rules

- `delete`: template phrases, repeated transitions, card-like headings, or over-closed summary moves that can be removed.
- `keep`: facts, claim direction, citations, numbers, terms, formulas, labels, and any necessary section function.
- `observed_human_move`: what the quoted author actually does, based on the quote.
- `why_this_quote_fits_user_paragraph`: why the user paragraph has an analogous writing problem.
- `transferable_structure`: the human move to imitate at the structure level, not at the surface phrase level.
- `non_transferable_surface`: exact wording, source-specific entities, examples, data, and topic-specific phrases that must not be copied.
- `adaptation_plan`: how to apply the human move to the user's own facts and boundary.
- `restructure_as`: the concise operation derived from `adaptation_plan`.
- `evidence_boundary`: what the source text actually supports.
- `sentence_rhythm`: expected structural shift, such as asymmetry, compression, one long sentence plus short caveat, or figure/table offload.
- `citation_number_policy`: exact handling of citations and numeric tokens.

## Pass/Fail Rubric

| Check | Pass | Fail |
|---|---|---|
| Source binding | points to real practice cards | invented card, vague "human style" |
| Quote context | includes real source wording and locator | only abstract analysis of "human writing" |
| A-code trace | every operation maps to hit modes | operation not tied to scan result |
| Semantic safety | core claim and evidence strength protected | claim upgraded or softened without basis |
| Token safety | citations/numbers/terms explicitly preserved | no immutable-token handling |
| Transfer reasoning | explains why the quote's move fits this paragraph | mechanically maps an A-code to a rewrite |
| Copy boundary | uses quote as context and transfers structure only | copies quote wording or OCR noise |

## Template

Use `templates/rewrite-prescription-template.md` as a copyable blank/fixture.

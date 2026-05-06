# Anchor Curation Review Gate

This gate separates mechanically extracted corpus candidates from human-approved writing anchors.

The anchor database is allowed to store long, useful candidate excerpts. A candidate becomes safe for rewrite binding only after curator review marks it as `keep`.

## Corpus Policy

Do not keep expanding the corpus by default.

Use this priority order:

1. Review and keep the strongest existing excerpts.
2. Add Chinese papers opportunistically when reliable full text is available.
3. Add English papers only for clear gaps such as dissertation style, social science, management, education, medicine, or limitation/null-result writing.

Missing Chinese master's or undergraduate theses are not a blocker for runtime use if the current DB has enough verified anchors for the user's task. Keep the gap visible instead of forcing low-quality sources.

## Review Decisions

Use one of these decisions for each candidate anchor:

| decision | meaning |
|---|---|
| `pending` | mechanically extracted; not yet usable as a final rewrite anchor |
| `keep` | curator confirms this is a strong human-writing anchor |
| `reject` | generic, templated, noisy, misleading, or not reusable |
| `needs_source_check` | promising but source locator/OCR/provenance must be checked |
| `negative_style_only` | useful as a counterexample, never as a positive rewrite anchor |

Only `keep` may bind a suspect paragraph during `deweight-human-anchor-bind`.

## Human-Likeness Criteria

A strong human-writing anchor usually has at least three of these:

- Local specificity: the paragraph names a concrete method, object, cohort, dataset, scene, constraint, or observed result.
- Author stance: it contains cautious judgment, scoped confidence, contrast, uncertainty, or limitation handling.
- Evidence-to-claim pacing: claims are connected to evidence or procedure rather than stacked as slogans.
- Non-template rhythm: sentences vary in length and function; the paragraph is not a parallel list of generic transitions.
- Boundary awareness: it says what the finding does not prove, where the method fails, or why a recommendation is conditional.
- Transferable structure: the paragraph has a reusable move such as "phenomenon -> mechanism -> constraint", not merely attractive wording.

Reject or mark `needs_source_check` when any of these dominate:

- OCR/MinerU noise, table fragments, formula fragments, reference-list fragments.
- Generic survey boilerplate such as "has attracted increasing attention" without a local claim.
- Pure policy slogan chains such as "strengthen / improve / promote / enhance" with no actor, condition, or evidence.
- Overlong paragraphs that mix several unrelated moves.
- Single-line extraction artifacts where the source locator cannot be inspected.

## Negative Candidate Boundary

`negative_candidate` rows are style-only counterexamples. They must preserve:

```text
ai_judgement = "no, style-only"
```

Do not label a real paper as AI-generated unless a real external verifier artifact exists. A negative candidate may explain why a template pattern is risky, but it cannot be used as a positive human-writing practice card.

## Required DB Support

The SQLite asset should include:

```text
anchor_review_decisions(source_table, source_id, source_slug, batch, decision, reviewer, reviewed_at, human_quality_notes, reject_reasons, flags)
negative_candidate(..., ai_judgement)
```

Use the script:

```bash
python3 _shared/scripts/review_anchor_candidates.py _shared/assets/academic_deweight_anchors.sqlite --sync-pending --batch corpus-20260505 --summary
```

The script can flag deterministic risks, but it does not decide whether prose has "human flavor". The curator decides `keep/reject/needs_source_check`.

## Binding Rule

When `deweight-human-anchor-bind` retrieves an anchor whose `source_slug` begins with `corpus-`, it must check `anchor_review_decisions`.

If no `keep` decision exists, return:

```text
blocked: unreviewed_human_anchor
paragraph_id:
candidate_anchor:
required_action: curator review must mark decision=keep before rewrite binding
```

Runtime practice cards and the Hu Yuxiao curated anchor note remain usable through their existing field checks, but they still must satisfy source provenance and rewrite-prescription boundaries.

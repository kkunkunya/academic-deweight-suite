# Academic Deweight Workflow Contract

This contract is the shared runtime map for the six gate skills. It keeps the workflow evidence-driven and prevents "rewrite from feeling".

## Gate Order

```text
source text
-> Integrity Snapshot
-> Semantic Anchor
-> Pattern Coverage Matrix
-> Human Anchor Binding
-> Rewrite Prescription
-> Anchor-Bound Rewrite
-> Residual AI Gate
```

No rewrite may run before the first four artifacts exist for the target paragraph.

## Artifact Chain

| Gate | Required Artifact | Blocking Condition |
|---|---|---|
| intake-anchor | `Integrity Snapshot`, `Semantic Anchor` | missing paragraph IDs, uncertain citation/number truth |
| coverage-scan | `Pattern Coverage Matrix` | omitted paragraph, suspect row without A-code evidence |
| human-anchor-bind | `Human Anchor Binding`, `Rewrite Prescription` | suspect paragraph has no real practice-card source |
| anchor-rewrite | `rewritten_text` plus applied prescription | no binding, changed immutable token, copied example wording |
| verify-gate | `Residual AI Gate Report` | semantic drift, immutable token drift, severe residual or new A-code |

## Routing Boundaries

- `orchestrator`: chooses short-text vs long-document route and enforces artifact order.
- `deweight-intake-anchor`: locks what cannot change. It never rewrites.
- `deweight-coverage-scan`: diagnoses every paragraph. It never rewrites.
- `deweight-human-anchor-bind`: binds suspect paragraphs to real practice cards and writes prescriptions. It never creates fake cards.
- `deweight-anchor-rewrite`: rewrites only paragraphs with valid prescriptions.
- `deweight-verify-gate`: verifies residuals and drift. It never performs fresh rewriting.

## Real-Example Requirement

A complete reusable example contains all of the following:

1. Original academic paragraph with paragraph ID.
2. Integrity Snapshot and Semantic Anchor for that paragraph.
3. Pattern Coverage Matrix row with A-code evidence.
4. Human practice-card binding from a real paper card.
5. Rewrite prescription.
6. Rewritten paragraph.
7. Residual AI Gate row.

Current status is tracked in `real-example-index.md`. If a complete chain is absent, report `missing-real-workflow-example` instead of inventing one.

## Long-Document Contract

For a chapter, thesis, paper, or any input with 12+ paragraphs:

- assign stable `Pxxx` IDs before scanning.
- use overlapping local shards.
- aggregate into one final paragraph status table.
- require section-level mother-skeleton judgment.
- run anti-miss review before rewrite.

If isolated subagent scanning is unavailable and the user did not permit serial fallback, return `blocked: needs_subagent_runtime`.

## Deterministic Checks

Scripts in `../scripts/` only validate structure:

- `check_semantic_anchor.py`
- `check_pattern_matrix.py`
- `check_rewrite_prescription.py`
- `check_residual_report.py`

They do not judge prose quality, human style, or AIGC probability.

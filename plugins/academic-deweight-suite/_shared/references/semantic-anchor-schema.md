# Semantic Anchor And Integrity Snapshot Schema

Use this schema before any AI-pattern scan or rewrite. The purpose is to lock facts, claims, and paragraph function.

## Integrity Snapshot

Required sections:

```text
terms:
citations:
numbers:
equations:
labels:
```

Definitions:

- `terms`: domain terms, named methods, variables, named datasets, tools, institutions, people.
- `citations`: citation keys, author-year strings, bracket citations, page numbers.
- `numbers`: numeric values, percentages, p values, sample sizes, dates, thresholds, rankings.
- `equations`: formulas, symbols, code identifiers, pseudo-code names.
- `labels`: table, figure, appendix, theorem, lemma, section labels.

Use `none` only when a category was checked and absent.

## Semantic Anchor

Each paragraph block requires:

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

Rules:

- `paragraph_id` must be stable `Pxxx`.
- `writing_function` is a paper-function label such as intro gap, method choice, result contrast, limitation, or discussion boundary.
- `core_claim` is the smallest claim that must survive rewrite.
- `evidence_or_basis` names the evidence already present in the text. Do not add evidence.
- `claim_polarity` is `positive`, `negative`, `mixed`, `neutral`, or `not_applicable`.
- `evidence_strength` is `strong`, `moderate`, `weak`, `descriptive`, or `not_applicable`.
- `format_exempt_reason` is required when `status: format-exempt`; otherwise use `none`.

## Drift-Sensitive Fields

These fields must match after rewrite:

- `core_claim`
- `evidence_or_basis`
- `immutable_tokens`
- `claim_polarity`
- `evidence_strength`

If any is uncertain, the workflow returns `blocked: needs_source_check`.

## Template

Use `templates/semantic-anchor-template.md` as a copyable blank/fixture.

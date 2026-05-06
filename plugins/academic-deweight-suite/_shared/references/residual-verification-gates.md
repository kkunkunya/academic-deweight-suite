# Residual Verification Gates

`deweight-verify-gate` proves the rewrite did not become a different AI-flavored text. It checks residual A-codes, new A-codes, semantic drift, and immutable-token drift.

## Required Report Fields

```text
paragraph_id:
original_hit_modes:
remaining_hit_modes:
new_hit_modes:
max_remaining_severity:
max_new_severity:
semantic_anchor_match:
immutable_token_match:
claim_polarity_match:
evidence_strength_match:
verdict:
reason:
next_action:
```

Allowed values:

- match fields: `pass`, `fail`, or `uncertain`
- `verdict`: `pass`, `revise`, or `blocked`
- severities: `0`, `1`, `2`, or `3`

## Blocking Rules

- If `immutable_token_match` is `fail` or `uncertain`, verdict must be `blocked`.
- If `semantic_anchor_match` is `fail` or `uncertain`, verdict must be `blocked`.
- If `claim_polarity_match` is `fail`, verdict must be `blocked`.
- If `evidence_strength_match` is `fail`, verdict must be `blocked`.
- If `max_remaining_severity >= 2`, verdict must be `revise` unless a blocking rule already applies.
- If `max_new_severity >= 2`, verdict must be `revise` unless a blocking rule already applies.

## Round Delta Gate

For multi-round rewriting:

| Signal | Interpretation | Required Action |
|---|---|---|
| A28 down but A38 up | polished conclusion became reflective-AI | rescan conclusion and reduce meta-commentary |
| surface modes down but A30/A33/A35/A37 up | mother skeleton remains | return to coverage scan and binding |
| one section worsens while overall improves | local regression | rescan section before more rewriting |
| token drift appears after style fix | unsafe rewrite | restore tokens before further style work |

## AI Detection Tool Boundary

External AIGC detector output may be recorded only as user-provided or tool-provided evidence with date, tool name, and raw result. Do not write `verified by detector` unless the actual verifier output exists in the run evidence.

## Template

Use `templates/residual-report-template.md` as a copyable blank/fixture.

---
name: deweight-verify-gate
description: 学术降重的残留验收门。用于改写后复扫原 A-code 是否下降、新 A-code 是否冒出、Semantic Anchor 是否漂移、不可变 token 是否漂移。触发关键词：残留验收、Residual AI Gate、改后复扫、文意漂移检查、降重验证。
---

# Deweight Verify Gate

## Purpose

证明改写不是“换了一种 AI 味”。验收必须同时检查 AI 残留、事实完整性和文意锚定。

## Runtime References

- Residual verification gates: `../../_shared/references/residual-verification-gates.md`
- Semantic Anchor schema: `../../_shared/references/semantic-anchor-schema.md`
- Pattern Coverage Matrix schema: `../../_shared/references/pattern-coverage-matrix-schema.md`
- Copyable template: `../../_shared/references/templates/residual-report-template.md`
- Deterministic check: `../../_shared/scripts/check_residual_report.py`

## Required Checks

For every rewritten paragraph:

```text
paragraph_id:
original_hit_modes:
remaining_hit_modes:
new_hit_modes:
max_remaining_severity:
max_new_severity:
semantic_anchor_match: pass | fail
immutable_token_match: pass | fail
claim_polarity_match: pass | fail
evidence_strength_match: pass | fail
verdict: pass | revise | blocked
reason:
next_action:
```

## Gates

- If immutable token check fails: `blocked`.
- If Semantic Anchor hard fields fail: `blocked`.
- If original A-code remains severe: `revise`.
- If a new A-code appears with severity 2 or 3: `revise`.
- If revision would require new evidence or citation verification: `blocked`.
- If an external detector result is cited without raw verifier output: record it as unverified user/tool evidence, not as a pass condition.

## Round Delta Gate

For multi-round rewriting, compare previous and current matrices:

- A28 down but A38 up -> possible A39.
- Surface modes down but A30/A33/A35/A37 up -> mother skeleton not fixed.
- Overall cleaner but one section worse -> rescan that section before more rewriting.

## Output

Return a concise verification table. Do not do fresh rewriting in this skill.

Before claiming pass, the report should pass:

```bash
python3 ../../_shared/scripts/check_residual_report.py <residual-report.md>
```

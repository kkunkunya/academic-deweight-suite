---
name: orchestrator
description: 学术降重主编排器。用于论文、学位论文、基金文本、技术报告的去 AI 味/降重流程；按短文本或长文路线强制执行文意锚定、全量模式扫描、真人写作实践卡绑定、锚点约束改写和残留验收。触发关键词：学术降重、论文降重、去 AI 味、AIGC 检测、academic deweight、母骨架诊断、长文扫描、真人写法锚点。不用于个人口语化改写（那是 deweight-suite:ai-deweight-personal）。
---

# Academic Deweight Orchestrator

## Goal

降低学术文本 AI 模板痕迹，同时保持术语、引用、数字、公式、论断方向和章节功能不漂移。

核心原则：

```text
先锚定事实与文意
-> 再全量识别 AI 模式
-> 再绑定真人写作实践卡
-> 再改写
-> 最后复扫残留
```

## Workflow Profile

先参考 `../../references/workflow-profile.md` 获取 plugin interview、硬门禁、handoff artifact 和 verification evidence。该 profile 只提供高层路线参考，不锁死调用顺序；如果用户已经明确点名单个子 skill，仍直接走对应子 skill。

## Runtime References

- Workflow contract: `../../_shared/references/deweight-workflow-contract.md`
- Pattern rules: `../../_shared/references/pattern-catalog.md`
- Semantic anchor: `../../_shared/references/semantic-anchor.md`
- Semantic anchor schema: `../../_shared/references/semantic-anchor-schema.md`
- Pattern matrix schema: `../../_shared/references/pattern-coverage-matrix-schema.md`
- Rewrite prescription rubric: `../../_shared/references/rewrite-prescription-rubric.md`
- Residual verification gates: `../../_shared/references/residual-verification-gates.md`
- Real example index: `../../_shared/references/real-example-index.md`
- Anchor DB schema: `../../_shared/references/anchor-db-schema.md`
- Anchor curation review gate: `../../_shared/references/anchor-curation-review-gate.md`
- Scoring gate: `../../_shared/references/scoring.md`
- Safety guardrails: `../../_shared/references/safety-guardrails.md`
- Long document protocol: `../../_shared/references/long-document-coverage-protocol.md`
- Human practice cards: `../../_shared/references/human-writing-practice-cards/`
- Portable anchor DB: `../../_shared/assets/academic_deweight_anchors.sqlite`
- Deterministic field checks: `../../_shared/scripts/check_semantic_anchor.py`, `../../_shared/scripts/check_pattern_matrix.py`, `../../_shared/scripts/check_rewrite_prescription.py`, `../../_shared/scripts/check_residual_report.py`

## Inputs

- Required: source text or source file path.
- Optional: `mode = aggressive | balanced | safe`，默认 `aggressive`。
- Optional: `target_tone = strict_academic | readable_academic`，默认 `readable_academic`。
- Optional: `segment_length`，默认 450 中文字符或相近 token。
- Optional: `report = rewrite_only | diagnosis | full_trace`，默认 `rewrite_only`。

## Required Flow

1. Call or internally execute `deweight-intake-anchor`.
2. Call or internally execute `deweight-coverage-scan`.
3. Call or internally execute `deweight-human-anchor-bind` for every `suspect` paragraph.
4. Call or internally execute `deweight-anchor-rewrite`.
5. Call or internally execute `deweight-verify-gate`.

No step may be skipped unless the input is explicitly marked `format-exempt` and the reason is recorded.

The artifact chain must match `deweight-workflow-contract.md`. If a complete real example is requested and `real-example-index.md` says the workflow example is unavailable, report `missing-real-workflow-example` instead of inventing a case.

## Routing Rules

- Short text: fewer than 12 paragraphs and no chapter-level claim. Run all gates in one context, but still produce paragraph IDs and anchor bindings.
- Long text: 12+ paragraphs, any chapter, or user asks for full paper/thesis. `deweight-coverage-scan` must use subagent-isolated scanning.
- If subagents are unavailable for long text, return:

```text
blocked: needs_subagent_runtime
reason: long-document coverage scan requires isolated Local Scanner / Section Diagnostician / Global Aggregator / Anti-Miss Reviewer roles
```

Do not silently downgrade to single-agent long-document scanning.

## Output Contract

Default output is rewritten text only after all gates pass. If `report=diagnosis` or `full_trace`, include:

- `Integrity Snapshot` summary.
- `Semantic Anchor` summary.
- `Pattern Coverage Matrix`.
- `Human Anchor Binding Table`.
- rewrite prescription per changed paragraph.
- verification result from `deweight-verify-gate`.

## Resource Plan Template

When auditing or extending this suite, answer per child skill:

```text
SKILL.md 保留:
references/ 新增或整理:
scripts/ 新增或整理:
assets/ 新增或不适用:
本轮能补:
仍缺 / blocked / needs-user:
判断依据来自哪些现有文件:
```

## Hard Stops

- Missing paragraph numbering in scan output.
- Any unscanned paragraph in long-document mode.
- Any `suspect` paragraph without human-writing practice card binding.
- Any corpus-derived anchor used as final binding without `anchor_review_decisions.decision=keep`.
- Any rewrite that changes citation, number, unit, formula, terminology, or claim polarity.
- Any `uncertain` mother skeleton that was not rescanned or explicitly left blocked.
- Any claim that an AIGC detector was verified without a real verifier output artifact.

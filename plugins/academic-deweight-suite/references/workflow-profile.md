# Academic Deweight Suite Workflow Profile

This profile is a high-level route map for the plugin. It helps the model understand the skill map, gates, handoff artifacts, and verification evidence without locking the exact call order.

## Plugin Interview

```yaml
primary_jobs: [academic de-AI diagnosis, source-preserving rewrite, long-document coverage scan, human-anchor curation, residual verification]
entry_skill: orchestrator
child_skills: [deweight-intake-anchor, deweight-coverage-scan, deweight-human-anchor-bind, deweight-anchor-rewrite, deweight-verify-gate]
inputs_it_accepts: [paper/thesis/report text, suspect sections, detection feedback, source constraints, terminology/citation/number anchors]
outputs_it_produces: [Integrity Snapshot, Semantic Anchor, Pattern Coverage Matrix, rewrite prescriptions, rewritten passages, Residual AI Gate report]
upstream_plugins: [academic-suite, literature-review-suite, paper-positioning-suite]
downstream_plugins: [academic-suite, document-suite, git-workflow]
hard_gates: [no rewrite before Semantic Anchor, long text requires coverage scan, suspect paragraph must bind to A-code and human practice card, corpus anchors require curator keep decision, verify after rewrite]
optional_branches: [short-text fast path, long-document subagent scan, diagnosis-only, rewrite-only after valid anchors]
parallel_safe_steps: [coverage scan by section, A-code binding by suspect block, verification by section]
must_not_do: [personal口语化改写, change citations/numbers/formulas, rewrite unanchored text, claim clean without residual scan]
user_approval_points: [scope of rewrite, acceptable semantic compression, final delivery to customer/school]
verification_evidence: [coverage matrix, before/after A-code diff, anchor review decision, anchor drift check, immutable-token check]
```

## Route Hints

- Use the orchestrator for broad academic deweighting requests, especially when the user has not separated diagnosis, rewrite, and verification.
- Direct single-step requests may go straight to the named child skill when the required upstream artifact already exists.
- Treat the flow as a safety chain, not a rigid script: repeat coverage, binding, rewrite, or verification when the evidence shows drift.

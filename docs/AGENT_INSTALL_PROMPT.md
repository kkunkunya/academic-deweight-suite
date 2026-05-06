# Agent Install Prompt

Use this prompt with an agent that can read a GitHub repository:

```text
Install or emulate the Academic Deweight Suite plugin from this repository.

Reading order:
1. README.md
2. plugins/academic-deweight-suite/README.md
3. plugins/academic-deweight-suite/skills/orchestrator/SKILL.md
4. plugins/academic-deweight-suite/_shared/references/deweight-workflow-contract.md
5. plugins/academic-deweight-suite/_shared/references/rewrite-prescription-rubric.md
6. plugins/academic-deweight-suite/_shared/references/anchor-curation-review-gate.md

Do not assume the public repo includes a local anchor database.
If a rewrite needs human-writing anchors, ask the user for a local SQLite DB or use only approved runtime cards that are present in the repository.

Hard boundary:
- no rewrite without Semantic Anchor
- no rewrite without Pattern Coverage Matrix
- no rewrite without human quote evidence
- no corpus-derived anchor unless curator decision is keep
- no AIGC detector claim without real verifier output
```

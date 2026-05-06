# Installation

## Claude Code

Clone this repository and install the plugin from a local marketplace or project scope according to your Claude Code plugin workflow.

Recommended reading order:

```text
plugins/academic-deweight-suite/README.md
plugins/academic-deweight-suite/skills/orchestrator/SKILL.md
plugins/academic-deweight-suite/_shared/references/deweight-workflow-contract.md
plugins/academic-deweight-suite/_shared/references/anchor-curation-review-gate.md
```

## Codex

Clone this repository, then register the local plugin marketplace or copy the plugin into your Codex plugin source path according to your Codex setup.

Enable:

```text
academic-deweight-suite
```

## Local Anchor Database

The public repo does not include `academic_deweight_anchors.sqlite`.

Create the asset locally at:

```text
plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

Then verify it with:

```bash
python3 plugins/academic-deweight-suite/_shared/scripts/check_anchor_db.py plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

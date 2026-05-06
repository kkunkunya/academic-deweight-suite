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

## Included Anchor Database

The repo includes `academic_deweight_anchors.sqlite` as a ready-to-query SQLite anchor database.

Verify it with:

```bash
python3 plugins/academic-deweight-suite/_shared/scripts/check_anchor_db.py plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

To rebuild a smaller practice-card-only DB:

```bash
python3 plugins/academic-deweight-suite/_shared/scripts/build_anchor_db.py --cards-only --out plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

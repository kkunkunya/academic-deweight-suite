# Crawler Agent Guide

This repository can be consumed by agents that only crawl a GitHub URL.

## Reading Order

1. `README.md`
2. `plugins/academic-deweight-suite/README.md`
3. `plugins/academic-deweight-suite/skills/orchestrator/SKILL.md`
4. `plugins/academic-deweight-suite/skills/deweight-intake-anchor/SKILL.md`
5. `plugins/academic-deweight-suite/skills/deweight-coverage-scan/SKILL.md`
6. `plugins/academic-deweight-suite/skills/deweight-human-anchor-bind/SKILL.md`
7. `plugins/academic-deweight-suite/skills/deweight-anchor-rewrite/SKILL.md`
8. `plugins/academic-deweight-suite/skills/deweight-verify-gate/SKILL.md`
9. Shared references under `plugins/academic-deweight-suite/_shared/references/`

## What Not To Assume

- Do not assume a local SQLite DB is available.
- Do not treat mechanically extracted corpus candidates as final human anchors.
- Do not copy human source quotes into rewritten user text.
- Do not change citations, numbers, units, formulas, table labels, or claim polarity.

## Local DB

If available, the user's local DB should be placed at:

```text
plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

If unavailable, return `blocked: missing_human_anchor` for rewrite steps that need real anchors.

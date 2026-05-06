# Academic Deweight Suite

Academic Deweight Suite is an agent plugin for source-preserving academic de-AI and deweighting workflows.

It is designed for papers, theses, grants, and technical reports where rewriting must not drift citations, numbers, formulas, terms, or claim strength.

## What It Does

The suite routes academic rewrite work through six gates:

| Gate | Skill |
|---|---|
| Orchestration | `academic-deweight-suite:orchestrator` |
| Source anchoring | `academic-deweight-suite:deweight-intake-anchor` |
| Full coverage scan | `academic-deweight-suite:deweight-coverage-scan` |
| Human anchor binding | `academic-deweight-suite:deweight-human-anchor-bind` |
| Anchor-bound rewrite | `academic-deweight-suite:deweight-anchor-rewrite` |
| Residual verification | `academic-deweight-suite:deweight-verify-gate` |

The core workflow is:

```text
Integrity Snapshot
-> Semantic Anchor
-> Pattern Coverage Matrix
-> Human quote evidence
-> Rewrite Prescription
-> Anchor-bound rewrite
-> Residual verification
```

## SQLite Anchor Database

This package includes a complete SQLite anchor database:

```text
plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

The included DB lets agents quickly retrieve A-code / writing-function anchors, human-writing practice cards, curated excerpts, corpus segments, negative style-only candidates, and review-decision state.

The corpus redistribution rights are handled by the maintainer. Local absolute source paths inside the database are replaced with portable placeholders so the asset can move across machines.

To rebuild a DB with your own full-text sources, use:

```text
python3 plugins/academic-deweight-suite/_shared/scripts/build_anchor_db.py --out plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite --hu-full <LOCAL_FULL_MD> --hu-anchor <LOCAL_ANCHOR_MD>
```

## Install

See:

- [Installation](docs/INSTALLATION.md)
- [Agent Install Prompt](docs/AGENT_INSTALL_PROMPT.md)
- [Crawler Guide](docs/AGENT_CRAWLER_GUIDE.md)
- [API Keys and Local Config](docs/API_KEYS_AND_LOCAL_CONFIG.md)

Chinese docs:

- [安装说明](docs/INSTALLATION.zh-CN.md)
- [Agent 安装提示词](docs/AGENT_INSTALL_PROMPT.zh-CN.md)
- [Crawler 指南](docs/AGENT_CRAWLER_GUIDE.zh-CN.md)
- [API Key 与本地配置](docs/API_KEYS_AND_LOCAL_CONFIG.zh-CN.md)

## Safety

This plugin does not verify AIGC detector results unless the user provides a real verifier artifact. It does not label real papers as AI-generated from style overlap alone.

See [Security](SECURITY.md).

## Author

Kunkun

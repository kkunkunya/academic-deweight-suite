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

## Public Package Boundary

This public package intentionally does not include the local SQLite anchor corpus.

The original local database may contain real academic excerpts, local file paths, and private curation state. For public distribution, only the schema, scripts, templates, and plugin workflow are included.

To use a local anchor database, build or provide it on your own machine and keep it out of Git:

```text
plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
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

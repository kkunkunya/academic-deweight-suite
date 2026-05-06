# 安装说明

## Claude Code

克隆本仓库，然后按你的 Claude Code plugin 流程用 local marketplace 或项目级 scope 安装。

推荐读取顺序：

```text
plugins/academic-deweight-suite/README.md
plugins/academic-deweight-suite/skills/orchestrator/SKILL.md
plugins/academic-deweight-suite/_shared/references/deweight-workflow-contract.md
plugins/academic-deweight-suite/_shared/references/anchor-curation-review-gate.md
```

## Codex

克隆本仓库，然后按你的 Codex 配置注册本地 plugin marketplace，或把 plugin 放进 Codex 的 plugin source 路径。

启用：

```text
academic-deweight-suite
```

## 内置锚点数据库

仓库包含一个可直接查询的 SQLite 锚点库 `academic_deweight_anchors.sqlite`。

验证：

```bash
python3 plugins/academic-deweight-suite/_shared/scripts/check_anchor_db.py plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

如需重新生成较小的 practice-card-only DB：

```bash
python3 plugins/academic-deweight-suite/_shared/scripts/build_anchor_db.py --cards-only --out plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

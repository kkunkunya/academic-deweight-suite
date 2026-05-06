# Crawler Agent 指南

这个仓库可以给只能爬取 GitHub URL 的 agent 使用。

## 读取顺序

1. `README.zh-CN.md`
2. `plugins/academic-deweight-suite/README.md`
3. `plugins/academic-deweight-suite/skills/orchestrator/SKILL.md`
4. `plugins/academic-deweight-suite/skills/deweight-intake-anchor/SKILL.md`
5. `plugins/academic-deweight-suite/skills/deweight-coverage-scan/SKILL.md`
6. `plugins/academic-deweight-suite/skills/deweight-human-anchor-bind/SKILL.md`
7. `plugins/academic-deweight-suite/skills/deweight-anchor-rewrite/SKILL.md`
8. `plugins/academic-deweight-suite/skills/deweight-verify-gate/SKILL.md`
9. `plugins/academic-deweight-suite/_shared/references/` 下的共享参考

## 不要假设

- 使用仓库内置 SQLite DB 检索 runtime-card 和 corpus anchors。
- 不要把机械摘录的 corpus candidate 当成最终真人锚点。
- 不要把真人原句复制进用户改写文本。
- 不要改动引用、数字、单位、公式、表格标签或论断方向。

## 锚点 DB

DB 已包含在：

```text
plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

如果任务需要内置 DB 之外的新锚点，再向用户索取本地 DB 或本地源文件。

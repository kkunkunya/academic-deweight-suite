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

- 不要假设本地 SQLite DB 已存在。
- 不要把机械摘录的 corpus candidate 当成最终真人锚点。
- 不要把真人原句复制进用户改写文本。
- 不要改动引用、数字、单位、公式、表格标签或论断方向。

## 本地 DB

如果用户提供本地 DB，应放在：

```text
plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

如果没有 DB，而任务又需要真人锚点，则返回 `blocked: missing_human_anchor`。

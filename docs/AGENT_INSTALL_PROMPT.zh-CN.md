# Agent 安装提示词

给能读取 GitHub 仓库的 agent 使用：

```text
请从这个仓库安装或模拟 Academic Deweight Suite plugin。

读取顺序：
1. README.zh-CN.md
2. plugins/academic-deweight-suite/README.md
3. plugins/academic-deweight-suite/skills/orchestrator/SKILL.md
4. plugins/academic-deweight-suite/_shared/references/deweight-workflow-contract.md
5. plugins/academic-deweight-suite/_shared/references/rewrite-prescription-rubric.md
6. plugins/academic-deweight-suite/_shared/references/anchor-curation-review-gate.md

使用仓库内置 SQLite 锚点库做 A-code / writing_function 检索、真人原句证据绑定、reviewed corpus anchor 检索和 negative style-only 反例检索。
如果任务需要超出内置 DB 的新私有 corpus 锚点，请向用户索取本地 SQLite DB 或本地源文件。

硬边界：
- 没有 Semantic Anchor 不改写
- 没有 Pattern Coverage Matrix 不改写
- 没有真人原句证据不改写
- corpus 来源锚点没有 curator keep 决策不得使用
- 没有真实 verifier 输出不得声称 AIGC 检测已验证
```

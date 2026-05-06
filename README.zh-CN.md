# Academic Deweight Suite

Academic Deweight Suite 是一个面向论文、学位论文、基金文本和技术报告的学术降重 / 去 AI 味 agent plugin。

它的目标不是普通润色，而是在不漂移引用、数字、公式、术语和论断强度的前提下，降低模板化 AI 痕迹。

## 它做什么

插件把降重拆成六个门：

| 阶段 | Skill |
|---|---|
| 编排 | `academic-deweight-suite:orchestrator` |
| 文意锚定 | `academic-deweight-suite:deweight-intake-anchor` |
| 全量扫描 | `academic-deweight-suite:deweight-coverage-scan` |
| 真人锚点绑定 | `academic-deweight-suite:deweight-human-anchor-bind` |
| 锚点约束改写 | `academic-deweight-suite:deweight-anchor-rewrite` |
| 残留验收 | `academic-deweight-suite:deweight-verify-gate` |

核心流程：

```text
Integrity Snapshot
-> Semantic Anchor
-> Pattern Coverage Matrix
-> 真人原句证据
-> Rewrite Prescription
-> 锚点约束改写
-> 残留验收
```

## SQLite 锚点数据库

这个 GitHub 包包含完整 SQLite 锚点数据库：

```text
plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite
```

这个 DB 方便 agent 按 A-code / writing_function 快速检索真人写法锚点、实践卡、精选摘录、corpus segments、negative style-only candidates 和 review decision 状态。

语料再分发权限由维护者处理。数据库里的本机绝对路径已替换为可迁移占位符，方便跨机器使用。

如果你要用自己的 full-text 语料重新构建 DB，可以运行：

```text
python3 plugins/academic-deweight-suite/_shared/scripts/build_anchor_db.py --out plugins/academic-deweight-suite/_shared/assets/academic_deweight_anchors.sqlite --hu-full <LOCAL_FULL_MD> --hu-anchor <LOCAL_ANCHOR_MD>
```

## 安装

见：

- [安装说明](docs/INSTALLATION.zh-CN.md)
- [Agent 安装提示词](docs/AGENT_INSTALL_PROMPT.zh-CN.md)
- [Crawler 指南](docs/AGENT_CRAWLER_GUIDE.zh-CN.md)
- [API Key 与本地配置](docs/API_KEYS_AND_LOCAL_CONFIG.zh-CN.md)

英文文档：

- [Installation](docs/INSTALLATION.md)
- [Agent Install Prompt](docs/AGENT_INSTALL_PROMPT.md)
- [Crawler Guide](docs/AGENT_CRAWLER_GUIDE.md)
- [API Keys and Local Config](docs/API_KEYS_AND_LOCAL_CONFIG.md)

## 安全边界

除非用户提供真实 verifier artifact，本插件不会把 AIGC 检测结果写成已验证，也不会仅凭风格相似把真实论文标成 AI 生成。

见 [Security](SECURITY.md)。

## 作者

Kunkun

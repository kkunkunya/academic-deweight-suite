---
status: draft
created: 2026-05-03
source: academic-deweight-suite long-document scanning discussion
---

# 长文 AI 模式扫描协议

## 背景问题

`academic-deweight-suite` 已经把 AI 痕迹拆成 A1-A39，并进一步收敛为 7 个诊断大类与 4 个母骨架入口。但长文场景里，仅靠一个模型一次性全量阅读会出现两个硬问题：

1. **上下文限制**：论文、学位论文或长报告可能超过模型稳定扫描窗口。
2. **漏检风险**：AI 感有主观成分，模型读长文时容易只记住显眼模式，漏掉局部高影响句、章节母骨架或多轮改写迁移。

因此长文扫描不能依赖“单模型认真读完”，而应改成：

```text
分片普查 -> 章节聚合 -> 全局矩阵 -> 反漏检门控 -> 目标重扫
```

核心目标不是让模型凭感觉判断“像不像 AI”，而是把主观 AI 感转成可统计、可复查、可定位的模式证据。

## 总原则

### 1. A1-A39 保留为底层词典

不要删除 39 个模式。它们适合做证据词典、局部手术清单和训练模型识别粒度。

### 2. 执行入口收敛为 7 个诊断大类

扫描时先按大类判断，再下钻到 A-code：

| 大类 | 覆盖模式 | 诊断重点 |
|---|---|---|
| 空话包装型 | A1-A6、A8-A10、A14 | 宣传、客服、填充、模糊归因 |
| 机械对称型 | A7、A11-A13、A15-A18、A20-A23、A26、A29 | 并列、等长、连接词、格式同构、中文对偶 |
| 技术散文模板型 | A24-A27 | 公式、变量定义、模块、数值结果的流水线叙述 |
| 论证过度闭合型 | A19、A30、A32、A33 | 段内太完整、段间太顺、因果链无跳步 |
| 教科书/贴源型 | A3、A31、A35 | 教材复述、模糊归因、贴源改写 |
| 作者性缺席型 | A16、A36 | 作者不承担判断，只剩客观外包表述 |
| 混写与新式精修型 | A34、A37、A38、A39 | 推理模式接缝、混合作者接缝、精修 AI 风、多轮风格迁移 |

### 3. 四个母骨架是长文优先入口

长文不应逐条扫 A1-A39 后才找根因。章节级诊断优先问：

| 母骨架 | 典型章节 | 核心问题 |
|---|---|---|
| A30 认知自足 | Analysis / Discussion / Conclusion | 每段都是完整小论文 |
| A33 段间过滑 | Introduction / 连贯论述节 | 段与段之间过渡无毛刺 |
| A35 贴源骨架 | Literature Review / Background | 论证顺序贴着某篇 source |
| A37 混合作者接缝 | 人写 + AI polish 混合稿 | 段落分布突变、局部高影响句露馅 |

## 长文分片策略

### Paragraph Numbering

扫描前先把全文切成稳定段落编号：

```text
P001, P002, P003 ...
```

所有诊断必须引用段落编号。没有段落编号的判断不能进入最终矩阵。

### Local Shard

局部分片用于抓局部证据。

```text
范围：3-5 个自然段
长度：约 1200-2500 中文字，或相近 token 量
重叠：前后各带 1 段 overlap
重点：A1-A29、A31、A36、A38
```

局部 subagent 不能只输出“像 AI”。每个命中必须给出：

```text
pattern: A33
paragraph_ids: P021-P026
evidence: 每段开头都有“进一步/在此基础上/与此同时”
signal_type: 承接句均匀 + 主题线性 + 无毛刺
severity: 0-3
confidence: high / medium / low / uncertain
```

### Section Shard

章节分片用于抓母骨架。

```text
范围：一整节或一个章节的段落索引 + local shard 摘要
重点：A30 / A33 / A35 / A37
输出：本章最可能的母骨架，以及支持和反证
```

章节 subagent 必须回答：

```text
mother_skeleton: A30 | A33 | A35 | A37 | none | uncertain
why_this_skeleton:
counter_evidence:
minimal_surgery:
```

### Global Shard

全局分片不读全文正文，而读所有 local / section 输出。

职责：

- 统计全文模式分布。
- 找出高密度章节。
- 判断全局主模式与章节差异。
- 判断是否存在 A37 混写接缝或 A39 多轮迁移。
- 生成 Pattern Coverage Matrix。

## Pattern Coverage Matrix

每次长文扫描必须生成矩阵，而不是只生成文字诊断。

```text
section | paragraphs | dominant_group | mother_skeleton | A-codes | count | density | confidence | examples
Intro   | P001-P012   | 论证过度闭合型 | A33             | A33,A38 | 8     | high    | high       | P003,P007
LitRev  | P013-P044   | 教科书/贴源型   | A35             | A35,A7  | 11    | medium  | medium     | P019,P026
Method  | P045-P070   | 技术散文模板型 | none            | A24,A31 | 14    | high    | high       | P052,P060
```

矩阵字段要求：

- `section`：章节名或扫描块名。
- `paragraphs`：段落编号范围。
- `dominant_group`：7 个诊断大类之一。
- `mother_skeleton`：A30 / A33 / A35 / A37 / none / uncertain。
- `A-codes`：实际命中的底层模式。
- `count`：命中次数或命中段数。
- `density`：low / medium / high。
- `confidence`：high / medium / low / uncertain。
- `examples`：最多列 2-5 个代表段落编号。

## 五道门控

### Gate 1：Coverage Gate

全文每个段落必须至少被 1 个 local shard 扫过。

失败条件：

- 存在未扫描段落。
- overlap 丢失，导致段间模式无法判断。
- 段落编号在多个输出中不一致。

### Gate 2：Pattern Gate

7 个诊断大类都必须有结论：

```text
hit | not_seen | uncertain
```

不能只报告看见的模式。未明确检查就不能写 `not_seen`。

### Gate 3：Mother-Skeleton Gate

每一章必须回答：

```text
A30 / A33 / A35 / A37 / none / uncertain
```

如果 `uncertain`，必须触发章节重扫或外部 reviewer。

### Gate 4：Anti-Miss Gate

单独派 reviewer subagent 做反漏检。

输入：

- Pattern Coverage Matrix
- 每章代表段落
- 高风险 `uncertain` 区域

任务：

- 不改写。
- 不复述已有结论。
- 只找遗漏、误判、过度自信。

典型问题：

```text
为什么 P018-P023 没算 A38？
为什么 LitRev 只报 A7，没有判断 A35？
为什么 Conclusion 没判断 A30？
这个 A33 是真实过渡，还是被你过度诊断？
```

### Gate 5：Round Delta Gate

多轮降重必须比较上一轮矩阵。

关注：

- A28 降了但 A38 升了：可能触发 A39。
- 表层模式少了，但 A30/A33/A35/A37 更明显：说明没有打母骨架。
- 整体分数下降，但某章节反升：优先查章节母骨架误判。

## Subagent 分工

不要让所有 subagent 做同一件事。角色必须分层：

| 角色 | 输入 | 输出 | 不做 |
|---|---|---|---|
| Local Scanner | 3-5 段正文 + overlap | 局部 A-code 命中证据 | 不判断全文结论 |
| Section Diagnostician | 一章摘要 + local 输出 | 母骨架判断 | 不逐句改写 |
| Global Aggregator | 所有扫描输出 | Pattern Coverage Matrix | 不新增未经定位的判断 |
| Anti-Miss Reviewer | 矩阵 + 抽样段落 | 漏检/误判挑战清单 | 不做润色 |
| Rewrite Planner | 最终矩阵 | 手术优先级 | 不重新发明诊断 |

## 推荐执行流程

```text
1. normalize document
2. paragraph numbering
3. create local shards with overlap
4. run local scanners
5. run section diagnosticians
6. build global Pattern Coverage Matrix
7. run Coverage Gate
8. run Pattern Gate
9. run Mother-Skeleton Gate
10. run Anti-Miss Gate
11. targeted rescan uncertain zones
12. produce final diagnosis + rewrite priority
13. after rewrite, run Round Delta Gate
```

## 扫描输出模板

```text
## Scan Summary

- document:
- paragraph_range:
- total_paragraphs:
- scanned_paragraphs:
- missing_paragraphs:
- status: pass | partial | blocked

## Pattern Coverage Matrix

| section | paragraphs | dominant_group | mother_skeleton | A-codes | count | density | confidence | examples |
|---|---|---|---|---|---:|---|---|---|

## High-Risk Zones

| zone | reason | required_rescan |
|---|---|---|

## Anti-Miss Notes

- possible_missing:
- overconfident_diagnosis:
- needs_section_rescan:

## Rewrite Priority

1. mother_skeleton:
2. high_density_local_patterns:
3. integrity-sensitive zones:
4. optional polish:
```

## 关键判断

长文降重的关键不是一次性读完整篇，而是建立可追踪的模式普查系统。

```text
局部 subagent 负责证据
章节 subagent 负责母骨架
全局 subagent 负责统计
反漏检 subagent 负责挑战
主 agent 负责裁决与手术计划
```

这样才能把“AI 感”从主观印象变成可复查的统计矩阵，并显著降低长文扫描遗漏。


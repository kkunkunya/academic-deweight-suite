# 章节级降重策略差异化

> 2026-04-23 新增。上游认知：`[[章节级降重策略差异化]]` / `[[母骨架诊断法]]`。
> 用途：做方案 C 手术前强制先判断章节类型，避免"一刀切清单在某类章节反升"。
> **重要**：本文件内容 `status: signal`，证据强度有限（单次样本），2-3 次任务验证后再升级为 verified。

## 章节类型 × 母骨架对照表

| 章节 | 主母骨架 | 次母骨架 | 主要手术动作 | 证据强度 |
|---|---|---|---|---|
| **Abstract** | A30 认知自足 | — | 写成一气呵成的连续长段、避免 purpose/method/findings/implications 显式模板线 | 多次经验（前轮 Abstract 从 22% 降至 0%） |
| **Introduction** | A33 段间过滑 | standalone takeaway、punchy beat | 删承接句 / 允许冷启动 / 删两拍口号句 / 删 "Evidence first. Framework second." 这类尖峰句 | private local signal |
| **Literature Review** | **A35 贴源骨架** | A15 三拍展开、A17 等量覆盖 | 重组论证骨架（不按 source 顺序） / 一 source 多次引 / 证据交叉 / 术语簇替换 | **反证支持**（本次 r5 用 A30 手术 +8% 反升） |
| **Methodology/Framework** | A24 公式-散文耦合 | A31 教科书式 | 变量定义块详略差异 / 打破五段式顺序 / 压缩标准解释 / 只保留本文特有选型判断 | 推测（未在本次论文验证） |
| **Analysis/Discussion** | **A30 认知自足** | A7 并列对偶、A21 H3 parade | 删 standalone takeaway / 合并对偶段 / H3 数减一 / 段落外溢 / 四维度 parade 压成 2+1+qualifier | **正证支持**（private local case positive evidence） |
| **Conclusion** | **A30 认知自足** | standalone takeaway、summary card、aphoristic recap | 合并 summary card（`Heroic action:` 卡片句） / 段间悬置 / 反 "label + colon" / 限制段不做 not-X-but-Y 漂亮闭环 | **正证支持**（private local case positive evidence） |

## 决策流程

进入方案 C 手术前：

```
1. 这一章节是哪种类型？（对照上表）

2. 这一章节的母骨架候选是什么？
   - 有多次经验的 → 直接用表里的母骨架
   - 单次经验或推测的 → 启用多 agent 辩论三叉戟（见 multi-agent-debate-prompts.md）识别

3. 如果沿用其他章节的成功手术清单，是否和本章节母骨架冲突？
   - 不冲突 → 执行
   - 冲突 → 按本章节母骨架专属最小动作重新设计手术

4. 手术后是否 AIGC 下降？
   - 下降 → 证据入库，升级该章节母骨架的证据强度
   - 不降或反升 → 母骨架假设可能错误，触发二次诊断
```

## 为什么综述章节的母骨架大概率是 A35 不是 A30

综述章节天然就是"一篇 source → 其观点 → 作者评价"的单元堆叠——这结构本身是学科规范。

==如果强行用 A30 手术把每段打破自足性==（比如删作者评价 / 让段落不完整 / 段尾悬置），会让文本从"一气呵成读完某源"退化到"源与源之间的论证跳跃"——这种跳跃**在贴源骨架仍在的情况下反而会被检测器识别为 humanize 残片**，因为真实综述作者不会在贴源的同时故意打破自足性。

真人综述作者的反骨架做法是：
- 同一 source 在章节中重复引（弹药少、反复用）
- 源 A 刚说完不评价，直接进源 B，评价放到两源之后统一做
- 按论证需要重排 source 顺序，不按时间或重要性排
- 段落字数方差大（有的 60 词，有的 180 词）

这正是 A35 的处理策略。

## 判断型章节（Analysis/Conclusion）的 A30 手术清单

对已确诊 A30 母骨架的章节执行：

1. **删所有 standalone takeaway 段**（< 50 词的独立总结段）
2. **章节 H3 数量减一个**（合并相邻 sub-dim，比如 Ch4 sacrifice 并入 conflict）
3. **强制段落外溢**：至少 3 段结尾不收束 / 悬置到下段 / 抛出未答问题
4. **合并对偶双段为单段对比**：破坏"CN 段 / US 段"两两镜像
5. **parade 压缩**：四维度 parade 压成"主维 + 次维 + qualifier"（IDV 深 / PDI 中 / MAS-UAI 压 1 段）
6. **删 editorial stance**：搜 "What my reading / which is why / that is the shape / sit honestly" 整句删
7. **删 hyphenated 术语前缀对偶**（Low-IDV / high-IDV）
8. **破折号节奏降密**：每段最多 1 个破折号

## 综述章节（Literature Review）的 A35 手术清单（待验证）

对怀疑 A35 母骨架的章节执行：

1. **重组论证骨架**：按作者论证需要重排，不按文献出版时间或综述逻辑线排
2. **一 source 多次引**：Yang & Zhao / Zhang & Song 等关键文献在同章节出现 2-3 次（真人弹药少）
3. **证据交叉**：某论点不是"引 source A 一段"，而是"引 source A + source B 各一句从句"
4. **打破"一 source 一段"**：有的段塞 2-3 source、有的段只一句带过某 source
5. **术语簇替换**：用领域通用术语替换 source 特有术语组合
6. **段落字数方差拉大**：不要 60-120 词均匀区间
7. **不评价的文献留 1-2 条**：真人综述会列某些文献而不做判断

## 风险与限制

- 本表所有母骨架判定**样本数 ≤ 1**，`status: signal`
- 跨学科（文科 / 理工科 / 医学）章节母骨架是否稳定未验证
- Method 章节未实战验证
- 若某章节用对应母骨架手术后仍不降，应启动多 agent 辩论重新识别母骨架

## Skill 接入

- `SKILL.md` 的工作流第 4 步"主去痕改写"前建议先做章节类型判断
- `pattern-catalog.md` 的前置步骤 0c 引用本表做母骨架推测

# 05_engineering DOMAIN_SUMMARY

## 覆盖范围

- 输入论文：4 篇。
- 输出锚点卡：4 张。
- 结构化摘录：39 条。
- 语言：英文原文短片段 + 中文结构解释。
- 重点覆盖：建模、仿真设置、敏感性分析、优化算法对比、工程建议、review 型综述段。

## 工程类最适合贡献的 A-code

- A24 公式-散文耦合模板：工程论文大量在公式前后解释变量、约束和目标函数，适合训练“公式不等于模板”的改写边界。
- A27 数值密集型结果陈述：RMSE、样本数、优化问题数量、成功率、误差范围等都要求数字与机制解释绑定。
- A31 教科书式概念复述陷阱：PINN、Pareto、GSA/LSA 等概念很容易被改成百科定义，真实论文通常只解释与本文任务相关的判定条件。
- A32 过度严密因果链：工程讨论常需要因果解释，但真实写法会留下实验条件、模型边界和异常形态，不会把每一步推理抹平。
- A35 生成式贴源改写：综述和方法比较段很容易沿某篇文献的骨架复写，应训练“比较对象 -> 本文差异 -> 限定边界”的重排能力。
- A36 作者性抽薄：工程作者会解释为什么选这个模型、这个扰动、这个阈值、这个终止规则；不能全篇被动描述。
- A14/A17 范围与覆盖过度：工程引言经常诱发“经济、社会、环境、未来”全景铺陈，锚点应压回具体系统和参数。
- A33 段间衔接过滑：真实工程论文在 method/result/discussion 之间常直接冷启动到参数、图形、失败机制，不需要每段优雅过渡。

## 工程类写作功能贡献

- 问题约束化：把研究动机写成建模成本、变量不可观测、参数不可辨识、计算量不可接受等约束。
- 方法接口化：说明模型、约束、损失函数、优化变量和控制输入之间怎样连接。
- 仿真可复现化：对象、地点/年份、分辨率、样本划分、特征数、扰动输入、采样数、重复次数。
- 结果机制化：指标后必须接失败机制、图形移动方向、前沿形状、参数误差传导或控制变量变化。
- 建议条件化：用“如果采用某策略”“当非关键参数未知”“若边界条件变化”等条件限制结论。
- 综述边界化：承认术语混乱、相邻框架存在、理论问题未解，避免单一路线叙事。

## 推荐给全局矩阵的候选摘录

> 下列为候选锚点引用位置；为避免重复原文，具体 `quote` 字段见对应论文卡。

| candidate_id | card | anchor_id | 推荐理由 | 主要 A-code |
|---|---|---|---|---|
| ENG-C01 | engineering_modeling_2017_building_energy_rnn_optimization.md | E2017-01 | 用工程成本打开方法动机，克制替代“重大挑战”。 | A1, A14 |
| ENG-C02 | engineering_modeling_2017_building_energy_rnn_optimization.md | E2017-05 | 仿真对象写到尺度和来源，适合复现实验设置。 | A25, A17 |
| ENG-C03 | engineering_modeling_2017_building_energy_rnn_optimization.md | E2017-07 | 指标数值后接旧模型失败时段，适合训练结果机制化。 | A27, A20 |
| ENG-C04 | engineering_modeling_2022_sciml_pinns_review.md | E2022-02 | review 段主动承认命名混乱，适合边界化综述。 | A14, A36 |
| ENG-C05 | engineering_modeling_2022_sciml_pinns_review.md | E2022-06 | 介绍主线后承认相邻框架，避免单中心综述。 | A17, A14 |
| ENG-C06 | engineering_modeling_2022_sciml_pinns_review.md | E2022-09 | 潜力与未解问题同段出现，适合反模板展望。 | A4, A28 |
| ENG-C07 | engineering_optimization_2024_pareto_power_systems.md | E2024-04 | 用判定条件解释 Pareto 概念，避免教科书定义。 | A31, A12 |
| ENG-C08 | engineering_optimization_2024_pareto_power_systems.md | E2024-06 | 用求解流程差异说明本文贡献，适合打 A35。 | A35, A36 |
| ENG-C09 | engineering_optimization_2024_pareto_power_systems.md | E2024-09 | 把图形方向、需求增长和物理含义绑定。 | A32, A33 |
| ENG-C10 | engineering_sensitivity_2023_power_system_parameter_identification.md | E2023-01 | 参数范围同时依赖物理背景和工程判断，作者性强。 | A36, A31 |
| ENG-C11 | engineering_sensitivity_2023_power_system_parameter_identification.md | E2023-03 | 区分相关性与可辨识性，适合训练反误推理。 | A32, A31 |
| ENG-C12 | engineering_sensitivity_2023_power_system_parameter_identification.md | E2023-09 | 随机搜索失败保护写入算法流程，方法节很有工程质感。 | A24, A36 |
| ENG-C13 | engineering_sensitivity_2023_power_system_parameter_identification.md | E2023-12 | 结论给出条件化警告，不只是重复贡献。 | A28, A4 |

## 使用边界

- 这些锚点来自 MinerU `full.md`，不是校对后的出版 PDF；全局矩阵吸收前应保留 `noise_note` 或二次核对。
- 工程论文中的数值和公式 token 在降重时应默认不可变；可改的是叙述顺序、解释密度和机制连接。
- 不要把工程论文的具体仿真数值迁移到其他论文；只能迁移“数值如何嵌入论证”的写法。
- Review 型锚点和实验型锚点应分开使用：前者贡献边界、谱系和未解问题，后者贡献设置、指标和机制解释。
- 对中文工程论文改写时，需额外检查 A29 中文本土对偶承接；本批英文锚点不覆盖中文连接词风险。


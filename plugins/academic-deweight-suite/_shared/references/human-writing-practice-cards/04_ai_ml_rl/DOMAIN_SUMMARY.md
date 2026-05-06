# DOMAIN_SUMMARY: 04_ai_ml_rl

## 覆盖统计

- 输入学科目录：`<LOCAL_HUMAN_WRITING_CORPUS>`
- 输出目录：`<LOCAL_HUMAN_WRITING_ANCHOR_LIBRARY>`
- 已处理论文：4 篇
- 每篇锚点卡：8 条短摘录
- 总摘录数：32 条
- 覆盖写作功能：related work、method、experiment setup、ablation、benchmark comparison、limitations / boundary statement

## AI/RL 最适合贡献的 A-code

- A14 虚假范围与全景总括：AI/RL 真人论文通常从具体瓶颈、目标函数、benchmark 口径切入，而不是用“大背景 + 重大意义”托起贡献。
- A15 论证结构模板化：强方法论文的段落结构经常由技术取舍驱动，如“去掉 X、保留 Y、因此 Z”，不是稳定的总分总。
- A17 面面俱到的覆盖感：related work 与实验比较不是均匀铺满，而是围绕本文要解决的单一约束选择性展开。
- A24 公式-散文耦合模板：真人写法会解释公式改变了什么优化激励、约束或可计算性，而不是在公式后翻译符号。
- A27 数值密集型结果陈述：好结果段会先锁 evaluation protocol，再解释核心指标；次要数字留给表格。
- A31 教科书式概念复述陷阱：这些论文很少长篇解释通识概念，会快速跳到本文具体限制、模块或实验口径。
- A32 过度严密因果链：真实方法段常保留 tradeoff、mismatch、baseline 失败观察，不把 every step 写成完美推导。
- A33 段落间衔接过于顺滑：AI/RL 论文经常从公式、setup、结果、图表冷启动；不必每段都优雅承接。
- A35 生成式贴源改写：related work 需要围绕自己的技术坐标重排文献，而不是贴着某篇综述顺序改写。
- A36 作者性抽薄：method/experiment 段需要出现“我们为何这样设定/为何保留该 baseline/为何不展开背景”的研究者取舍。

## AI/RL 最适合学习的写作功能

- 方法空间定位：用两个极端、一个瓶颈或一个约束把新方法放进现有谱系。
- 目标函数解释：公式之后解释优化激励、下界、约束或可计算性变化。
- 设计取舍暴露：主动写不采用某种直接方案的原因，以及新设计缓解了哪个副作用。
- 实验口径锁定：在结果前定义 seed、episode、checkpoint、metric、cost 或调参范围。
- 机制型消融：每个 ablation 对应一个核心机制，不把消融写成“全都证明有效”。
- Benchmark fairness：强化被否定的 baseline，或说明保留表现较差 baseline 的理由。
- 成本-性能同框：在模型论文中把质量指标与训练成本、硬件、训练时长放在同一解释单元。
- 条件化结论：承认某组件在简单任务上未必必要，或某迁移实验只做了有限调参。
- Dataset rationale：说明数据形态为什么服务于训练目标，而不是只列规模。
- Transfer boundary：跨任务结果要写调参范围和任务差异，避免“泛化能力强”的空泛结论。

## 推荐给全局矩阵的候选摘录

> 为避免重复堆叠原文，本节用 `paper_id#Qn` 指向各卡片中的短摘录；全局矩阵可直接回填对应 quote 字段。

1. `ai_MARL_2018_qmix_multi_agent_rl#Q1`：method positioning；对抗 A14/A15/A31；贡献在两端方案之间定位。
2. `ai_MARL_2018_qmix_multi_agent_rl#Q2`：method insight；对抗 A24/A32/A36；用弱化约束写算法洞见。
3. `ai_MARL_2018_qmix_multi_agent_rl#Q6`：benchmark setup；对抗 A25/A36/A35；写清关闭环境捷径如何保证测量对象。
4. `ai_MARL_2018_qmix_multi_agent_rl#Q8`：ablation interpretation；对抗 A2/A27/A36；承认组件只在异质任务中必要。
5. `ai_RL_2017_proximal_policy_optimization#Q1`：problem framing；对抗 A14/A7/A31；用强 baseline 的具体缺陷组织引言。
6. `ai_RL_2017_proximal_policy_optimization#Q4`：objective explanation；对抗 A24/A31/A25；逐项解释 loss 改变的优化激励。
7. `ai_RL_2017_proximal_policy_optimization#Q5`：baseline treatment；对抗 A17/A36/A2；保留重要但表现较差的 baseline。
8. `ai_RL_2017_proximal_policy_optimization#Q7`：hyperparameter search setup；对抗 A36/A27/A17；把实验成本写成设计理由。
9. `ai_method_2017_attention_is_all_you_need#Q1`：problem bottleneck；对抗 A14/A31/A33；从 sequential computation 收束研究问题。
10. `ai_method_2017_attention_is_all_you_need#Q4`：limitation with tradeoff；对抗 A2/A32/A36；在优势段主动写代价和补偿。
11. `ai_method_2017_attention_is_all_you_need#Q6`：evaluation criteria；对抗 A7/A15/A27；比较前先锁三个技术维度。
12. `ai_method_2017_attention_is_all_you_need#Q8`：transfer experiment；对抗 A14/A36/A27；迁移结果附调参边界。
13. `ai_method_2018_bert_language_understanding#Q3`：scope control；对抗 A31/A17/A36；对已成共识模块主动省略背景。
14. `ai_method_2018_bert_language_understanding#Q4`：training objective rationale；对抗 A32/A36/A24；写出解决一个问题后引入的 mismatch。
15. `ai_method_2018_bert_language_understanding#Q7`：ablation interpretation；对抗 A2/A27/A35；强化被否定 baseline 后再给结论。

## 复用边界

- AI/RL 真人写法的核心不是“更强结论”，而是“更明确的实验口径和技术取舍”。复用到其他学科时，不能照搬公式/benchmark 结构。
- RL 论文的实验不确定性较强，适合学习条件化判断；不适合学习过度榜单化表达。
- Transformer/BERT 这类标志性论文的写法很强势，复用时需要保留成本、数据、任务范围，否则容易变成 A1/A14。
- 公式密集段落的真人感来自“公式后解释行为变化”，不是公式越多越像论文。
- MinerU 的 OCR 噪音普遍存在：空格化公式、HTML 表格、图片占位、断词粘词。全局矩阵不得把这些当作英文写法特征。

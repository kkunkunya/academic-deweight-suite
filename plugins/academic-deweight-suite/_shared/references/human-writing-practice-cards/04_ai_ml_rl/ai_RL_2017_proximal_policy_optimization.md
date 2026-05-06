# ai_RL_2017_proximal_policy_optimization


## 真人写作实践卡

### P01 problem framing

- source: `04_ai_ml_rl/ai_RL_2017_proximal_policy_optimization/full.md`
- location: lines 13-15, Introduction
- language: English
- writing_function: problem framing
- quote_short: "room for improvement"
- quote_context_summary: 该短摘录出现在“problem framing”功能位；前后文承担的作用是：先点名主流候选方法，再逐一指出每类方法的具体缺陷；问题不是泛泛“RL 很难”，而是 scalable、data efficient、robust 三个目标同时未满足。
- human_move: 作者在这里执行“problem framing”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先点名主流候选方法，再逐一指出每类方法的具体缺陷；问题不是泛泛“RL 很难”，而是 scalable、data efficient、robust 三个目标同时未满足。
- anti_ai_modes: A14 虚假范围与全景总括；A7 机械并列；A31 教科书式概念复述陷阱。
- rewrite_recipe: 写研究动机时，用“已有强方法仍缺什么”替代“该领域具有重要意义”；列缺陷时让每个缺陷对应一种方法。
- boundary: 适用于已有清晰方法家族的领域；如果领域尚无 strong contenders，不要假装有三分格局。
- do_not_copy_noise: MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR；不要学习这种排版。；Algorithm 1 被抽成一行，缺少真实伪代码换行；锚点只学习“训练循环如何被叙述”，不学该行格式。；文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。；论文 conclusion 较短，limitations 主要散落在比较段中；学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。

### P02 contribution claim

- source: `04_ai_ml_rl/ai_RL_2017_proximal_policy_optimization/full.md`
- location: lines 15-17, Introduction
- language: English
- writing_function: contribution claim
- quote_short: "pessimistic estimate"
- quote_context_summary: 该短摘录出现在“contribution claim”功能位；前后文承担的作用是：贡献句把目标函数性质和训练流程放在一起：clipped ratio 给出保守估计，sample/optimize 交替说明算法实际怎么跑。
- human_move: 作者在这里执行“contribution claim”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 贡献句把目标函数性质和训练流程放在一起：clipped ratio 给出保守估计，sample/optimize 交替说明算法实际怎么跑。
- anti_ai_modes: A1 空泛意义夸大；A20 操作-评价耦合；A36 作者性抽薄。
- rewrite_recipe: 算法贡献不要只说“提高稳定性”，要把稳定性来自哪个目标函数性质写出来。
- boundary: 适用于可从 objective 或 constraint 解释行为的算法；不适合纯经验超参组合。
- do_not_copy_noise: MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR；不要学习这种排版。；Algorithm 1 被抽成一行，缺少真实伪代码换行；锚点只学习“训练循环如何被叙述”，不学该行格式。；文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。；论文 conclusion 较短，limitations 主要散落在比较段中；学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。

### P03 limitation setup

- source: `04_ai_ml_rl/ai_RL_2017_proximal_policy_optimization/full.md`
- location: lines 29-35, Background
- language: English
- writing_function: limitation setup
- quote_short: "destructively large policy updates"
- quote_context_summary: 该短摘录出现在“limitation setup”功能位；前后文承担的作用是：先承认多步优化同一 trajectory 的吸引力，再指出理论上不充分且经验上会导致过大更新；缺陷从读者可能想做的自然操作中长出来。
- human_move: 作者在这里执行“limitation setup”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先承认多步优化同一 trajectory 的吸引力，再指出理论上不充分且经验上会导致过大更新；缺陷从读者可能想做的自然操作中长出来。
- anti_ai_modes: A6 过度 hedging；A32 过度严密因果链；A36 作者性抽薄。
- rewrite_recipe: 写方法限制时，先给对方方案一个合理动机，再说明它为什么失败；这样比直接贬低 baseline 更像真实学术论证。
- boundary: 适用于替代方案确实有直觉吸引力的场景；不要给明显错误方案强行补动机。
- do_not_copy_noise: MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR；不要学习这种排版。；Algorithm 1 被抽成一行，缺少真实伪代码换行；锚点只学习“训练循环如何被叙述”，不学该行格式。；文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。；论文 conclusion 较短，limitations 主要散落在比较段中；学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。

### P04 objective explanation

- source: `04_ai_ml_rl/ai_RL_2017_proximal_policy_optimization/full.md`
- location: lines 69-75, Clipped Surrogate Objective
- language: English
- writing_function: objective explanation
- quote_short: "lower bound"
- quote_context_summary: 该短摘录出现在“objective explanation”功能位；前后文承担的作用是：公式后用逐项解释展开：第一项对应旧 surrogate，第二项剪裁 ratio，最后取 min 形成保守目标；散文服务于公式拆解。
- human_move: 作者在这里执行“objective explanation”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 公式后用逐项解释展开：第一项对应旧 surrogate，第二项剪裁 ratio，最后取 min 形成保守目标；散文服务于公式拆解。
- anti_ai_modes: A24 公式-散文耦合模板；A31 教科书式概念复述陷阱；A25 短密信息弹。
- rewrite_recipe: 复杂目标函数后不要重述符号，而要逐项说明每个操作改变了优化激励。
- boundary: 适用于 loss/objective 可拆成有意义子项的算法；不适合黑箱指标。
- do_not_copy_noise: MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR；不要学习这种排版。；Algorithm 1 被抽成一行，缺少真实伪代码换行；锚点只学习“训练循环如何被叙述”，不学该行格式。；文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。；论文 conclusion 较短，limitations 主要散落在比较段中；学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。

### P05 baseline treatment

- source: `04_ai_ml_rl/ai_RL_2017_proximal_policy_optimization/full.md`
- location: lines 87-90, Adaptive KL Penalty
- language: English
- writing_function: baseline treatment
- quote_short: "important baseline"
- quote_context_summary: 该短摘录出现在“baseline treatment”功能位；前后文承担的作用是：作者明确说 KL penalty 表现更差但仍纳入，因为它是重要 baseline；这把实验完整性和主方法偏好同时保住。
- human_move: 作者在这里执行“baseline treatment”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 作者明确说 KL penalty 表现更差但仍纳入，因为它是重要 baseline；这把实验完整性和主方法偏好同时保住。
- anti_ai_modes: A17 面面俱到的覆盖感；A36 作者性抽薄；A2 宣传式形容词。
- rewrite_recipe: 对表现不佳的 baseline，要说明保留原因；不要把所有对比都写成“证明本文方法优越”。
- boundary: 适用于读者预期会问到的自然替代方案；不必把无关弱 baseline 纳入。
- do_not_copy_noise: MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR；不要学习这种排版。；Algorithm 1 被抽成一行，缺少真实伪代码换行；锚点只学习“训练循环如何被叙述”，不学该行格式。；文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。；论文 conclusion 较短，limitations 主要散落在比较段中；学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。

### P06 implementation bridge

- source: `04_ai_ml_rl/ai_RL_2017_proximal_policy_optimization/full.md`
- location: lines 106-112, Algorithm
- language: English
- writing_function: implementation bridge
- quote_short: "minor change"
- quote_context_summary: 该短摘录出现在“implementation bridge”功能位；前后文承担的作用是：先降低实现门槛：把 surrogate loss 换进去即可；再补充共享 policy/value 网络时需要合并 value loss 与 entropy bonus。
- human_move: 作者在这里执行“implementation bridge”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先降低实现门槛：把 surrogate loss 换进去即可；再补充共享 policy/value 网络时需要合并 value loss 与 entropy bonus。
- anti_ai_modes: A31 教科书式概念复述陷阱；A20 操作-评价耦合；A36 作者性抽薄。
- rewrite_recipe: 工程实现段可以写“改动很小”，但随后必须说明小改动发生在哪个训练对象上。
- boundary: 适用于与标准 pipeline 兼容的算法；不适合大量系统重构却声称“few lines”。
- do_not_copy_noise: MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR；不要学习这种排版。；Algorithm 1 被抽成一行，缺少真实伪代码换行；锚点只学习“训练循环如何被叙述”，不学该行格式。；文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。；论文 conclusion 较短，limitations 主要散落在比较段中；学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。

### P07 hyperparameter search setup

- source: `04_ai_ml_rl/ai_RL_2017_proximal_policy_optimization/full.md`
- location: lines 155-159, Experiments
- language: English
- writing_function: hyperparameter search setup
- quote_short: "computationally cheap benchmark"
- quote_context_summary: 该短摘录出现在“hyperparameter search setup”功能位；前后文承担的作用是：先说明正在为每个算法变体搜索超参，再解释为何选择便宜的 7 个 MuJoCo 任务；实验成本成为设计理由的一部分。
- human_move: 作者在这里执行“hyperparameter search setup”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先说明正在为每个算法变体搜索超参，再解释为何选择便宜的 7 个 MuJoCo 任务；实验成本成为设计理由的一部分。
- anti_ai_modes: A36 作者性抽薄；A27 数值密集型结果陈述；A17 面面俱到的覆盖感。
- rewrite_recipe: 超参搜索实验要写清“为什么先在这个小集合上调”；不要把调参平台写成最终泛化证据。
- boundary: 适用于调参成本高的 RL/ML 实验；若只跑一次默认设置，不应套用此写法。
- do_not_copy_noise: MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR；不要学习这种排版。；Algorithm 1 被抽成一行，缺少真实伪代码换行；锚点只学习“训练循环如何被叙述”，不学该行格式。；文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。；论文 conclusion 较短，limitations 主要散落在比较段中；学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。

### P08 benchmark comparison

- source: `04_ai_ml_rl/ai_RL_2017_proximal_policy_optimization/full.md`
- location: lines 7-9 and 214-216, Abstract/Conclusion
- language: English
- writing_function: benchmark comparison
- quote_short: "favorable balance"
- quote_context_summary: 该短摘录出现在“benchmark comparison”功能位；前后文承担的作用是：结论不只说 PPO 胜出，而是把 sample complexity、simplicity、wall-time 放在同一个取舍平面；读者看到的是多目标折中。
- human_move: 作者在这里执行“benchmark comparison”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 结论不只说 PPO 胜出，而是把 sample complexity、simplicity、wall-time 放在同一个取舍平面；读者看到的是多目标折中。
- anti_ai_modes: A1 空泛意义夸大；A14 虚假范围与全景总括；A27 数值密集型结果陈述。
- rewrite_recipe: 当方法不是每个指标都绝对第一时，用“balance between X, Y, Z”组织贡献，但必须让实验表真正覆盖这些维度。
- boundary: 适用于多目标方法比较；若只有单指标提升，不要使用“平衡”包装。
- do_not_copy_noise: MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR；不要学习这种排版。；Algorithm 1 被抽成一行，缺少真实伪代码换行；锚点只学习“训练循环如何被叙述”，不学该行格式。；文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。；论文 conclusion 较短，limitations 主要散落在比较段中；学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。

## 不应模仿的 MinerU/OCR 噪音或论文弱点

- MinerU 把参考文献压缩成 `[Mni+15]` 风格，且公式里有 `m a x i m i z e` 这类空格化 OCR
- 不要学习这种排版。
- Algorithm 1 被抽成一行，缺少真实伪代码换行
- 锚点只学习“训练循环如何被叙述”，不学该行格式。
- 文中若出现 `in in Table 3` 这类重复词，应视为 OCR/原文小瑕疵，不作为写法模板。
- 论文 conclusion 较短，limitations 主要散落在比较段中
- 学习时应主动补出适用边界，避免把 PPO 写成无条件优胜。
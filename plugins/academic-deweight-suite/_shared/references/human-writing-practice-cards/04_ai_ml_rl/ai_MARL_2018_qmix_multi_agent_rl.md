# ai_MARL_2018_qmix_multi_agent_rl


## 真人写作实践卡

### P01 method positioning

- source: `04_ai_ml_rl/ai_MARL_2018_qmix_multi_agent_rl/full.md`
- location: lines 30-36, Introduction
- language: English
- writing_function: method positioning
- quote_short: "between the extremes"
- quote_context_summary: 该短摘录出现在“method positioning”功能位；前后文承担的作用是：先摆出 IQL 与全中心化 critic 两个端点，再把 VDN 和 QMIX放在中间地带；新方法不是凭空出现，而是在已有方法谱系上推进一个更细的可行区间。
- human_move: 作者在这里执行“method positioning”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先摆出 IQL 与全中心化 critic 两个端点，再把 VDN 和 QMIX放在中间地带；新方法不是凭空出现，而是在已有方法谱系上推进一个更细的可行区间。
- anti_ai_modes: A14 虚假范围与全景总括；A15 论证结构模板化；A31 教科书式概念复述陷阱。
- rewrite_recipe: 写新算法贡献时，先列出两端方法的真实代价，再说本文移动了哪一个边界；不要用“本文提出一种有效方法”直接开场。
- boundary: 适用于方法空间已有明显两端方案的论文；不适用于完全探索性或无成熟 baseline 的任务。
- do_not_copy_noise: MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token；锚点库只学论证结构，不学这种排版。；图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。；个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。；论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion；学习时应补足失败条件，不要只学成功叙事。

### P02 method insight

- source: `04_ai_ml_rl/ai_MARL_2018_qmix_multi_agent_rl/full.md`
- location: lines 36-42, Introduction
- language: English
- writing_function: method insight
- quote_short: "full factorisation"
- quote_context_summary: 该短摘录出现在“method insight”功能位；前后文承担的作用是：句子先否定一个看似自然但过强的条件，再给出较弱条件；把贡献落在“少要求什么也能成立”上。
- human_move: 作者在这里执行“method insight”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 句子先否定一个看似自然但过强的条件，再给出较弱条件；把贡献落在“少要求什么也能成立”上。
- anti_ai_modes: A24 公式-散文耦合模板；A32 过度严密因果链；A36 作者性抽薄。
- rewrite_recipe: 当方法贡献来自放宽约束时，用“不是必须 X，只需 Y”来写，让读者看到约束削减，而不是只看到模块增加。
- boundary: 只有在弱条件能由公式或实验支撑时使用；不能把未证明的直觉包装成“只需”。
- do_not_copy_noise: MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token；锚点库只学论证结构，不学这种排版。；图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。；个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。；论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion；学习时应补足失败条件，不要只学成功叙事。

### P03 method mechanism

- source: `04_ai_ml_rl/ai_MARL_2018_qmix_multi_agent_rl/full.md`
- location: lines 118-128, QMIX
- language: English
- writing_function: method mechanism
- quote_short: "monotonicity constraint"
- quote_context_summary: 该短摘录出现在“method mechanism”功能位；前后文承担的作用是：先给出可保证 decentralised argmax 一致性的数学条件，再说明网络结构如何强制满足该条件；机制说明紧贴可验证性质。
- human_move: 作者在这里执行“method mechanism”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先给出可保证 decentralised argmax 一致性的数学条件，再说明网络结构如何强制满足该条件；机制说明紧贴可验证性质。
- anti_ai_modes: A31 教科书式概念复述陷阱；A24 公式-散文耦合模板；A35 生成式贴源改写。
- rewrite_recipe: 方法段写公式后要马上回答“这个公式约束了什么行为”；散文不要重复公式定义，而要解释约束带来的操作后果。
- boundary: 适用于理论约束可映射到架构设计的算法；不适合把经验 trick 硬写成理论保证。
- do_not_copy_noise: MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token；锚点库只学论证结构，不学这种排版。；图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。；个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。；论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion；学习时应补足失败条件，不要只学成功叙事。

### P04 design rationale

- source: `04_ai_ml_rl/ai_MARL_2018_qmix_multi_agent_rl/full.md`
- location: lines 132-144, QMIX
- language: English
- writing_function: design rationale
- quote_short: "extra state information"
- quote_context_summary: 该短摘录出现在“design rationale”功能位；前后文承担的作用是：解释为何状态不直接进 mixing network，而由 hypernetwork 生成权重；理由不是“更强”，而是避免单调网络对状态依赖的过度限制。
- human_move: 作者在这里执行“design rationale”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 解释为何状态不直接进 mixing network，而由 hypernetwork 生成权重；理由不是“更强”，而是避免单调网络对状态依赖的过度限制。
- anti_ai_modes: A1 空泛意义夸大；A20 操作-评价耦合；A36 作者性抽薄。
- rewrite_recipe: 写架构选择时，把“为什么不采用更直接方案”写出来；真实作者常在这里暴露设计取舍。
- boundary: 仅在有可比较的替代接线或替代模块时适用；若没有真实取舍，不要硬造排除项。
- do_not_copy_noise: MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token；锚点库只学论证结构，不学这种排版。；图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。；个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。；论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion；学习时应补足失败条件，不要只学成功叙事。

### P05 controlled diagnostic experiment

- source: `04_ai_ml_rl/ai_MARL_2018_qmix_multi_agent_rl/full.md`
- location: lines 167-179, Two-Step Game
- language: English
- writing_function: controlled diagnostic experiment
- quote_short: "full exploration ensures"
- quote_context_summary: 该短摘录出现在“controlled diagnostic experiment”功能位；前后文承担的作用是：用一个小型矩阵游戏把表征能力从环境噪声中剥离出来；先固定探索充分性，再让剩余差异指向函数类限制。
- human_move: 作者在这里执行“controlled diagnostic experiment”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 用一个小型矩阵游戏把表征能力从环境噪声中剥离出来；先固定探索充分性，再让剩余差异指向函数类限制。
- anti_ai_modes: A27 数值密集型结果陈述；A32 过度严密因果链；A17 面面俱到的覆盖感。
- rewrite_recipe: 当主实验复杂时，加一个小实验只检验单一机制；写清控制了哪些干扰，而不是把它写成又一个 benchmark。
- boundary: 适用于理论机制可被 toy environment 隔离的算法；不适合把 toy 结果外推成真实性能结论。
- do_not_copy_noise: MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token；锚点库只学论证结构，不学这种排版。；图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。；个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。；论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion；学习时应补足失败条件，不要只学成功叙事。

### P06 benchmark setup

- source: `04_ai_ml_rl/ai_MARL_2018_qmix_multi_agent_rl/full.md`
- location: lines 187-199, Experimental Setup
- language: English
- writing_function: benchmark setup
- quote_short: "force the agents to explore"
- quote_context_summary: 该短摘录出现在“benchmark setup”功能位；前后文承担的作用是：实验设置不是只列环境名，而是交代关闭 idle 攻击、attack-move 等内置行为；这些细节解释了任务为何测量学习而非游戏内建策略。
- human_move: 作者在这里执行“benchmark setup”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 实验设置不是只列环境名，而是交代关闭 idle 攻击、attack-move 等内置行为；这些细节解释了任务为何测量学习而非游戏内建策略。
- anti_ai_modes: A25 短密信息弹；A36 作者性抽薄；A35 生成式贴源改写。
- rewrite_recipe: 写 benchmark setup 时优先说明会影响结论解释的环境开关；参数清单只保留与论断相关的项。
- boundary: 适用于仿真/游戏/机器人环境；不适用于无法控制系统行为的纯观测数据集。
- do_not_copy_noise: MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token；锚点库只学论证结构，不学这种排版。；图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。；个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。；论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion；学习时应补足失败条件，不要只学成功叙事。

### P07 evaluation metric definition

- source: `04_ai_ml_rl/ai_MARL_2018_qmix_multi_agent_rl/full.md`
- location: lines 236-238, Results
- language: English
- writing_function: evaluation metric definition
- quote_short: "test win rate"
- quote_context_summary: 该短摘录出现在“evaluation metric definition”功能位；前后文承担的作用是：先定义训练暂停、独立评估 episode 数、greedy decentralised action selection，再命名评价指标；结果段先锁 metric 口径，后解释曲线。
- human_move: 作者在这里执行“evaluation metric definition”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先定义训练暂停、独立评估 episode 数、greedy decentralised action selection，再命名评价指标；结果段先锁 metric 口径，后解释曲线。
- anti_ai_modes: A27 数值密集型结果陈述；A18 显式逻辑黏合剂过密；B2 证据口径漂移。
- rewrite_recipe: 在 AI/RL 实验中，先写 evaluation protocol，再写胜负或提升；不要让“提升显著”脱离评估窗口。
- boundary: 适用于训练过程评估；若指标已是标准 leaderboard 指标，可简化但仍需交代 trial/seed。
- do_not_copy_noise: MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token；锚点库只学论证结构，不学这种排版。；图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。；个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。；论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion；学习时应补足失败条件，不要只学成功叙事。

### P08 ablation interpretation

- source: `04_ai_ml_rl/ai_MARL_2018_qmix_multi_agent_rl/full.md`
- location: lines 260-262, Ablation Results
- language: English
- writing_function: ablation interpretation
- quote_short: "not always required"
- quote_context_summary: 该短摘录出现在“ablation interpretation”功能位；前后文承担的作用是：结果解释先承认非线性分解在同质 agent 地图上不是必要条件，再转到异质地图中 state information 与 nonlinear factorisation 的组合必要性。
- human_move: 作者在这里执行“ablation interpretation”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 结果解释先承认非线性分解在同质 agent 地图上不是必要条件，再转到异质地图中 state information 与 nonlinear factorisation 的组合必要性。
- anti_ai_modes: A2 宣传式形容词；A27 数值密集型结果陈述；A36 作者性抽薄。
- rewrite_recipe: 消融段要允许“某组件在某类任务中不必要”；真实作者的贡献感来自条件化判断，不来自全局胜利叙述。
- boundary: 适用于有异质/同质、简单/复杂等任务分层的实验；不适合样本量太少却细分解释。
- do_not_copy_noise: MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token；锚点库只学论证结构，不学这种排版。；图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。；个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。；论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion；学习时应补足失败条件，不要只学成功叙事。

## 不应模仿的 MinerU/OCR 噪音或论文弱点

- MinerU 把公式变量拆成 `Q _ { t o t }`、`a r g m a x` 等空格化 token
- 锚点库只学论证结构，不学这种排版。
- 图片与表格以 `![](images/...)` 和 HTML table 混入正文，不能作为写作格式参考。
- 个别 OCR 行把跨行句子切断，例如 setup 和 results 中的断行，会影响 quote 定位但不代表原文写法。
- 论文自身的 limitation 较短，主要放在 representational complexity 与 conclusion
- 学习时应补足失败条件，不要只学成功叙事。
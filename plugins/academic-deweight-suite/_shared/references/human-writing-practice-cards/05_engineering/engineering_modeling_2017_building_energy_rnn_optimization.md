# engineering_modeling_2017_building_energy_rnn_optimization


## 真人写作实践卡

### P01 用问题成本引出方法必要性

- source: `05_engineering/engineering_modeling_2017_building_energy_rnn_optimization/full.md`
- location: Abstract
- language: en
- writing_function: 用问题成本引出方法必要性
- quote_short: "huge cost and effort"
- quote_context_summary: 该短摘录出现在“用问题成本引出方法必要性”功能位；前后文承担的作用是：先给传统建模的工程成本，再允许后文提出数据驱动替代方案。
- human_move: 作者在这里执行“用问题成本引出方法必要性”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先给传统建模的工程成本，再允许后文提出数据驱动替代方案。
- anti_ai_modes: [A1 空泛意义夸大, A14 虚假范围与全景总括]
- rewrite_recipe: 写工程问题背景时，先落到成本、变量数量、建模负担等可感知约束，再说方法动机。
- boundary: 只能用于确实存在建模或试验成本的场景；不要把所有研究问题都写成“巨大挑战”。
- do_not_copy_noise: MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。；数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。；原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。；“RNN model” 与 “always modeling accurately” 连用属于过强表述；复用时应改成由验证集或实验条件限定的说法。；图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。

### P02 用短标签压缩方法定位

- source: `05_engineering/engineering_modeling_2017_building_energy_rnn_optimization/full.md`
- location: Abstract
- language: en
- writing_function: 用短标签压缩方法定位
- quote_short: "model-free and data-driven"
- quote_context_summary: 该短摘录出现在“用短标签压缩方法定位”功能位；前后文承担的作用是：两个并列形容词直接界定方法属性，不展开教程式定义。
- human_move: 作者在这里执行“用短标签压缩方法定位”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 两个并列形容词直接界定方法属性，不展开教程式定义。
- anti_ai_modes: [A31 教科书式概念复述陷阱, A5 填充短语]
- rewrite_recipe: 当术语已被领域读者理解时，用短标签定位即可，详细机制留到方法节。
- boundary: 不适用于新概念或读者不熟悉的缩写；否则会显得跳跃。
- do_not_copy_noise: MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。；数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。；原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。；“RNN model” 与 “always modeling accurately” 连用属于过强表述；复用时应改成由验证集或实验条件限定的说法。；图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。

### P03 说明方法闭环

- source: `05_engineering/engineering_modeling_2017_building_energy_rnn_optimization/full.md`
- location: Introduction
- language: en
- writing_function: 说明方法闭环
- quote_short: "closes the loop"
- quote_context_summary: 该短摘录出现在“说明方法闭环”功能位；前后文承担的作用是：用一个动作隐喻概括“预测模型”和“实时控制”之间的闭合关系。
- human_move: 作者在这里执行“说明方法闭环”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 用一个动作隐喻概括“预测模型”和“实时控制”之间的闭合关系。
- anti_ai_modes: [A15 论证结构模板化, A33 段落间衔接过于顺滑]
- rewrite_recipe: 当方法贡献不是单个模块，而是把两个环节接起来时，用功能动词概括接口。
- boundary: 必须在后文给出真实接口；不能只把“闭环”当漂亮说法。
- do_not_copy_noise: MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。；数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。；原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。；“RNN model” 与 “always modeling accurately” 连用属于过强表述；复用时应改成由验证集或实验条件限定的说法。；图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。

### P04 保留工程约束

- source: `05_engineering/engineering_modeling_2017_building_energy_rnn_optimization/full.md`
- location: Problem formulation
- language: en
- writing_function: 保留工程约束
- quote_short: "physical constraints"
- quote_context_summary: 该短摘录出现在“保留工程约束”功能位；前后文承担的作用是：在定义控制变量时同步说明舒适区、上下界和不可控测量的约束。
- human_move: 作者在这里执行“保留工程约束”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 在定义控制变量时同步说明舒适区、上下界和不可控测量的约束。
- anti_ai_modes: [A24 公式-散文耦合模板, A36 作者性抽薄]
- rewrite_recipe: 写模型公式前后都要交代约束来自哪里，使变量不是纯符号。
- boundary: 不要把真实工程边界压缩成泛泛的“constraints”；至少说明约束类型。
- do_not_copy_noise: MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。；数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。；原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。；“RNN model” 与 “always modeling accurately” 连用属于过强表述；复用时应改成由验证集或实验条件限定的说法。；图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。

### P05 锚定仿真对象

- source: `05_engineering/engineering_modeling_2017_building_energy_rnn_optimization/full.md`
- location: Case study / Experimental setup
- language: en
- writing_function: 锚定仿真对象
- quote_short: "12-storey large office building"
- quote_context_summary: 该短摘录出现在“锚定仿真对象”功能位；前后文承担的作用是：用建筑层数和用途先固定实验对象，再补充面积、分区和年份。
- human_move: 作者在这里执行“锚定仿真对象”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 用建筑层数和用途先固定实验对象，再补充面积、分区和年份。
- anti_ai_modes: [A25 短密信息弹, A17 面面俱到的覆盖感]
- rewrite_recipe: 仿真设置优先给对象身份和尺度，数字按读者复现实验的需要排序。
- boundary: 不应把所有可得元数据堆成同等权重的长句。
- do_not_copy_noise: MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。；数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。；原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。；“RNN model” 与 “always modeling accurately” 连用属于过强表述；复用时应改成由验证集或实验条件限定的说法。；图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。

### P06 说明数据维度

- source: `05_engineering/engineering_modeling_2017_building_energy_rnn_optimization/full.md`
- location: Case study / Experimental setup
- language: en
- writing_function: 说明数据维度
- quote_short: "55 input features"
- quote_context_summary: 该短摘录出现在“说明数据维度”功能位；前后文承担的作用是：数据集描述落到输入特征数量，并举 controllable / uncontrollable 两类例子。
- human_move: 作者在这里执行“说明数据维度”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 数据集描述落到输入特征数量，并举 controllable / uncontrollable 两类例子。
- anti_ai_modes: [A27 数值密集型结果陈述, A19 抽象层次平推]
- rewrite_recipe: 数值后接分类解释，避免数字孤立出现。
- boundary: 仅在特征数量对模型复杂度或复现性有意义时使用。
- do_not_copy_noise: MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。；数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。；原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。；“RNN model” 与 “always modeling accurately” 连用属于过强表述；复用时应改成由验证集或实验条件限定的说法。；图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。

### P07 指标对比

- source: `05_engineering/engineering_modeling_2017_building_energy_rnn_optimization/full.md`
- location: Simulation results
- language: en
- writing_function: 指标对比
- quote_short: "RMSE of 0.076"
- quote_context_summary: 该短摘录出现在“指标对比”功能位；前后文承担的作用是：先说评价指标，再给基线数值和新模型数值，随后解释失败时段。
- human_move: 作者在这里执行“指标对比”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先说评价指标，再给基线数值和新模型数值，随后解释失败时段。
- anti_ai_modes: [A27 数值密集型结果陈述, A20 操作-评价耦合]
- rewrite_recipe: 结果句不要只写“显著提升”；至少包含指标名、基线、新结果和一个机制解释入口。
- boundary: 指标必须和任务目标一致；不能用单一指标覆盖所有性能面。
- do_not_copy_noise: MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。；数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。；原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。；“RNN model” 与 “always modeling accurately” 连用属于过强表述；复用时应改成由验证集或实验条件限定的说法。；图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。

### P08 控制效果解释

- source: `05_engineering/engineering_modeling_2017_building_energy_rnn_optimization/full.md`
- location: Simulation results
- language: en
- writing_function: 控制效果解释
- quote_short: "control inputs"
- quote_context_summary: 该短摘录出现在“控制效果解释”功能位；前后文承担的作用是：结果不是只报节能率，而是回到控制变量序列和约束区间的变化。
- human_move: 作者在这里执行“控制效果解释”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 结果不是只报节能率，而是回到控制变量序列和约束区间的变化。
- anti_ai_modes: [A32 过度严密因果链, A36 作者性抽薄]
- rewrite_recipe: 优化结果要把“目标函数改善”写回“决策变量如何变了”。
- boundary: 如果没有展示输入轨迹或调度策略，不应强行解释控制机制。
- do_not_copy_noise: MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。；数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。；原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。；“RNN model” 与 “always modeling accurately” 连用属于过强表述；复用时应改成由验证集或实验条件限定的说法。；图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。

## 不应模仿的 MinerU/OCR 噪音或论文弱点

- MinerU 将 `building` 切成 `build-` / `ing`，不能当作真实换行风格。
- 数学符号有大量空格拆分，例如 `6 8 . 3 3 \%`，后续锚点使用时应恢复正常数值。
- 原文有少量语言瑕疵，如 `furthur`、`hight`、`Section.`、重复 `firstly`，只能作为弱点标注，不能模仿。
- “RNN model” 与 “always modeling accurately” 连用属于过强表述
- 复用时应改成由验证集或实验条件限定的说法。
- 图注和正文的图片占位路径不是写法锚点，不进入全局矩阵。
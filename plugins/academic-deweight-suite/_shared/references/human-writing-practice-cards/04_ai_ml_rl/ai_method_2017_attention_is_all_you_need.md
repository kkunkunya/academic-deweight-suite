# ai_method_2017_attention_is_all_you_need


## 真人写作实践卡

### P01 problem bottleneck

- source: `04_ai_ml_rl/ai_method_2017_attention_is_all_you_need/full.md`
- location: lines 47-53, Introduction
- language: English
- writing_function: problem bottleneck
- quote_short: "fundamental constraint"
- quote_context_summary: 该短摘录出现在“problem bottleneck”功能位；前后文承担的作用是：先承认 RNN/LSTM/GRU 已是强方法，再把瓶颈收束到 sequential computation；贡献从一个具体计算限制中推出，而不是从“模型复杂”泛泛推出。
- human_move: 作者在这里执行“problem bottleneck”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先承认 RNN/LSTM/GRU 已是强方法，再把瓶颈收束到 sequential computation；贡献从一个具体计算限制中推出，而不是从“模型复杂”泛泛推出。
- anti_ai_modes: A14 虚假范围与全景总括；A31 教科书式概念复述陷阱；A33 段落间衔接过于顺滑。
- rewrite_recipe: 引言写法应从强 baseline 的真实瓶颈切入；不要把领域历史写成均匀背景综述。
- boundary: 适用于技术改动直接解除某个可命名瓶颈的论文；不适用于贡献主要来自数据或规模。
- do_not_copy_noise: MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`；不要学这种无空格格式。；公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token；只取结构，不取排版。；表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。；原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件；锚点复用时应主动补足边界。

### P02 contribution definition

- source: `04_ai_ml_rl/ai_method_2017_attention_is_all_you_need/full.md`
- location: lines 51-53, Introduction
- language: English
- writing_function: contribution definition
- quote_short: "without recurrence"
- quote_context_summary: 该短摘录出现在“contribution definition”功能位；前后文承担的作用是：句子先说明模型架构“舍弃什么”，再说“依赖什么”；新意通过删除既有组件而非堆叠新模块显现。
- human_move: 作者在这里执行“contribution definition”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 句子先说明模型架构“舍弃什么”，再说“依赖什么”；新意通过删除既有组件而非堆叠新模块显现。
- anti_ai_modes: A1 空泛意义夸大；A15 论证结构模板化；A36 作者性抽薄。
- rewrite_recipe: 如果贡献是去掉某类结构，写清被去掉的机制及替代机制；不要只说“简化架构”。
- boundary: 适用于 replacement-style contribution；若只是增加辅助模块，不应套用。
- do_not_copy_noise: MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`；不要学这种无空格格式。；公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token；只取结构，不取排版。；表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。；原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件；锚点复用时应主动补足边界。

### P03 related work comparison

- source: `04_ai_ml_rl/ai_method_2017_attention_is_all_you_need/full.md`
- location: lines 57-63, Background
- language: English
- writing_function: related work comparison
- quote_short: "constant number"
- quote_context_summary: 该短摘录出现在“related work comparison”功能位；前后文承担的作用是：相关工作段不是逐篇罗列，而是把 ConvS2S、ByteNet、Transformer 放进“任意两个位置建立依赖所需操作数”的同一评价轴。
- human_move: 作者在这里执行“related work comparison”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 相关工作段不是逐篇罗列，而是把 ConvS2S、ByteNet、Transformer 放进“任意两个位置建立依赖所需操作数”的同一评价轴。
- anti_ai_modes: A7 机械并列；A17 面面俱到的覆盖感；A35 生成式贴源改写。
- rewrite_recipe: related work 尽量建立一个能区分方法的技术坐标轴；每篇文献只保留与该坐标有关的信息。
- boundary: 适用于方法差异能被统一指标刻画的领域；不适合人文式争论或不可量化理论流派。
- do_not_copy_noise: MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`；不要学这种无空格格式。；公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token；只取结构，不取排版。；表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。；原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件；锚点复用时应主动补足边界。

### P04 limitation with tradeoff

- source: `04_ai_ml_rl/ai_method_2017_attention_is_all_you_need/full.md`
- location: lines 57-58, Background
- language: English
- writing_function: limitation with tradeoff
- quote_short: "averaging inhibits this"
- quote_context_summary: 该短摘录出现在“limitation with tradeoff”功能位；前后文承担的作用是：作者先承认 self-attention 降低 path length 的代价是 effective resolution 下降，再说明 multi-head attention 是补偿机制。
- human_move: 作者在这里执行“limitation with tradeoff”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 作者先承认 self-attention 降低 path length 的代价是 effective resolution 下降，再说明 multi-head attention 是补偿机制。
- anti_ai_modes: A2 宣传式形容词；A32 过度严密因果链；A36 作者性抽薄。
- rewrite_recipe: 方法优势段中应主动暴露代价；随后说明本文如何缓解，而不是删除缺点。
- boundary: 适用于有真实 tradeoff 的架构；若代价未验证，不要过度解释。
- do_not_copy_noise: MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`；不要学这种无空格格式。；公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token；只取结构，不取排版。；表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。；原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件；锚点复用时应主动补足边界。

### P05 module rationale

- source: `04_ai_ml_rl/ai_method_2017_attention_is_all_you_need/full.md`
- location: lines 109-125, Multi-Head Attention
- language: English
- writing_function: module rationale
- quote_short: "jointly attend"
- quote_context_summary: 该短摘录出现在“module rationale”功能位；前后文承担的作用是：先描述多次线性投影和并行 attention，再用一句话解释为什么多个 head 有意义：不同表示子空间和不同位置。
- human_move: 作者在这里执行“module rationale”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先描述多次线性投影和并行 attention，再用一句话解释为什么多个 head 有意义：不同表示子空间和不同位置。
- anti_ai_modes: A31 教科书式概念复述陷阱；A24 公式-散文耦合模板；A25 短密信息弹。
- rewrite_recipe: 模块段先讲操作，再给一句机制解释；不要把每个模块都写成“提升模型表达能力”的同义重复。
- boundary: 适用于可由子空间/位置/通道等机制解释的模块；不适合纯经验 ensemble。
- do_not_copy_noise: MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`；不要学这种无空格格式。；公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token；只取结构，不取排版。；表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。；原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件；锚点复用时应主动补足边界。

### P06 evaluation criteria

- source: `04_ai_ml_rl/ai_method_2017_attention_is_all_you_need/full.md`
- location: lines 171-177, Why Self-Attention
- language: English
- writing_function: evaluation criteria
- quote_short: "three desiderata"
- quote_context_summary: 该短摘录出现在“evaluation criteria”功能位；前后文承担的作用是：作者在比较前先声明三个评价维度：layer complexity、parallelizable computation、path length；后文表格和解释都服从这三个维度。
- human_move: 作者在这里执行“evaluation criteria”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 作者在比较前先声明三个评价维度：layer complexity、parallelizable computation、path length；后文表格和解释都服从这三个维度。
- anti_ai_modes: A7 机械并列；A15 论证结构模板化；A27 数值密集型结果陈述。
- rewrite_recipe: benchmark 或理论比较前先锁住评价维度；维度应来自方法瓶颈，而不是为了凑齐三点。
- boundary: 适用于比较对象较多且容易散的 method paper；不适合单一实验结果陈述。
- do_not_copy_noise: MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`；不要学这种无空格格式。；公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token；只取结构，不取排版。；表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。；原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件；锚点复用时应主动补足边界。

### P07 benchmark comparison

- source: `04_ai_ml_rl/ai_method_2017_attention_is_all_you_need/full.md`
- location: lines 225-231, Machine Translation Results
- language: English
- writing_function: benchmark comparison
- quote_short: "fraction of the training cost"
- quote_context_summary: 该短摘录出现在“benchmark comparison”功能位；前后文承担的作用是：结果段同时写 BLEU、single/ensemble 对照、训练天数和 GPU 数；性能提升和训练成本被放在同一个句群中解释。
- human_move: 作者在这里执行“benchmark comparison”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 结果段同时写 BLEU、single/ensemble 对照、训练天数和 GPU 数；性能提升和训练成本被放在同一个句群中解释。
- anti_ai_modes: A27 数值密集型结果陈述；A1 空泛意义夸大；A14 虚假范围与全景总括。
- rewrite_recipe: 若主张“更高效”，结果段必须同时给质量指标和成本指标；不要只在结论里喊 efficient。
- boundary: 适用于成本是贡献组成部分的模型；若硬件或训练预算不可比，应谨慎使用。
- do_not_copy_noise: MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`；不要学这种无空格格式。；公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token；只取结构，不取排版。；表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。；原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件；锚点复用时应主动补足边界。

### P08 transfer experiment

- source: `04_ai_ml_rl/ai_method_2017_attention_is_all_you_need/full.md`
- location: lines 253-261, English Constituency Parsing
- language: English
- writing_function: transfer experiment
- quote_short: "lack of task-specific tuning"
- quote_context_summary: 该短摘录出现在“transfer experiment”功能位；前后文承担的作用是：迁移实验承认只做少量开发集调参，并把“不专门调任务”作为结果解释的一部分；成功没有被写成全面通用性证明。
- human_move: 作者在这里执行“transfer experiment”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 迁移实验承认只做少量开发集调参，并把“不专门调任务”作为结果解释的一部分；成功没有被写成全面通用性证明。
- anti_ai_modes: A14 虚假范围与全景总括；A36 作者性抽薄；A27 数值密集型结果陈述。
- rewrite_recipe: 迁移或泛化实验要明确调参范围和未调整项；这样比直接说“generalizes well”更可防 AI 味。
- boundary: 适用于跨任务验证；若为了目标任务做了大量定制，不能再使用该写法。
- do_not_copy_noise: MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`；不要学这种无空格格式。；公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token；只取结构，不取排版。；表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。；原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件；锚点复用时应主动补足边界。

## 不应模仿的 MinerU/OCR 噪音或论文弱点

- MinerU 中标题前有较长作者/机构残片，且部分词被粘连，如 `Englishto-German`、`sourcetarget`
- 不要学这种无空格格式。
- 公式被 OCR 成 `A t t e n t i o n`、`w h e r e` 之类空格化 token
- 只取结构，不取排版。
- 表格以长 HTML 单行呈现，不能作为可读 Markdown 表格模板。
- 原论文 limitation 分散在 tradeoff 和 future work 中，较少集中讨论失败条件
- 锚点复用时应主动补足边界。
# biology_bioinformatics_2021_rnaseq_quantification


## 真人写作实践卡

### P01 将方法选择上升为下游解释风险

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Abstract, Background
- language: English
- writing_function: 将方法选择上升为下游解释风险
- quote_short: "careful selection"
- quote_context_summary: 该短摘录出现在“将方法选择上升为下游解释风险”功能位；前后文承担的作用是：先给出 RNA-seq 数据解读的目标，再指出定量指标选择是前置条件，最后落到跨样本比较和差异表达等具体后果。
- human_move: 作者在这里执行“将方法选择上升为下游解释风险”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先给出 RNA-seq 数据解读的目标，再指出定量指标选择是前置条件，最后落到跨样本比较和差异表达等具体后果。
- anti_ai_modes: A14 虚假全景总括、A31 教科书式概念复述、A36 作者性抽薄
- rewrite_recipe: 写方法重要性时，不说“该方法具有重要意义”，而说“若目标是 X，则 Y 的选择会影响 Z 结果”。
- boundary: 适合引言和摘要背景；不适合在没有明确下游分析任务时强行拔高。 2.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P02 用样本构成直接限定研究问题

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Abstract, Methods
- language: English
- writing_function: 用样本构成直接限定研究问题
- quote_short: "replicate samples"
- quote_context_summary: 该短摘录出现在“用样本构成直接限定研究问题”功能位；前后文承担的作用是：样本来源、模型数量、肿瘤类型、总样本量和比较对象在同一方法句中给出，让读者看到实验设计如何服务复现性问题。
- human_move: 作者在这里执行“用样本构成直接限定研究问题”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 样本来源、模型数量、肿瘤类型、总样本量和比较对象在同一方法句中给出，让读者看到实验设计如何服务复现性问题。
- anti_ai_modes: A17 面面俱到覆盖感、A21 列表条目同构、A35 贴源改写
- rewrite_recipe: 生信方法比较要把“数据集为什么能回答问题”写出来，优先写样本关系而不是工具清单。
- boundary: 适合有明确样本层级的数据集；若样本异质性无法说明，应改用数据来源限制句。 3.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P03 定义方法时同步声明适用范围

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Methods, RPKM and FPKM
- language: English
- writing_function: 定义方法时同步声明适用范围
- quote_short: "single sample"
- quote_context_summary: 该短摘录出现在“定义方法时同步声明适用范围”功能位；前后文承担的作用是：先说明指标原本用途，再指出它解决的校正因素，隐含排除跨样本比较的误用空间。
- human_move: 作者在这里执行“定义方法时同步声明适用范围”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先说明指标原本用途，再指出它解决的校正因素，隐含排除跨样本比较的误用空间。
- anti_ai_modes: A31 教科书式概念复述、A15 论证结构模板化
- rewrite_recipe: 写概念定义时追加“该定义成立的比较范围”，比泛泛解释公式更像真实方法论文。
- boundary: 适合指标、检测方法、归一化方法；不适合已经被领域公认为通用的基础术语。 4.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P04 用可视化隐喻解释统计归一化

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Methods, Count normalization methods
- language: English
- writing_function: 用可视化隐喻解释统计归一化
- quote_short: "virtual reference"
- quote_context_summary: 该短摘录出现在“用可视化隐喻解释统计归一化”功能位；前后文承担的作用是：不先评价 DESeq2，而是解释它如何构造参考样本，再说每个样本如何对齐到该参考。
- human_move: 作者在这里执行“用可视化隐喻解释统计归一化”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 不先评价 DESeq2，而是解释它如何构造参考样本，再说每个样本如何对齐到该参考。
- anti_ai_modes: A19 抽象层次平推、A24 公式-散文耦合模板
- rewrite_recipe: 复杂统计步骤可用“构造对象 -> 对齐动作 -> 得到参数”的三步骨架，减少公式后空泛解释。
- boundary: 只适合方法本身确有中间对象时使用；不能为了好懂而编造不存在的机制。 5.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P05 如实交代为便于计算而做的取舍

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Methods, ICC calculation
- language: English
- writing_function: 如实交代为便于计算而做的取舍
- quote_short: "uniform data matrix"
- quote_context_summary: 该短摘录出现在“如实交代为便于计算而做的取舍”功能位；前后文承担的作用是：先点出一个模型有 4 个重复而其他模型有 3 个，再说明取前三个重复的目的，最后说明这样做带来的计算便利。
- human_move: 作者在这里执行“如实交代为便于计算而做的取舍”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先点出一个模型有 4 个重复而其他模型有 3 个，再说明取前三个重复的目的，最后说明这样做带来的计算便利。
- anti_ai_modes: A30 认知完整性均匀、A36 作者性抽薄
- rewrite_recipe: 对非核心但影响分析的处理，不要藏在脚注；用“异常情况 -> 处理动作 -> 分析收益”的小段交代。
- boundary: 适合低风险技术取舍；若取舍可能改变结论，需要加敏感性分析或限制声明。 6.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P06 让表格指标承担局部反证功能

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Results, hierarchical clustering
- language: English
- writing_function: 让表格指标承担局部反证功能
- quote_short: "discordant models"
- quote_context_summary: 该短摘录出现在“让表格指标承担局部反证功能”功能位；前后文承担的作用是：先报告聚类结果是否把重复样本聚在一起，再用模型不一致数把“看图印象”压成可比较指标。
- human_move: 作者在这里执行“让表格指标承担局部反证功能”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先报告聚类结果是否把重复样本聚在一起，再用模型不一致数把“看图印象”压成可比较指标。
- anti_ai_modes: A27 数值密集型结果陈述、A20 操作-评价耦合
- rewrite_recipe: 结果段不要只说某方法最好；给一个可数的失败类型，让读者知道“好”具体好在哪里。
- boundary: 适合有清楚错误单元的比较；不适合把连续差异硬切成胜负。 7.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P07 用图形异常解释方法失效

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Results, TPM scatter plots
- language: English
- writing_function: 用图形异常解释方法失效
- quote_short: "upward shift"
- quote_context_summary: 该短摘录出现在“用图形异常解释方法失效”功能位；前后文承担的作用是：先指出散点相对 45 度线的偏移，再解释这种偏移意味着同一模型重复样本出现系统差异，最后对照 normalized count 中异常消失。
- human_move: 作者在这里执行“用图形异常解释方法失效”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先指出散点相对 45 度线的偏移，再解释这种偏移意味着同一模型重复样本出现系统差异，最后对照 normalized count 中异常消失。
- anti_ai_modes: A32 过度严密因果链、A27 数值结果模板
- rewrite_recipe: 解释图时抓一个肉眼可见的形态，再谨慎推断它对应的统计问题。
- boundary: 适合图形信号明确的结果；若图形只是辅助展示，不应过度机制化。 8.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P08 从少数异常特征推出分布层影响

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Results, highly expressed genes
- language: English
- writing_function: 从少数异常特征推出分布层影响
- quote_short: "top five"
- quote_context_summary: 该短摘录出现在“从少数异常特征推出分布层影响”功能位；前后文承担的作用是：先锁定极高表达基因集合，再比较其在重复样本中的占比，最后说明固定 TPM 总和如何让其他转录本相对丰度被牵动。
- human_move: 作者在这里执行“从少数异常特征推出分布层影响”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先锁定极高表达基因集合，再比较其在重复样本中的占比，最后说明固定 TPM 总和如何让其他转录本相对丰度被牵动。
- anti_ai_modes: A32 过度严密因果链、A31 教科书式解释、A35 贴源骨架
- rewrite_recipe: 生物信息学讨论机制时要从可观测异常出发，不从“可能存在多种因素”空转。
- boundary: 适合分布受少数大值影响的场景；不适合没有异常特征定位的数据。 9.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P09 将方法推荐收束到统计假设

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Discussion, normalization assumptions
- language: English
- writing_function: 将方法推荐收束到统计假设
- quote_short: "assumptions"
- quote_context_summary: 该短摘录出现在“将方法推荐收束到统计假设”功能位；前后文承担的作用是：先承认每种归一化都有前提，再分别说明不同方法依赖的表达分布假设，最后把本研究观察放入这些前提是否成立的判断中。
- human_move: 作者在这里执行“将方法推荐收束到统计假设”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先承认每种归一化都有前提，再分别说明不同方法依赖的表达分布假设，最后把本研究观察放入这些前提是否成立的判断中。
- anti_ai_modes: A14 虚假范围、A28 结论模板、A36 作者性抽薄
- rewrite_recipe: 推荐某方法时必须写“它为什么在本实验设置下成立”，而不是写成普适最佳。
- boundary: 适合讨论节；摘要结论中可压缩，但不能删掉条件。 10.
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

### P10 用作者立场提醒读者避免机械套用

- source: `02_biology/biology_bioinformatics_2021_rnaseq_quantification/full.md`
- location: Discussion, method selection warning
- language: English
- writing_function: 用作者立场提醒读者避免机械套用
- quote_short: "context"
- quote_context_summary: 该短摘录出现在“用作者立场提醒读者避免机械套用”功能位；前后文承担的作用是：先指出方法会在前提被违反时失败，再把读者行动落到研究场景、方法假设和数据特征的共同判断上。
- human_move: 作者在这里执行“用作者立场提醒读者避免机械套用”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先指出方法会在前提被违反时失败，再把读者行动落到研究场景、方法假设和数据特征的共同判断上。
- anti_ai_modes: A36 作者性抽薄、A38 精炼反思型结尾、A30 段内闭合过满
- rewrite_recipe: 结论可给建议，但建议要带使用条件和失败条件，保留研究者判断痕迹。
- boundary: 适合方法学论文结尾；不适合用来包装证据不足的主张。
- do_not_copy_noise: MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字；图表和图片标签被插入正文；公式空格化严重；表格 HTML 可读性差。；写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景；多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。；不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。

## 不应模仿的 MinerU/OCR 噪音或论文弱点

- MinerU/OCR 噪音：`Quantifcation`、`coefcient`、`Tis/Te` 等缺字
- 图表和图片标签被插入正文
- 公式空格化严重
- 表格 HTML 可读性差。
- 写作弱点：PDX 场景非常明确，不能把 normalized counts 的结论外推到所有 RNA-seq 场景
- 多数模型只有 3 个重复，讨论时必须保留复现性评价的样本规模边界。
- 不要模仿：摘要中“compelling evidence”“best choice”一类强判断，若迁移到弱证据稿件会造成论断升级。
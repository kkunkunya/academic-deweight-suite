# engineering_modeling_2022_sciml_pinns_review


## 真人写作实践卡

### P01 定义方法核心

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: Abstract
- language: en
- writing_function: 定义方法核心
- quote_short: "PDE residual"
- quote_context_summary: 该短摘录出现在“定义方法核心”功能位；前后文承担的作用是：以一个技术残差项说明 PINN 和普通神经网络的差异。
- human_move: 作者在这里执行“定义方法核心”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 以一个技术残差项说明 PINN 和普通神经网络的差异。
- anti_ai_modes: [A31 教科书式概念复述陷阱, A1 空泛意义夸大]
- rewrite_recipe: 综述定义要抓住造成方法差异的最小技术构件。
- boundary: 不能只摘术语；必须在正文说明残差如何进入损失函数。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P02 暴露术语不稳定性

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: Introduction
- language: en
- writing_function: 暴露术语不稳定性
- quote_short: "clear nomenclature"
- quote_context_summary: 该短摘录出现在“暴露术语不稳定性”功能位；前后文承担的作用是：先承认领域命名不统一，再说明本文选择的研究对象。
- human_move: 作者在这里执行“暴露术语不稳定性”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先承认领域命名不统一，再说明本文选择的研究对象。
- anti_ai_modes: [A14 虚假范围与全景总括, A36 作者性抽薄]
- rewrite_recipe: 综述开头可以主动指出分类边界的不稳定，从而合理限定范围。
- boundary: 适用于术语确实混用的领域；不要把清晰领域故意写乱。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P03 说明数据需求边界

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: What the PINNs are
- language: en
- writing_function: 说明数据需求边界
- quote_short: "does not require"
- quote_context_summary: 该短摘录出现在“说明数据需求边界”功能位；前后文承担的作用是：用否定句说明 PINN 不依赖标注数据，再补充它依赖方程和边界条件。
- human_move: 作者在这里执行“说明数据需求边界”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 用否定句说明 PINN 不依赖标注数据，再补充它依赖方程和边界条件。
- anti_ai_modes: [A6 过度 hedging, A31 教科书式概念复述陷阱]
- rewrite_recipe: 当方法优势是“少依赖某类资源”时，用否定式写清缺的是什么。
- boundary: 不能推导成完全不需要数据；逆问题和含观测任务仍可能需要数据。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P04 方法机制压缩

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: What the PINNs are
- language: en
- writing_function: 方法机制压缩
- quote_short: "mesh-free technique"
- quote_context_summary: 该短摘录出现在“方法机制压缩”功能位；前后文承担的作用是：用一个技术标签把“直接解方程”改写成“优化损失”的机制概括出来。
- human_move: 作者在这里执行“方法机制压缩”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 用一个技术标签把“直接解方程”改写成“优化损失”的机制概括出来。
- anti_ai_modes: [A24 公式-散文耦合模板, A19 抽象层次平推]
- rewrite_recipe: 解释算法机制时，先给机制标签，再落到具体替换关系。
- boundary: 若任务仍依赖网格或离散点，应避免使用绝对化的 mesh-free 叙述。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P05 对比纯数据拟合

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: What the PINNs are
- language: en
- writing_function: 对比纯数据拟合
- quote_short: "underlying PDE"
- quote_context_summary: 该短摘录出现在“对比纯数据拟合”功能位；前后文承担的作用是：将方法差异放在“物理方程”与“状态值拟合”的对比上。
- human_move: 作者在这里执行“对比纯数据拟合”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 将方法差异放在“物理方程”与“状态值拟合”的对比上。
- anti_ai_modes: [A15 论证结构模板化, A31 教科书式概念复述陷阱]
- rewrite_recipe: 综述对比不要只列优缺点，最好抓住输入信息类型的差异。
- boundary: 对无明确 governing equation 的问题不适用。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P06 防止单一路线叙事

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: What the PINNs are
- language: en
- writing_function: 防止单一路线叙事
- quote_short: "not the only"
- quote_context_summary: 该短摘录出现在“防止单一路线叙事”功能位；前后文承担的作用是：在介绍主线后立即承认相邻框架存在，避免把领域写成单中心史。
- human_move: 作者在这里执行“防止单一路线叙事”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 在介绍主线后立即承认相邻框架存在，避免把领域写成单中心史。
- anti_ai_modes: [A17 面面俱到的覆盖感, A14 虚假范围与全景总括]
- rewrite_recipe: 综述中的范围限定可用“不是唯一”句式打开旁支，但随后要选择性收束。
- boundary: 不要因为提到旁支就展开成无边界文献清单。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P07 术语使用约定

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: What the PINNs are
- language: en
- writing_function: 术语使用约定
- quote_short: "singular form"
- quote_context_summary: 该短摘录出现在“术语使用约定”功能位；前后文承担的作用是：作者显式交代全文术语约定，减少后文复数/族群概念歧义。
- human_move: 作者在这里执行“术语使用约定”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 作者显式交代全文术语约定，减少后文复数/族群概念歧义。
- anti_ai_modes: [A36 作者性抽薄, A5 填充短语]
- rewrite_recipe: 当术语形式可能误导读者时，用一句话设定本文用法。
- boundary: 不需要为所有常规缩写都写使用约定。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P08 分解方法构件

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: Building blocks
- language: en
- writing_function: 分解方法构件
- quote_short: "three components"
- quote_context_summary: 该短摘录出现在“分解方法构件”功能位；前后文承担的作用是：把 PINN 拆成神经网络、物理信息网络和反馈机制三个功能块。
- human_move: 作者在这里执行“分解方法构件”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 把 PINN 拆成神经网络、物理信息网络和反馈机制三个功能块。
- anti_ai_modes: [A7 机械并列, A21 列表条目格式同构]
- rewrite_recipe: 结构化拆分要对应真实功能模块，不要为了三段式而凑三项。
- boundary: 当系统构件之间强耦合时，拆分后需补充连接机制。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P09 保留未解问题

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: PINN in the SciML Framework
- language: en
- writing_function: 保留未解问题
- quote_short: "many questions remain unsolved"
- quote_context_summary: 该短摘录出现在“保留未解问题”功能位；前后文承担的作用是：先承认潜力，再转入传统数值方法替代场景中的未解问题。
- human_move: 作者在这里执行“保留未解问题”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先承认潜力，再转入传统数值方法替代场景中的未解问题。
- anti_ai_modes: [A4 公式化挑战-前景结尾, A28 结论/展望节级模板]
- rewrite_recipe: 展望段不要只写“潜力巨大”；必须同时列出会阻碍落地的问题。
- boundary: 未解问题要可技术化，不能停在“仍需进一步研究”。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

### P10 拒绝浅层迁移

- source: `05_engineering/engineering_modeling_2022_sciml_pinns_review/full.md`
- location: PINN in the SciML Framework
- language: en
- writing_function: 拒绝浅层迁移
- quote_short: "beyond basic copy-paste"
- quote_context_summary: 该短摘录出现在“拒绝浅层迁移”功能位；前后文承担的作用是：用带判断色彩的短语提醒方法不能机械迁移，随后说明问题-模型关系要加深。
- human_move: 作者在这里执行“拒绝浅层迁移”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 用带判断色彩的短语提醒方法不能机械迁移，随后说明问题-模型关系要加深。
- anti_ai_modes: [A36 作者性抽薄, A38 精炼反思型学术风格]
- rewrite_recipe: 综述中可保留作者判断，但要紧接技术原因，不写成金句。
- boundary: 不应滥用口语化批评；需要有前文失败机制支撑。
- do_not_copy_noise: `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。；个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。；公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。；综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。；引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。

## 不应模仿的 MinerU/OCR 噪音或论文弱点

- `stars form the vanilla PINN`、`deeplearning`、`physicsbased` 等是 OCR 或排版粘连，不是可模仿表达。
- 个别句子过长且语法拧巴，例如摘要中 `while the primary goal` 开头的连接关系不稳，不能作为句法模板。
- 公式区域混入错误矩阵和排版残片，应只提取散文功能，不把异常公式当锚点。
- 综述里有少量泛化较大的判断，复用时需要补上应用域或证据来源。
- 引文列表和图注中的自动断行、URL 断裂不进入全局矩阵。
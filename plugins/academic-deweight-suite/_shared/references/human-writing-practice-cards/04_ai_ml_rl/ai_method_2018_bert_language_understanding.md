# ai_method_2018_bert_language_understanding


## 真人写作实践卡

### P01 limitation framing

- source: `04_ai_ml_rl/ai_method_2018_bert_language_understanding/full.md`
- location: lines 19-25, Introduction
- language: English
- writing_function: limitation framing
- quote_short: "restrict the power"
- quote_context_summary: 该短摘录出现在“limitation framing”功能位；前后文承担的作用是：先把已有策略分成 feature-based 与 fine-tuning，再指出二者共享的 unidirectional LM 目标限制；问题由分类后的共同约束推出。
- human_move: 作者在这里执行“limitation framing”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先把已有策略分成 feature-based 与 fine-tuning，再指出二者共享的 unidirectional LM 目标限制；问题由分类后的共同约束推出。
- anti_ai_modes: A31 教科书式概念复述陷阱；A14 虚假范围与全景总括；A15 论证结构模板化。
- rewrite_recipe: 写引言时可先分类再找共同瓶颈；分类要服务于后续方法，不要变成 related work 摘要。
- boundary: 适用于已有方法可归成少数路线的领域；若分类本身有争议，需要先限定范围。
- do_not_copy_noise: MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`；锚点不学习这些拼写。；公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`；不要作为英文排版参考。；多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。；原论文结果段较强势，风险是学成“榜单胜利叙事”；复用时应保留预训练成本、数据规模和任务选择边界。

### P02 related method contrast

- source: `04_ai_ml_rl/ai_method_2018_bert_language_understanding/full.md`
- location: lines 19-21, Introduction
- language: English
- writing_function: related method contrast
- quote_short: "minimal task-specific parameters"
- quote_context_summary: 该短摘录出现在“related method contrast”功能位；前后文承担的作用是：对 feature-based 和 fine-tuning 的差异用“任务架构加入特征”与“少量任务参数微调全模型”对照，随后才进入本文问题。
- human_move: 作者在这里执行“related method contrast”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 对 feature-based 和 fine-tuning 的差异用“任务架构加入特征”与“少量任务参数微调全模型”对照，随后才进入本文问题。
- anti_ai_modes: A7 机械并列；A17 面面俱到的覆盖感；A35 生成式贴源改写。
- rewrite_recipe: related work 分类要用操作差异定义，而不是只用论文名或流派标签。
- boundary: 适用于方法工作流差异明确的领域；不适合纯性能榜单对比。
- do_not_copy_noise: MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`；锚点不学习这些拼写。；公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`；不要作为英文排版参考。；多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。；原论文结果段较强势，风险是学成“榜单胜利叙事”；复用时应保留预训练成本、数据规模和任务选择边界。

### P03 scope control

- source: `04_ai_ml_rl/ai_method_2018_bert_language_understanding/full.md`
- location: lines 66-70, BERT
- language: English
- writing_function: scope control
- quote_short: "omit an exhaustive background"
- quote_context_summary: 该短摘录出现在“scope control”功能位；前后文承担的作用是：作者说明 Transformer 已常见，本文实现又接近原始版本，因此不展开背景；这是一种主动控篇幅的写法。
- human_move: 作者在这里执行“scope control”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 作者说明 Transformer 已常见，本文实现又接近原始版本，因此不展开背景；这是一种主动控篇幅的写法。
- anti_ai_modes: A31 教科书式概念复述陷阱；A17 面面俱到的覆盖感；A36 作者性抽薄。
- rewrite_recipe: 对读者已经熟悉且非本文贡献的模块，明确引用来源并省略背景，把篇幅让给差异点。
- boundary: 适用于顶会读者已熟悉的基础模块；教学论文或综述不能这样省略。
- do_not_copy_noise: MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`；锚点不学习这些拼写。；公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`；不要作为英文排版参考。；多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。；原论文结果段较强势，风险是学成“榜单胜利叙事”；复用时应保留预训练成本、数据规模和任务选择边界。

### P04 training objective rationale

- source: `04_ai_ml_rl/ai_method_2018_bert_language_understanding/full.md`
- location: lines 87-91, Pre-training BERT
- language: English
- writing_function: training objective rationale
- quote_short: "pre-train/fine-tune mismatch"
- quote_context_summary: 该短摘录出现在“training objective rationale”功能位；前后文承担的作用是：先说明 bidirectional LM 的目标泄漏问题，再提出 mask 部分 token；随后承认 [MASK] 不出现在 fine-tuning 中并给出 80/10/10 替换策略。
- human_move: 作者在这里执行“training objective rationale”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先说明 bidirectional LM 的目标泄漏问题，再提出 mask 部分 token；随后承认 [MASK] 不出现在 fine-tuning 中并给出 80/10/10 替换策略。
- anti_ai_modes: A32 过度严密因果链；A36 作者性抽薄；A24 公式-散文耦合模板。
- rewrite_recipe: 方法段要写“修复一个问题又引入哪个新问题”，再给缓解策略；真实写法保留设计的副作用。
- boundary: 适用于训练目标与下游使用存在差异的模型；若没有 mismatch，不要硬造。
- do_not_copy_noise: MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`；锚点不学习这些拼写。；公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`；不要作为英文排版参考。；多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。；原论文结果段较强势，风险是学成“榜单胜利叙事”；复用时应保留预训练成本、数据规模和任务选择边界。

### P05 dataset rationale

- source: `04_ai_ml_rl/ai_method_2018_bert_language_understanding/full.md`
- location: lines 102-103, Pre-training Data
- language: English
- writing_function: dataset rationale
- quote_short: "long contiguous sequences"
- quote_context_summary: 该短摘录出现在“dataset rationale”功能位；前后文承担的作用是：数据选择不是只列 BooksCorpus/Wikipedia，而是说明文档级语料对 NSP 和长序列抽取的必要性。
- human_move: 作者在这里执行“dataset rationale”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 数据选择不是只列 BooksCorpus/Wikipedia，而是说明文档级语料对 NSP 和长序列抽取的必要性。
- anti_ai_modes: A25 短密信息弹；A36 作者性抽薄；A31 教科书式概念复述陷阱。
- rewrite_recipe: 数据集段写清“为什么这类数据适配任务目标”；不要只堆数据规模。
- boundary: 适用于数据形态影响训练目标的场景；如果数据只是常规 benchmark，可简化。
- do_not_copy_noise: MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`；锚点不学习这些拼写。；公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`；不要作为英文排版参考。；多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。；原论文结果段较强势，风险是学成“榜单胜利叙事”；复用时应保留预训练成本、数据规模和任务选择边界。

### P06 method unification

- source: `04_ai_ml_rl/ai_method_2018_bert_language_understanding/full.md`
- location: lines 104-112, Fine-tuning BERT
- language: English
- writing_function: method unification
- quote_short: "relatively inexpensive"
- quote_context_summary: 该短摘录出现在“method unification”功能位；前后文承担的作用是：先说 self-attention 允许单句/句对任务统一输入输出，再说明每个任务只替换适当 output；最后给出 fine-tuning 成本。
- human_move: 作者在这里执行“method unification”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 先说 self-attention 允许单句/句对任务统一输入输出，再说明每个任务只替换适当 output；最后给出 fine-tuning 成本。
- anti_ai_modes: A14 虚假范围与全景总括；A20 操作-评价耦合；A36 作者性抽薄。
- rewrite_recipe: 写统一框架时，要用具体输入输出映射证明“统一”，而不是只说“适用于多任务”。
- boundary: 适用于多任务共享骨干模型；若任务间接口差异很大，不要过度统一。
- do_not_copy_noise: MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`；锚点不学习这些拼写。；公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`；不要作为英文排版参考。；多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。；原论文结果段较强势，风险是学成“榜单胜利叙事”；复用时应保留预训练成本、数据规模和任务选择边界。

### P07 ablation interpretation

- source: `04_ai_ml_rl/ai_method_2018_bert_language_understanding/full.md`
- location: lines 187-201, Ablation Studies
- language: English
- writing_function: ablation interpretation
- quote_short: "good faith attempt"
- quote_context_summary: 该短摘录出现在“ablation interpretation”功能位；前后文承担的作用是：作者在比较 LTR 与 MLM 时主动加强 LTR baseline：加随机 BiLSTM；然后说明仍落后且伤害 GLUE，避免 weak baseline 指控。
- human_move: 作者在这里执行“ablation interpretation”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 作者在比较 LTR 与 MLM 时主动加强 LTR baseline：加随机 BiLSTM；然后说明仍落后且伤害 GLUE，避免 weak baseline 指控。
- anti_ai_modes: A2 宣传式形容词；A27 数值密集型结果陈述；A35 生成式贴源改写。
- rewrite_recipe: 关键消融中，应尝试强化被否定的替代方案；写出“我们给它合理机会但仍不足”。
- boundary: 适用于可能被质疑 baseline 太弱的实验；若没有合理强化方式，不要伪造。
- do_not_copy_noise: MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`；锚点不学习这些拼写。；公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`；不要作为英文排版参考。；多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。；原论文结果段较强势，风险是学成“榜单胜利叙事”；复用时应保留预训练成本、数据规模和任务选择边界。

### P08 limitation and alternative use

- source: `04_ai_ml_rl/ai_method_2018_bert_language_understanding/full.md`
- location: lines 213-231, Feature-based Approach
- language: English
- writing_function: limitation and alternative use
- quote_short: "computational benefits"
- quote_context_summary: 该短摘录出现在“limitation and alternative use”功能位；前后文承担的作用是：在主张 fine-tuning 之后，仍承认 feature-based 方法有架构适配与预计算成本优势，并用 NER 任务实测。
- human_move: 作者在这里执行“limitation and alternative use”动作；用具体对象、证据关系、比较口径或边界条件改变段落功能，而不是替换同义词。
- structure_skeleton: 在主张 fine-tuning 之后，仍承认 feature-based 方法有架构适配与预计算成本优势，并用 NER 任务实测。
- anti_ai_modes: A17 面面俱到的覆盖感；A36 作者性抽薄；A14 虚假范围与全景总括。
- rewrite_recipe: 讨论替代使用方式时，要先承认其优势，再给实验边界；不要把非主方法写成失败陪衬。
- boundary: 适用于同一模型可有多种部署方式的论文；不适用于目标唯一的算法。
- do_not_copy_noise: MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`；锚点不学习这些拼写。；公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`；不要作为英文排版参考。；多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。；原论文结果段较强势，风险是学成“榜单胜利叙事”；复用时应保留预训练成本、数据规模和任务选择边界。

## 不应模仿的 MinerU/OCR 噪音或论文弱点

- MinerU 把 `task-specific`、`downstream` 等词多处断裂或粘连，如 `taskspecific`、`finetuning`
- 锚点不学习这些拼写。
- 公式和参数出现空格化与括号错位，如 `4 . 5 %`、`L { = } 6`
- 不要作为英文排版参考。
- 多个大表被抽成单行 HTML，卡片只引用段落写法，不学习表格转写。
- 原论文结果段较强势，风险是学成“榜单胜利叙事”
- 复用时应保留预训练成本、数据规模和任务选择边界。
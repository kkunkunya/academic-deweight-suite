# 01_medicine DOMAIN_SUMMARY

## 覆盖统计

- 已处理论文：5 篇
- 生成锚点卡：5 个
- 原文短摘录：55 条
- 覆盖类型：英文 RCT 2 篇、中文 RCT 1 篇、中文流行病学二次数据分析 1 篇、英文系统综述 / meta 分析 1 篇
- 主要场景：RCT 摘要、随机化/盲法、临床结果、阴性结果、亚组探索、干预安全性、系统综述方法、偏倚风险、临床意义、局限性

## 医学类最适合贡献的 A-code

- A27 数值密集型结果陈述：医学结果段天然有大量指标、CI、P 值和组间/组内比较；真人写法常把关键数字留在正文，次要数字交给表格。
- A36 作者性抽薄：医学论文看似客观，但在模型选择、亚组降级、局限性解释和讨论判断处会出现作者决策痕迹。
- A32 过度严密因果链：阴性 RCT 和 meta 分析经常拒绝把观察结果解释成完整机制链，是对 AI“补全因果”的强锚点。
- A28 公式化结论/展望：医学结论的未来研究建议往往直接回应当前限制，如复制、扩大样本、延长随访、机制验证，而不是泛写“具有广阔前景”。
- A25 短密信息弹：摘要和结果节常压缩大量数据，但真人论文会用表格、分层小节、轨迹词和安全性短句来调节密度。
- A14 虚假范围与全景总括：医学写法重视人群、时间窗、测量方式和结局定义，天然反对“普遍有效”“广泛适用”的泛化。
- A31 教科书式概念复述：RCT 和 meta 方法节不解释基础概念，直接写操作化设计、阈值、模型和流程。
- A35 生成式贴源改写：综述和公共卫生讨论容易贴着参考文献顺序写；医学真人写法会按本研究数据需要重排证据。
- A33 段间衔接过于顺滑：医学正文常从表格结果突然转入局限、从方法细节转入偏倚控制，不追求每段优雅过渡。
- B2 证据强度守恒：阴性结果、非显著结果、亚组发现和小效应 meta 结果都要求严格保留证据等级。
- B4 可检验性优先：医学方法锚点强依赖样本、入排、随机化、盲法、测量、随访、统计模型等可复核字段。
- B5 局部具体性优先：讨论节用具体对象、限制和决策场景替代泛泛价值判断。

## 医学类高价值写作功能

- 阴性 RCT：用“neither X nor Y”“No significant difference”直接承认主终点未达成，同时分开安全性和探索性信号。
- 亚组/探索性结果：主动标注 “not the primary outcome” 和 “hypothesis generating”，避免把信号升级为结论。
- 盲法与偏倚控制：非药物干预或单盲试验会直说不能盲哪些角色，再写统计者单盲、自动测量或客观结局补救。
- 结果节密度控制：正文保留基线相似、主效应、时间轨迹和安全性，表格承载次要指标。
- 系统综述方法：双人筛选、分歧解决、语言限制、RoB domain、SMD/随机效应模型都写成可复核流程。
- 小效应解释：统计显著后立即说明 effect size small，再转到临床意义阈值。
- 局限性：从短随访、小样本、单中心、测量来源、语言限制、缺失处理、机制未验证等具体边界写起。
- 中文临床结果：用“组间比较 / 组内比较 / 安全性评价”组织，但要防止句式机械重复。

## 推荐给全局矩阵的候选摘录

1. `medicine_RCT_2021_peginterferon_lambda_covid19`, line 15, English, quote: "neither shortened ... nor improved symptoms"  
   推荐原因：阴性 RCT 摘要结论锚点；强对抗 A2/A28/B2 漂移。

2. `medicine_RCT_2021_peginterferon_lambda_covid19`, line 103, English, quote: "should only be considered hypothesis generating"  
   推荐原因：亚组探索降级锚点；适合作为 B2 证据强度守恒样例。

3. `medicine_RCT_2021_peginterferon_lambda_covid19`, line 121, English, quote: "not strictly “double-blind”"  
   推荐原因：方法透明度锚点；对抗 A36 和术语美化。

4. `medicine_RCT_2021_ai_coaching_cancer_survivors`, line 29, English, quote: "Baseline characteristics were similar"  
   推荐原因：基线表正文最小化样例；对抗 A25/A27 逐项复述。

5. `medicine_RCT_2021_ai_coaching_cancer_survivors`, line 33, English, quote: "early and sustained increase"  
   推荐原因：时间轨迹结果锚点；让结果段从终点数值转向曲线形态。

6. `medicine_RCT_2021_ai_coaching_cancer_survivors`, line 70, English, quote: "may not be generalizable"  
   推荐原因：外部效度边界锚点；对抗 A14 全景泛化。

7. `medicine_RCT_2025_wuti_balance_hypertension`, line 66, Chinese, quote: "故无法设计受试者和治疗者盲法"  
   推荐原因：中文非药物干预盲法边界；方法缺口不遮掩。

8. `medicine_RCT_2025_wuti_balance_hypertension`, line 95, Chinese, quote: "安全性分析采用描述性统计"  
   推荐原因：不同问题不同统计策略；避免安全性小事件硬检验。

9. `medicine_RCT_2025_wuti_balance_hypertension`, line 182, Chinese, quote: "未探索相关生物标志物和分子机制"  
   推荐原因：临床有效性与机制边界分离；对抗 A32 因果补全。

10. `medicine_meta_2023_china_multimorbidity_trend`, line 79, Chinese, quote: "患有 $\geqslant 2$ 种慢性病定义为共病"  
   推荐原因：操作性定义锚点；对抗 A31 概念解释。

11. `medicine_meta_2023_china_multimorbidity_trend`, line 175, Chinese, quote: "可能导致骨关节疾病的过量估计"  
   推荐原因：变量定义偏差方向锚点；强 B2/B4 样例。

12. `medicine_meta_2023_physical_activity_interventions`, line 17, English, quote: "The mean effect size was small"  
   推荐原因：显著但小效应的主动降温；对抗 A2 和夸大结论。

13. `medicine_meta_2023_physical_activity_interventions`, line 41, English, quote: "defned long term as at least 24 months"  
   推荐原因：无统一定义时给操作阈值；注意正式复用需修正 OCR。

14. `medicine_meta_2023_physical_activity_interventions`, line 169, English, quote: "interpreted with caution"  
   推荐原因：讨论首段谨慎解释锚点；与效应量和研究数量限制联动。

15. `medicine_meta_2023_physical_activity_interventions`, lines 163-165, English, quote: "no intervention components that were clearly associated"  
   推荐原因：拒绝强造机制答案；对抗 A32 完整因果链。

## 全局复用建议

- 医学锚点应优先进入“证据强度守恒”和“数值结果重构”矩阵；这些片段能直接纠正 AI 把临床结果写成宣传性胜利叙事的问题。
- 中文医学锚点适合补充 A29 的反例：保留必要的“组间/组内”功能性连接，但限制其重复密度。
- 英文 RCT 阴性结果适合做 A36 的正样本：作者可以出现，但出现方式是“we show / we conducted / we found no suggestion”，不是 editorial voice。
- 系统综述锚点适合补 A31/A32：方法选择由异质性、随访阈值、测量方式推出，而不是教科书解释。
- 所有医学锚点复用时必须守住人群、时间窗、结局、测量方式和统计口径；这些字段缺一项，医学语气就容易漂移。

# Rewrite Prescription Template

paragraph_id: P001
semantic_anchor_ref: P001
writing_function: method choice boundary
hit_modes: A31,A36
human_anchor:
  a_code_cards: 00_A1-A39_实践卡矩阵.md#A31; 00_A1-A39_实践卡矩阵.md#A36
  function_cards: 00_写作功能_实践卡矩阵.md#方法
  paper_practice_cards: 05_engineering/engineering_modeling_2022_sciml_pinns_review.md
  source_anchor_origin: _shared runtime practice cards
human_anchor_evidence:
  quote_exact: "Replace this with the real human source excerpt used as local context."
  source_locator: 05_engineering/engineering_modeling_2022_sciml_pinns_review.md#card-id-or-line
  source_decision: runtime_card
  observed_human_move: the author narrows a method choice by naming what the variables can and cannot prove
  why_this_quote_fits_user_paragraph: the user paragraph also overstates what the selected variables prove
  transferable_structure: method choice -> supported scope -> unsupported causal boundary
  non_transferable_surface: do not copy the source paper's variables, dataset, examples, or phrasing
  adaptation_plan: keep the user's variables and citation tokens, replace generic method praise with a scoped method-boundary sentence
rewrite_operation:
  delete: generic framework praise
  keep: Hofstede; IDV; PDI; 20; 91; [12]
  restructure_as: method choice first, then boundary of what the variables can and cannot prove
  evidence_boundary: descriptive comparison only; no causal claim
  sentence_rhythm: one compressed setup sentence plus one boundary sentence
  citation_number_policy: preserve all citation brackets and numeric values exactly
forbidden:
  - no new fact
  - no claim upgrade
  - no citation or number drift
  - no OCR/MinerU noise copying
verification_focus: A31 down, A36 down, no token drift

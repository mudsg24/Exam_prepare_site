import json
import os

questions = [
  {
    "id": "anca_gn_q01",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 1,
    "stem": "A 65-year-old man presents with a 3-week history of fatigue, low-grade fever, migratory arthralgias, and dark urine. Laboratory evaluation reveals serum creatinine 4.2 mg/dL (baseline 1.0 mg/dL), urinalysis showing dysmorphic red blood cells and red blood cell casts, and normal serum complement C3 and C4 levels. Serologic testing demonstrates a positive c-ANCA with high-titer antibodies against proteinase 3 (PR3-ANCA). A chest CT reveals bilateral pulmonary cavitary nodules. Which of the following is the most likely diagnosis?",
    "options": [
      {
        "id": "A",
        "text": "Granulomatosis with Polyangiitis (GPA)"
      },
      {
        "id": "B",
        "text": "Microscopic Polyangiitis (MPA)"
      },
      {
        "id": "C",
        "text": "Anti-Glomerular Basement Membrane (Anti-GBM) Disease"
      },
      {
        "id": "D",
        "text": "Lupus Nephritis Class IV"
      }
    ],
    "sourceProvidedAnswer": "A",
    "selectedOption": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "患者呈現 Rapidly Progressive Glomerulonephritis (RPGN)、正常血清 C3/C4、高滴度 PR3-ANCA (c-ANCA 陽性) 以及雙側肺部 Cavitary Nodules，此為 Granulomatosis with Polyangiitis (GPA) 的典型三聯表現。Microscopic Polyangiitis (MPA) 多為 MPO-ANCA (p-ANCA) 且無 Granulomatous Cavitary Lesions；Lupus Nephritis 會伴隨 Hypocomplementemia 與 Full-House 免疫沉積；Anti-GBM Disease 則為 Anti-α3(IV)NC1 抗體陽性且呈 Linear IF 圖譜。",
    "resolvedImages": [
      "/server-data/assets/Brenner_Fig_32_14.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q02",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 2,
    "stem": "In the molecular pathogenesis of ANCA-associated vasculitis and pauci-immune glomerulonephritis, which complement pathway component plays a critical role in priming neutrophils, promoting chemoattraction, and amplifying the inflammatory loop via its specific receptor CD88?",
    "options": [
      {
        "id": "A",
        "text": "Complement C1q binding to immune complexes"
      },
      {
        "id": "B",
        "text": "Complement C5a interacting with C5a Receptor (C5aR / CD88)"
      },
      {
        "id": "C",
        "text": "Complement C3b mediating opsonization via CR1"
      },
      {
        "id": "D",
        "text": "Membrane Attack Complex (C5b-9) causing direct podocyte lysis"
      }
    ],
    "sourceProvidedAnswer": "B",
    "selectedOption": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "ANCA 相關血管炎的核心分子致病機轉中，Alternative Complement Pathway 的活化會產生 Complement C5a，C5a 結合至 Neutrophils 表面之 C5a Receptor (C5aR / CD88)，驅動強烈之 Chemoattraction、Priming 以及 ANCA 自體抗原 (PR3 與 MPO) 易位至細胞膜上。這是新型標靶藥物 Avacopan (C5aR Antagonist) 作用的標的部位。C1q 與 C5b-9 則屬於 Classical Pathway 或 Complete Lytic Complex，在 Pauci-Immune 腎炎中不扮演主導的角色。",
    "resolvedImages": [
      "/server-data/assets/anca_netosis_ai.jpg"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q03",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 3,
    "stem": "A 58-year-old female presents with rapidly declining renal function (serum creatinine rising from 1.1 to 3.8 mg/dL over 2 weeks), hemoptysis due to pulmonary capillaritis, and dysmorphic hematuria. Serologic testing is positive for MPO-ANCA (p-ANCA). Renal biopsy demonstrates necrotizing crescentic glomerulonephritis. Immunofluorescence microscopy reveals absence of significant immunoglobulin or complement deposition. Which histopathologic category best describes this renal biopsy finding?",
    "options": [
      {
        "id": "A",
        "text": "Linear Immunoglobulin Glomerulonephritis"
      },
      {
        "id": "B",
        "text": "Full-House Immune Complex Glomerulonephritis"
      },
      {
        "id": "C",
        "text": "Pauci-Immune Necrotizing Crescentic Glomerulonephritis"
      },
      {
        "id": "D",
        "text": "Membranoproliferative Glomerulonephritis Type I"
      }
    ],
    "sourceProvidedAnswer": "C",
    "selectedOption": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "患者呈現 MPO-ANCA (p-ANCA) 陽性、Necrotizing Crescentic GN 且 Immunofluorescence 下缺乏或僅有微量 Immunoglobulin/Complement 沉積，定義上即為典型的 Pauci-Immune Necrotizing Crescentic Glomerulonephritis。Linear IF 為 Anti-GBM Disease 的標誌；Full-House 為 Lupus Nephritis 的特徵；MPGN 則伴隨大量 Subendothelial 免疫沉積與 Hypocomplementemia。",
    "resolvedImages": [
      "/server-data/assets/Brenner_Fig_32_16.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q04",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 4,
    "stem": "According to the Berden Histopathologic Classification of ANCA-Associated Glomerulonephritis, a renal biopsy showing 60% normal glomeruli (without fibrinoid necrosis or crescents) is classified into which histopathologic class, and what is its associated long-term renal outcome?",
    "options": [
      {
        "id": "A",
        "text": "Crescentic Class; associated with high risk of ESRD"
      },
      {
        "id": "B",
        "text": "Mixed Class; associated with unpredictable renal survival"
      },
      {
        "id": "C",
        "text": "Sclerotic Class; associated with irreversible renal failure"
      },
      {
        "id": "D",
        "text": "Focal Class; associated with the best long-term renal survival"
      }
    ],
    "sourceProvidedAnswer": "D",
    "selectedOption": "D",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "根據 Berden 分型 (Berden Histopathologic Classification)，凡腎臟切片中含有 ≥ 50% Normal Glomeruli 者，歸類為 Focal Class。Focal Class 代表大部分腎元結構未受嚴重壞死侵犯，在四種病理分型 (Focal, Crescentic, Mixed, Sclerotic) 中擁有最佳的長期腎臟存活率 (Best Long-Term Renal Survival)。",
    "resolvedImages": [
      "/server-data/assets/anca_berden_ai.jpg"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q05",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 5,
    "stem": "A 52-year-old male with severe MPO-ANCA vasculitis achieves complete clinical remission after 6 months of induction therapy. The treating nephrologist is selecting a maintenance regimen. According to the 2024 KDIGO Guideline Update, which of the following is the preferred first-line agent for maintenance therapy in ANCA-associated vasculitis?",
    "options": [
      {
        "id": "A",
        "text": "Rituximab (RTX)"
      },
      {
        "id": "B",
        "text": "Oral Cyclophosphamide"
      },
      {
        "id": "C",
        "text": "Continuous High-Dose Corticosteroids"
      },
      {
        "id": "D",
        "text": "Cyclosporine A"
      }
    ],
    "sourceProvidedAnswer": "A",
    "selectedOption": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "KDIGO 2024 指引強烈推薦 Rituximab (RTX) 作為 ANCA 相關血管炎 Remission 達成後的首選 Maintenance Therapy 藥物。MAINRITSAN Trial 實證顯示 RTX 在預防 Relapse 之效果顯著優於 Azathioprine。Cyclophosphamide 僅用於 Induction，不推薦用於 Maintenance；高劑量 Corticosteroids 會產生嚴重 Steroid Toxicity。",
    "resolvedImages": [
      "/server-data/assets/KDIGO_2024_ANCA_Fig_2.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q06",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 6,
    "stem": "The landmark PEXIVAS Trial evaluated the role of Plasma Exchange (PLEX) and glucocorticoid dosing in patients with ANCA-associated vasculitis. Which of the following represents the key conclusion of the PEXIVAS trial regarding Plasma Exchange?",
    "options": [
      {
        "id": "A",
        "text": "Routine Plasma Exchange significantly reduces 1-year all-cause mortality in all ANCA vasculitis patients."
      },
      {
        "id": "B",
        "text": "Plasma Exchange does not reduce the composite outcome of end-stage renal disease (ESRD) or death in unselected AAV patients."
      },
      {
        "id": "C",
        "text": "Plasma Exchange should completely replace induction chemotherapy with Rituximab or Cyclophosphamide."
      },
      {
        "id": "D",
        "text": "Plasma Exchange is superior to high-dose corticosteroids for inducing complete remission in non-severe disease."
      }
    ],
    "sourceProvidedAnswer": "B",
    "selectedOption": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "PEXIVAS Trial (目前最大的 AAV 隨機對照試驗) 的核心結論為：在未經篩選的 ANCA 相關血管炎患者中，加用 Plasma Exchange (PLEX) 並未能降低的主要終點 (ESRD 或死亡 Composite Outcome) 風險。因此 KDIGO 2024 已取消 PLEX 的常規推薦，僅保留於重度 DAH 伴低氧血症、Dual-Positive Anti-GBM 或極重度 AKI (Scr ≥ 5.7 mg/dL) 患者。",
    "resolvedImages": [
      "/server-data/assets/KDIGO_2024_ANCA_Table_1.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q07",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 7,
    "stem": "A 45-year-old man with active PR3-ANCA glomerulonephritis is started on induction therapy with Rituximab and Cyclophosphamide. To minimize steroid-induced toxicity while ensuring sustained remission, the nephrologist prescribes Avacopan. What is the precise pharmacological target and mechanism of action of Avacopan?",
    "options": [
      {
        "id": "A",
        "text": "Monoclonal antibody against CD20 on mature B cells"
      },
      {
        "id": "B",
        "text": "Competitive inhibitor of Inosine Monophosphate Dehydrogenase (IMPDH)"
      },
      {
        "id": "C",
        "text": "Selective oral antagonist of the Complement C5a Receptor (C5aR / CD88)"
      },
      {
        "id": "D",
        "text": "Direct inhibitor of C3 convertase preventing C3a and C3b cleavage"
      }
    ],
    "sourceProvidedAnswer": "C",
    "selectedOption": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Avacopan 為一高特異性口服 Complement C5a Receptor (C5aR / CD88) Antagonist。基於 ADVOCATE Trial 成果，Avacopan 能精準阻斷 C5a 趨化與活化 Neutrophils 的發炎迴路，成功替代或大幅減少口服 Corticosteroids 劑量，同時保留 C5b-9 MAC 的病原體防禦能力。CD20 為 Rituximab 標的；IMPDH 為 Mycophenolate 標的。",
    "resolvedImages": [
      "/server-data/assets/anca_avacopan_ai.jpg"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q08",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 8,
    "stem": "A 40-year-old woman taking Hydralazine for resistant hypertension presents with fever, polyarthralgia, purpura, and AKI. Laboratory workup reveals p-ANCA positive, MPO-ANCA high titer, and unexpectedly positive PR3-ANCA (dual ANCA positivity), along with positive Anti-Histone antibodies and ANA. Biopsy confirms pauci-immune crescentic GN. What is the most appropriate initial management step?",
    "options": [
      {
        "id": "A",
        "text": "Immediate discontinuation of Hydralazine and clinical monitoring"
      },
      {
        "id": "B",
        "text": "Immediate initiation of Plasma Exchange and high-dose intravenous Cyclophosphamide"
      },
      {
        "id": "C",
        "text": "Increase Hydralazine dosage and add Spironolactone"
      },
      {
        "id": "D",
        "text": "Lifelong maintenance therapy with Rituximab"
      }
    ],
    "sourceProvidedAnswer": "A",
    "selectedOption": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "此患者呈特徵性 Drug-Induced ANCA Vasculitis (由 Hydralazine 引發)，典型特徵包含：Dual ANCA Positivity (MPO-ANCA 與 PR3-ANCA 同時陽性)、Anti-Histone Antibodies 陽性及皮膚/關節/腎臟侵犯。處置的最高優先且必要的首要步驟為「立刻停用引發藥物 (Discontinuation of Hydralazine)」。大部分患者在停藥後症狀與 ANCA 滴度會逐漸消退；僅在器官衰竭嚴重時才需短期輔助免疫抑制劑。",
    "resolvedImages": [
      "/server-data/assets/anca_maintenance_ai.jpg"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q09",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 9,
    "stem": "When evaluating epidemiologic data regarding crescentic glomerulonephritis across different age groups, which immunopathologic category represents the most common cause of crescentic glomerulonephritis in elderly patients (> 60 years old)?",
    "options": [
      {
        "id": "A",
        "text": "Anti-Glomerular Basement Membrane (Anti-GBM) Glomerulonephritis"
      },
      {
        "id": "B",
        "text": "Immune Complex Crescentic Glomerulonephritis (e.g. IgA Nephritis)"
      },
      {
        "id": "C",
        "text": "Pauci-Immune Crescentic Glomerulonephritis (ANCA-Associated)"
      },
      {
        "id": "D",
        "text": "Post-Infectious Glomerulonephritis"
      }
    ],
    "sourceProvidedAnswer": "C",
    "selectedOption": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "根據 Brenner & Rector's The Kidney 統計，在所有年齡層中（特別是 >60 歲的中老年族群中），Pauci-Immune Crescentic Glomerulonephritis (ANCA 相關) 是引發 Crescentic GN / RPGN 最常見的病因 (>60% 以上)。Anti-GBM Disease 反而是 Crescentic GN 中佔比最少的類型。",
    "resolvedImages": [
      "/server-data/assets/Brenner_Fig_32_16.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q10",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 10,
    "stem": "A 35-year-old patient with long-standing severe asthma, nasal polyposis, and peripheral blood eosinophilia (eosinophil count 3,500/μL) develops foot drop (mononeuritis multiplex) and hematuria. Serum testing shows positive p-ANCA (MPO-ANCA). Biopsy of an affected skin lesion reveals granulomatous inflammation with marked eosinophilic infiltration. What is the diagnosis?",
    "options": [
      {
        "id": "A",
        "text": "Granulomatosis with Polyangiitis (GPA)"
      },
      {
        "id": "B",
        "text": "Eosinophilic Granulomatosis with Polyangiitis (EGPA)"
      },
      {
        "id": "C",
        "text": "Microscopic Polyangiitis (MPA)"
      },
      {
        "id": "D",
        "text": "Henoch-Schönlein Purpura (IgA Vasculitis)"
      }
    ],
    "sourceProvidedAnswer": "B",
    "selectedOption": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "嚴重 Asthma、Asthma-associated Nasal Polyps、顯著 Peripheral Eosinophilia、Mononeuritis Multiplex 加上 Eosinophil-Rich Granulomatous Inflammation，為 Eosinophilic Granulomatosis with Polyangiitis (EGPA / 舊稱 Churg-Strauss Syndrome) 的三大典型臨床階段。約 40-50% 的 EGPA 患者呈現 MPO-ANCA / p-ANCA 陽性。",
    "resolvedImages": [
      "/server-data/assets/Brenner_Fig_32_17.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q11",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 11,
    "stem": "Which of the following histologic features on renal biopsy represents an active, potentially reversible inflammatory lesion in ANCA-associated glomerulonephritis, rather than a chronic irreversible sclerotic scar?",
    "options": [
      {
        "id": "A",
        "text": "Fibrous crescent with complete collagen deposition"
      },
      {
        "id": "B",
        "text": "Global glomerulosclerosis with hyalinized matrix"
      },
      {
        "id": "C",
        "text": "Segmental fibrinoid necrosis with cellular crescent"
      },
      {
        "id": "D",
        "text": "Severe tubular atrophy and interstitial fibrosis (TA/IF > 50%)"
      }
    ],
    "sourceProvidedAnswer": "C",
    "selectedOption": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Segmental Fibrinoid Necrosis 與 Cellular Crescent (細胞性新月體) 代表正在發生的急性活動性發炎病變 (Active Inflammatory Lesions)，在強效免疫抑制劑治療下具有相當高比例的可逆性 (Reversibility)。相反地，Fibrous Crescents、Global Sclerosis 及 Severe TA/IF 均屬於不可逆的慢性纖維化瘢痕 (Chronic Irreversible Scarring)。",
    "resolvedImages": [
      "/server-data/assets/anca_berden_ai.jpg"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q12",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 12,
    "stem": "A 60-year-old patient with PR3-ANCA glomerulonephritis is in complete remission while receiving maintenance Rituximab. During routine follow-up at month 12, serum ANCA titer shows a 4-fold increase. Urinalysis shows no hematuria or proteinuria, and serum creatinine remains stable at 1.0 mg/dL. The patient feels completely well. According to KDIGO 2024 guidelines, what is the most appropriate management?",
    "options": [
      {
        "id": "A",
        "text": "Immediately administer high-dose IV Methylprednisolone pulse therapy"
      },
      {
        "id": "B",
        "text": "Switch maintenance therapy from Rituximab to Cyclophosphamide"
      },
      {
        "id": "C",
        "text": "Continue current plan and monitor clinical parameters closely without automatic immunosuppression escalation"
      },
      {
        "id": "D",
        "text": "Perform emergency plasma exchange to clear circulating ANCA"
      }
    ],
    "sourceProvidedAnswer": "C",
    "selectedOption": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "根據 KDIGO 2024 指引，單純的 Serum ANCA Titer 上升 (Seroconversion / Rising Titer) 在缺乏臨床發炎徵兆 (無血尿、無蛋白尿、無 eGFR 下降或全身症狀) 時，絕對不能作為自動加強免疫抑制劑的唯一理由！過度治療會顯著增加致命性感染與副作用。正確作為是維持密切臨床追蹤。",
    "resolvedImages": [
      "/server-data/assets/KDIGO_2024_ANCA_Fig_3.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q13",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 13,
    "stem": "Which of the following clinical factors is associated with the highest risk of relapse in patients with ANCA-associated vasculitis following remission induction?",
    "options": [
      {
        "id": "A",
        "text": "MPO-ANCA positivity"
      },
      {
        "id": "B",
        "text": "PR3-ANCA positivity and upper respiratory tract involvement"
      },
      {
        "id": "C",
        "text": "Renal-limited vasculitis phenotype"
      },
      {
        "id": "D",
        "text": "Complete seroconversion to ANCA negativity within 3 months"
      }
    ],
    "sourceProvidedAnswer": "B",
    "selectedOption": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "在 ANCA 相關血管炎中，PR3-ANCA (c-ANCA) 陽性、既往有 Relapse 史以及 Upper Respiratory Tract / Pulmonary Involvement 是預測疾病高復發率 (High Relapse Risk) 最顯著的臨床因子。這類患者在 KDIGO 2024 指引中被建議延長 Rituximab Maintenance 期間 (> 24 個月)。MPO-ANCA 及 Renal-Limited Disease 的復發率相對較低。",
    "resolvedImages": [
      "/server-data/assets/anca_maintenance_ai.jpg"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q14",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 14,
    "stem": "A 68-year-old male with end-stage renal disease secondary to MPO-ANCA pauci-immune glomerulonephritis has been on hemodialysis for 1 year. He has been in complete clinical remission for 9 months, though low-titer MPO-ANCA remains persistently detectable. He is being evaluated for kidney transplantation. What is the recommended strategy regarding transplantation in this patient?",
    "options": [
      {
        "id": "A",
        "text": "Kidney transplantation is strictly contraindicated until ANCA titers become completely negative."
      },
      {
        "id": "B",
        "text": "Kidney transplantation can safely proceed as he has been in clinical remission for > 6 months."
      },
      {
        "id": "C",
        "text": "The patient must undergo 12 months of bilateral nephrectomy before transplantation."
      },
      {
        "id": "D",
        "text": "Transplantation should be delayed until the patient completes 5 years of maintenance Cyclophosphamide."
      }
    ],
    "sourceProvidedAnswer": "B",
    "selectedOption": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "指引共識指出，ANCA 相關血管炎患者接受腎臟移植 (Kidney Transplantation) 的前提是「臨床完全緩解 (Complete Clinical Remission) 持續至少 6 個月」。即使血清中殘留低滴度 ANCA，只要臨床上完全無發炎活動性，並非移植的絕對禁忌症。移植後血管炎復發率低 (~5-10%) 且 graft survival 良好。",
    "resolvedImages": [
      "/server-data/assets/KDIGO_2024_ANCA_Fig_1.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q15",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 15,
    "stem": "Which of the following laboratory findings on kidney biopsy immunofluorescence microscopy effectively rules out Pauci-Immune Glomerulonephritis and points directly to Lupus Nephritis Class IV?",
    "options": [
      {
        "id": "A",
        "text": "Complete absence of IgG and C3 staining"
      },
      {
        "id": "B",
        "text": "Linear continuous staining of IgG along the glomerular basement membrane"
      },
      {
        "id": "C",
        "text": "'Full-House' intense staining for IgG, IgA, IgM, C3, and C1q"
      },
      {
        "id": "D",
        "text": "Pauci-immune staining with focal segmental C3 deposition"
      }
    ],
    "sourceProvidedAnswer": "C",
    "selectedOption": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Full-House Immunofluorescence (IgG, IgA, IgM, C3, C1q 強烈陽性) 是 Lupus Nephritis (狼瘡性腎炎) 的特徵性表現，能明確排除了以「IF 陰性或極微量沉積」為定義的 Pauci-Immune Glomerulonephritis。Linear IgG 代表 Anti-GBM Disease。",
    "resolvedImages": [
      "/server-data/assets/Brenner_Fig_32_14.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q16",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 16,
    "stem": "In patients with severe ANCA-associated glomerulonephritis requiring induction therapy, the PEXIVAS reduced-dose glucocorticoid regimen achieved which of the following outcomes compared to the standard-dose glucocorticoid regimen?",
    "options": [
      {
        "id": "A",
        "text": "Significantly higher rate of end-stage renal disease at 1 year"
      },
      {
        "id": "B",
        "text": "Non-inferior efficacy for remission and ESRD/death, with a significant reduction in serious infections"
      },
      {
        "id": "C",
        "text": "Higher rate of disease relapse during the first 6 months"
      },
      {
        "id": "D",
        "text": "Complete failure to achieve clinical remission"
      }
    ],
    "sourceProvidedAnswer": "B",
    "selectedOption": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "PEXIVAS Trial 的 Glucocorticoid 減量協定證實：減量組 (Reduced-Dose Glucocorticoids) 在達成 Remission 以及預防 Death / ESRD 上「不劣於 (Non-inferior)」傳統標準高劑量組，同時大幅降低了前 1 年發生嚴重感染 (Serious Infection) 的風險達 30-50%。因此 KDIGO 2024 指引強烈推薦採用減量類固醇方案。",
    "resolvedImages": [
      "/server-data/assets/KDIGO_2024_ANCA_Table_1.png"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q17",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 17,
    "stem": "A 62-year-old male with Propylthiouracil (PTU)-induced ANCA vasculitis presents with mild skin purpura and focal segmental necrotizing glomerulonephritis with eGFR 55 mL/min. In addition to stopping PTU, what is the characteristic serologic feature expected in drug-induced ANCA vasculitis caused by PTU or Hydralazine?",
    "options": [
      {
        "id": "A",
        "text": "Isolated high-titer Anti-dsDNA without ANCA antibodies"
      },
      {
        "id": "B",
        "text": "High reactivity against multiple target antigens, including dual MPO-ANCA and PR3-ANCA positivity"
      },
      {
        "id": "C",
        "text": "Isolated Anti-C1q antibodies with profound hypocomplementemia"
      },
      {
        "id": "D",
        "text": "Monoclonal IgA kappa paraproteinemia"
      }
    ],
    "sourceProvidedAnswer": "B",
    "selectedOption": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "藥物誘發型 ANCA 血管炎 (Drug-Induced ANCA Vasculitis, 如 PTU, Hydralazine, Levamisole 所致) 的血清學招牌特徵為「多重抗原反應性 (Multi-Antigen Reactivity)」，常出現 MPO-ANCA 與 PR3-ANCA 同時陽性 (Dual ANCA Positivity)，並常伴隨 Anti-Histone, Anti-Lactoferrin, Anti-Elastase Antibodies 陽性。",
    "resolvedImages": [
      "/server-data/assets/anca_maintenance_ai.jpg"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  },
  {
    "id": "anca_gn_q18",
    "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
    "questionNumber": 18,
    "stem": "According to the Brix Renal Risk Score for ANCA-Associated Glomerulonephritis, which combination of parameters is utilized to generate a numerical score that stratifies patients into low, medium, and high risk of progression to End-Stage Renal Disease (ESRD)?",
    "options": [
      {
        "id": "A",
        "text": "Percentage of normal glomeruli, percentage of tubular atrophy/interstitial fibrosis (TA/IF), and baseline eGFR"
      },
      {
        "id": "B",
        "text": "Serum ANCA titer, C3 level, and proteinuria severity"
      },
      {
        "id": "C",
        "text": "Patient age, gender, and presence of pulmonary hemorrhage"
      },
      {
        "id": "D",
        "text": "Percentage of cellular crescents, presence of arterial vasculitis, and serum uric acid"
      }
    ],
    "sourceProvidedAnswer": "A",
    "selectedOption": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Brix Renal Risk Score (2018 年建立) 結合了三項核心參數：(1) Percentage of Normal Glomeruli；(2) Percentage of Tubular Atrophy and Interstitial Fibrosis (TA/IF)；(3) Baseline eGFR (≥15 vs <15 mL/min)。此算式能比單純病理切片更精準地將患者分層為 Low, Medium, High Risk of ESRD。",
    "resolvedImages": [
      "/server-data/assets/anca_berden_ai.jpg"
    ],
    "nlmResponses": [],
    "qcStatus": "PENDING",
    "qcVerified": False
  }
]

paper_data = {
  "id": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
  "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
  "title": "2026 ANCA-Associated Glomerulonephritis (ANCA 相關腎絲球腎炎) 分子機轉、病理分型、KDIGO 2024 指引與臨床實戰",
  "sourceCategory": "2026 年主題練習",
  "year": 2026,
  "updatedAt": "2026-07-30T09:50:00.000Z",
  "questions": questions
}

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"
with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated question bank JSON at {paper_path} with {len(questions)} questions.")

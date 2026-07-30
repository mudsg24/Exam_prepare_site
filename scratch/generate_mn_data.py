import json
import os

tutorial_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials/2026_Membranous_nephropathy_(主題備考)_tutorial.json'
mcq_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Membranous_nephropathy_(主題備考).json'

os.makedirs(os.path.dirname(tutorial_path), exist_ok=True)
os.makedirs(os.path.dirname(mcq_path), exist_ok=True)

# 1. Build Tutorial JSON
tutorial_data = {
  "paperId": "2026_Membranous_nephropathy_(主題備考)",
  "title": "2026 Membranous Nephropathy (膜性腎病變) 分子標的、病理分型、KDIGO 2021 指引與臨床實戰",
  "sections": [
    {
      "id": "sec_1",
      "title": "Section 1: Molecular Autoantigens & Etiologic Classification of Membranous Nephropathy",
      "content": """### 拓撲陣列 (Topology Mapping Matrix)
* **Primary Autoantigens**:
  - **PLA2R (Phospholipase A2 Receptor)**: 占 Primary Membranous Nephropathy 約 70-80%。與 Serum Anti-PLA2R Titer、Disease Activity、Proteinuria 嚴格平行。
  - **THSD7A (Thrombospondin Type-1 Domain-Containing 7A)**: 占 3-5%。高達 20% 患者可能伴隨 Occult Malignancy。
  - **NELL1 (Neural EGFL-Like 1)**: 常與 Secondary Etiologies (Malignancy, Traditional Medicine, Lipoic Acid) 相關。
  - **EXT1/EXT2 (Exostosin 1/Exostosin 2)**: 主要出現在 Lupus Nephritis Class V (Membranous Lupus Nephritis)。
  - **Semaphorin 3B**: 主要出現在 Pediatric Membranous Nephropathy。
  - **PCDH7 & NCAM1**: 見於特定 Complement-rich 或 Autoimmune-associated 膜性腎病變。

### 鑑別對比表 (High-Yield Differential Comparison Table)
| Feature | Primary Membranous Nephropathy | Malignancy-Associated / Secondary MN |
| :--- | :--- | :--- |
| **Dominant IgG Subclass** | IgG4 predominance | IgG1, IgG2, or IgG3 predominance |
| **Glomerular Staining** | Diffuse subepithelial Anti-PLA2R (+), NO C1q | Anti-PLA2R (-), C1q (+), Full-House staining |
| **Hypercellularity** | Pure capillary thickening, NO mesangial/endocapillary proliferation | Mesangial or endocapillary hypercellularity present (>8 inflammatory cells/glomerulus) |
| **Ultrastructure** | Subepithelial deposits ONLY | Subepithelial + Subendothelial / Mesangial deposits + Tubuloreticular Inclusions |

### 機轉決策樹 (Pathophysiological Decision Tree)
```
[Adult Patient with Nephrotic Syndrome]
       │
       ├─► Check Serum Anti-PLA2R Antibody Titer
       │     ├─► Positive (>20 RU/mL) ──► High Specificity for Primary MN
       │     └─► Negative ──► Evaluate Secondary Etiologies
       │
       └─► Secondary Screening Panel:
             ├─► Malignancy Screening (Age > 65, Smoking > 20 pack-years, IgG1/IgG2 predominance)
             ├─► Infections (Hepatitis B, Hepatitis C, Syphilis)
             ├─► Drugs (NSAIDs, Penicillamine, Bucillamine, Gold)
             └─► Autoimmune (Lupus Class V: EXT1/EXT2 +, C1q +)
```

### 觀念避坑指南 (Conceptual Trap Analysis)
1. **IgG Subclass Trap**: Primary MN 以 IgG4 為主，而 Secondary / Solid Tumor-Associated MN 則以 IgG1 和 IgG2 為主。
2. **PLA2R Negative Trap**: 就算 Serum Anti-PLA2R 為負值，切片 Tissue Staining 仍可能呈 PLA2R 陽性；此外必須加做 THSD7A 與 NELL1。""",
      "diagrams": [
        {
          "id": "diag_1_1",
          "type": "ai_illustration",
          "path": "/server-data/assets/mn_autoantigens_mechanism.jpg",
          "caption": "Pathogenesis and Molecular Autoantigens in Membranous Nephropathy"
        },
        {
          "id": "diag_1_2",
          "type": "micrograph",
          "path": "/server-data/assets/Brenner_Table_42_7.png",
          "caption": "Brenner 11e Table 42.7: Distinguishing Primary from Malignancy-Associated Membranous Nephropathy"
        }
      ]
    },
    {
      "id": "sec_2",
      "title": "Section 2: Ultrastructural Staging & Histopathological Diagnosis",
      "content": """### 拓撲陣列 (Topology Mapping Matrix)
* **Ultrastructural EM Stages of Membranous Nephropathy**:
  - **Stage I**: Small subepithelial electron-dense deposits along the outer aspect of GBM without projections of basement membrane material.
  - **Stage II**: Projections of GBM material ("Spikes") extend between subepithelial electron-dense deposits (PAM / Silver stain demonstrates "spike formation").
  - **Stage III**: Deposits are completely surrounded and encircled by newly formed GBM material, producing marked GBM thickening.
  - **Stage IV**: Thickened GBM shows irregular lucent areas ("moth-eaten appearance") where electron-dense deposits have undergone resorption and clearing.

### 鑑別對比表 (High-Yield Differential Comparison Table)
| EM Stage | Light Microscopy (Silver/PAM Stain) | Electron Microscopy Features | Clinical Remission Potential |
| :--- | :--- | :--- | :--- |
| **Stage I** | Normal or mild diffuse thickening | Subepithelial deposits, NO GBM spikes | High responsiveness |
| **Stage II** | Distinct "Spikes" protruding outward | Projections of GBM between deposits | Active immune deposition |
| **Stage III** | Double-contour appearance / Encasement | Deposits completely encircled by GBM | Advanced structural lesion |
| **Stage IV** | Irregularly thickened GBM | Lucent, moth-eaten spaces after deposit clearing | Chronic scarring phase |

### 機轉決策樹 (Pathophysiological Decision Tree)
```
[In Situ Immune Complex Deposition in Subepithelial Space]
       │
       ▼
[Subepithelial IgG4 & C3 Accumulation]
       │
       ▼
[Complement Activation: C5b-9 Membrane Attack Complex (MAC)]
       │
       ▼
[Podocyte Cytoskeletal Rearrangement & Slit Diaphragm Disruption]
       │
       ▼
[Severe Non-selective Nephrotic Proteinuria]
```

### 觀念避坑指南 (Conceptual Trap Analysis)
1. **Stage IV vs Active Disease**: Stage IV 代表沉積物吸收後的修復期（Moth-eaten appearance），不一定代表免疫反應仍處於 Active Phase。
2. **C1q & Mesangial Deposit Trap**: 凡切片出現顯著 C1q 沉積、Mesangial Deposits 或 Endothelial Tubuloreticular Inclusions，極力暗示 Lupus Nephritis Class V 或 Secondary MN。""",
      "diagrams": [
        {
          "id": "diag_2_1",
          "type": "ai_illustration",
          "path": "/server-data/assets/mn_em_staging_pathology.jpg",
          "caption": "Four Ultrastructural Stages of Membranous Nephropathy under Electron Microscopy"
        },
        {
          "id": "diag_2_2",
          "type": "micrograph",
          "path": "/server-data/assets/Brenner_Fig_31_7.png",
          "caption": "Brenner 11e Fig 31.7: Ultrastructural Stages of Membranous Nephropathy"
        },
        {
          "id": "diag_2_3",
          "type": "micrograph",
          "path": "/server-data/assets/Brenner_Fig_31_8.png",
          "caption": "Brenner 11e Fig 31.8: EM Micrograph of Stage II Membranous Nephropathy with GBM Spikes"
        }
      ]
    },
    {
      "id": "sec_3",
      "title": "Section 3: Nephrotic Complications & Hypercoagulability Management",
      "content": """### 拓撲陣列 (Topology Mapping Matrix)
* **Hypercoagulability Risk in Membranous Nephropathy**:
  - **Highest Risk Among Glomerulopathies**: Membranous Nephropathy 擁有所有 Glomerular Diseases 中最高的 Thromboembolism (DVT, PE, RVT) 發生率。
  - **Renal Vein Thrombosis (RVT)**: 臨床表現為突發性 Flank Pain, Gross Hematuria, Acute Drop in eGFR, 及 Progressive Proteinuria。
  - **Pathophysiological Mechanisms**:
    1. Urinary Loss of Anticoagulants: Low-molecular-weight Antithrombin III, Protein S, and Plasminogen are lost in urine.
    2. Hepatic Overproduction: Compensatory hepatic synthesis of high-molecular-weight Fibrinogen, Factor V, Factor VIII, and VWF.
    3. Hemoconcentration & Platelet Hyperreactivity: Hypoalbuminemia leads to decreased intravascular volume and increased blood viscosity.

### 鑑別對比表 (High-Yield Differential Comparison Table)
| Clinical Parameter | Prophylactic Anticoagulation Indicated | Prophylactic Anticoagulation Withheld |
| :--- | :--- | :--- |
| **Serum Albumin Level** | Serum Albumin < 2.0 - 2.5 g/dL | Serum Albumin > 3.0 g/dL |
| **Bleeding Risk Score** | Low Bleeding Risk (NO history of GI bleeding or severe thrombocytopenia) | High Bleeding Risk (Active ulcer, severe hypertension) |
| **First-Line Anticoagulant** | Low-Molecular-Weight Heparin (LMWH) or Warfarin / DOACs | N/A |

### 機轉決策樹 (Pathophysiological Decision Tree)
```
[Membranous Nephropathy with Serum Albumin < 2.5 g/dL]
       │
       ▼
[Assess Bleeding Risk vs Thrombotic Risk]
       │
       ├─► High Bleeding Risk ──► Frequent Monitoring, Avoid Anticoagulation
       └─► Low Bleeding Risk ──► Initiate Prophylactic Anticoagulation (Warfarin / LMWH / DOAC)
                                       │
                                       ▼
                       [Continue until Serum Albumin > 3.0 g/dL]
```

### 觀念避坑指南 (Conceptual Trap Analysis)
1. **Albumin Threshold Trap**: Prophylactic Anticoagulation 的建議切點為 Serum Albumin < 2.0-2.5 g/dL，而非僅看蛋白尿總量。
2. **Renal Vein Thrombosis Presentation**: 若 MN 患者無預警出現單側腰痛 (Flank Pain) 或急劇腎功能惡化，第一時間必須排除 Renal Vein Thrombosis (RVT)。""",
      "diagrams": [
        {
          "id": "diag_3_1",
          "type": "ai_illustration",
          "path": "/server-data/assets/mn_hypercoagulation_rvt.jpg",
          "caption": "Pathophysiology of Hypercoagulability and Renal Vein Thrombosis in Membranous Nephropathy"
        },
        {
          "id": "diag_3_2",
          "type": "micrograph",
          "path": "/server-data/assets/Brenner_Table_31_5.png",
          "caption": "Brenner 11e Table 31.5: Pathologic Features of Nonlupus Membranous Nephropathy"
        }
      ]
    },
    {
      "id": "sec_4",
      "title": "Section 4: KDIGO 2021 Risk Stratification & Evidence-Based Therapeutics",
      "content": """### 拓撲陣列 (Topology Mapping Matrix)
* **KDIGO 2021 Risk Stratification for Primary MN**:
  - **Low Risk**: Normal eGFR AND UPCR < 3.5 g/d (or Anti-PLA2R < 20 RU/mL).
  - **Moderate Risk**: Normal eGFR AND UPCR 3.5 - 8.0 g/d (or Anti-PLA2R 20 - 50 RU/mL) stable over 6 months.
  - **High Risk**: UPCR > 8.0 g/d for > 6 months OR Anti-PLA2R > 50 RU/mL OR eGFR decline.
  - **Very High Risk**: Life-threatening Nephrotic Syndrome OR Rapidly Declining eGFR not attributable to complications.

### 鑑別對比表 (High-Yield Differential Comparison Table)
| Risk Category | Recommended Initial Immunosuppressive Therapy | Monitoring & Milestones |
| :--- | :--- | :--- |
| **Low Risk** | Conservative Management (Maximum tolerated RASi) for 6 months | Monitor UPCR, Serum Albumin, eGFR |
| **Moderate Risk** | Rituximab OR Calcineurin Inhibitor (Tacrolimus / Cyclosporine) | Check Anti-PLA2R titer at 3 & 6 months |
| **High Risk** | Rituximab OR Cyclophosphamide + Steroids (Modified Ponticelli Regimen) | Re-evaluate immunological response at 6 months |
| **Very High Risk** | Cyclophosphamide + Steroids (Modified Ponticelli Regimen) | Intensive eGFR and toxicities surveillance |

### 機轉決策樹 (Pathophysiological Decision Tree)
```
[Primary Membranous Nephropathy Diagnosis]
       │
       ├─► Low Risk ──► RASi Conservative Management for 6 months
       │
       ├─► Moderate Risk ──► Rituximab (1000 mg IV on Day 1 & 15) OR Tacrolimus
       │
       ├─► High Risk ──► Rituximab OR Modified Ponticelli Regimen
       │
       └─► Very High Risk ──► Alternating 6-month Cyclophosphamide + Corticosteroids
                                      │
                                      ▼
             [Monitor Serum Anti-PLA2R: Immunological Remission Precedes Clinical Remission]
```

### 觀念避坑指南 (Conceptual Trap Analysis)
1. **Immunological vs Clinical Remission Trap**: Anti-PLA2R 抗體效價下降 (Immunological Remission) 通常比 Proteinuria 的減少 (Clinical Remission) 早出數個月。不應因蛋白尿未立即過關而過早判定治療失敗。
2. **CNI Relapse Rate Trap**: Calcineurin Inhibitors (Tacrolimus/Cyclosporine) 停藥後 Relapse Rate 很高（高達 40-50%），因此常需長期維持或與 Rituximab 併用。""",
      "diagrams": [
        {
          "id": "diag_4_1",
          "type": "ai_illustration",
          "path": "/server-data/assets/mn_kdigo_algorithm_treatment.jpg",
          "caption": "KDIGO 2021 Decision Algorithm for Primary Membranous Nephropathy Risk Stratification and Management"
        },
        {
          "id": "diag_4_2",
          "type": "micrograph",
          "path": "/server-data/assets/Brenner_Fig_31_9.png",
          "caption": "Brenner 11e Fig 31.9: Immunofluorescence Micrograph of Granular PLA2R and IgG Capillary Staining"
        }
      ]
    }
  ]
}

with open(tutorial_path, 'w', encoding='utf-8') as f:
    json.dump(tutorial_data, f, ensure_ascii=False, indent=2)

print(f"Tutorial JSON successfully created: {tutorial_path}")

# 2. Build 18 MCQs Test Bank JSON
questions = [
  {
    "id": "q1",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 1,
    "stem": "A 52-year-old man presents with progressive lower extremity edema and nephrotic-range proteinuria (7.8 g/day). Serum creatinine is 1.0 mg/dL and serum albumin is 2.1 g/dL. Serum anti-PLA2R antibody titer is markedly elevated at 145 RU/mL. Which of the following immunofluorescence findings on kidney biopsy would be MOST characteristic of primary membranous nephropathy in this patient?",
    "options": [
      {"id": "A", "text": "Diffuse granular capillary loop staining predominantly for IgG4 and C3"},
      {"id": "B", "text": "Mesangial and subendothelial full-house staining for IgG, IgA, IgM, C3, and C1q"},
      {"id": "C", "text": "Linear basement membrane staining for IgG1 along the glomerular capillary wall"},
      {"id": "D", "text": "Granular staining predominantly for IgG1 and IgG2 with negative PLA2R staining"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "原發性膜性腎病變 (Primary Membranous Nephropathy) 最主要的 Target Autoantigen 為 M-type Phospholipase A2 Receptor (PLA2R)，占約 70-80%。其典型免疫螢光 (IF) 呈現極為特異的 Diffuse Granular Capillary Wall 沉積，且 Immunoglobulin Subclass 以 IgG4 及 C3 為主。相反地，Secondary MN (如 Solid Tumor 或 Lupus Class V) 則常呈現 IgG1/IgG2 沉積或 Full-house (C1q (+)) 沉積。",
    "resolvedImages": ["/server-data/assets/Brenner_Fig_31_9.png"]
  },
  {
    "id": "q2",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 2,
    "stem": "A 68-year-old male smoker presents with nephrotic syndrome. Renal biopsy reveals membranous nephropathy. Further serologic testing shows negative anti-PLA2R autoantibodies. Immunohistochemical staining of the biopsy specimen demonstrates glomerular deposition of IgG1 and IgG2, along with prominent infiltration of intra-glomerular inflammatory cells (> 8 per glomerulus). Which underlying cause should be MOST aggressively evaluated in this patient?",
    "options": [
      {"id": "A", "text": "Idiopathic podocyte injury secondary to APOL1 risk alleles"},
      {"id": "B", "text": "Occult solid organ malignancy (such as lung, colon, or gastric carcinoma)"},
      {"id": "C", "text": "Undiagnosed Type 1 Diabetes Mellitus with nodular glomerulosclerosis"},
      {"id": "D", "text": "Acute post-streptococcal glomerulonephritis"}
    ],
    "selectedOption": "B",
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "根據 Brenner 11e Table 42.7，Malignancy-Associated Membranous Nephropathy 的臨床與病理特徵包括：(1) 年齡 > 65 歲、吸菸史 > 20 pack-years；(2) 血清 Anti-PLA2R 陰性；(3) 切片呈 IgG1 及 IgG2 沉積為主（而非 IgG4）；(4) 腎絲球內有顯著發炎細胞浸潤 (> 8 inflammatory cells/glomerulus)。因此應積極排查 Occult Solid Organ Malignancy。",
    "resolvedImages": ["/server-data/assets/Brenner_Table_42_7.png"]
  },
  {
    "id": "q3",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 3,
    "stem": "Electron microscopy of a renal biopsy specimen from a patient with heavy proteinuria demonstrates subepithelial electron-dense deposits separated by projections of glomerular basement membrane material ('spike formation'). No subendothelial or mesangial deposits are identified. What is the ultrastructural EM stage of membranous nephropathy in this biopsy?",
    "options": [
      {"id": "A", "text": "Stage I"},
      {"id": "B", "text": "Stage II"},
      {"id": "C", "text": "Stage III"},
      {"id": "D", "text": "Stage IV"}
    ],
    "selectedOption": "B",
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Membranous Nephropathy 在電子顯微鏡 (EM) 下分為 4 個演進階段：Stage I 為單純 Subepithelial Deposits 無基底膜反應；Stage II 沉積物之間出現 GBM 材質突出，即銀染色可見的『Spike Formation』；Stage III 沉積物被 GBM 完全包覆 (Encircled)；Stage IV 為基底膜不規則增厚並出現透亮被吸收區 (Lucent moth-eaten spaces)。",
    "resolvedImages": ["/server-data/assets/Brenner_Fig_31_7.png", "/server-data/assets/Brenner_Fig_31_8.png"]
  },
  {
    "id": "q4",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 4,
    "stem": "A 45-year-old woman with membranous nephropathy and a serum albumin level of 1.7 g/dL develops sudden-onset left flank pain, gross hematuria, and an acute rise in serum creatinine from 0.9 mg/dL to 2.3 mg/dL. Which of the following complications is MOST likely responsible for her acute presentation?",
    "options": [
      {"id": "A", "text": "Acute pyelonephritis with perinephric abscess formation"},
      {"id": "B", "text": "Left renal vein thrombosis (RVT)"},
      {"id": "C", "text": "Crescentic transformation to anti-GBM disease"},
      {"id": "D", "text": "Drug-induced acute interstitial nephritis"}
    ],
    "selectedOption": "B",
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "膜性腎病變 (Membranous Nephropathy) 是所有腎絲球疾病中並發 Thromboembolism (特別是 Renal Vein Thrombosis, RVT) 風險最高者。當 Serum Albumin 低於 2.0 - 2.5 g/dL 時風險大幅劇增。RVT 的典型急性表現即為單側 Flank Pain、Gross Hematuria 以及腎功能急速惡化 (Acute drop in eGFR)。",
    "resolvedImages": ["/server-data/assets/mn_hypercoagulation_rvt.jpg"]
  },
  {
    "id": "q5",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 5,
    "stem": "According to the KDIGO 2021 Clinical Practice Guideline for Glomerular Diseases, which of the following patients with primary membranous nephropathy is classified as HIGH RISK for progressive loss of kidney function?",
    "options": [
      {"id": "A", "text": "A patient with UPCR of 2.1 g/d and normal eGFR after 6 months of conservative management"},
      {"id": "B", "text": "A patient with persistent UPCR > 8.0 g/d or anti-PLA2R antibody titer > 50 RU/mL"},
      {"id": "C", "text": "A patient with complete immunological remission and negative anti-PLA2R antibody titer"},
      {"id": "D", "text": "A patient with pediatric-onset Semaphorin 3B-associated membranous nephropathy"}
    ],
    "selectedOption": "B",
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "KDIGO 2021 指引將 Primary MN 進行 Risk Stratification：High Risk 的定義包括 UPCR > 8.0 g/d 持續超過 6 個月、Serum Anti-PLA2R Titer > 50 RU/mL、或 eGFR 不可逆下降。此類 High Risk 患者建議啟動 Immunosuppressive Therapy (如 Rituximab 或 Cyclophosphamide + Steroids)。",
    "resolvedImages": ["/server-data/assets/mn_kdigo_algorithm_treatment.jpg"]
  },
  {
    "id": "q6",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 6,
    "stem": "Which novel target autoantigen in membranous nephropathy is characteristically enriched in patients with secondary membranous nephropathy associated with traditional medicine use, lipoic acid exposure, or underlying solid malignancies?",
    "options": [
      {"id": "A", "text": "Exostosin 1 (EXT1)"},
      {"id": "B", "text": "Neural EGFL-Like 1 (NELL1)"},
      {"id": "C", "text": "Semaphorin 3B (SEMA3B)"},
      {"id": "D", "text": "Protocadherin 7 (PCDH7)"}
    ],
    "selectedOption": "B",
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "NELL1 (Neural EGFL-Like 1) 是近年發現的重要抗原標的，占膜性腎病變約 5-10%。NELL1-associated MN 的重要臨床特點在於其高度關聯二次性原因，特別是服用 Traditional Medicine (草藥/中藥)、Lipoic Acid (硫辛酸) 補充劑，或伴隨 Solid Organ Malignancy。",
    "resolvedImages": ["/server-data/assets/mn_autoantigens_mechanism.jpg"]
  },
  {
    "id": "q7",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 7,
    "stem": "A 38-year-old female with systemic lupus erythematosus (SLE) undergoes a kidney biopsy for 4.5 g/day proteinuria. Biopsy shows subepithelial immune deposits with strong C1q, IgA, IgM, IgG, and C3 staining ('full-house' immunofluorescence) and subendothelial tubuloreticular inclusions on electron microscopy. Which antigen marker is MOST specifically associated with this Class V lupus membranous nephropathy?",
    "options": [
      {"id": "A", "text": "Phospholipase A2 Receptor (PLA2R)"},
      {"id": "B", "text": "Exostosin 1 / Exostosin 2 (EXT1/EXT2)"},
      {"id": "C", "text": "Thrombospondin Type-1 Domain-Containing 7A (THSD7A)"},
      {"id": "D", "text": "Neural EGFL-Like 1 (NELL1)"}
    ],
    "selectedOption": "B",
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "EXT1/EXT2 (Exostosin 1 / Exostosin 2) 是 Lupus Nephritis Class V (Membranous Lupus Nephropathy) 最具特異性的 Biomarker (約占 30-40%)。此類患者 IF 呈 Full-house 反應 (C1q +)，且 EM 常見 Tubuloreticular Inclusions。",
    "resolvedImages": ["/server-data/assets/mn_autoantigens_mechanism.jpg"]
  },
  {
    "id": "q8",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 8,
    "stem": "Which of the following statements regarding the therapeutic management of primary membranous nephropathy with Calcineurin Inhibitors (CNIs, e.g., Tacrolimus or Cyclosporine) is CORRECT?",
    "options": [
      {"id": "A", "text": "CNIs achieve permanent cure with a relapse rate of less than 5% after drug discontinuation"},
      {"id": "B", "text": "CNIs have a high relapse rate (up to 40-50%) following abrupt withdrawal, often requiring prolonged maintenance"},
      {"id": "C", "text": "CNIs act primarily by inducing cytotoxic B-cell depletion via anti-CD20 monoclonal antibody pathways"},
      {"id": "D", "text": "CNIs are strictly contraindicated in patients with moderate-risk primary membranous nephropathy"}
    ],
    "selectedOption": "B",
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Calcineurin Inhibitors (Tacrolimus / Cyclosporine) 能藉由穩定 Podocyte Actin Cytoskeleton 及抑制 T-cell activation 迅速減少蛋白尿。然而其最大的臨床缺陷為 停藥後的高復發率 (Relapse rate 達 40-50%)，因此 KDIGO 指引建議 CNI 應維持治療至少 12 個月，或考慮與 Rituximab 聯合使用。",
    "resolvedImages": ["/server-data/assets/mn_kdigo_algorithm_treatment.jpg"]
  },
  {
    "id": "q9",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 9,
    "stem": "In the Modified Ponticelli Regimen used for very high-risk primary membranous nephropathy, what is the alternating 6-month treatment schedule?",
    "options": [
      {"id": "A", "text": "Alternating months of IV/oral Corticosteroids and oral Cyclophosphamide for 6 months"},
      {"id": "B", "text": "Monthly infusions of Rituximab combined with Mycophenolate Mofetil"},
      {"id": "C", "text": "Continuous Tacrolimus therapy for 3 months followed by Plasmapheresis"},
      {"id": "D", "text": "Intravenous Immunoglobulin (IVIG) alternating with ACE inhibitors"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Modified Ponticelli Regimen 是治療 High-risk / Very High-risk Primary MN 的古典強效方案，總療程為 6 個月，採用單雙數月份交替：第 1, 3, 5 個月給予 IV Methylprednisolone + Oral Prednisolone；第 2, 4, 6 個月給予 Oral Cyclophosphamide (2 mg/kg/day)。",
    "resolvedImages": ["/server-data/assets/mn_kdigo_algorithm_treatment.jpg"]
  },
  {
    "id": "q10",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 10,
    "stem": "What is the key clinical relationship between serum anti-PLA2R antibody titers and clinical response in patients undergoing immunosuppressive therapy for primary membranous nephropathy?",
    "options": [
      {"id": "A", "text": "Immunological remission (decline/disappearance of anti-PLA2R titers) precedes clinical remission (reduction in proteinuria) by months"},
      {"id": "B", "text": "Reduction in proteinuria occurs immediately, while anti-PLA2R titers remain elevated for several years"},
      {"id": "C", "text": "Anti-PLA2R titers correlate only with serum creatinine and show no relationship with proteinuria"},
      {"id": "D", "text": "Anti-PLA2R antibody levels increase during therapeutic response due to immune complex dissociation"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "血清 Anti-PLA2R 抗體效價是評估療效的『即時指標 (Real-time Biomarker)』。免疫緩解 (Immunological Remission, 抗體轉陰或大幅下降) 通常在啟動治療後 3-6 個月內發生，比臨床緩解 (Clinical Remission, 蛋白尿顯著下降) 早出數個月。因此抗體下降預示著未來的蛋白尿緩解。",
    "resolvedImages": ["/server-data/assets/mn_kdigo_algorithm_treatment.jpg"]
  },
  {
    "id": "q11",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 11,
    "stem": "A 58-year-old patient with severe nephrotic syndrome secondary to PLA2R-positive membranous nephropathy has a serum albumin of 1.6 g/dL. Which pathophysiological change MOST directly contributes to the severe hypercoagulable state in this patient?",
    "options": [
      {"id": "A", "text": "Urinary loss of Antithrombin III combined with increased hepatic synthesis of Fibrinogen"},
      {"id": "B", "text": "Massive urinary excretion of Factor VIII and Fibrinogen"},
      {"id": "C", "text": "Decreased hepatic production of Factor V and Factor VII"},
      {"id": "D", "text": "Isolated deficiency of von Willebrand factor (vWF)"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "腎病症候群 (Nephrotic Syndrome) 高凝血狀態 (Hypercoagulability) 的主要機轉為：低分子量抗凝血蛋白（如 Antithrombin III、Protein S）由尿液大量流失；同時肝臟為了補償低血清白蛋白而過度合成高分子量凝血因子（如 Fibrinogen、Factor V、Factor VIII）。二者疊加導致血液呈高凝狀態。",
    "resolvedImages": ["/server-data/assets/mn_hypercoagulation_rvt.jpg"]
  },
  {
    "id": "q12",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 12,
    "stem": "Which of the following light microscopy features on kidney biopsy would strongly suggest SECONDARY membranous nephropathy rather than idiopathic primary membranous nephropathy?",
    "options": [
      {"id": "A", "text": "Endocapillary hypercellularity and mesangial cell proliferation"},
      {"id": "B", "text": "Diffuse, uniform basement membrane thickening without cellular proliferation"},
      {"id": "C", "text": "Absence of inflammatory cell infiltration in capillary lumens"},
      {"id": "D", "text": "Isolated podocyte foot process effacement"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Primary Membranous Nephropathy 在光學顯微鏡 (LM) 下的典型特徵為『純粹的 GBM 均勻彌漫增厚』，完全沒有內皮或系膜細胞增生 (NO proliferation)。若切片出現顯著的 Endocapillary hypercellularity 或 Mesangial proliferation，應高度懷疑 Secondary MN (如 SLE Class V, Cancer, Sjogren)。",
    "resolvedImages": ["/server-data/assets/Brenner_Table_31_5.png"]
  },
  {
    "id": "q13",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 13,
    "stem": "A 28-year-old woman is diagnosed with primary membranous nephropathy with anti-PLA2R positivity. Her eGFR is 95 mL/min/1.73m2 and 24-hour urine protein is 2.8 g/day. According to KDIGO 2021 guidelines, what is the initial management strategy?",
    "options": [
      {"id": "A", "text": "Immediate initiation of high-dose intravenous Cyclophosphamide"},
      {"id": "B", "text": "Maximal tolerated dose of ACE inhibitor or ARB for at least 6 months"},
      {"id": "C", "text": "Urgent bilateral nephrectomy"},
      {"id": "D", "text": "Intravenous Rituximab 1000 mg combined with plasma exchange"}
    ],
    "selectedOption": "B",
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "根據 KDIGO 2021 指引，該患者 eGFR 正常且蛋白尿 < 3.5 g/day，屬於 Low Risk 分組。Low Risk 患者有相當高比例 (> 30-40%) 會發生 Spontaneous Remission，首選治療為使用最高耐受劑量的 RASi (ACEi/ARB) 進行保守治療並追蹤至少 6 個月，暫不需啟動免疫抑制劑。",
    "resolvedImages": ["/server-data/assets/mn_kdigo_algorithm_treatment.jpg"]
  },
  {
    "id": "q14",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 14,
    "stem": "Which of the following drugs is a well-established cause of drug-induced secondary membranous nephropathy?",
    "options": [
      {"id": "A", "text": "Bucillamine and D-Penicillamine"},
      {"id": "B", "text": "Metformin"},
      {"id": "C", "text": "Loop diuretics (Furosemide)"},
      {"id": "D", "text": "Sodium-glucose cotransporter-2 (SGLT2) inhibitors"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "藥物引起之 Secondary Membranous Nephropathy 的常見致病藥物包括：D-Penicillamine、Bucillamine (常用於類風濕性關節炎)、NSAIDs、Gold salts、及 Captopril。停藥後蛋白尿通常可逐漸緩解。",
    "resolvedImages": ["/server-data/assets/Brenner_Table_31_5.png"]
  },
  {
    "id": "q15",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 15,
    "stem": "What component of the complement cascade is directly implicated in causing podocyte injury, slit diaphragm detachment, and subepithelial deposit formation in membranous nephropathy?",
    "options": [
      {"id": "A", "text": "C5b-9 Membrane Attack Complex (MAC)"},
      {"id": "B", "text": "C1q monomer isolated without antibody binding"},
      {"id": "C", "text": "Factor H autoantibodies without C3 involvement"},
      {"id": "D", "text": "Manose-binding lectin in isolation"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "在 Membranous Nephropathy 中，In situ 原位免疫複合物形成後會激活補體路徑，最終生成 C5b-9 Membrane Attack Complex (MAC)。C5b-9 插入 Podocyte 膜上致使 Podocyte 產生 Reactive Oxygen Species (ROS)、足細胞骨架重排及 Slit Diaphragm 破壞，進而導致蛋白尿。",
    "resolvedImages": ["/server-data/assets/mn_autoantigens_mechanism.jpg"]
  },
  {
    "id": "q16",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 16,
    "stem": "In Stage IV membranous nephropathy under electron microscopy, what characteristic morphological appearance is seen in the glomerular basement membrane?",
    "options": [
      {"id": "A", "text": "Irregularly thickened GBM with lucent, moth-eaten areas due to deposit resorption"},
      {"id": "B", "text": "Dense continuous ribbon-like intramembranous deposit replacing lamina densa"},
      {"id": "C", "text": "Widespread subendothelial deposits with double-contour splitting"},
      {"id": "D", "text": "Complete absence of basement membrane structure"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "EM Stage IV Membranous Nephropathy 的特徵為基底膜顯著且不規則增厚，先前在 Subepithelial 空間的 Electron-dense deposits 逐漸被清創與吸收，留下缺損的『Lucent, moth-eaten appearance (蟲蝕狀透亮區)』。",
    "resolvedImages": ["/server-data/assets/Brenner_Fig_31_7.png"]
  },
  {
    "id": "q17",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 17,
    "stem": "Which antibody marker in primary membranous nephropathy accounts for approximately 3-5% of cases and is notable for having up to a 20% association with underlying occult malignancy?",
    "options": [
      {"id": "A", "text": "Thrombospondin Type-1 Domain-Containing 7A (THSD7A)"},
      {"id": "B", "text": "Anti-PLA2R antibody"},
      {"id": "C", "text": "Anti-GBM antibody"},
      {"id": "D", "text": "Anti-double stranded DNA antibody"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "THSD7A (Thrombospondin Type-1 Domain-Containing 7A) 是第二個被確定的 Primary MN 自體抗原 (占 3-5%)。臨床上 THSD7A 陽性患者中約有 高達 20% 被發現伴隨 隱性腫瘤 (Occult Malignancy)，因此 THSD7A 陽性者仍應維持適當的癌症篩檢。",
    "resolvedImages": ["/server-data/assets/mn_autoantigens_mechanism.jpg"]
  },
  {
    "id": "q18",
    "paperId": "2026_Membranous_nephropathy_(主題備考)",
    "questionNumber": 18,
    "stem": "A 60-year-old male with high-risk primary membranous nephropathy (anti-PLA2R > 180 RU/mL, UPCR 11.2 g/day) is being evaluated for prophylactic anticoagulation. His serum albumin is 1.8 g/dL. What is the recommended decision regarding anticoagulation according to evidence-based nephrology guidelines?",
    "options": [
      {"id": "A", "text": "Initiate prophylactic anticoagulation (e.g., Warfarin or LMWH) after confirming low bleeding risk, because serum albumin is < 2.0-2.5 g/dL"},
      {"id": "B", "text": "Withhold anticoagulation completely regardless of serum albumin because anticoagulants increase podocyte apoptosis"},
      {"id": "C", "text": "Administer high-dose Aspirin only, as oral anticoagulants are ineffective in nephrotic syndrome"},
      {"id": "D", "text": "Anticoagulation is indicated only if the patient has already suffered a confirmed pulmonary embolism"}
    ],
    "selectedOption": "A",
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "膜性腎病變患者當 Serum Albumin < 2.0 - 2.5 g/dL 時，發生 VTE / RVT 的風險顯著攀升。只要經出血風險評估 (Bleeding Risk Assessment) 判定為 Low Bleeding Risk，指引強烈建議投予 預防性抗凝血治療 (Prophylactic Anticoagulation with LMWH or Warfarin / DOAC)，直至 Serum Albumin 提升回 > 3.0 g/dL。",
    "resolvedImages": ["/server-data/assets/mn_hypercoagulation_rvt.jpg"]
  }
]

mcq_data = {
  "id": "2026_Membranous_nephropathy_(主題備考)",
  "paperId": "2026_Membranous_nephropathy_(主題備考)",
  "title": "2026 Membranous Nephropathy (膜性腎病變) 腎專主題精選與實戰模擬題庫",
  "filename": "2026_Membranous_nephropathy_(主題備考).json",
  "sourceCategory": "2026 GN",
  "year": 2026,
  "questionCount": len(questions),
  "hasTutorial": True,
  "tutorialFilename": "tutorials/2026_Membranous_nephropathy_(主題備考)_tutorial.json",
  "questions": questions
}

with open(mcq_path, 'w', encoding='utf-8') as f:
    json.dump(mcq_data, f, ensure_ascii=False, indent=2)

print(f"MCQ Bank JSON successfully created: {mcq_path} (Question count: {len(questions)})")

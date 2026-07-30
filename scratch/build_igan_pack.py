import json
import os
import shutil

# Paths
SITE_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site"
PUBLIC_DATA_DIR = os.path.join(SITE_DIR, "public/server-data")
ASSETS_DIR = os.path.join(PUBLIC_DATA_DIR, "assets")
TUTORIALS_DIR = os.path.join(PUBLIC_DATA_DIR, "tutorials")
MANIFEST_PATH = os.path.join(PUBLIC_DATA_DIR, "exams_manifest.json")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(TUTORIALS_DIR, exist_ok=True)

# Copy reference images from PDF Outputs to public/server-data/assets/
REF_IMAGE_COPIES = [
    ("/Users/yuan/Projects/PDF/Outputs/2020 Brenner 11e/31. Primary Glomerular Disease/Fig_31_26.png", "Brenner_Fig_31_26.png"),
    ("/Users/yuan/Projects/PDF/Outputs/2020 Brenner 11e/31. Primary Glomerular Disease/Fig_31_27.png", "Brenner_Fig_31_27.png"),
    ("/Users/yuan/Projects/PDF/Outputs/2020 Brenner 11e/31. Primary Glomerular Disease/Fig_31_28.png", "Brenner_Fig_31_28.png"),
    ("/Users/yuan/Projects/PDF/Outputs/2020 Brenner 11e/31. Primary Glomerular Disease/Fig_31_29.png", "Brenner_Fig_31_29.png"),
    ("/Users/yuan/Projects/PDF/Outputs/2020 Brenner 11e/33. Treatment of Glomerulonephritis/Fig_33_1.png", "Brenner_Fig_33_1.png"),
    ("/Users/yuan/Projects/PDF/Outputs/KDIGO/KDIGO-2025-IgAN-IgAV-Guideline/Fig_1.png", "KDIGO_2025_IgAN_Fig_1.png"),
    ("/Users/yuan/Projects/PDF/Outputs/KDIGO/KDIGO-2025-IgAN-IgAV-Guideline/Fig_2.png", "KDIGO_2025_IgAN_Fig_2.png"),
    ("/Users/yuan/Projects/PDF/Outputs/KDIGO/KDIGO-2025-IgAN-IgAV-Guideline/Fig_3.png", "KDIGO_2025_IgAN_Fig_3.png"),
    ("/Users/yuan/Projects/PDF/Outputs/KDIGO/KDIGO-2025-IgAN-IgAV-Guideline/Fig_4.png", "KDIGO_2025_IgAN_Fig_4.png")
]

for src, fname in REF_IMAGE_COPIES:
    if os.path.exists(src):
        dst = os.path.join(ASSETS_DIR, fname)
        shutil.copy2(src, dst)
        print(f"Copied {fname}")

# Copy AI generated illustrations
AI_IMAGE_COPIES = [
    ("/Users/yuan/.gemini/antigravity/brain/4d13912f-62b0-407a-9d9f-3f8246bf28b0/igan_pathogenesis_ai_1785377245752.jpg", "igan_pathogenesis_ai.jpg"),
    ("/Users/yuan/.gemini/antigravity/brain/4d13912f-62b0-407a-9d9f-3f8246bf28b0/igan_supportive_ai_1785377258313.jpg", "igan_supportive_ai.jpg")
]

for src, fname in AI_IMAGE_COPIES:
    if os.path.exists(src):
        dst = os.path.join(ASSETS_DIR, fname)
        shutil.copy2(src, dst)
        print(f"Copied AI Image {fname}")

# 1. Masterclass Lecture JSON
tutorial_data = {
    "paperId": "2026_IgA_Nephropathy_(主題備考)",
    "tutorialTitle": "TSN 腎臟專科考點精華：IgA Nephropathy (IgAN) 臨床診斷、Oxford MEST-C 分級與最新治療指引",
    "lastUpdated": "2026-07-30",
    "sections": [
        {
            "id": "sec_1",
            "title": "Pathogenesis & Multi-Hit Hypothesis (Gd-IgA1, MEST-C Score & Podocytopathic Variant)",
            "content": """IgA Nephropathy (IgAN) 是全球最常見的原發性腎小球腎炎 (Primary Glomerular Disease)。其發病機轉嚴格遵從 **Four-Hit Hypothesis**：

1. **Hit 1 (Aberrant Galactosylation)**：在腸道黏膜關聯淋巴組織 (MALT, Peyer's patches) 中，B cells 受刺激產生 **Galactose-deficient IgA1 (Gd-IgA1)**。
2. **Hit 2 (Autoantibody Formation)**：循環中產生針對 Gd-IgA1 鉸鏈區 (hinge region) O-glycans 的 IgG 或 IgA **autoantibodies**。
3. **Hit 3 (Immune Complex Formation)**：Gd-IgA1 與 autoantibodies 結合形成大分子 **circulating immune complexes**。
4. **Hit 4 (Mesangial Deposition & Complement Activation)**：免疫複合物沉積於腎小球系膜區 (Mesangium)，活化替代途徑 (Alternative Pathway) 與凝集素途徑 (Lectin Pathway) 之 **Complement C3**，誘發系膜細胞增生 (Mesangial hypercellularity)、基質擴張 (Matrix expansion) 與腎絲球硬化。

#### Oxford Classification (MEST-C Score)
Oxford 分級為判斷 IgAN 預後與指引治療之金標準：
- **M (Mesangial hypercellularity)**: M0 (<= 0.5) vs M1 (> 0.5)
- **E (Endocapillary hypercellularity)**: E0 (absent) vs E1 (present, 提示活動性發炎)
- **S (Segmental glomerulosclerosis)**: S0 (absent) vs S1 (present)
- **T (Tubular atrophy / Interstitial fibrosis)**: T0 (<= 25%), T1 (26-50%), T2 (> 50%, 最強獨立預後因子)
- **C (Crescent)**: C0 (absent), C1 (< 25%), C2 (>= 25%)

#### Podocytopathic IgAN Variant (MCD-like IgAN)
極少數 IgAN 患者臨床呈現 Full-blown Nephrotic Syndrome (大量蛋白尿 > 3.5 g/d、低血清白蛋白、水腫)，但腎切片光學顯微鏡僅呈現輕微系膜增生，電子顯微鏡 (EM) 則可見廣泛的 **Podocyte Foot Process Effacement**。KDIGO 指引建議此特殊變異型應比照 **Minimal Change Disease (MCD)**，給予高劑量 Systemic Glucocorticoids 治療，通常能獲得快速緩解 (Rapid Remission)。""",
            "diagrams": [
                {
                    "id": "diag_1_1",
                    "type": "micrograph",
                    "caption": "Brenner 11e Fig 31.26: Immunofluorescence micrograph showing intense mesangial staining for IgA.",
                    "imagePath": "/server-data/assets/Brenner_Fig_31_26.png"
                },
                {
                    "id": "diag_1_2",
                    "type": "ai_illustration",
                    "caption": "Pathophysiological Decision Tree: Four-Hit Hypothesis of IgA Nephropathy.",
                    "imagePath": "/server-data/assets/igan_pathogenesis_ai.jpg"
                }
            ],
            "tables": [
                {
                    "title": "Oxford Classification MEST-C Score Summary Matrix",
                    "headers": ["Pathological Feature", "Definition / Cutoff", "Clinical & Therapeutic Significance"],
                    "rows": [
                        ["M (Mesangial hypercellularity)", "M0: <=50% glomeruli; M1: >50% glomeruli", "Prognostic marker of glomerular injury."],
                        ["E (Endocapillary hypercellularity)", "E0: Absent; E1: Present in any glomerulus", "Active inflammation; potentially responsive to immunosuppression."],
                        ["S (Segmental glomerulosclerosis)", "S0: Absent; S1: Present", "Indicates irreversible structural scarring and podocyte injury."],
                        ["T (Tubular atrophy/Fibrosis)", "T0: <=25%; T1: 26-50%; T2: >50%", "Strongest independent predictor of eGFR decline and ESKD risk."],
                        ["C (Crescents)", "C0: 0%; C1: <25%; C2: >=25%", "Reflects acute necrotizing injury; C2 requires active consideration."]
                    ]
                }
            ],
            "trapAnalysis": [
                {
                    "title": "Crescents without Rapidly Progressive Renal Failure",
                    "description": "腎切片若發現 Crescents，但患者 serum creatinine 完全穩定、無 eGFR 快速下降者，不應判定為 Rapidly Progressive IgAN (RPGN)。KDIGO 指引強調此類情況不應盲目啟動強效 immunosuppressive therapy，而應先優化非免疫支持治療並密切監測。"
                }
            ]
        },
        {
            "id": "sec_2",
            "title": "Clinical Presentations & Pathology (Hematuria, IF IgA/C3/C1q-neg vs Lupus)",
            "content": """IgA Nephropathy 在臨床上最典型的發病模式為 **Synpharyngitic Gross Hematuria** (在急性上呼吸道感染後 1-2 天內即出現肉眼血尿，與 Poststreptococcal Glomerulonephritis [PSGN] 感染後需等待 1-3 週之 Latent Period 形成鮮明對比)。

#### Immunofluorescence & Electron Microscopy Diagnosis
- **Immunofluorescence (IF)**：呈現顯著的 **Mesangial IgA Deposition** (通常與 C3 共沉積)。最關鍵之鑑別點：
  - IgAN 的 IgA 輕鏈常呈現 **Lambda > Kappa** 傾向。
  - **C1q 呈 Negative**。若切片同時出現強烈 C1q、IgG、IgM、IgA 全陽性 (Full-House Pattern)，必須強烈懷疑 **Lupus Nephritis Class III/IV**。
- **Electron Microscopy (EM)**：特徵為 **Mesangial and Subendothelial Electron-Dense Deposits**。若觀察到龐大 Subepithelial Humps，則應考量 PSGN。""",
            "diagrams": [
                {
                    "id": "diag_2_1",
                    "type": "micrograph",
                    "caption": "Brenner 11e Fig 31.29: Light micrograph showing segmental mesangial matrix expansion and hypercellularity.",
                    "imagePath": "/server-data/assets/Brenner_Fig_31_29.png"
                },
                {
                    "id": "diag_2_2",
                    "type": "micrograph",
                    "caption": "Brenner 11e Fig 31.28: Electron micrograph showing mesangial dense deposits.",
                    "imagePath": "/server-data/assets/Brenner_Fig_31_28.png"
                }
            ],
            "tables": [
                {
                    "title": "Differential Comparison: IgAN vs Lupus Nephritis vs PSGN",
                    "headers": ["Diagnostic Feature", "IgA Nephropathy", "Lupus Nephritis (Class III/IV)", "Poststreptococcal GN"],
                    "rows": [
                        ["Clinical Timing", "Synpharyngitic (1-2 days post-URI)", "Systemic flare (ANA/dsDNA positive)", "Post-infectious (1-3 weeks post-strep)"],
                        ["IF Deposition", "IgA dominant/co-dominant, C3 (+)", "IgG, IgM, IgA, C3, C1q (Full-House)", "C3 'starry sky' / 'lumpy-bumpy'"],
                        ["C1q Staining", "Strictly Negative", "Strongly Positive", "Usually Negative"],
                        ["Serum Complement", "Normal C3 and C4", "Low C3 and Low C4", "Low C3, Normal C4 (transient 8 wks)"]
                    ]
                }
            ],
            "trapAnalysis": [
                {
                    "title": "Normal Serum Complement in IgAN",
                    "description": "血清 C3 與 C4 在 IgAN 患者中通常維持在正常範圍 (Normal)。若發現血清 C3 / C4 顯著降低，應轉向思考 Lupus Nephritis, MPGN 或 PSGN。"
                }
            ]
        },
        {
            "id": "sec_3",
            "title": "Optimized Supportive Care & Novel Non-Immunosuppressive Therapies (RAASi, SGLT2i, Sparsentan / ERA)",
            "content": """KDIGO 最新指引強調，所有 IgAN 患者在考慮免疫抑制劑前，必須接受 **至少 3-6 個月極大化支持治療 (Optimized Supportive Care)**。

#### 1. RAAS Blockade (ACEi / ARB)
- 為第一線治療，應逐步滴定至患者最大可耐受劑量 (Maximal Tolerated Dose)。
- 蛋白尿控制目標：Urinary Protein Excretion < 0.5-1.0 g/day。

#### 2. SGLT2 Inhibitors (Dapagliflozin / Empagliflozin)
- **DAPA-CKD** 與 **EMPA-KIDNEY** 臨床試驗奠定 SGLT2i 於 IgAN 的核心地位。
- 機制：藉由活化致密斑 (Macula Densa) 之 Tubuloglomerular Feedback (TGF)，誘發入球小動脈 (Afferent Arteriole) 收縮，降低腎絲球內高壓 (Intraglomerular Hypertension)。
- 臨床考點：使用 SGLT2i 初期可能出現 **Initial eGFR Dip (up to 30%)**，此為血流動力學效應，不應停藥。長期追蹤可顯著減緩 eGFR 衰退速率。

#### 3. Sparsentan (Dual Endothelin & Angiotensin Receptor Antagonist)
- 雙重抑制 **Endothelin Type A (ETA)** 區受體與 **Angiotensin II Type 1 (AT1)** 受體。
- **PROTECT Trial** 證實 Sparsentan 在降低蛋白尿方面顯著優於傳統最大劑量 Irbesartan，且具備優秀之腎臟保護作用。""",
            "diagrams": [
                {
                    "id": "diag_3_1",
                    "type": "micrograph",
                    "caption": "KDIGO 2025 IgAN Guideline Fig 3: Treatment targets and positioning of non-immunosuppressive drugs in IgAN.",
                    "imagePath": "/server-data/assets/KDIGO_2025_IgAN_Fig_3.png"
                },
                {
                    "id": "diag_3_2",
                    "type": "ai_illustration",
                    "caption": "Glomerular Hemodynamics: Mechanisms of Sparsentan and SGLT2 Inhibitors in IgAN.",
                    "imagePath": "/server-data/assets/igan_supportive_ai.jpg"
                }
            ],
            "tables": [
                {
                    "title": "High-Yield Summary: Novel Non-Immunosuppressive Therapies in IgAN",
                    "headers": ["Drug Class / Agent", "Primary Mechanism", "Key Clinical Nuance & Trial Evidence"],
                    "rows": [
                        ["RAAS Inhibitors (ACEi/ARB)", "Efferent arteriolar vasodilation", "First-line baseline care; titrate to max tolerated dose."],
                        ["SGLT2 Inhibitors (Dapa/Empa)", "Afferent arteriolar vasoconstriction via TGF", "Reduces hyperfiltration; expect initial eGFR dip; DAPA-CKD."],
                        ["Sparsentan (Dual ERA/ARB)", "Dual ETA and AT1 receptor blockade", "Superior proteinuria reduction vs irbesartan; PROTECT trial."]
                    ]
                }
            ],
            "trapAnalysis": [
                {
                    "title": "eGFR Dip Handling with SGLT2 Inhibitors",
                    "description": "開始使用 SGLT2i 後前 2-4 週內出現 <30% 的 eGFR 下降屬於預期的血流動力學反應。只要 serum potassium 與安全性指標穩定，絕不可因 Initial eGFR Dip 貿然中斷 SGLT2i 治療。"
                }
            ]
        },
        {
            "id": "sec_4",
            "title": "Immunosuppressive Guidelines & Decision-Making (Systemic Steroids, Nefecon / TRF-Budesonide, MMF, RPGN)",
            "content": """當患者經 3-6 個月極大化支持治療後，蛋白尿仍持續 > 0.75-1.0 g/day，且 eGFR >= 30 mL/min/1.73m2 時，始需考量免疫抑制治療。

#### 1. Targeted-Release Budesonide (Nefecon / TRF-Budesonide)
- 專門設計於迴腸末端 (Distal Ileum) 腸溶包衣釋放的局部類固醇，精準作用於 Peyer's patches。
- **NefIgArd Trial** 證明 Nefecon 能顯著降低 Gd-IgA1 產生、降低蛋白尿並延緩 eGFR 下降，且全身性類固醇副作用遠低於口服 Prednisone。

#### 2. Systemic Glucocorticoids (TESTING Trial Protocol)
- **TESTING Trial** 顯示高劑量口服 Oral Steroids (Full-dose Prednisone 0.6-0.8 mg/kg/d) 雖能降低腎衰竭風險，但嚴重感染 (Severe Serious Adverse Events) 風險極高。
- 修正後的 **Reduced-dose Corticosteroid Protocol** (0.4 mg/kg/d + Pneumocystis jirovecii 預防性抗生素如 TMP-SMX) 展現更佳之利益風險比 (Benefit-Risk Profile)。

#### 3. Mycophenolate Mofetil (MMF)
- KDIGO 指引指出，MMF 在亞洲人種 (Asian Population) 中作為 Steroid-Sparing Agent 具備顯著療效，但在高加索人種中效果不彰。

#### 4. Rapidly Progressive IgAN (RPGN)
- 定義：腎切片呈現 **>= 50% Crescents** 伴隨 eGFR 短期內急遽下降。
- 處置：應比照 ANCA-associated Vasculitis，立即給予 High-dose IV Pulse Methylprednisolone 加上 Cyclophosphamide。""",
            "diagrams": [
                {
                    "id": "diag_4_1",
                    "type": "micrograph",
                    "caption": "KDIGO 2025 IgAN Guideline Fig 2: Algorithm for immunosuppressive decision-making in IgAN.",
                    "imagePath": "/server-data/assets/KDIGO_2025_IgAN_Fig_2.png"
                }
            ],
            "tables": [
                {
                    "title": "Immunosuppressive Agents in IgAN: Comparison Matrix",
                    "headers": ["Therapy", "Target Site / Mechanism", "Indication & Safety Considerations"],
                    "rows": [
                        ["TRF-Budesonide (Nefecon)", "Ileal Peyer's patches (Gut MALT)", "Targeted Gd-IgA1 reduction; lower systemic steroid adverse effects."],
                        ["Systemic Steroids (TESTING)", "Systemic anti-inflammatory / immune", "Persistent proteinuria >=0.75-1g/d; requires PJP prophylaxis."],
                        ["Mycophenolate Mofetil (MMF)", "Inosine monophosphate dehydrogenase", "Effective steroid-sparing agent primarily in Asian patients."],
                        ["IV Cyclophosphamide + Steroids", "Cytotoxic DNA alkylation", "Restricted strictly to RPGN with >=50% crescents and acute eGFR drop."]
                    ]
                }
            ],
            "trapAnalysis": [
                {
                    "title": "Contraindications for Systemic Glucocorticoids",
                    "description": "eGFR < 30 mL/min/1.73m2、嚴重未控制糖尿病、肥胖 (BMI > 30)、活動性結核病或慢性感染者，屬於類固醇高風險族群。KDIGO 建議避免使用全量 Systemic Steroids。"
                }
            ]
        },
        {
            "id": "sec_5",
            "title": "Secondary IgA Nephropathy & Differential Diagnosis (IgA Vasculitis / HSP, Hepatic IgAN, Celiac, Syphilis, Sirolimus)",
            "content": """當診斷 IgAN 時，必須積極排查次發性因子 (Secondary Causes of IgA Nephropathy)：

#### 1. IgA Vasculitis (formerly Henoch-Schönlein Purpura, HSP)
- 全身性小血管炎。腎臟切片之光學、螢光與電鏡表現與 Primary IgAN 完全相同，但臨床上伴隨 **Purpuric Skin Lesions (下肢可觸摸紫斑)**、**Arthralgia (關節痛)** 及 **Colicky Abdominal Pain (腹痛/腸胃道出血)**。

#### 2. Hepatic IgAN (Alcoholic Cirrhosis)
- 酒精性肝硬化患者因肝臟 **Kupffer Cells** 清除循環中 IgA 複合物的能力下降，導致二度系膜 IgA 沉積。通常臨床無症狀或僅微量血尿。

#### 3. Mucosal Disease & Infections
- **Celiac Disease (麩質過敏性腸病)** & **Inflammatory Bowel Disease (IBD, Crohn's Disease)**：因黏膜屏障破壞，增加腸道 Gd-IgA1 暴露。
- **Secondary Syphilis (梅毒)**：二期梅毒可呈現皮疹並伴隨蛋白尿，腎切片可呈現 IgAN 或 Membranous Nephropathy 樣改變。
- **Drug-Induced**: **Sirolimus (mTOR inhibitor)** 被報導與器官移植後 De Novo IgAN 或 FSGS 之產生相關。""",
            "diagrams": [
                {
                    "id": "diag_5_1",
                    "type": "micrograph",
                    "caption": "Brenner 11e Box 31.8: Classification of Secondary IgA Nephropathy.",
                    "imagePath": "/server-data/assets/Brenner_Fig_31_27.png"
                }
            ],
            "tables": [
                {
                    "title": "Causes of Secondary IgA Nephropathy Matrix",
                    "headers": ["Category", "Representative Disease", "Pathophysiological Mechanism"],
                    "rows": [
                        ["Systemic Vasculitis", "IgA Vasculitis (HSP)", "Systemic small vessel vasculitis with cutaneous, joint, and GI involvement."],
                        ["Hepatic Disease", "Alcoholic Liver Cirrhosis", "Impaired hepatic clearance of circulating IgA complexes by Kupffer cells."],
                        ["Gastrointestinal", "Celiac Disease / Crohn's", "Mucosal barrier disruption leading to increased antigen exposure and Gd-IgA1."],
                        ["Infectious / Drug", "Secondary Syphilis / Sirolimus", "Immune complex deposition secondary to Treponema infection or mTOR inhibition."]
                    ]
                }
            ],
            "trapAnalysis": [
                {
                    "title": "Renal Biopsy Cannot Distinguish Primary IgAN from IgA Vasculitis",
                    "description": "腎切片本身無法劃分 Primary IgAN 與 IgA Vasculitis (HSP)。兩者之鑑別完全仰賴有無腎外症狀 (Purpura, Arthralgia, Abdominal Pain)。"
                }
            ]
        }
    ]
}

with open(os.path.join(TUTORIALS_DIR, "2026_IgA_Nephropathy_(主題備考)_tutorial.json"), "w", encoding="utf-8") as f:
    json.dump(tutorial_data, f, ensure_ascii=False, indent=2)

print("Saved Tutorial JSON successfully.")

# 2. 18 High-Yield MCQs JSON
questions_data = [
    {
        "id": "q1",
        "stem": "Which of the following is the critical initial event ('Hit 1') in the multi-hit pathogenesis of IgA nephropathy?",
        "options": [
            {"id": "A", "text": "Production of galactose-deficient IgA1 (Gd-IgA1) in mucosal lymphoid tissue"},
            {"id": "B", "text": "Formation of IgG autoantibodies against glomerular basement membrane"},
            {"id": "C", "text": "Overactivation of classical complement pathway by C1q"},
            {"id": "D", "text": "Direct cytotoxicity of podocytes mediated by anti-PLA2R antibodies"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "IgA nephropathy (IgAN) 發病機轉遵守 Four-Hit Hypothesis。Hit 1 為在腸道黏膜 MALT (Peyer's patches) 中產生 Galactose-deficient IgA1 (Gd-IgA1)。Option B 為 Anti-GBM disease 的機制；Option C 中 IgAN 通常為 C1q negative；Option D 為 Primary Membranous Nephropathy 的機制。"
    },
    {
        "id": "q2",
        "stem": "Immunofluorescence microscopy of a kidney biopsy specimen from a patient with IgA nephropathy typically demonstrates which of the following characteristic features?",
        "options": [
            {"id": "A", "text": "Full-house staining positive for IgG, IgM, IgA, C3, and C1q"},
            {"id": "B", "text": "Dominant mesangial IgA and C3 deposition with negative C1q staining"},
            {"id": "C", "text": "Linear capillary wall staining for IgG along the glomerular basement membrane"},
            {"id": "D", "text": "Subepithelial granular deposits containing anti-PLA2R and IgG4"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "IgAN 的免疫螢光 (IF) 典型為系膜區 IgA 占主導地位 (Dominant/Co-dominant IgA)，並常伴隨 C3 沉積，且 C1q 呈 Negative。若出現 Full-house pattern (C1q 陽性) 應懷疑 Lupus Nephritis (Option A)；Option C 為 Anti-GBM disease；Option D 為 Membranous Nephropathy。"
    },
    {
        "id": "q3",
        "stem": "According to the Oxford Classification of IgA nephropathy (MEST-C score), which of the following pathological features is recognized as the STRONGEST independent predictor of eGFR decline and progressive kidney disease?",
        "options": [
            {"id": "A", "text": "M1 (Mesangial hypercellularity in >50% of glomeruli)"},
            {"id": "B", "text": "E1 (Endocapillary hypercellularity)"},
            {"id": "C", "text": "T1 or T2 (Tubular atrophy and interstitial fibrosis)"},
            {"id": "D", "text": "C1 (Crescents in <25% of glomeruli)"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "在 Oxford MEST-C 分級中，Tubular atrophy and interstitial fibrosis (T1: 26-50%, T2: >50%) 是預測 eGFR 下降速率與 ESKD 風險的最強獨立因子 (Strongest Independent Predictor)。"
    },
    {
        "id": "q4",
        "stem": "A 28-year-old man with biopsy-proven IgA nephropathy presents with stable serum creatinine (1.0 mg/dL). His kidney biopsy shows crescents in 15% of glomeruli (C1 score). According to KDIGO 2021/2025 guidelines, what is the most appropriate management regarding the crescents?",
        "options": [
            {"id": "A", "text": "Immediately initiate high-dose IV pulse methylprednisolone plus cyclophosphamide"},
            {"id": "B", "text": "Do not start immunosuppressive therapy solely for crescents if renal function is stable; optimize supportive care"},
            {"id": "C", "text": "Perform emergent plasmapheresis to clear circulating crescents"},
            {"id": "D", "text": "Start maintenance rituximab therapy for active crescentic glomerulonephritis"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "KDIGO 指引強調，若腎切片出現 Crescents 但血清 Creatinine 完全穩定、未呈現 Rapidly Progressive eGFR drop 者，不符合 RPGN 診斷，絕對不應盲目啟動強效 Immunosuppressant，而應採優化支持治療 (Optimized Supportive Care) 與密切監測。"
    },
    {
        "id": "q5",
        "stem": "A 24-year-old woman with IgA nephropathy presents with full-blown nephrotic syndrome (proteinuria 6.5 g/day, serum albumin 2.2 g/dL). Renal biopsy reveals mild mesangial IgA deposits on IF, but electron microscopy shows diffuse podocyte foot process effacement (>80%). How should this 'Podocytopathic IgAN' variant be managed?",
        "options": [
            {"id": "A", "text": "Treat with high-dose glucocorticoids as per Minimal Change Disease (MCD) protocol"},
            {"id": "B", "text": "Initiate IV cyclophosphamide and plasma exchange immediately"},
            {"id": "C", "text": "Avoid glucocorticoids completely and give only SGLT2 inhibitors"},
            {"id": "D", "text": "Refer for urgent bilateral nephrectomy due to rapid progression"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Podocytopathic IgAN Variant (MCD-like IgAN) 臨床呈現大量蛋白尿與水腫，EM 顯示廣泛 Foot Process Effacement。KDIGO 指引建議應比照 Minimal Change Disease (MCD) 給予高劑量 Systemic Glucocorticoids，通常可獲得快速完全緩解。"
    },
    {
        "id": "q6",
        "stem": "What is the primary target for urinary protein excretion during the initial 3 to 6 months of optimized supportive care in patients with IgA nephropathy?",
        "options": [
            {"id": "A", "text": "< 0.5 to 1.0 g/day"},
            {"id": "B", "text": "< 3.5 g/day"},
            {"id": "C", "text": "< 0.05 g/day (completely zero)"},
            {"id": "D", "text": "< 5.0 g/day"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "KDIGO 指引建議，IgAN 優化支持治療的核心蛋白尿控制目標為降至 < 0.5 - 1.0 g/day。若低於此範圍，能顯著減緩長期腎功能衰退率。"
    },
    {
        "id": "q7",
        "stem": "A patient with IgA nephropathy is started on Dapagliflozin (SGLT2 inhibitor). At week 3, repeat serum creatinine increases from 1.4 mg/dL to 1.6 mg/dL (eGFR dips by 15%). Which of the following statements correctly explains this finding?",
        "options": [
            {"id": "A", "text": "This is an expected hemodynamic eGFR dip caused by tubuloglomerular feedback and afferent arteriolar constriction"},
            {"id": "B", "text": "This indicates acute tubular necrosis induced by direct SGLT2 inhibitor nephrotoxicity"},
            {"id": "C", "text": "The SGLT2 inhibitor should be immediately discontinued and high-dose steroids initiated"},
            {"id": "D", "text": "This reflects acute allergic interstitial nephritis requiring urgent renal biopsy"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "SGLT2 抑制劑藉由激活 Macula Densa 之 Tubuloglomerular Feedback (TGF)，使 Afferent Arteriole 收縮以降低腎絲球高壓。使用前幾週出現 <30% 的 eGFR Dip 屬於預期的血流動力學效應，不需停藥。"
    },
    {
        "id": "q8",
        "stem": "Sparsentan is a novel therapeutic agent approved for IgA nephropathy. What is its mechanism of action?",
        "options": [
            {"id": "A", "text": "Dual Endothelin Type A (ETA) and Angiotensin II Type 1 (AT1) receptor antagonist"},
            {"id": "B", "text": "Targeted-release corticosteroid acting on ileal Peyer's patches"},
            {"id": "C", "text": "Monoclonal antibody against B-cell activating factor (BAFF)"},
            {"id": "D", "text": "Selective inhibitor of complement Factor B in the alternative pathway"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Sparsentan 為世界首創之雙重 Endothelin Type A (ETA) 區與 Angiotensin II Type 1 (AT1) 受體拮抗劑 (Dual ERA/ARB)，PROTECT 試驗證實其降蛋白尿效果優於傳統高劑量 Irbesartan。"
    },
    {
        "id": "q9",
        "stem": "Targeted-release Budesonide (Nefecon / TRF-Budesonide) is uniquely formulated to deliver glucocorticoids to which specific anatomical site in patients with IgA nephropathy?",
        "options": [
            {"id": "A", "text": "Distal ileum targeting Peyer's patches in the mucosal-associated lymphoid tissue (MALT)"},
            {"id": "B", "text": "Proximal convoluted tubule to block megalin-mediated protein reabsorption"},
            {"id": "C", "text": "Splenic red pulp to destroy autoantibody-producing plasma cells"},
            {"id": "D", "text": "Hepatic Kupffer cells to enhance IgA immune complex clearance"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Nefecon (TRF-Budesonide) 為特殊腸溶錠，專一釋放於迴腸末端 (Distal Ileum) 之 Peyer's patches，在源頭抑制 Galactose-deficient IgA1 (Gd-IgA1) 的合成，顯著降低全身性類固醇副作用。"
    },
    {
        "id": "q10",
        "stem": "According to the TESTING trial and KDIGO guidelines, which of the following is a MANDATORY co-prescription when initiating systemic glucocorticoids for IgA nephropathy?",
        "options": [
            {"id": "A", "text": "Prophylaxis for Pneumocystis jirovecii pneumonia (PJP) such as Trimethoprim-Sulfamethoxazole"},
            {"id": "B", "text": "High-dose intravenous immunoglobulin (IVIG)"},
            {"id": "C", "text": "Prophylactic plasmapheresis prior to each steroid dose"},
            {"id": "D", "text": "Concurrent oral cyclophosphamide for all low-risk patients"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "TESTING 試驗顯示高劑量口服類固醇會增加重度感染風險。因此在實施全身性類固醇治療時，強制要求併用 Pneumocystis jirovecii (PJP) 預防性抗生素 (如 TMP-SMX)。"
    },
    {
        "id": "q11",
        "stem": "In which patient population does KDIGO specifically highlight Mycophenolate Mofetil (MMF) as an effective steroid-sparing immunosuppressive agent for IgA nephropathy?",
        "options": [
            {"id": "A", "text": "Asian patients with persistent proteinuria despite optimized supportive care"},
            {"id": "B", "text": "Caucasian patients with baseline eGFR < 15 mL/min/1.73m2"},
            {"id": "C", "text": "Pediatric patients with minimal change disease only"},
            {"id": "D", "text": "Patients with acute poststreptococcal glomerulonephritis"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "KDIGO 指引指出，Mycophenolate Mofetil (MMF) 在亞洲人群 (Asian Population) 中作為類固醇減量/替代藥物 (Steroid-sparing agent) 展現出顯著之療效與腎臟保護作用。"
    },
    {
        "id": "q12",
        "stem": "Which novel therapeutic category directly targets B-cell survival factors (BAFF/APRIL) to reduce Gd-IgA1 production in IgA nephropathy?",
        "options": [
            {"id": "A", "text": "Dual BAFF/APRIL inhibitors (such as Sibeprenlimab or Telitacicept)"},
            {"id": "B", "text": "SGLT2 inhibitors (such as Empagliflozin)"},
            {"id": "C", "text": "Calcimimetic agents (such as Cinacalcet)"},
            {"id": "D", "text": "Mineralocorticoid receptor antagonists (such as Finerenone)"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Sibeprenlimab 與 Telitacicept 為雙重 BAFF/APRIL 抑制劑，能抑制 B-cell 及 Plasma cell 分化，從源頭減少 Gd-IgA1 及 Autoantibodies 產生。"
    },
    {
        "id": "q13",
        "stem": "Secondary IgA nephropathy is commonly observed in patients with advanced alcoholic liver cirrhosis. What is the underlying pathophysiology?",
        "options": [
            {"id": "A", "text": "Impaired clearance of circulating IgA immune complexes by hepatic Kupffer cells"},
            {"id": "B", "text": "Overproduction of IgA autoantibodies driven by hepatitis B viral surface antigen"},
            {"id": "C", "text": "Direct cytotoxic effect of ethanol on glomerular mesangial cells"},
            {"id": "D", "text": "Depletion of hepatic complement C3 causing systemic complement activation"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "酒精性肝硬化患者因肝臟網狀內皮系統 (Kupffer Cells) 功能受損，無法正常清除循環中自然發生的 IgA 複合物，導致二度系膜區 IgA 沉積 (Hepatic IgAN)。"
    },
    {
        "id": "q14",
        "stem": "A 10-year-old boy presents with palpable purpura on his buttocks and lower extremities, colicky abdominal pain, and microscopic hematuria. A kidney biopsy shows mesangial proliferative GN with dominant IgA deposits on IF. Which statement correctly distinguishes IgA Vasculitis (HSP) from Primary IgA Nephropathy?",
        "options": [
            {"id": "A", "text": "Renal histopathology on biopsy is identical; differentiation relies on systemic extrarenal manifestations"},
            {"id": "B", "text": "IgA Vasculitis strictly lacks C3 deposition on immunofluorescence"},
            {"id": "C", "text": "Primary IgA Nephropathy manifests with lower extremity purpura while IgA Vasculitis does not"},
            {"id": "D", "text": "Electron microscopy shows humps in IgA Vasculitis but line deposits in IgAN"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "IgA Vasculitis (HSP) 與 Primary IgAN 在腎切片之光學、螢光與電鏡下完全無法劃分 (Identical histopathology)。兩者之鑑別完全仰賴有無腎外症狀 (如紫斑、關節痛、腹痛)。"
    },
    {
        "id": "q15",
        "stem": "Which of the following gastrointestinal conditions is strongly associated with secondary IgA nephropathy due to mucosal barrier breakdown and increased antigen exposure?",
        "options": [
            {"id": "A", "text": "Celiac disease (gluten-sensitive enteropathy)"},
            {"id": "B", "text": "Helicobacter pylori gastritis"},
            {"id": "C", "text": "Clostridioides difficile colitis"},
            {"id": "D", "text": "Agalactasia enteritis"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Celiac disease (麩質過敏性腸病) 及 Crohn's disease 因腸道黏膜屏障破壞，導致抗原暴露增加與 Gd-IgA1 過度合成，為次發性 IgAN 之典型腸道誘因。"
    },
    {
        "id": "q16",
        "stem": "Which immunosuppressive drug used in solid organ transplantation has been reported to induce de novo IgA nephropathy or FSGS?",
        "options": [
            {"id": "A", "text": "Sirolimus (mTOR inhibitor)"},
            {"id": "B", "text": "Tacrolimus (calcineurin inhibitor)"},
            {"id": "C", "text": "Mycophenolate mofetil"},
            {"id": "D", "text": "Basiliximab (IL-2R antagonist)"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Sirolimus (mTOR 抑制劑) 在器官移植患者中被報導與 de novo IgA nephropathy 以及 focal segmental glomerulosclerosis (FSGS) 的發生相關。"
    },
    {
        "id": "q17",
        "stem": "A 35-year-old man presents with a generalized maculopapular rash, palmoplantar lesions, microscopic hematuria, and proteinuria (1.8 g/day). Serology reveals positive VDRL and RPR. Kidney biopsy shows IgA deposition. Which infectious disease is responsible for this secondary IgAN/membranous presentation?",
        "options": [
            {"id": "A", "text": "Secondary Syphilis (Treponema pallidum infection)"},
            {"id": "B", "text": "Primary HIV acute seroconversion"},
            {"id": "C", "text": "Epstein-Barr virus mononucleosis"},
            {"id": "D", "text": "Acute Hepatitis A infection"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Secondary Syphilis (二期梅毒) 典型表現為手掌腳掌皮疹 (Palmoplantar lesions) 並可併發腎病變 (呈 IgAN 或 Membranous Pattern)。治療抗生素 (Penicillin) 後腎病變通常可逆。"
    },
    {
        "id": "q18",
        "stem": "In patients with end-stage kidney disease (ESKD) secondary to IgA nephropathy who receive a kidney transplant, what is the reported rate of IgAN recurrence in the renal allograft?",
        "options": [
            {"id": "A", "text": "20% to 60% over long-term follow-up, though graft loss occurs in a minority"},
            {"id": "B", "text": "0% (IgAN never recurs post-transplant)"},
            {"id": "C", "text": "100% within the first week post-transplant leading to hyperacute rejection"},
            {"id": "D", "text": "Strictly limited to living donor transplants only"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "IgA nephropathy 在腎臟移植後有高達 20% - 60% 的 Recurrence Rate (組織學上相當常見)，但大部分患者在移植腎中進展緩解，僅少數會導致全移植腎失能 (Graft Loss)。"
    }
]

paper_data = {
    "paperId": "2026_IgA_Nephropathy_(主題備考)",
    "paperTitle": "2026 IgA Nephropathy (主題備考)",
    "sourceCategory": "2026 年主題練習",
    "totalQuestions": len(questions_data),
    "questions": questions_data
}

with open(os.path.join(PUBLIC_DATA_DIR, "2026_IgA_Nephropathy_(主題備考).json"), "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print("Saved Paper JSON successfully.")

# 3. Update exams_manifest.json
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# Remove existing item with same paperId if present
manifest = [item for item in manifest if item.get("paperId") != "2026_IgA_Nephropathy_(主題備考)"]

manifest_item = {
    "paperId": "2026_IgA_Nephropathy_(主題備考)",
    "paperTitle": "2026 IgA Nephropathy (主題備考)",
    "sourceCategory": "2026 年主題練習",
    "totalQuestions": 18,
    "hasTutorial": True
}
manifest.append(manifest_item)

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print("Updated Manifest successfully.")

# 4. Prepare NLM Asking Payload (without answers/explanations)
nlm_payload_items = []
for q in questions_data:
    nlm_payload_items.append({
        "id": q["id"],
        "paperId": "2026_IgA_Nephropathy_(主題備考)",
        "stem": q["stem"],
        "options": q["options"]
    })

payload_path = os.path.join(SITE_DIR, "scratch/igan_nlm_payload.json")
with open(payload_path, "w", encoding="utf-8") as f:
    json.dump(nlm_payload_items, f, ensure_ascii=False, indent=2)

print("Saved NLM Payload successfully.")

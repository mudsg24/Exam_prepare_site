import json
import os

paper_id = "2026_Nephrotic_Syndrome_(主題備考)"

tutorial_data = {
    "paperId": paper_id,
    "title": "Nephrotic Syndrome Masterclass Lecture",
    "sourceCategory": "2026 年主題練習",
    "sections": [
        {
            "id": "section-1",
            "title": "Module 1: Podocyte Biology, Slit Diaphragm Architecture, and Pathophysiology of Proteinuria",
            "content": """### 1. Podocyte Molecular Architecture & Glomerular Filtration Barrier

Glomerular Filtration Barrier 由 Capillary Endothelium、Glomerular Basement Membrane (GBM) 與 Podocyte Foot Processes 三層結構共同組成。Podocyte 為高度特化之 Terminal Differentiated Epithelial Cells，其 Foot Processes 彼此交錯形成 Slit Diaphragm。

#### Slit Diaphragm Key Molecular Components:
- **Nephrin (NPHS1)**: Transmembrane cell adhesion protein，雙分子交聯構成 Filtration Slit 之主要 Meshwork。缺陷導致 Congenital Nephrotic Syndrome of the Finnish Type。
- **Podocin (NPHS2)**: Hairpin-like membrane protein，錨定 Nephrin 至 Podocyte Cytoskeleton。缺陷導致 Steroid-Resistant Nephrotic Syndrome (SRNS)。
- **CD2AP** & **α-Actinin-4 (ACTN4)**: 連接 Slit Diaphragm 與 Actin Cytoskeleton。

### 2. Pathophysiology of Nephrotic Syndrome Manifestations

#### Topology Mapping Matrix: Microstructural Injury to Systemic Features
| Target Structure / Injury | Pathophysiological Cascade | Systemic Clinical Manifestation |
| :--- | :--- | :--- |
| Slit Diaphragm Disruption & Foot Process Effacement | Loss of size-selective barrier & Negative charge reduction | Heavy Proteinuria (> 3.5 g/24h) |
| Severe Urinary Albumin Loss | Hepatic albumin synthesis capacity exceeded | Hypoalbuminemia (< 3.0 g/dL) |
| Decreased Plasma Oncotic Pressure | Fluid shift from intravascular to interstitial space (Underfill mechanism) | Peripheral & Facial Edema |
| Hepatic Compensatory Lipoprotein Synthesis | Increased ApoB-100 & Decreased LPL Activity | Hyperlipidemia & Lipiduria (Oval Fat Bodies) |
| Loss of Antithrombin III & Plasminogen | Elevated Factor V, VIII, Fibrinogen & Platelet hyperaggregability | Hypercoagulability & Renal Vein Thrombosis |

### 3. Pathophysiological Decision Tree: Edema Mechanisms

```
Nephrotic Syndrome State
  ├─ Underfill Mechanism (Primary Alteration)
  │    └─ Hypoalbuminemia -> Decreased Plasma Oncotic Pressure -> Interstitial Extravasation -> Intravascular Depletion -> RAAS Activation & ADH Release -> Sodium & Water Retention
  └─ Overfill Mechanism (Primary Tubular Alteration)
       └─ Primary Intrarenal Sodium Retention (ENaC Activation via Protease Cleavage) -> Intravascular Expansion -> Suppression of RAAS -> Hypertension & Edema
```

### 4. Conceptual Trap Analysis
> [!WARNING]
> **Conceptual Trap 1**: 不可將所有 Nephrotic Edema 皆歸因於 Underfill Mechanism。在 Minimal Change Disease 常見 Underfill，但在 Adult Focal Segmental Glomerulosclerosis 及 Membranous Nephropathy 中，過半患者表現 Overfill Mechanism (ENaC activation via urinary plasmin proteolytic cleavage)。
> 
> **Conceptual Trap 2**: Prophylactic Anticoagulation 需評估 Serum Albumin 數值。Membranous Nephropathy 患者當 Serum Albumin < 2.2 g/dL 且伴有 High VTE Risk 時，應積極給予 Full-dose Anticoagulation (如 Warfarin 或 DOACs)。""",
            "diagrams": [
                {
                    "id": "Brenner 11e_Fig_4_2.png",
                    "title": "Anatomy of the Glomerular Filter and Slit Diaphragm Architecture",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/04. Glomerular Cell Biology and Podocytopathies/Fig_4_2.png"
                },
                {
                    "id": "Brenner 11e_Fig_30_1.png",
                    "title": "Hypothetical Model of Podocyte Slit Diaphragm and Actin Cytoskeleton Linkage",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/30. Pathophysiology of Proteinuria/Fig_30_1.png"
                },
                {
                    "id": "nephrotic_podocyte_pathology",
                    "title": "Glomerular Filtration Barrier vs Podocytopathy Foot Process Effacement Mechanism",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/nephrotic_podocyte_pathology.jpg"
                }
            ]
        },
        {
            "id": "section-2",
            "title": "Module 2: Primary Glomerular Diseases (MCD, FSGS, MN, MPGN)",
            "content": """### 1. Primary Glomerulopathies Overview

Primary Glomerular Diseases 為引發 Adult 與 Pediatric Nephrotic Syndrome 之首要病因。區分各自的 Histopathology、Electron Microscopy (EM) 與 Immunofluorescence (IF) 呈現為核心檢定考點。

### 2. High-Yield Differential Comparison Table

| Feature / Disease | Minimal Change Disease (MCD) | Focal Segmental Glomerulosclerosis (FSGS) | Membranous Nephropathy (MN) | Membranoproliferative GN (MPGN) |
| :--- | :--- | :--- | :--- | :--- |
| **Peak Incidence** | Children (80%), Adults (10-15%) | Adults & Children | Adults > 40 years | Young Adults & Children |
| **Light Microscopy** | Normal Glomeruli, Lipid in Tubules | Focal & Segmental Sclerosis / Hyalinosis | Thickened Capillary Loops, GBM Spikes | Tram-track (Double Contours), Lobular Accentuation |
| **Immunofluorescence** | Negative | IgM & C3 in Segmental Sclerotic lesions | Granular IgG & C3 along Capillary Walls | Granular C3, IgG, C1q (Immune-complex pattern) |
| **Electron Microscopy** | Diffuse Podocyte Foot Process Effacement | Foot Process Effacement (Diffuse in Primary, Segmental in Secondary) | Subepithelial Electron-dense Deposits | Subendothelial (Type I) or Dense Deposits (DDD) |
| **Serologic Markers** | None | APOL1 Risk Alleles (African Ancestry) | Anti-PLA2R (70-80%), Anti-THSD7A, Anti-NELL1 | Low Complement (C3, C4 in Immune-complex; Low C3 only in C3G) |

### 3. Histologic Variants of FSGS & Prognostic Significance
- **Perihilar Variant**: 常見於 Secondary FSGS (Hyperfiltration due to reduced nephron mass or obesity).
- **Tip Lesion Variant**: 預後最佳，對 Steroids 反應良好.
- **Collapsing Variant**: 最具侵襲性，Glomerular Tuft Collapse & Podocyte Hyperplasia. 常見於 HIV, COVID-19, APOL1 High-risk Genotypes, Pamidronate use.
- **Cellular Variant**: Endocapillary Hypercellularity filling Capillary Lumens.
- **NOS (Not Otherwise Specified)**: 最常見之傳統 FSGS 類型.

### 4. Membranous Nephropathy Ultrastructural Stages
- **Stage I**: Small Subepithelial Deposits, Normal GBM on Light Microscopy.
- **Stage II**: Subepithelial Deposits with Projection of GBM Spikes around deposits (PAM stain positive).
- **Stage III**: GBM Enclosure of Deposits (Dome-and-Spike pattern).
- **Stage IV**: Lucent Deposits within Markedly Thickened GBM (Moth-eaten appearance).

### 5. Conceptual Trap Analysis
> [!WARNING]
> **Conceptual Trap 1**: 勿因 Subepithelial Deposits 即判定為 Lupus Class V。Secondary Membranous Nephropathy 需主動排除 Solid Organ Malignancy (Prostate, Lung, Colon, Breast), Hepatitis B Virus, Syphilis, 藥物 (NSAIDs, Penicillamine)。
> 
> **Conceptual Trap 2**: MPGN 於 2021 KDIGO 已重分類為 **Immune-Complex Mediated MPGN** (Ig positive, Immunoglobulins + Complement) 與 **Complement-Mediated MPGN / C3 Glomerulopathy** (Ig negative, C3 only). 勿再使用舊版 Type I / II / III 混淆診斷。""",
            "diagrams": [
                {
                    "id": "Brenner 11e_Fig_31_4.png",
                    "title": "Electron Micrograph of Minimal Change Disease Showing Diffuse Foot Process Effacement",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_4.png"
                },
                {
                    "id": "Brenner 11e_Fig_31_5.png",
                    "title": "Histologic Variants of Focal Segmental Glomerulosclerosis (FSGS)",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_5.png"
                },
                {
                    "id": "Brenner 11e_Fig_31_7.png",
                    "title": "Membranous Nephropathy Ultrastructural Stages (Stage I to Stage IV)",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_7.png"
                },
                {
                    "id": "primary_gn_immunopathology",
                    "title": "Comparative Immunopathology of Nephrotic Primary Glomerular Diseases",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/primary_gn_immunopathology.jpg"
                }
            ]
        },
        {
            "id": "section-3",
            "title": "Module 3: Secondary Glomerular Diseases & Systemic Etiologies",
            "content": """### 1. Secondary Glomerular Involvement Spectrum

Secondary Nephrotic Syndrome 由 Systemic Diseases, Metabolic Disorders, Autoimmune Diseases, Infections 或 Malignancy 引起。精準判讀 Renal Biopsy 特徵與全身特徵為重要解題樞紐。

### 2. High-Yield Secondary Etiologies Differential Matrix

| Secondary Etiology | Key Histopathological Finding | Immunofluorescence Pattern | Key Diagnostic / Serologic Marker |
| :--- | :--- | :--- | :--- |
| **Diabetic Kidney Disease (DKD)** | Kimmelstiel-Wilson Nodules, Nodular Glomerulosclerosis, Capsular Drop | Linear IgG staining along GBM (Non-immune trapping) | Long-standing Diabetes, Retinopathy, Microalbuminuria progression |
| **Renal Amyloidosis (AL / AA)** | Amorphous Acellular Deposits in Mesangium & Vessels; Congo Red Positive | Monoclonal Light Chain (κ or λ) in AL; Negative in AA | Apple-Green Birefringence under Polarized Light; Serum Free Light Chains |
| **Lupus Nephritis Class V (Membranous)** | Diffuse Subepithelial Deposits with Thickened GBM | Full-House Pattern (IgG, IgA, IgM, C3, C1q Positive) | ANA, Anti-dsDNA, Low Complement C3/C4, Anti-Sm |
| **Hepatitis B Virus (HBV) Associated GN** | Membranous Nephropathy or MPGN Pattern | Granular HBeAg / HBsAg deposits | HBV Serology (HBsAg+, HBeAg+, High HBV DNA) |
| **Hepatitis C Virus (HCV) Associated GN** | MPGN Pattern with Type II Mixed Cryoglobulinemia | Granular IgG, IgM, C3 with Intracapillary Thrombi | HCV RNA+, Positive Rheumatoid Factor, Cryoglobulins |
| **Syphilis Associated GN** | Membranous Nephropathy with Subepithelial Deposits | Granular IgG & C3 | Positive VDRL/RPR, TPHA/TPPA, Skin Rash (Palmar Papules) |

### 3. Pathophysiological Decision Tree: Amyloidosis Classification
```
Glomerular Amorphous Deposits Suspected
  ├─ Congo Red Stain Positive
  │    ├─ Polarized Light Inspection -> Apple-Green Birefringence Confirmed
  │    ├─ AL Amyloidosis Subtype -> Monoclonal Plasma Cell Dyscrasia (Serum/Urine Immunofixation, SPEP/UPEP, SPEP Free Light Chain Ratio)
  │    └─ AA Amyloidosis Subtype -> Chronic Inflammatory Condition (Rheumatoid Arthritis, Osteomyelitis, FMF, Bronchiectasis)
  └─ Congo Red Stain Negative
       └─ Consider Fibrillary Glomerulonephritis (DNAJB9 Positive, 16-24 nm Fibrils) or Immunotactoid Glomerulopathy (Microtubules > 30 nm)
```

### 4. Conceptual Trap Analysis
> [!WARNING]
> **Conceptual Trap 1**: Diabetic Nodular Glomerulosclerosis (Kimmelstiel-Wilson) 需與 Amyloidosis, MPGN, Light Chain Deposition Disease (LCDD) 鑑別。Amyloidosis 為 Congo Red 陽性；LCDD 為 Monoclonal κ/λ 染色；DKD 則伴隨 Retinopathy, Arteriosclerosis 與 Thickened Capillary Loops。
> 
> **Conceptual Trap 2**: Secondary Syphilitic Nephropathy 在年輕男性表現為 Nephrotic Syndrome 伴手掌皮疹 (Palmar Skin Rash)。其 Pathology 多為 Membranous Nephropathy。Podocyte Foot Process Effacement 亦極顯著，不可誤診為 Minimal Change Disease。""",
            "diagrams": [
                {
                    "id": "Brenner 11e_Fig_39_6.png",
                    "title": "Diabetic Kidney Disease Biopsy Showing Kimmelstiel-Wilson Mesangial Nodules",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/39. Epidemiology of Diabetic Kidney Disease/Fig_39_6.png"
                },
                {
                    "id": "Brenner 11e_Fig_32_24.png",
                    "title": "Renal Amyloidosis Glomerular Fibrillar Deposits and Subepithelial Spikes",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/32. Secondary Glomerular Disease/Fig_32_24.png"
                },
                {
                    "id": "Brenner 11e_Fig_32_25.png",
                    "title": "Congo Red Stain of Renal Amyloidosis Demonstrating Apple-Green Birefringence",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/32. Secondary Glomerular Disease/Fig_32_25.png"
                },
                {
                    "id": "secondary_gn_histopathology",
                    "title": "Secondary Causes of Nephrotic Syndrome Pathological Comparison",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/secondary_gn_histopathology.jpg"
                }
            ]
        },
        {
            "id": "section-4",
            "title": "Module 4: Treatment Strategies and KDIGO Guidelines",
            "content": """### 1. Management Principles of Nephrotic Syndrome

Nephrotic Syndrome 之治療包含 Supportive Care 與 Disease-Specific Immunosuppressive Therapy。KDIGO 2021 Guidelines 依據 Serology (Anti-PLA2R Titer), Histology 與 Risk Stratification 制定精準治療藍圖。

### 2. KDIGO Risk Stratification & Immunosuppression Guidelines

#### Minimal Change Disease (MCD):
- **First-line Therapy**: High-dose Oral Corticosteroids (Prednisone 1 mg/kg/day, max 80 mg/day, for 4-16 weeks).
- **Relapsing / Steroid-Dependent MCD**: Cyclophosphamide, Calcineurin Inhibitors (Tacrolimus / Cyclosporine), or Rituximab.

#### Primary Focal Segmental Glomerulosclerosis (FSGS):
- **First-line Therapy**: High-dose Corticosteroids for at least 8-16 weeks.
- **Steroid-Resistant FSGS**: Calcineurin Inhibitors (CNIs, Tacrolimus / Cyclosporine) for at least 6 months.

#### Primary Membranous Nephropathy (MN):
- **Low Risk** (Normal eGFR, Proteinuria < 3.5 g/day, Anti-PLA2R Low): Wait-and-see with maximum ACEi/ARB for 6 months.
- **Moderate Risk** (Proteinuria 3.5-8 g/day, Normal eGFR, Anti-PLA2R Moderate): Rituximab OR CNI + Low-dose Steroids.
- **High Risk** (Proteinuria > 8 g/day or eGFR decline, Anti-PLA2R High > 50 RU/mL): Rituximab OR Cyclophosphamide + Steroids (Modified Ponticelli Regimen) OR CNI + Rituximab.
- **Very High Risk** (Rapidly declining eGFR, Severe Nephrotic Syndrome): Cyclophosphamide + High-dose Steroids.

### 3. Supportive Management Guidelines Matrix

| Supportive Intervention | Clinical Target | Guideline Recommendation & Mechanism |
| :--- | :--- | :--- |
| **Renin-Angiotensin System Blockade** | Proteinuria & Intrarenal Pressure | ACEi or ARB titrated to maximum tolerated dose; Reduce intraglomerular hyperfiltration |
| **Prophylactic Anticoagulation** | Venous Thromboembolism (VTE) | Indicated in Membranous Nephropathy with Serum Albumin < 2.0-2.5 g/dL & High VTE Risk; Aspirin for Arterial Risk |
| **Lipid Management** | Hyperlipidemia & Cardiovascular Risk | HMG-CoA Reductase Inhibitor (Statin) for persistent nephrotic hypercholesterolemia |
| **Edema Management** | Fluid Overload & Anasarca | Dietary Sodium Restriction (< 2 g/day); Loop Diuretics (Furosemide / Bumetanide) +/- Thiazide or ENaC Blocker |
| **Infection Prophylaxis** | Encapsulated Bacterial Infections | Pneumococcal Vaccination (PCV20 / PPSV23); Annual Influenza Vaccine |

### 4. Conceptual Trap Analysis
> [!WARNING]
> **Conceptual Trap 1**: 在 Membranous Nephropathy 中，Anti-PLA2R Antibody Titer 下降快於 Proteinuria 改善 (Immunologic Remission leads Clinical Remission by 3-6 months)。切勿在 Anti-PLA2R 已轉陰性但 Proteinuria 尚未完全消除時盲目加重 Immunosuppressants。
> 
> **Conceptual Trap 2**: Secondary FSGS (如 Obesity-related, Reflux-related, reduced nephron mass) **禁止給予 High-dose Corticosteroids 或 Immunosuppressive Therapy**！應使用 Maximum RAS Blockade, SGLT2 Inhibitors 與 Weight Management 減緩 Hyperfiltration。""",
            "diagrams": [
                {
                    "id": "Brenner 11e_Fig_33_1.png",
                    "title": "Differential Impact of Proteinuria on Glomerular Filtration Decline Rate",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/33. Treatment of Glomerulonephritis/Fig_33_1.png"
                },
                {
                    "id": "KDIGO_Fig_1.png",
                    "title": "KDIGO Guideline Decision Matrix for Primary Glomerular Diseases",
                    "type": "micrograph",
                    "relPath": "/reference-images/KDIGO/KDIGO-2009-Transplant-Recipient-Guideline-English/Fig_1.png"
                },
                {
                    "id": "kdigo_treatment_algorithm_gn",
                    "title": "KDIGO Clinical Decision Tree Treatment of Nephrotic Syndrome",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/kdigo_treatment_algorithm_gn.jpg"
                }
            ]
        }
    ]
}

tutorial_dir = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials"
os.makedirs(tutorial_dir, exist_ok=True)
tutorial_file = os.path.join(tutorial_dir, f"{paper_id}_tutorial.json")

with open(tutorial_file, "w", encoding="utf-8") as f:
    json.dump(tutorial_data, f, ensure_ascii=False, indent=2)

print(f"Wrote tutorial JSON: {tutorial_file}")

# Generate 20 MCQs Question Bank JSON
questions_data = [
    {
        "id": f"{paper_id}_Q01",
        "stem": "A 6-year-old boy presents with sudden onset of diffuse facial and peripheral edema following an upper respiratory infection. Urinalysis reveals 4+ protein, no red blood cells, and a urine protein-to-creatinine ratio of 6.5 g/g. Serum albumin is 1.8 g/dL and serum creatinine is 0.5 mg/dL. Renal biopsy performed in similar cases demonstrates normal glomeruli under light microscopy. What is the characteristic electron microscopic finding in this condition?",
        "options": [
            {"id": "A", "text": "Diffuse effacement of podocyte foot processes"},
            {"id": "B", "text": "Subepithelial electron-dense deposits with spike formation"},
            {"id": "C", "text": "Subendothelial deposits with double-contour capillary walls"},
            {"id": "D", "text": "Mesangial dense deposits"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "患者為典型 Pediatric Minimal Change Disease (MCD)。MCD 在 Light Microscopy 下球體近乎正常，Immunofluorescence 為 Negative，其特徵性診斷關鍵為 Electron Microscopy 下呈現 Diffuse Foot Process Effacement。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_31_4.png",
                "title": "Minimal Change Disease EM Effacement",
                "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_4.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q02",
        "stem": "A 45-year-old male with nephrotic syndrome (proteinuria 7.2 g/24h, serum albumin 2.1 g/dL) undergoes a renal biopsy. Light microscopy demonstrates segmental sclerosis involving 2 out of 15 glomeruli, primarily located at the vascular pole (perihilar region). Genetic testing is negative, but the patient has a history of unmanaged morbid obesity (BMI 42 kg/m2). Which of the following features best distinguishes Secondary FSGS from Primary FSGS?",
        "options": [
            {"id": "A", "text": "Abrupt onset of nephrotic syndrome"},
            {"id": "B", "text": "Segmental (rather than diffuse) podocyte foot process effacement on electron microscopy"},
            {"id": "C", "text": "High rate of response to high-dose systemic corticosteroid therapy"},
            {"id": "D", "text": "Presence of circulating anti-PLA2R autoantibodies"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "selectedOption": "B",
        "sourceExplanation": "Secondary FSGS (如 Obesity-induced hyperfiltration) 的 Electron Microscopy 特徵為 Segmental (非 Diffuse) Foot Process Effacement。相較之下，Primary FSGS 常為 Abrupt onset 且 Foot Process Effacement 呈 Diffuse pattern。Secondary FSGS 應以 Hyperfiltration Control (RAS Blockade, SGLT2i) 為主，禁用高劑量 Steroids。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_31_5.png",
                "title": "FSGS Histologic Variants",
                "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_5.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q03",
        "stem": "A 52-year-old male presents with nephrotic syndrome. Serological testing is positive for anti-phospholipase A2 receptor (anti-PLA2R) autoantibodies with a high titer (180 RU/mL). Renal biopsy reveals diffusely thickened glomerular capillary walls with subepithelial deposits. According to KDIGO 2021 guidelines, what is the initial recommended immunosuppressive strategy for this high-risk Primary Membranous Nephropathy patient?",
        "options": [
            {"id": "A", "text": "High-dose Oral Prednisone monotherapy for 6 months"},
            {"id": "B", "text": "Observation with ACE inhibitor for 6 months before initiating immunosuppression"},
            {"id": "C", "text": "Rituximab therapy OR Cyclophosphamide with Alternating Corticosteroids"},
            {"id": "D", "text": "Mycophenolate Mofetil monotherapy"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "selectedOption": "C",
        "sourceExplanation": "KDIGO 2021 指引針對 High Risk 的 Primary Membranous Nephropathy (Anti-PLA2R 高滴定抗體或高度蛋白尿)，第一線建議使用 Rituximab 或 Cyclophosphamide 加 Alternating Corticosteroids (Modified Ponticelli Regimen)，單用 Prednisone 對 Primary MN 無效。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_31_9.png",
                "title": "Membranous Nephropathy Immunofluorescence",
                "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_9.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q04",
        "stem": "A 38-year-old female patient with a history of long-standing systemic lupus erythematosus presents with 5.5 g/24h proteinuria, normal serum complement levels (C3, C4), and negative anti-dsDNA antibodies. Renal biopsy demonstrates diffuse subepithelial immune deposits and GBM spike formation without endocapillary proliferation or necrosis. What is the correct ISN/RPS classification for this renal biopsy?",
        "options": [
            {"id": "A", "text": "Class II (Mesangial Proliferative Lupus Nephritis)"},
            {"id": "B", "text": "Class III (Focal Lupus Nephritis)"},
            {"id": "C", "text": "Class IV (Diffuse Lupus Nephritis)"},
            {"id": "D", "text": "Class V (Membranous Lupus Nephritis)"}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "selectedOption": "D",
        "sourceExplanation": "表現為 Diffuse Subepithelial Immune Deposits 與 GBM Spikes 且無 Endocapillary Proliferation 者，為典型的 Class V Lupus Nephritis (Membranous Lupus Nephritis)。Class V 可單獨存在或與 Class III/IV 併存。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_32_10.png",
                "title": "Lupus Nephritis Class V",
                "relPath": "/reference-images/Brenner 11e/32. Secondary Glomerular Disease/Fig_32_10.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q05",
        "stem": "A 68-year-old male with a 15-year history of Type 2 Diabetes Mellitus presents with worsening peripheral edema and 4.8 g/24h proteinuria. Renal biopsy displays nodular mesangial expansion with acellular, PAS-positive nodules surrounded by dilated capillaries. What is the eponym for these classic histopathological lesions?",
        "options": [
            {"id": "A", "text": "Kimmelstiel-Wilson nodules"},
            {"id": "B", "text": "Wire-loop lesions"},
            {"id": "C", "text": "Crescentic lesions"},
            {"id": "D", "text": "Fleas-bitten kidney lesions"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "Diabetic Kidney Disease 的典型 Nodular Glomerulosclerosis 結節稱為 Kimmelstiel-Wilson Nodules。此為 PAS 陽性之 Mesangial Matrix Expansion。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_39_6.png",
                "title": "DKD Kimmelstiel-Wilson Nodules",
                "relPath": "/reference-images/Brenner 11e/39. Epidemiology of Diabetic Kidney Disease/Fig_39_6.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q06",
        "stem": "A 62-year-old female presents with nephrotic syndrome, bilateral macroglossia, and hepatomegaly. Renal biopsy shows amorphous, eosinophilic extracellular deposits in the mesangium. Congo Red staining is performed. Which characteristic finding under polarized light microscopy confirms the diagnosis of Renal Amyloidosis?",
        "options": [
            {"id": "A", "text": "Bright red fluorescence"},
            {"id": "B", "text": "Apple-green birefringence"},
            {"id": "C", "text": "Granular yellow-green luminescence"},
            {"id": "D", "text": "Maltese cross appearance"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "selectedOption": "B",
        "sourceExplanation": "Renal Amyloidosis 之診斷基石為 Congo Red Stain 在 Polarized Light 下呈現特異性之 Apple-Green Birefringence。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_32_25.png",
                "title": "Renal Amyloidosis Apple-Green Birefringence",
                "relPath": "/reference-images/Brenner 11e/32. Secondary Glomerular Disease/Fig_32_25.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q07",
        "stem": "A 26-year-old male presents with nephrotic-range proteinuria (4.2 g/day), hypoalbuminemia (2.0 g/dL), and a maculopapular skin rash on his palms and soles. Serologic testing shows positive RPR (1:64) and TPPA. A renal biopsy is performed. Which of the following is the most likely glomerular histopathological pattern associated with Secondary Syphilitic Nephropathy?",
        "options": [
            {"id": "A", "text": "Membranous Nephropathy pattern with subepithelial immune deposits"},
            {"id": "B", "text": "Crescentic Glomerulonephritis with pauci-immune pattern"},
            {"id": "C", "text": "Focal Segmental Glomerulosclerosis collapsing variant"},
            {"id": "D", "text": "Dense Deposit Disease"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "Secondary Syphilis 引起的腎病變典型臨床呈現為手掌/腳掌皮疹伴隨 Nephrotic Syndrome，其 Renal Biopsy Pathology 最常表現為 Membranous Nephropathy (Subepithelial Immune Deposits)。病患接受 Penicillin 治療後腎病可完全緩解。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q08",
        "stem": "A 58-year-old patient with severe Membranous Nephropathy and a serum albumin level of 1.7 g/dL develops sudden right flank pain, gross hematuria, and a rapid decline in renal function. Doppler ultrasound reveals thrombosis of the main right renal vein. Loss of which of the following plasma proteins in the urine is primarily responsible for the hypercoagulable state in Nephrotic Syndrome?",
        "options": [
            {"id": "A", "text": "Antithrombin III"},
            {"id": "B", "text": "Fibrinogen"},
            {"id": "C", "text": "Factor V"},
            {"id": "D", "text": "Factor VIII"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "Nephrotic Syndrome 患者極易引發 Hypercoagulability 與 Renal Vein Thrombosis。主因為低分子量之 Endogenous Anticoagulants (特別是 Antithrombin III 及 Protein S/C) 經由尿液大量流失，同時肝臟代償性增加 Fibrinogen, Factor V, Factor VIII 等 Procoagulant Factors 合成。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q09",
        "stem": "Which molecular component of the podocyte slit diaphragm is encoded by the NPHS1 gene, mutational deficiency of which leads to Congenital Nephrotic Syndrome of the Finnish Type?",
        "options": [
            {"id": "A", "text": "Nephrin"},
            {"id": "B", "text": "Podocin"},
            {"id": "C", "text": "CD2AP"},
            {"id": "D", "text": "alpha-Actinin-4"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "NPHS1 基因轉譯產物為 Nephrin，其突變導致 Congenital Nephrotic Syndrome of the Finnish Type。NPHS2 則編碼 Podocin。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_4_2.png",
                "title": "Slit Diaphragm Architecture",
                "relPath": "/reference-images/Brenner 11e/04. Glomerular Cell Biology and Podocytopathies/Fig_4_2.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q10",
        "stem": "A 32-year-old HIV-positive patient not on antiretroviral therapy presents with massive proteinuria (14 g/24h) and rapidly progressive renal failure. Renal biopsy shows severe collapse of glomerular capillaries, podocyte hypertrophy, and microcystic tubular dilation. Which histologic variant of FSGS is classically associated with HIV-associated nephropathy (HIVAN)?",
        "options": [
            {"id": "A", "text": "Collapsing variant"},
            {"id": "B", "text": "Tip lesion variant"},
            {"id": "C", "text": "Perihilar variant"},
            {"id": "D", "text": "Cellular variant"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "HIVAN (HIV-Associated Nephropathy) 之特徵病理為 Collapsing Variant FSGS，伴隨 Glomerular Tuft Collapse, Podocyte Hyperplasia 以及 Tubular Microcysts。該型態預後極差。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_31_5.png",
                "title": "FSGS Histologic Variants",
                "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_5.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q11",
        "stem": "In patients with Primary Membranous Nephropathy, monitoring serologic autoantibody titers has revolutionized clinical decision-making. Which autoantibody titer decline typically precedes clinical remission of proteinuria by several months?",
        "options": [
            {"id": "A", "text": "Anti-PLA2R (Phospholipase A2 Receptor) antibody"},
            {"id": "B", "text": "Anti-dsDNA antibody"},
            {"id": "C", "text": "Anti-GBM antibody"},
            {"id": "D", "text": "Anti-Neutrophil Cytoplasmic Antibody (ANCA)"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "Anti-PLA2R Antibody Titer 代表 Immunologic Activity。在成功治療後，Immunologic Remission (Anti-PLA2R 清除) 領先 Clinical Remission (Proteinuria 下降) 約 3 至 6 個月。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q12",
        "stem": "A 24-year-old female presents with nephrotic syndrome, hypocomplementemia (low C3 and low C4), and positive HCV antibody with positive HCV RNA. Renal biopsy demonstrates endocapillary hypercellularity, mesangial interposition, and double contours (tram-track appearance) of the basement membrane on silver stain. What is the underlying pathophysiological mechanism?",
        "options": [
            {"id": "A", "text": "Immune-complex mediated MPGN driven by Type II Mixed Cryoglobulinemia"},
            {"id": "B", "text": "Alternative complement pathway dysregulation causing C3 Glomerulopathy"},
            {"id": "C", "text": "Podocyte slit diaphragm gene mutation"},
            {"id": "D", "text": "Direct viral infection of podocytes causing podocyte apoptosis"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "HCV 感染常透過 Type II Mixed Cryoglobulinemia 引發 Immune-complex mediated MPGN。輕微及電子顯微鏡下呈 Double-contour Tram-track 樣翻倍，且 C3 與 C4 皆會因 Classical Pathway 消耗而降低。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_31_11.png",
                "title": "MPGN Pathologic Classification Algorithm",
                "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_11.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q13",
        "stem": "Which of the following histologic variants of Focal Segmental Glomerulosclerosis (FSGS) carries the most favorable renal prognosis and highest likelihood of complete remission with corticosteroid therapy?",
        "options": [
            {"id": "A", "text": "Tip lesion variant"},
            {"id": "B", "text": "Collapsing variant"},
            {"id": "C", "text": "Perihilar variant"},
            {"id": "D", "text": "Cellular variant"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "Tip Lesion Variant FSGS (Sclerosis 位於 Tubular Outlet 鄰近之 Proximal Tubule Pole) 具備最佳預後，對 Steroids 反應良好。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q14",
        "stem": "A 50-year-old adult patient diagnosed with biopsy-proven Minimal Change Disease receives first-line high-dose oral Prednisone (1 mg/kg/day). According to KDIGO guidelines, what is the recommended minimum duration of initial corticosteroid therapy before declaring Steroid Resistance?",
        "options": [
            {"id": "A", "text": "16 weeks"},
            {"id": "B", "text": "2 weeks"},
            {"id": "C", "text": "4 weeks"},
            {"id": "D", "text": "24 weeks"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "成人 MCD 對 Steroid 反應較兒童慢。KDIGO 指引建議成人高劑量 Prednisone 需維持至 Remission 或最長達 16 週，方可判定為 Steroid-Resistant MCD。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q15",
        "stem": "Which primary tubular alteration explains the 'Overfill Mechanism' of sodium retention and edema formation in adult Nephrotic Syndrome patients with resistant sodium retention?",
        "options": [
            {"id": "A", "text": "Aberrant activation of the Epithelial Sodium Channel (ENaC) in the cortical collecting duct by urinary plasmin"},
            {"id": "B", "text": "Inhibition of Na-K-2Cl cotransporter (NKCC2) in the thick ascending limb"},
            {"id": "C", "text": "Downregulation of the Sodium-Glucose Cotransporter 2 (SGLT2)"},
            {"id": "D", "text": "Primary suppression of aldosterone release"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "Nephrotic Overfill Mechanism 主要是由於大量漏出至尿液中的 Plasminogen 被轉化為 Plasmin，進而 Proteolytic Cleavage 切割並異常活化 Cortical Collecting Duct 之 Epithelial Sodium Channel (ENaC)。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q16",
        "stem": "A 65-year-old male with long-standing Rheumatoid Arthritis presents with nephrotic syndrome. Renal biopsy reveals Congo Red positive extracellular fibrillar deposits that measure 8 to 12 nm in diameter on electron microscopy. Immunofluorescence is negative for immunoglobulin light chains but positive for Serum Amyloid A protein. What is the diagnosis?",
        "options": [
            {"id": "A", "text": "AA Amyloidosis"},
            {"id": "B", "text": "AL Amyloidosis"},
            {"id": "C", "text": "Fibrillary Glomerulonephritis"},
            {"id": "D", "text": "Immunotactoid Glomerulopathy"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "患者為長期 Rheumatoid Arthritis引發之 Secondary AA Amyloidosis。Congo Red 陽性且 Serum Amyloid A (SAA) 蛋白陽性，纖維直徑為 8-12 nm。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q17",
        "stem": "A 40-year-old male with biopsy-proven Primary FSGS fails to achieve remission after 16 weeks of high-dose oral Prednisone therapy (Steroid-Resistant FSGS). According to KDIGO guidelines, which immunosuppressive agent is recommended as the next line of treatment?",
        "options": [
            {"id": "A", "text": "Calcineurin Inhibitor (Tacrolimus or Cyclosporine)"},
            {"id": "B", "text": "Azathioprine monotherapy"},
            {"id": "C", "text": "High-dose Intravenous Cyclophosphamide monotherapy"},
            {"id": "D", "text": "Observation with low-salt diet"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "KDIGO 2021 指引規定 Steroid-Resistant Primary FSGS 的首選第二線治療為 Calcineurin Inhibitor (CNI，如 Tacrolimus 或 Cyclosporine) 療程至少 6 個月。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q18",
        "stem": "A patient with nephrotic syndrome secondary to Membranous Nephropathy is being evaluated for venous thromboembolism (VTE) risk. Which clinical variable serves as the primary laboratory threshold to consider initiating prophylactic anticoagulation?",
        "options": [
            {"id": "A", "text": "Serum Albumin < 2.0-2.5 g/dL"},
            {"id": "B", "text": "Serum Cholesterol > 400 mg/dL"},
            {"id": "C", "text": "24-hour urine protein > 20 g/day"},
            {"id": "D", "text": "Serum Creatinine > 3.0 mg/dL"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "KDIGO 建議在 Membranous Nephropathy 當 Serum Albumin < 2.0-2.5 g/dL 且伴有 High VTE Risk 時，考量預防性抗凝血治療 (Prophylactic Anticoagulation)。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q19",
        "stem": "On renal electron microscopy of a patient with Membranous Nephropathy, basement membrane material projects between subepithelial electron-dense deposits forming characteristic 'spikes'. Which ultrastructural stage of Membranous Nephropathy does this represent?",
        "options": [
            {"id": "A", "text": "Stage II"},
            {"id": "B", "text": "Stage I"},
            {"id": "C", "text": "Stage III"},
            {"id": "D", "text": "Stage IV"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "Membranous Nephropathy Stage II 的關鍵特徵為 GBM 增生形成包繞 Subepithelial Deposits 之 Spikes。Stage I 僅有 Deposits 無 Spikes；Stage III 為 Dome-and-Spike 完全包覆；Stage IV 為 Moth-eaten Lucent Deposits。",
        "resolvedImages": [
            {
                "id": "Brenner 11e_Fig_31_7.png",
                "title": "Membranous Nephropathy Stages",
                "relPath": "/reference-images/Brenner 11e/31. Primary Glomerular Disease/Fig_31_7.png"
            }
        ],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    },
    {
        "id": f"{paper_id}_Q20",
        "stem": "High-risk APOL1 gene variants (G1 and G2 alleles), common in individuals of West African ancestry, strongly predispose individuals to which primary glomerular disease?",
        "options": [
            {"id": "A", "text": "Focal Segmental Glomerulosclerosis (FSGS)"},
            {"id": "B", "text": "Minimal Change Disease (MCD)"},
            {"id": "C", "text": "Membranous Nephropathy (MN)"},
            {"id": "D", "text": "IgA Nephropathy"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "selectedOption": "A",
        "sourceExplanation": "APOL1 (Apolipoprotein L1) 高風險對偶基因 (G1/G2) 是引發 African Ancestry 人群之 Non-diabetic CKD, HIVAN 與 Primary FSGS (特別是 Collapsing FSGS) 的強烈遺傳風險因子。",
        "resolvedImages": [],
        "nlmResponses": [],
        "reconciliationStatus": "PENDING",
        "qcVerified": False,
        "qcStatus": "PENDING"
    }
]

paper_data = {
    "paperId": paper_id,
    "paperTitle": "Nephrotic Syndrome 專題精選試題與雙重 NLM 解析 (2026)",
    "year": 2026,
    "category": "TSN 歷年交換題",
    "sourceCategory": "2026 年主題練習",
    "totalQuestions": len(questions_data),
    "questions": questions_data
}

paper_file = f"/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{paper_id}.json"
with open(paper_file, "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print(f"Wrote question bank JSON: {paper_file}")

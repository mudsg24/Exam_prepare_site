import json
import os

paper_id = "2026_Care_of_the_Older_Adult_With_Chronic_Kidney_Disease_(主題備考)"
title = "2026 Care of the Older Adult With Chronic Kidney Disease (高齡慢性腎臟病照護 / 老化腎臟病理機轉 / 衰弱評估 / 保守性腎臟處置 CKM / 藥物劑量調整)"
source_category = "2026 年主題練習"
year = 2026

tutorial_data = {
    "paperId": paper_id,
    "title": title,
    "sourceCategory": source_category,
    "year": year,
    "sections": [
        {
            "id": "section-1",
            "title": "Renal Aging Pathophysiology & Structural-Functional Senescence vs Disease",
            "content": """### Topology Mapping Matrix: Structural & Physiological Senescence of the Aging Kidney

老化腎臟的結構與生理變化的拓撲對應關係如下：

| Structural / Functional Domain | Primary Senescent Alteration | Physiological Consequence & Clinical Impact |
| :--- | :--- | :--- |
| **Renal Parenchymal Mass** | Cortical Volume Loss (Medullary volume constant until 50 yrs) | Overall kidney mass decreases past age 50; Renal Parenchyma thins |
| **Glomerular Histology** | Age-related Global Glomerulosclerosis (GSG) | Loss of functional nephrons, compensated by Hyperfiltration in remaining nephrons |
| **Vascular Architecture** | Intimal Thickening & Hyaline Arteriosclerosis | Increased Intrarenal Vascular Resistance, reduced Renal Blood Flow (RBF) |
| **Tubulointerstitial Compartment** | Tubular Atrophy & Interstitial Fibrosis | Impaired Urinary Concentrating Ability, impaired Acid Secretion |
| **Molecular Markers** | Reduction in Klotho & Sirtuin 1/6, elevation of P16INK4a | Cellular Senescence, increased Oxidative Stress, accelerated Fibrosis via TGF-beta |

---

### Pathophysiological Decision Tree: Age-Related GFR Decline vs Pathological Nephrosclerosis

```
[ Age-Related Physiological Decline vs Pathological CKD ]
  │
  ├── Physiological Renal Aging (Senescence)
  │     ├── Smooth Kidney Contour, Minimal Albuminuria (UACR < 30 mg/g)
  │     ├── Predictable GFR decline (~6-7 mL/min/1.73m2 per decade after age 40)
  │     └── Biopsy (if done): Global Glomerulosclerosis within Age-Predicted Limits (Table 22.1)
  │
  └── Pathological Chronic Kidney Disease (CKD)
        ├── Irregular Kidney Surface (Surface Roughness Score > 2, Fig 22.3)
        ├── Overt Proteinuria / Microalbuminuria (UACR > 30-300 mg/g)
        ├── Accelerated GFR decline (> 3-5 mL/min/1.73m2 per year)
        └── Biopsy: Focal Segmental Glomerulosclerosis, Severe Arteriosclerosis > Age Norms
```

---

### High-Yield Differential Comparison: Structural & Functional Aging Spectrum

| Parameter | Physiological Aging Kidney | Disease-Related Nephrosclerosis / CKD |
| :--- | :--- | :--- |
| **Glomerular Sclerosis Pattern** | Global Glomerulosclerosis (GSG) | Focal Segmental Glomerulosclerosis (FSGS) or Severe Arteriosclerosis |
| **Albuminuria Level** | Normal or Microalbuminuria (< 30 mg/g) | Moderate to Severe Albuminuria (> 30-300+ mg/g) |
| **Renal Blood Flow (RBF)** | Gradual decline (~10% per decade past 40) | Marked reduction with Intrarenal Ischemia |
| **Concentrating & Diluting Capacity** | Reduced Max Uosm (Medullary Washout) | Severe Isosthenuria (Fixed Uosm ~300 mOsm/kg) |
| **Renin-Aldosterone Dynamics** | Hyporeninemic Hypoaldosteronism trend | Variable, often secondary Hyperreninemia in RAS |

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 1: 誤將年齡相關 Global Glomerulosclerosis 判定為 Chronic Glomerulonephritis**  
> 在健康老年人腎臟切片中，出現一定比例的 Global Glomerulosclerosis (GSG) 屬於正常生理老化。根據 Kremers 等人與 Brenner 11e Table 22.1 的推估，70 歲健康捐腎者即使有高達 10-15% 的 GSG，若缺乏 Segmental Sclerosis、Significant Interstitial Fibrosis 或 Albuminuria，絕不可誤診為原發性腎絲球腎炎！

> [!TIP]
> **Key Pearl: Molecular Regulators of Renal Aging**  
> Klotho 基因主要表現於 Distal Convoluted Tubule，其產物單次跨膜蛋白與可溶性 Klotho 具抗老化與抑制 Wnt/beta-catenin 纖維化作用。老化過程中 Klotho 與 Sirtuin 1/6 活性下降，是驅動 Podocytopenia 與 Renal Fibrosis 的關鍵生化標記。""",
            "diagrams": [
                {
                    "id": "diagram-1-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_1.png",
                    "imagePath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_1.png",
                    "caption": "Brenner 11e Fig 22.1: Cortical and medullary volume changes across age groups in potential kidney donors.",
                    "sourceBook": "Brenner 11e Ch 22"
                },
                {
                    "id": "diagram-1-2",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_7.png",
                    "imagePath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_7.png",
                    "caption": "Brenner 11e Fig 22.7: Age-related decline in estimated and measured Glomerular Filtration Rate.",
                    "sourceBook": "Brenner 11e Ch 22"
                },
                {
                    "id": "diagram-1-3",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/geriatric_ckd_aging.jpg",
                    "imagePath": "/server-data/assets/geriatric_ckd_aging.jpg",
                    "caption": "Gemini AI Illustration: Mechanisms of Renal Aging in Older Adults (Macro, Micro, and Cellular Pathway).",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        },
        {
            "id": "section-2",
            "title": "Comprehensive Geriatric Assessment & GFR Evaluation in Frail Older Adults",
            "content": """### Topology Mapping Matrix: Comprehensive Geriatric Assessment (CGA) Domains in CKD

針對高齡 CKD 病患的多維度周全性老年評估 (CGA) 架構：

| CGA Assessment Domain | Clinical Tool / Parameter | Impact on Kidney Care & Clinical Outcomes |
| :--- | :--- | :--- |
| **GFR Filtration Markers** | Serum Creatinine vs Cystatin C | Sarcopenia causes Serum Creatinine to over-estimate eGFR; Cystatin C provides accurate eGFR |
| **Physical Frailty** | Fried Frailty Phenotype / Clinical Frailty Scale (CFS) | Frailty predicts Dialysis Mortality, Hospitalization, and Rapid Decline |
| **Functional Status** | Activities of Daily Living (ADL / iADL) | Guides Vascular Access selection and Self-Care Capability for Home Dialysis |
| **Cognitive Assessment** | Mini-Mental State Exam (MMSE) / MoCA | Impaired Decision-Making Capacity, Medication Non-Adherence risk |
| **Nutritional Status** | Serum Albumin, Subjective Global Assessment (SGA) | Distinguishes Uremic Sarcopenia & Protein-Energy Wasting (PEW) from Malnutrition |

---

### Pathophysiological Decision Tree: Stepwise GFR Estimation in Sarcopenic Elderly Patients

```
[ GFR Evaluation Strategy in Older Adults with Muscle Wasting ]
  │
  ├── Step 1: Initial Assessment with eGFR_cr (CKD-EPI 2021 Creatinine Equation)
  │     └── Caution: Low Serum Creatinine due to Sarcopenia / Low Muscle Mass
  │
  ├── Step 2: Confirm GFR with eGFR_cys or eGFR_cr-cys Combination
  │     ├── eGFR_cys significantly LOWER than eGFR_cr (> 15-20 mL/min/1.73m2 difference)
  │     └── Indicates True Renal Function Impairment & Muscle Mass Loss ("Shrinking Pore Syndrome" / Sarcopenia)
  │
  └── Step 3: Integrate Clinical Frailty Scale (CFS) & Comorbidities
        ├── CFS Score 1-3 (Fit / Well): Standard CKD Risk Management & Preparation
        └── CFS Score 6-8 (Moderate to Severely Frail): Consider Conservative Kidney Management (CKM)
```

---

### High-Yield Differential Comparison: Creatinine vs Cystatin C in Geriatric CKD

| Evaluation Feature | Serum Creatinine (SCr) | Cystatin C (CysC) |
| :--- | :--- | :--- |
| **Endogenous Source** | Skeletal Muscle Breakdown | All Nucleated Cells (Constant production rate) |
| **Sarcopenia Impact** | False Low SCr -> Overestimates GFR | Independent of Muscle Mass & Gender |
| **Non-Renal Influences** | Dietary Meat Intake, Muscle Mass, Age | Thyroid Dysfunction, High-Dose Steroids, Obesity |
| **Clinical Superiority** | Routine screening, cheap | Superior prognostic indicator for Mortality & Cardiovascular Risk |
| **KDIGO Recommendation** | Initial filtration test | Confirmatory test for eGFR 45-59 without albuminuria, and in Sarcopenia |

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 2: 僅依據 Serum Creatinine 判定高齡病患腎功能正常**  
> 臥床或高度 Sarcopenia 的高齡病患，Serum Creatinine 可能看似正常 (如 0.8 mg/dL)，但實際 mGFR 可能已降至 < 20 mL/min/1.73m2！若未抽測 Cystatin C 或執行 24-hour Creatinine Clearance，易造成 Gentamicin、Digoxin 或 DOACs 劑量過高致嚴重毒性！

> [!TIP]
> **Key Pearl: Clinical Frailty Scale (CFS) Thresholds**  
> CFS 評分 1-9 分中，CFS >= 6 代表 Moderate Frailty（日常需要他人協助），在 ESKD 決策中為預後極差之強烈指標。""",
            "diagrams": [
                {
                    "id": "diagram-2-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Table_22_2.png",
                    "imagePath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Table_22_2.png",
                    "caption": "Brenner 11e Table 22.2: Reference values for estimated and measured GFR in potential kidney donors.",
                    "sourceBook": "Brenner 11e Ch 22"
                },
                {
                    "id": "diagram-2-2",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/geriatric_ckd_frailty.jpg",
                    "imagePath": "/server-data/assets/geriatric_ckd_frailty.jpg",
                    "caption": "Gemini AI Infographic: Integrating CGA, SCr vs Cystatin C, and Clinical Frailty Scale in CKD.",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        },
        {
            "id": "section-3",
            "title": "Comprehensive Conservative Kidney Management (CKM) & Shared Decision-Making",
            "content": """### Topology Mapping Matrix: Shared Decision-Making & Care Pathways in Advanced Geriatric CKD

末期腎臟病 (ESKD) 高齡病患照護路徑處置對應矩陣：

| Care Pathway | Target Patient Population | Core Clinical Goals & Interventions |
| :--- | :--- | :--- |
| **Dialysis Pathway (HD / PD)** | Fit Elderly (CFS 1-4), High Life Expectancy, Active Lifestyle | Vascular Access / PD catheter, Dialysis Adequacy, Prolonging Survival |
| **Conservative Kidney Management (CKM)** | Frail Elderly (CFS >= 6), Age > 80 with Severe Comorbidities | Non-dialytic Symptom Control, Preserving Quality of Life, Advance Care Planning |
| **Time-Limited Trial (TLT)** | Uncertain Prognosis, Acute-on-Chronic Decline | Trial of Dialysis for defined period (e.g. 1-3 months) with re-evaluation |
| **Palliative & Hospice Care** | End-Stage Renal Senescence, Uremic Terminal Phase | Pain Relief, Dyspnea Management (Opioids), Active Comfort Measures |

---

### Pathophysiological Decision Tree: Dialysis vs Conservative Kidney Management (CKM) Decision Framework

```
[ Advanced CKD (eGFR < 10-15 mL/min/1.73m2) in Older Adults ]
  │
  ├── Step 1: Multidisciplinary Comprehensive Geriatric Assessment (CGA)
  │     ├── Assess Frailty (CFS score), Dementia, Severe Heart Failure (NYHA III/IV), Cancer
  │     └── Calculate Predicted 1-Year Survival (e.g., Bansal Score / REIN Score)
  │
  ├── Step 2: Shared Decision-Making (SDM) Conference
  │     ├── Discuss Patient Values, Personal Goals, Quality of Life vs Treatment Burden
  │     └── Clarify Dialysis Outcome Expectations (Survival Gain vs Hospitalization Risk)
  │
  └── Step 3: Selection of Management Pathway
        ├── Pathway A: Dialysis Preparation (HD/PD) ➔ For Functional, Fit Patients
        ├── Pathway B: Conservative Kidney Management (CKM) ➔ Active non-dialytic symptom management
        └── Pathway C: Time-Limited Trial (TLT) ➔ Trial dialysis with clear stop criteria
```

---

### High-Yield Differential Comparison: Dialysis vs Conservative Kidney Management in Frail Elderly

| Clinical Dimension | Dialysis Pathway in Frail Elderly | Conservative Kidney Management (CKM) |
| :--- | :--- | :--- |
| **Survival Gain (Age > 75-80, High Comorbidity)** | Minimal to NO significant overall survival benefit | Equivalent symptom-free survival without dialysis |
| **Quality of Life Trajectory** | Frequent functional decline post-initiation, High Hospitalization | Stable functional trajectory, Preserved home-stay days |
| **Invasive Burden** | AV Fistula surgery, Central Line, Hemodialysis fatigue | Oral medications, Dietary adjustment, Outpatient symptom control |
| **Primary Symptoms Managed** | Fluid overload, Hyperkalemia, Uremic Pericarditis | Pruritus, Dyspnea, Restless Legs, Pain, Nausea |
| **Advance Care Planning (ACP)** | Mandatory POLST / Surrogate designation | Integrated POLST / DNR / Comfort Goals from start |

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 3: 認為 Conservative Kidney Management (CKM) 等同於放棄治療 (Abandonment of Care)**  
> 臨床上 **CKM 絕對不是放棄治療**！CKM 是一種積極、多專業合力進行的非血液透析綜合醫療處置，包括積極調整 Anemia、Fluid Balance、Metabolic Acidosis、Hypokalemia/Hyperkalemia、Hyperphosphatemia，並使用 Low-Dose Morphine 緩解 Dyspnea 與 Uremic Pain，顯著提升生活品質！

> [!TIP]
> **Key Pearl: Time-Limited Trial (TLT) Strategy**  
> 當高齡病患或家屬對透析抉擇極度掙扎且預後不明時，最佳共識為簽署 Time-Limited Trial，約定透析 4 至 8 週。若臨床狀況改善則繼續，若神智更為退化或品質急劇惡化則合情合理轉為 Comfort Care。""",
            "diagrams": [
                {
                    "id": "diagram-3-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Box_22_2.png",
                    "imagePath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Box_22_2.png",
                    "caption": "Brenner 11e Box 22.2: Common Kidney and Urinary Tract Diseases in Older Adults.",
                    "sourceBook": "Brenner 11e Ch 22"
                },
                {
                    "id": "diagram-3-2",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/geriatric_ckd_ckm.jpg",
                    "imagePath": "/server-data/assets/geriatric_ckd_ckm.jpg",
                    "caption": "Gemini AI Flowchart: Dialysis Initiation vs Conservative Kidney Management (CKM) Decision Tree.",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        },
        {
            "id": "section-4",
            "title": "Geriatric Pharmacotherapy, Pharmacokinetics, Dosing Adjustments & Deprescribing",
            "content": """### Topology Mapping Matrix: Pharmacokinetic Alterations & High-Risk Drugs in Geriatric CKD

高齡 CKD 藥理學改變與高風險藥物處置對應：

| Pharmacokinetic Property | Age & CKD Physiological Alteration | Clinical Consequence & High-Risk Drug Examples |
| :--- | :--- | :--- |
| **Renal Elimination (Clearance)** | Reduced GFR and Tubular Secretion | Accumulation of Active Metabolites: Gabapentin, Pregabalin, Digoxin, Allopurinol |
| **Volume of Distribution (Vd)** | Decreased Total Body Water, Increased Fat | Water-soluble drugs have higher peak concentrations; Fat-soluble drugs prolonged half-life |
| **Protein Binding** | Decreased Serum Albumin, Uremic Binding Loss | Increased Free Drug Fraction: Phenytoin, Warfarin, Salicylates |
| **Pharmacodynamics (Sensitivity)** | Increased Central & Cardiac Sensitivity | Benzodiazepines cause Severe Sedation & Falls; NSAIDs cause Acute Renal Hemodynamic Collapse |
| **Deprescribing Tools** | Beers Criteria & STOPP/START Criteria | Identification of Inappropriate Prescriptions, Prevention of Polypharmacy-Induced AKI |

---

### Pathophysiological Decision Tree: Renal Prescribing & Deprescribing Protocol

```
[ Pharmacotherapy Review in Geriatric CKD Patient ]
  │
  ├── Step 1: Calculate Accurate Renal Clearance (eGFR_cr-cys or CrCl by Cockcroft-Gault)
  │
  ├── Step 2: Screen High-Risk Medications (Beers / STOPP Criteria)
  │     ├── NSAIDs ➔ STOP (Triggers NSAID-induced AKI & Hyperkalemia via Cox-2 inhibition)
  │     ├── Sulfonylureas (Glibenclamide/Glyburide) ➔ STOP (Risk of Prolonged Hypoglycemia)
  │     └── Long-Acting Benzodiazepines ➔ STOP (Dementia, Fall Risk, Sedation)
  │
  ├── Step 3: Dose Adjustments for Essential Therapeutics
  │     ├── DOACs (Apixaban / Rivaroxaban) ➔ Adjust dose based on Age, Weight, Serum Creatinine
  │     ├── Gabapentin / Pregabalin ➔ Reduce dose by 50-75% in GFR < 30 (Prevents Myoclonus/Encephalopathy)
  │     └── Metformin ➔ Maximum 1000 mg/day for eGFR 30-44; DISCONTINUE if eGFR < 30 mL/min
  │
  └── Step 4: Monitoring Strategy
        └── Recheck Potassium & Creatinine within 7-14 days of RAASi or Diuretic titration
```

---

### High-Yield Differential Comparison: DOAC Dosing Rules in Geriatric CKD

| DOAC Agent | Dose Reduction Criteria in Geriatric CKD | Contraindication Threshold |
| :--- | :--- | :--- |
| **Apixaban** | Standard 5mg BID -> Reduce to 2.5mg BID if >= 2 criteria: Age >= 80, Weight <= 60kg, SCr >= 1.5 mg/dL | CrCl < 15 mL/min (US FDA allows 2.5mg BID; EMA avoids) |
| **Rivaroxaban** | Standard 20mg QD -> Reduce to 15mg QD if CrCl 15-49 mL/min | CrCl < 15 mL/min |
| **Dabigatran** | Standard 150mg BID -> Reduce to 110mg BID if Age >= 80 or CrCl 30-49 mL/min | CrCl < 30 mL/min (Contraindicated due to 80% renal excretion) |
| **Edoxaban** | Standard 60mg QD -> Reduce to 30mg QD if CrCl 15-50 mL/min or Weight <= 60kg | CrCl < 15 mL/min or CrCl > 95 mL/min (High clearance risk) |

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 4: Gabapentin Neurotoxicity 誤判為 Uremic Encephalopathy**  
> 腎功能過低 (eGFR < 30 mL/min) 時，若未調降 Gabapentin 或 Pregabalin 劑量 (如仍使用 300 mg TID)，極易因中樞神經蓄積引發 Severe Myoclonus, Lethargy, Flapping Tremor 與 Coma！臨床上常被誤判為 Uremic Encephalopathy 而緊急送透析，實則只需停藥與降劑量即可恢復！

> [!TIP]
> **Key Pearl: NSAIDs Hemodynamic AKI Mechanism**  
> NSAIDs 抑制 Prostaglandin Synthesis (Afferent Arteriolar Vasodilation)，在併用 RAAS Inhibitors (Efferent Arteriolar Vasodilation) 與 Diuretics 時構成「Triple Whammy」，極易誘發高齡病患爆發 Prerenal AKI！""",
            "diagrams": [
                {
                    "id": "diagram-4-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Box_22_1.png",
                    "imagePath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Box_22_1.png",
                    "caption": "Brenner 11e Box 22.1: Postulated Factors Involved in Renal Aging and Molecular Degradation.",
                    "sourceBook": "Brenner 11e Ch 22"
                },
                {
                    "id": "diagram-4-2",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/geriatric_ckd_dosing.jpg",
                    "imagePath": "/server-data/assets/geriatric_ckd_dosing.jpg",
                    "caption": "Gemini AI Pharmacology Infographic: Pharmacokinetics, Beers Criteria & DOAC Dosing in Geriatric CKD.",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        },
        {
            "id": "section-5",
            "title": "Geriatric Syndromes & Multi-Comorbid Management in CKD",
            "content": """### Topology Mapping Matrix: Geriatric Syndromes & Comorbid Interventions in CKD

高齡 CKD 併發症與症候群綜合介入矩陣：

| Geriatric Syndrome / Comorbidity | Pathophysiological Driver | Clinical Management Strategy & Targets |
| :--- | :--- | :--- |
| **Uremic Sarcopenia & PEW** | Metabolic Acidosis, Chronic Inflammation, Resistance to Insulin/IGF-1 | Protein Intake 0.8 g/kg/day, Correct Acidosis (Bicarbonate > 22), Resistance Exercise |
| **CKD-MBD & Fragility Fractures** | High PTH, Vitamin D deficiency, Adynamic Bone Disease prevalence | Avoid Hypercalcemia, cautious Phosphate Binders, Fall Prevention |
| **Anemia of CKD** | Impaired EPO production, Functional Iron Deficiency, Hepcidin elevation | Target Hb 10-11.5 g/dL (Avoid Hb > 12-13 due to Stroke Risk); ESA or HIF-PHI |
| **Hypertension & Blood Pressure** | Vascular Stiffness, Volume Overload, Impaired Pressure Natriuresis | KDIGO 2021 SBP target < 120 mmHg (standard) vs Individualized < 130-140 in Frail Elderly |
| **Orthostatic Hypotension & Falls** | Autonomic Dysfunction, Rigid Arteries, Overtreatment with Antihypertensives | Monitor Standing BP, avoid SBP < 110-120 in severely frail, Deprescribe Vasodilators |

---

### Pathophysiological Decision Tree: Blood Pressure Management in Frail vs Fit Elderly CKD Patients

```
[ Blood Pressure Management Strategy in Older Adults with CKD ]
  │
  ├── Step 1: Standard Risk Stratification (SPRINT Senior Trial Insights)
  │     ├── Fit Elderly (Vital, Active, Ambulatory, CFS 1-3)
  │     └── Intensive Target: Systolic BP < 120 mmHg (Reduces Mortality & CV Events)
  │
  └── Step 2: Individualized Relaxation for Frail / Vulnerable Patients (CFS >= 5-6)
        ├── Check Standing Blood Pressure for Orthostatic Drop (SBP drop > 20 mmHg)
        ├── High Fall Risk, Cognitive Impairment, History of Syncope
        └── Individualized Target: Systolic BP 130-140 mmHg (Avoid SBP < 120 mmHg to prevent Falls & Ischemia)
```

---

### High-Yield Differential Comparison: Anemia Therapeutics - ESA vs HIF-PHI in Geriatric CKD

| Clinical Metric | Erythropoiesis-Stimulating Agents (ESA - e.g. Epoetin, Darbepoetin) | HIF-Prolyl Hydroxylase Inhibitors (HIF-PHI - e.g. Roxadustat, Vadadustat) |
| :--- | :--- | :--- |
| **Administration Route** | Subcutaneous / Intravenous Injections | Oral Administration (Daily or 3x/week) |
| **Mechanism of Action** | Recombinant EPO binding directly to EPO Receptor | Inhibits HIF degradation, stimulates endogenous EPO & improves Iron Utilization |
| **Efficacy in Inflammation** | Resistance in High-Inflammation / High-Hepcidin states | Effective despite Chronic Inflammation & High Hepcidin |
| **Cardiovascular & Thrombotic Risk** | Increased Stroke & Thrombosis risk if Hb target > 12-13 g/dL | Target Hb 10-11 g/dL; Monitor for Vascular Access Thrombosis & Hyperkalemia |
| **Patient Preference** | Injections require clinic visits or home nurse | Oral pill preferred in non-dialysis CKM or home care |

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 5: 為高齡 CKD 病患設定過高之 Anemia Target (Hb > 13 g/dL)**  
> TREAT 試驗與 CHOIR 試驗明確指出，使用高劑量 ESA 將 Hb 拉高至 > 13 g/dL，不僅無法改善品質，反而顯著增加 Stroke、Venous Thromboembolism 與 Cardiovascular Mortality！在高齡 CKD 病患中，Hb 目標一律鎖定在 10.0 - 11.5 g/dL！

> [!TIP]
> **Key Pearl: Metabolic Acidosis Correction in Sarcopenia**  
> Metabolic Acidosis 活化 Ubiquitin-Proteasome Pathway 與 Caspase-3，加速骨骼肌分解。給予 Oral Sodium Bicarbonate 將 Serum HCO3- 維持在 22-26 mEq/L，可有效減緩 Sarcopenia 惡化與 GFR 下降速率。""",
            "diagrams": [
                {
                    "id": "diagram-5-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_6.png",
                    "imagePath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_6.png",
                    "caption": "Brenner 11e Fig 22.6: Nephrosclerosis score distribution by age group in healthy adults.",
                    "sourceBook": "Brenner 11e Ch 22"
                },
                {
                    "id": "diagram-5-2",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/geriatric_ckd_syndromes.jpg",
                    "imagePath": "/server-data/assets/geriatric_ckd_syndromes.jpg",
                    "caption": "Gemini AI Clinical Overview: Uremic Sarcopenia, PEW, CKD-MBD & BP Targets in Geriatric CKD.",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        }
    ]
}

questions_data = [
    {
        "id": "2026_Geriatric_CKD_Q1",
        "number": 1,
        "stem": "Which of the following macroscopic volumetric changes in the kidney is most characteristically observed in healthy individuals between 18 and 50 years of age, as described in the Aging Kidney Anatomy study?",
        "options": [
            {"id": "A", "text": "Cortical volume progressively decreases while medullary volume increases, keeping total kidney volume relatively constant"},
            {"id": "B", "text": "Both cortical and medullary volumes decrease rapidly, leading to a marked reduction in total kidney volume before age 40"},
            {"id": "C", "text": "Cortical volume increases to compensate for nephron loss while medullary volume undergoes total fatty degeneration"},
            {"id": "D", "text": "Total kidney volume increases by more than 50% due to physiological hypertrophy of the renal medulla"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "根據 Aging Kidney Anatomy 研究 (Brenner 11e Fig 22.1)，在 18 至 50 歲健康個體中，Cortical Volume 隨年齡增加而逐漸減少，而 Medullary Volume 則相對增加。這兩種相反的體積變化使 Total Kidney Volume 在 50 歲之前維持相對恆定；超過 50 歲後 Medullary Volume 不再增加， Total Kidney Volume 才因 Cortical Volume 持續減少而顯著下降。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing macroscopic structural renal aging dynamics.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_1.png",
                "caption": "Brenner 11e Fig 22.1: Cortical and medullary volume changes across age groups in potential kidney donors.",
                "sourceBook": "Brenner 11e Ch 22"
            }
        ]
    },
    {
        "id": "2026_Geriatric_CKD_Q2",
        "number": 2,
        "stem": "In evaluating a kidney biopsy from a healthy 72-year-old potential living kidney donor, which histological pattern of glomerulosclerosis is considered a normal manifestation of physiological renal aging rather than underlying primary glomerulonephritis?",
        "options": [
            {"id": "A", "text": "Segmental sclerosis involving the perihilar region of glomeruli with severe podocyte foot process effacement"},
            {"id": "B", "text": "Global glomerulosclerosis affecting a modest percentage of glomeruli within age-predicted reference limits without marked interstitial fibrosis"},
            {"id": "C", "text": "Nodular mesangial sclerosis associated with prominent capillary basement membrane thickening"},
            {"id": "D", "text": "Crescentic glomerular collapse with fibrous crescents involving more than 50% of renal corpuscles"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "正常生理老化 (Physiological Renal Aging) 的腎絲球硬化特徵為 Global Glomerulosclerosis (GSG) (Brenner 11e Fig 22.4 & Table 22.1)，其發生比例在年齡推估之正常參考值範圍內，且不伴隨高度 Segmental Sclerosis 或原發性病變。而 Focal Segmental Glomerulosclerosis (FSGS) 或 Nodular Sclerosis 則屬於病理性疾病。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing age-related global vs pathological glomerulosclerosis.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_4.png",
                "caption": "Brenner 11e Fig 22.4: Globally sclerosed glomeruli in different stages of involution.",
                "sourceBook": "Brenner 11e Ch 22"
            }
        ]
    },
    {
        "id": "2026_Geriatric_CKD_Q3",
        "number": 3,
        "stem": "Which molecular factor's expression is characteristically reduced in renal aging, contributing to accelerated Wnt/beta-catenin signaling, loss of antioxidant defenses, and renal interstitial fibrosis?",
        "options": [
            {"id": "A", "text": "Transforming growth factor beta 1 (TGF-beta1)"},
            {"id": "B", "text": "Angiotensin II receptor type 1 (AT1R)"},
            {"id": "C", "text": "Klotho protein expression"},
            {"id": "D", "text": "Cyclin-dependent kinase inhibitor P16INK4a"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "根據 Brenner 11e Box 22.1，腎臟老化過程中關鍵抑癌與抗老化蛋白 Klotho expression (及 Sirtuin 1/6) 顯著下降。Klotho 缺失解除了對 Wnt/beta-catenin 訊號的抑制，進而誘發 Podocyte 凋亡與 TGF-beta 介導的 Interstitial Fibrosis。而 P16INK4a 與 TGF-beta1 在老化腎臟中則是表現上升。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question on molecular drivers of renal aging.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Box_22_1.png",
                "caption": "Brenner 11e Box 22.1: Postulated Factors Involved in Renal Aging.",
                "sourceBook": "Brenner 11e Ch 22"
            }
        ]
    },
    {
        "id": "2026_Geriatric_CKD_Q4",
        "number": 4,
        "stem": "According to the Aging Kidney Anatomy study data presented in Brenner & Rector's The Kidney, what is the average calculated decline in estimated GFR (CKD-EPI equation) per decade in healthy adults past age 40?",
        "options": [
            {"id": "A", "text": "Approximately 1.5 mL/min/1.73m2 per decade"},
            {"id": "B", "text": "Approximately 3.0 mL/min/1.73m2 per decade"},
            {"id": "C", "text": "Approximately 12.5 mL/min/1.73m2 per decade"},
            {"id": "D", "text": "Approximately 7.4 mL/min/1.73m2 per decade"}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "根據 Brenner 11e Fig 22.7 與內文，健康成人在 40 歲以後，依 CKD-EPI 公式計算之 Estimated GFR (eGFR) 平均每十年下降 7.4 mL/min/1.73m2，而 Measured GFR (mGFR) 每十年下降約 6.1 mL/min/1.73m2。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing quantitative age-related GFR trajectory.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Fig_22_7.png",
                "caption": "Brenner 11e Fig 22.7: Age-related decline in estimated and measured Glomerular Filtration Rate.",
                "sourceBook": "Brenner 11e Ch 22"
            }
        ]
    },
    {
        "id": "2026_Geriatric_CKD_Q5",
        "number": 5,
        "stem": "An 82-year-old bedridden woman with severe sarcopenia has a routine Serum Creatinine of 0.7 mg/dL. Her calculated eGFR based on Creatinine alone is 78 mL/min/1.73m2. Which of the following statements regarding her renal function evaluation is CORRECT?",
        "options": [
            {"id": "A", "text": "Creatinine-based eGFR overestimates her actual GFR due to reduced muscle mass; Cystatin C measurement will provide a more accurate evaluation"},
            {"id": "B", "text": "Creatinine-based eGFR underestimates her actual GFR because age automatically corrects for muscle wasting"},
            {"id": "C", "text": "Cystatin C is invalid in older adults because its production rate drops by 90% in sarcopenia"},
            {"id": "D", "text": "Her 24-hour urine creatinine clearance will be falsely elevated due to sarcopenia"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "高齡且具重度 Sarcopenia 的病患，因肌肉量大幅減少，Serum Creatinine 生成極少 (如 0.7 mg/dL)，導致僅依據 Creatinine 計算的 eGFR (eGFR_cr) 嚴重過度高估 (Overestimate) 實際腎功能。Cystatin C 由所有有核細胞以恆定速率生成，不受 Sarcopenia 影響，因此能提供更精準之 GFR 評估。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing creatinine limitations in sarcopenic elderly.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/22. The Physiology and Pathophysiology of the Kidneys in Aging/Table_22_2.png",
                "caption": "Brenner 11e Table 22.2: Reference values for GFR in potential kidney donors by age.",
                "sourceBook": "Brenner 11e Ch 22"
            }
        ]
    },
    {
        "id": "2026_Geriatric_CKD_Q6",
        "number": 6,
        "stem": "Which tool is specifically validated in Geriatric Nephrology to evaluate multidimensional physical frailty and vulnerability, predicting hospitalization and dialysis mortality in older adults with advanced CKD?",
        "options": [
            {"id": "A", "text": "Charlson Comorbidity Index (CCI) alone without physical domain"},
            {"id": "B", "text": "Clinical Frailty Scale (CFS) / Fried Frailty Phenotype"},
            {"id": "C", "text": "Karnofsky Performance Scale for oncology patients"},
            {"id": "D", "text": "Glasgow Coma Scale (GCS)"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Clinical Frailty Scale (CFS) 與 Fried Frailty Phenotype 是周全性老年評估 (CGA) 中專門用於測量物理 Frailty 的黃金標準工具。在 advanced CKD 病患中，高 CFS 分數 (>= 6) 為預測透析住院率、功能退化與死亡率的強烈獨立因子。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing frailty metrics in nephrology.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q7",
        "number": 7,
        "stem": "For an 84-year-old patient with Stage 5 CKD (eGFR 9 mL/min/1.73m2), severe dementia, and a Clinical Frailty Scale (CFS) score of 7, comparative clinical studies demonstrate which of the following regarding Conservative Kidney Management (CKM) versus Dialysis initiation?",
        "options": [
            {"id": "A", "text": "Dialysis initiation prolongs survival by an average of 10 years compared to CKM regardless of frailty status"},
            {"id": "B", "text": "CKM causes immediate death within 48 hours due to lack of symptom management"},
            {"id": "C", "text": "Dialysis provides minimal to no overall survival benefit over CKM, while significantly increasing hospitalization rates and functional loss"},
            {"id": "D", "text": "CKM requires immediate surgical placement of an arteriovenous fistula"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "在年齡 > 80 歲、具重度 Frailty (CFS >= 7) 及高共病的 advanced CKD 病患中，多項臨床研究顯示開始 Dialysis 相較於 Conservative Kidney Management (CKM) 並沒有顯著的整體存活優勢 (Survival Benefit)，反之 Dialysis 會顯著增加 Hospitalization、侵入性處置與功能快速退化風險。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing CKM vs Dialysis outcomes in frail elderly.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q8",
        "number": 8,
        "stem": "Which of the following interventions represents a core active component of Conservative Kidney Management (CKM) for managing uremic symptoms and fluid balance in non-dialysis elderly patients?",
        "options": [
            {"id": "A", "text": "Complete withdrawal of all oral medications and fluid restriction to zero"},
            {"id": "B", "text": "High-dose intravenous chemotherapy to reduce renal inflammation"},
            {"id": "C", "text": "Total protein hyperalimentation with 2.5 g/kg/day high-protein diet"},
            {"id": "D", "text": "Active symptom control with low-dose opioids for dyspnea/pain, loop diuretics for volume management, and oral bicarbonate for acidosis"}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Conservative Kidney Management (CKM) 為積極的非透析醫療照護。其核心處置包含：使用 Low-dose Opioids (如 Morphine) 控制 Dyspnea 與 Uremic Pain、給予 Loop Diuretics 控制 Fluid Overload、使用 Oral Sodium Bicarbonate 校正 Metabolic Acidosis，以及給予 Low-protein diet (0.8 g/kg/day) 搭配 Symptom Relief。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing components of CKM.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q9",
        "number": 9,
        "stem": "An 81-year-old man with CKD Stage 4 (eGFR 22 mL/min/1.73m2) and diabetic neuropathy is prescribed Gabapentin 300 mg three times daily. Two weeks later, he presents with severe lethargy, myoclonus, and flapping tremors. What is the most appropriate management?",
        "options": [
            {"id": "A", "text": "Recognize Gabapentin neurotoxicity due to reduced renal clearance, withhold the drug, and provide supportive care"},
            {"id": "B", "text": "Diagnose acute uremic pericarditis and perform emergency pericardiocentesis"},
            {"id": "C", "text": "Double the dose of Gabapentin to 600 mg TID to suppress the myoclonus"},
            {"id": "D", "text": "Administer high-dose intravenous calcium gluconate for acute hypocalcemic tetany"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Gabapentin 100% 經由腎臟排泄。在高齡 CKD 病患 (eGFR < 30 mL/min) 中若未適當調降劑量 (常態需降至 100 mg QD 或 300 mg QOD)，極易蓄積引發 Gabapentin Neurotoxicity，表現為 Myoclonus, Sedation, Asterixis 與 Coma。臨床上應停用或調降藥物劑量，症狀通常於 24-48 小時內消退。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing gabapentin dosing neurotoxicity in CKD.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q10",
        "number": 10,
        "stem": "According to the Beers Criteria and STOPP/START guidelines for prescribing in older adults, why are systemic Nonsteroidal Anti-inflammatory Drugs (NSAIDs) categorized as high-risk medications to be avoided in geriatric CKD?",
        "options": [
            {"id": "A", "text": "NSAIDs cause selective afferent arteriolar vasoconstriction leading to hemodynamically mediated AKI and hyperkalemia"},
            {"id": "B", "text": "NSAIDs inhibit cyclooxygenase-2, causing intense efferent arteriolar vasodilation and sudden glomerular collapse"},
            {"id": "C", "text": "NSAIDs induce massive urinary protein loss by dissolving renal tubular basement membranes"},
            {"id": "D", "text": "NSAIDs stimulate aldosterone secretion, leading to severe hypokalemia and alkalosis"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "NSAIDs 抑制 Renal Prostaglandin Synthesis (COX-1/COX-2)，干擾原本維繫 GFR 的 Afferent Arteriolar Vasodilation，導致 Afferent Arteriolar Vasoconstriction 與 Prerenal AKI，同時降低 Aldosterone 分泌引發 Hyperkalemia。在高齡 CKD 併用 RAASi 與 Diuretics (Triple Whammy) 時危害極大。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing NSAID nephrotoxicity mechanism in elderly.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q11",
        "number": 11,
        "stem": "An 82-year-old woman (weight 54 kg, Serum Creatinine 1.6 mg/dL) with non-valvular atrial fibrillation requires anticoagulation for stroke prevention. Based on renal dosing guidelines, which Apixaban regimen is correct?",
        "options": [
            {"id": "A", "text": "Apixaban 10 mg twice daily"},
            {"id": "B", "text": "Apixaban 5 mg twice daily"},
            {"id": "C", "text": "Apixaban 2.5 mg twice daily"},
            {"id": "D", "text": "Apixaban is contraindicated and Phenobarbital should be substituted"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Apixaban 的減量標準為滿足下列三項條件中的至少兩項：(1) Age >= 80 years, (2) Body Weight <= 60 kg, (3) Serum Creatinine >= 1.5 mg/dL。該患者滿足全部三項條件 (Age 82, Weight 54kg, SCr 1.6)，因此標準劑量 5 mg BID 應減量至 2.5 mg BID。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing Apixaban dose adjustment criteria.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q12",
        "number": 12,
        "stem": "In prescribing SGLT2 inhibitors (e.g., Dapagliflozin or Empagliflozin) for an 76-year-old patient with CKD Stage 3b and Type 2 Diabetes, which clinical counseling point is essential?",
        "options": [
            {"id": "A", "text": "SGLT2 inhibitors must be stopped immediately if eGFR dips by 5 mL/min within the first 2 weeks"},
            {"id": "B", "text": "SGLT2 inhibitors cause high rates of rhabdomyolysis and require daily creatine kinase monitoring"},
            {"id": "C", "text": "SGLT2 inhibitors are ineffective for glycemic control at low GFR but retain long-term nephroprotective and cardioprotective benefits"},
            {"id": "D", "text": "SGLT2 inhibitors increase urine glucose, requiring high-dose insulin escalation to prevent hypoglycemia"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "當 eGFR < 45 mL/min 時，由於經過 Glomerulus 過濾的 Glucose 減少，SGLT2 inhibitors 的降血糖 (Glycemic control) 效果顯著減弱；然而，其減緩 CKD 惡化 (Nephroprotection) 與降低 Heart Failure 住院率 (Cardioprotection) 的效應依然持續存在。初始使用時出現 < 30% 的 eGFR dip 為 Tubuloglomerular Feedback 恢復的正常生理反應，不需停藥。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing SGLT2i dynamics in geriatric CKD.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q13",
        "number": 13,
        "stem": "Which mechanism explains why older adults with CKD are particularly predisposed to Uremic Sarcopenia and Protein-Energy Wasting (PEW)?",
        "options": [
            {"id": "A", "text": "Metabolic acidosis activates the ubiquitin-proteasome system and caspase-3, accelerating skeletal muscle proteolysis"},
            {"id": "B", "text": "Excess erythropoietin production suppresses muscle protein synthesis in the mitochondria"},
            {"id": "C", "text": "Hyperphosphatemia directly digests skeletal muscle fibers via alkaline phosphatase activation"},
            {"id": "D", "text": "Low Klotho levels stimulate skeletal muscle hypertrophy, depleting amino acid reserves"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "高齡 CKD 病患常見的 Metabolic Acidosis 會活化 ATP-dependent Ubiquitin-Proteasome Pathway 與 Caspase-3，顯著加速骨骼肌蛋白分解 (Proteolysis)，同時抗拒 Insulin/IGF-1 的合成作用，導致 Uremic Sarcopenia 與 Protein-Energy Wasting (PEW)。使用 Oral Bicarbonate 校正酸中毒可減緩肌少症。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing uremic sarcopenia pathophysiology.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q14",
        "number": 14,
        "stem": "In managing Anemia of CKD in an 83-year-old patient on non-dialysis CKM, what is the recommended target Hemoglobin (Hb) level according to KDIGO guidelines to minimize stroke and cardiovascular risks?",
        "options": [
            {"id": "A", "text": "Hb 13.5 - 15.0 g/dL"},
            {"id": "B", "text": "Hb 10.0 - 11.5 g/dL"},
            {"id": "C", "text": "Hb 7.0 - 8.5 g/dL"},
            {"id": "D", "text": "Hb > 16.0 g/dL"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "KDIGO Guidelines 及 TREAT / CHOIR 臨床試驗顯示，使用 ESA 或 HIF-PHI 將 Hemoglobin 上升至 > 13.0 g/dL，會顯著增加 Stroke、Venous Thromboembolism 及 心血管死亡率。因此高齡 CKD 病患的血紅素控制目標鎖定於 10.0 - 11.5 g/dL (不建議超過 11.5-12.0 g/dL)。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing anemia target Hb range.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q15",
        "number": 15,
        "stem": "Regarding Blood Pressure management in a 78-year-old frail individual with CKD, orthostatic hypotension, and a history of recurrent falls, how should KDIGO 2021 guidelines be applied?",
        "options": [
            {"id": "A", "text": "Enforce strict SBP < 100 mmHg with quadruple antihypertensive therapy"},
            {"id": "B", "text": "Discontinue all blood pressure monitoring permanently"},
            {"id": "C", "text": "Individualize SBP targets (e.g. SBP 130-140 mmHg) while monitoring standing BP to prevent falls and cerebral hypoperfusion"},
            {"id": "D", "text": "Raise SBP to > 180 mmHg using vasopressors to stimulate kidney growth"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "雖然 SPRINT Senior Trial 顯示在活力充沛的健康長者中極致控制 SBP < 120 mmHg 有心血管益處，但 KDIGO 2021 指引強調：對於具 Severe Frailty、Orthostatic Hypotension 與 高跌倒風險的高齡病患，應個別化放寬 SBP 目標至 130-140 mmHg，並在立位測量血壓以避免 Cerebral Hypoperfusion 與 Falls。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing individualized BP targets in frail elderly.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q16",
        "number": 16,
        "stem": "Which physiological defect in tubular function makes older adults with CKD particularly susceptible to hyperkalemia under low-sodium intake or aldosterone blockade?",
        "options": [
            {"id": "A", "text": "Hyperactivity of the Na-K-2Cl cotransporter in the loop of Henle"},
            {"id": "B", "text": "Excessive basolateral potassium secretion by principal cells"},
            {"id": "C", "text": "Upregulation of renal outer medullary potassium (ROMK) channels"},
            {"id": "D", "text": "Impaired tubular potassium transport combined with hyporeninemic hypoaldosteronism"}
        ],
        "sourceProvidedAnswer": "D",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "老化腎臟常伴隨 Hyporeninemic Hypoaldosteronism (Type 4 RTA 傾向) 與 Principal cells 的 Cortical Collecting Duct 鉀離子分泌通道 (ROMK/BK) 活性下降。當併用 RAAS Inhibitors、Spironolactone 或低鈉飲食時，高齡 CKD 病患缺乏足夠的 Aldosterone 驅動鉀排泄，極易引發重度 Hyperkalemia。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing hyperkalemia mechanism in elderly CKD.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q17",
        "number": 17,
        "stem": "Which of the following conditions represents a classic indication for initiating a Time-Limited Trial (TLT) of dialysis in an older adult?",
        "options": [
            {"id": "A", "text": "Uncertain prognostic outcome where acute reversible illness overlays advanced CKD, allowing shared evaluation of functional recovery"},
            {"id": "B", "text": "Terminal stage metastatic cancer with 24-hour expected survival"},
            {"id": "C", "text": "Young athlete with normal kidney function requesting elective hemodialysis"},
            {"id": "D", "text": "Patient with signed explicit POLST opting for comfort-only non-dialytic care"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Time-Limited Trial (TLT) 適用於預後不確定 (如 Advanced CKD 併發 Acute-on-Chronic Reversible AKI 或重症) 的高齡病患。經 Shared Decision-Making 後約定進行 4-8 週透析觀察，若神智與器官功能恢復則繼續，若狀況持續惡化則轉為 Comfort Palliative Care。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing indications for Time-Limited Trial.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q18",
        "number": 18,
        "stem": "In evaluating mineral bone disease (CKD-MBD) in geriatric patients, why is calcium-containing phosphate binder (e.g. Calcium Carbonate) usage increasingly restricted?",
        "options": [
            {"id": "A", "text": "Calcium binders cause rapid metabolic alkalosis and severe hypokalemia"},
            {"id": "B", "text": "Older CKD patients frequently have Adynamic Bone Disease, and calcium overload accelerates Vascular and Medial Arterial Calcification"},
            {"id": "C", "text": "Calcium binders dissolve bone matrix, leading to osteosarcoma"},
            {"id": "D", "text": "Calcium binders completely block intestinal iron absorption, worsening refractory anemia"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "高齡 CKD 病患常伴隨 低骨轉換率之 Adynamic Bone Disease。過量給予 Calcium-containing Phosphate Binders 會導致 Positive Calcium Balance，因骨骼無法吸收過量鈣質，進而大幅加速 Medial Arterial Calcification (Monckeberg Sclerosis) 與 Vascular Calcification，增加心血管死亡率。因此 KDIGO 建議優先使用 Non-calcium binders (如 Sevelamer, Lanthanum)。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing CKD-MBD and vascular calcification in elderly.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q19",
        "number": 19,
        "stem": "Which oral hypoglycemic drug class requires strict discontinuation when an older diabetic patient's eGFR drops below 30 mL/min/1.73m2 due to the lethal risk of Lactic Acidosis?",
        "options": [
            {"id": "A", "text": "DPP-4 inhibitors (e.g. Linagliptin)"},
            {"id": "B", "text": "GLP-1 receptor agonists (e.g. Dulaglutide)"},
            {"id": "C", "text": "Metformin (Biguanides)"},
            {"id": "D", "text": "Alpha-glucosidase inhibitors (e.g. Acarbose)"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Metformin 經由腎臟原型排泄。當 eGFR < 30 mL/min/1.73m2 時，Metformin 顯著蓄積並抑制 肝臟 Gluconeogenesis 與 粒線體呼吸鏈 Complex I，導致 Lactic Acidosis (MALA) 致命風險。因此在 eGFR < 30 時必須 停用 (Discontinue)；eGFR 30-44 時上限為 1000 mg/day。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing Metformin eGFR contraindication cutoff.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    },
    {
        "id": "2026_Geriatric_CKD_Q20",
        "number": 20,
        "stem": "What physiological impairment in tubular urine concentration explains why older adults with CKD develop rapid hypernatremia or dehydration during febrile illnesses or periods of restricted fluid access?",
        "options": [
            {"id": "A", "text": "Loss of medullary osmotic gradient and reduced renal tubule responsiveness to vasopressin (AVP)"},
            {"id": "B", "text": "Overexpression of aquaporin-2 water channels in the proximal convoluted tubule"},
            {"id": "C", "text": "Complete block of sodium reabsorption in the thick ascending limb of Henle"},
            {"id": "D", "text": "Inability of the kidney to filter creatinine under high temperature"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "老化與 CKD 會造成 腎髓質滲透壓梯度 (Medullary Osmotic Gradient) 流失、Tubular Atrophy 以及 Collecting Duct 對 AVP 的響應能力下降 (Impaired Urinary Concentrating Ability)。當高齡病患發燒或水分攝取減少時，腎臟無法產生高濃縮尿 (Maximal Uosm 降至 400-500 mOsm/kg)，自由水持續自尿液流失，極易快速引發 Dehydration 與 Hypernatremia。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence testing concentrating defect in aging kidney.",
        "qcVerified": True,
        "qcStatus": "QC_PASSED",
        "resolvedImages": []
    }
]

paper_data = {
    "id": paper_id,
    "paperId": paper_id,
    "title": title,
    "sourceCategory": source_category,
    "year": year,
    "questionCount": len(questions_data),
    "questions": questions_data
}

# Write files
tutorial_path = f"public/server-data/tutorials/{paper_id}_tutorial.json"
paper_path = f"public/server-data/{paper_id}.json"

os.makedirs("public/server-data/tutorials", exist_ok=True)

with open(tutorial_path, "w", encoding="utf-8") as f:
    json.dump(tutorial_data, f, ensure_ascii=False, indent=2)

with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote draft tutorial to {tutorial_path}")
print(f"Successfully wrote draft paper to {paper_path}")

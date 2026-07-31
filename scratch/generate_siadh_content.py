import json
import os

# Define output paths
TUTORIAL_PATH = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials/2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考)_tutorial.json"
PAPER_PATH = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json"

PAPER_ID = "2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考)"
TITLE = "2026 Syndrome of Inappropriate Antidiuretic Hormone Secretion (SIADH) 分子水通道機制、臨床診斷標準、鑑別診斷與水鹽調控處置"
CATEGORY = "2026 Electrolytes"

# 1. Construct Tutorial JSON
tutorial_data = {
    "paperId": PAPER_ID,
    "title": TITLE,
    "sourceCategory": CATEGORY,
    "year": 2026,
    "sections": [
        {
            "id": "section-1",
            "title": "Molecular Mechanisms of Vasopressin, V2 Receptor Signaling, and Aquaporin-2 Trafficking",
            "content": """### Topology Mapping Matrix: Cellular Signal Transduction of Vasopressin

Vasopressin (arginine vasopressin, AVP) 調控水份重吸收的細胞分子路徑如下拓撲對應：

| Structural Component | Molecular Subtype / Signaling Factor | Functional Role & Physiological Impact |
| :--- | :--- | :--- |
| **Basolateral Receptor** | V2 Receptor (G protein-coupled receptor) | 結合 AVP 後活化 Gs protein，進而刺激 Adenylyl Cyclase (AC) 生成 intracellular cAMP |
| **Effector Kinase** | Protein Kinase A (PKA) | 被 cAMP 活化，進而直接磷酸化 (phosphorylation) 胞漿內 Aquaporin-2 (AQP2) vesicles |
| **Apical Transporter** | Aquaporin-2 (AQP2) | 經 SNARE proteins 媒介向 Principal Cells 的 apical plasma membrane 進行 exocytosis 膜融合 |
| **Basolateral Channels** | Aquaporin-3 (AQP3) & Aquaporin-4 (AQP4) | 常態性表現於 basolateral membrane，將水分子由細胞內轉運入 medullary interstitium |

---

### Pathophysiological Decision Tree: Four Osmoregulatory Secretion Types in SIADH

在健康生理狀態下，Plasma Osmolality < 280 mOsm/kg 時 AVP 分泌會被完全抑制。然而在 SIADH 病患中，AVP 非適當分泌呈現四種主要的病理生理分型：

```
[ SIADH Osmoregulatory Secretion Patterns ]
  │
  ├── Type A (Erratic / Unregulated Release) ➔ AVP 分泌與 Plasma Osmolality 完全解離，呈現隨機大量釋放 (佔約 37%)
  │
  ├── Type B (Reset Osmostat) ➔ Osmotic Threshold 向下重置，低滲透壓下仍維持常態性但穩定的 AVP 分泌 (佔約 33%)
  │
  ├── Type C (Constant Basal Leak) ➔ 垂體後葉存在持續性的 AVP Basal Leak，高滲透壓時對 Osmolality 上升仍有反應 (佔約 16%)
  │
  └── Type D (Normal Secretion / AQP2 Gain-of-Function) ➔ Plasma AVP 濃度正常，但 AQP2 恆定轉移至膜上或 V2 Receptor 發生過度活化 (佔約 14%)
```

---

### High-Yield Differential Comparison: Euvolemic Water Dynamics vs Intravascular Volume

| Physiological Parameter | Normal Water Excess (e.g. Primary Polydipsia) | SIADH (Inappropriate AVP Secretion) |
| :--- | :--- | :--- |
| **Plasma Osmolality** | < 275 mOsm/kg (Hypo-osmolar) | < 275 mOsm/kg (Hypo-osmolar) |
| **Plasma AVP Level** | Suppressed (Undetectable, < 0.5 pg/mL) | Inappropriately Elevated or Non-suppressed |
| **Urine Osmolality** | < 100 mOsm/kg (Maximally Dilute Urine) | > 100 mOsm/kg (Inappropriately Concentrated) |
| **Free Water Clearance** | Positive (Maximal free water excretion) | Negative (Net free water retention) |

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 1: 誤以為 SIADH 病患有明顯體液過多 (Hypervolemia) 或水腫 (Edema)**  
> SIADH 雖然導致水分滯留 (water retention)，但增加的體液 2/3 分佈於 intracellular fluid (ICF)，僅 1/3 存留於 extracellular fluid (ECF)。體液擴張會進一步抑制 Renin-Angiotensin-Aldosterone System (RAAS) 並刺激 Atrial Natriuretic Peptide (ANP) 分泌，引發 Natriuresis (Aldosterone Escape)，使 ECF Volume 恢復至正常範圍 (Euvolemia)。因此 SIADH 病患**絕對不會出現 Peripheral Edema 或 Ascites**！

> [!TIP]
> **Key Pearl: AQP2 Phosphorylation Sites**  
> PKA 主要磷酸化 AQP2 的 Serine 256 (Ser256) 位置，此步驟為 AQP2 vesicles 由 intracellular storage endosomes 移動並融合至 apical membrane 的絕對必要條件。""",
            "diagrams": [
                {
                    "id": "diagram-1-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/10. Urine Concentration and Dilution/Fig_10_9.png",
                    "imagePath": "/reference-images/Brenner 11e/10. Urine Concentration and Dilution/Fig_10_9.png",
                    "caption": "Brenner 11e Fig 10.9: Key events contributing to the regulation of Aquaporin-2 trafficking in renal collecting duct principal cells.",
                    "sourceBook": "Brenner 11e Ch 10"
                },
                {
                    "id": "diagram-1-2",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_18.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_18.png",
                    "caption": "Brenner 11e Fig 15.18: Plasma Vasopressin as a function of plasma osmolality in patients with SIADH showing four distinct osmoregulatory defects (Type A-D).",
                    "sourceBook": "Brenner 11e Ch 15"
                },
                {
                    "id": "diagram-1-3",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/siadh_v2r_aquaporin.jpg",
                    "imagePath": "/server-data/assets/siadh_v2r_aquaporin.jpg",
                    "caption": "Gemini Mechanism Diagram: Vasopressin V2 Receptor Activation, cAMP Signal Cascade, and Aquaporin-2 Apical Insertion.",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        },
        {
            "id": "section-2",
            "title": "Essential Diagnostic Criteria, Biomarkers, and Laboratory Evaluation",
            "content": """### Topology Mapping Matrix: Diagnostic Criteria Architecture

確定 SIADH 診斷必須嚴格滿足下列 Essential Diagnostic Criteria 與 Supplemental Diagnostic Biomarkers：

| Criteria Category | Clinical & Laboratory Parameter | Threshold Value & Interpretation |
| :--- | :--- | :--- |
| **Essential Criterion 1** | Effective Serum Osmolality | < 275 mOsm/kg H2O (Hypotonic Hyponatremia) |
| **Essential Criterion 2** | Urine Osmolality | > 100 mOsm/kg H2O (Impaired renal water dilution) |
| **Essential Criterion 3** | Clinical Volume Status | Clinical Euvolemia (No signs of ECF depletion or volume overload) |
| **Essential Criterion 4** | Urine Sodium Concentration | > 30 mEq/L (Under normal dietary sodium and water intake) |
| **Essential Criterion 5** | Endocrine & Renal Function | Normal Adrenal (Cortisol) & Thyroid (TSH) function; No diuretic use |
| **Supplemental Biomarker** | Serum Uric Acid | < 4.0 mg/dL (Hypouricemia due to increased urate clearance) |
| **Supplemental Biomarker** | Fractional Excretion of Urate (FE Urate) | > 10% (Inappropriately high urate excretion) |
| **Supplemental Biomarker** | Fractional Excretion of Sodium / Urea | FE Na > 1%, FE Urea > 55% |

---

### Pathophysiological Decision Tree: Stepwise Laboratory Workup for Hyponatremia

```
[ Stepwise Diagnostic Workup for Hypotonic Hyponatremia ]
  │
  ├── Step 1: Rule out Pseudohyponatremia & Hypertonic Hyponatremia ➔ Check Serum Osmolality (< 275 mOsm/kg)
  │
  ├── Step 2: Confirm Impaired Water Dilution ➔ Check Urine Osmolality (> 100 mOsm/kg)
  │
  ├── Step 3: Assess Clinical Volume Status ➔ Distinguish Hypovolemic vs Euvolemic vs Hypervolemic
  │
  ├── Step 4: Evaluate Urine Sodium (UNa) in Euvolemia
  │     ├── UNa < 30 mEq/L ➔ Primary Polydipsia, Low Solute Intake (Tea and Toast / Beer Potomania)
  │     └── UNa > 30 mEq/L ➔ Proceed to Step 5
  │
  └── Step 5: Exclude Endocrine Mimics
        ├── Exclude Glucocorticoid Deficiency (Check Morning Serum Cortisol / Cosyntropin Test)
        ├── Exclude Hypothyroidism (Check Serum TSH)
        └── Confirm SIADH Diagnosis
```

---

### High-Yield Differential Comparison: Diagnostic Biomarkers across Euvolemic States

| Diagnostic Parameter | SIADH | Primary Polydipsia | Glucocorticoid Deficiency |
| :--- | :--- | :--- | :--- |
| **Serum Na+** | Low (< 135 mEq/L) | Low (< 135 mEq/L) | Low (< 135 mEq/L) |
| **Urine Osmolality** | > 100 mOsm/kg (usually > 300) | < 100 mOsm/kg (dilute) | > 100 mOsm/kg |
| **Serum Uric Acid** | Low (< 4.0 mg/dL) | Normal / Mildly Low | Normal / Elevated |
| **Serum Cortisol Response** | Normal | Normal | Subnormal / Impaired |
| **Response to Fluid Restriction** | Serum Na+ Increases | Serum Na+ Increases | Partial / Poor (Requires Cortisol) |

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 2: 常規檢驗 Plasma AVP Level 來診斷 SIADH**  
> 臨床上**不需要也不建議常規抽取 Plasma AVP 濃度**來診斷 SIADH！因為 AVP 在血清中半衰期極短 (10-20 分鐘)，易於外周降解，且數值常隨採血壓力波動。SIADH 是純粹的臨床與實驗室功能性診斷 (Functional Diagnostic Criteria)。

> [!TIP]
> **Key Pearl: Hypouricemia & FE Urate in SIADH**  
> 體液輕微擴張引發的 Proximal Tubule 重吸收抑制，會導致 Serum Uric Acid 下降 (< 4 mg/dL) 與 FE Urate 上升 (> 10%)。當使用 Fluid Restriction 校正 Hyponatremia 後，Hypouricemia 也會隨之復原。""",
            "diagrams": [
                {
                    "id": "diagram-2-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_17.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_17.png",
                    "caption": "Brenner 11e Fig 15.17: Diagnostic approach and algorithm for the evaluation of the hyponatremic patient.",
                    "sourceBook": "Brenner 11e Ch 15"
                },
                {
                    "id": "diagram-2-2",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Table_15_4.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Table_15_4.png",
                    "caption": "Brenner 11e Table 15.4: Classification of Hyponatremia According to Severity of Presenting Symptoms.",
                    "sourceBook": "Brenner 11e Ch 15"
                },
                {
                    "id": "diagram-2-3",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/siadh_diagnostic_criteria.jpg",
                    "imagePath": "/server-data/assets/siadh_diagnostic_criteria.jpg",
                    "caption": "Gemini Clinical Infographic: Euvolemic Hyponatremia & SIADH Diagnostic Criteria Card.",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        },
        {
            "id": "section-3",
            "title": "Etiologies, Drug-Induced SIADH, and High-Yield Differential Diagnosis",
            "content": """### Topology Mapping Matrix: Etiology & Etiological Spectrum of SIADH

SIADH 的四大核心病因分類及其高頻致病機制如下：

| Etiology Category | Specific Pathologies & Trigger Agents | Pathophysiological Mechanism |
| :--- | :--- | :--- |
| **Malignancies** | Small Cell Lung Cancer (SCLC), Head & Neck Squamous Cell Carcinoma, Lymphoma | Paraneoplastic ectopic expression and unregulated synthesis/release of AVP |
| **CNS Disorders** | Stroke, Subarachnoid Hemorrhage, Head Trauma, Meningitis, Encephalitis, Brain Abscess | Disruption of central osmoregulatory pathways and direct pituitary stalk irritation |
| **Pulmonary Diseases** | Pneumonia, Tuberculosis, Lung Abscess, Acute Respiratory Distress Syndrome (ARDS) | Local hypoxia/hypercapnia and altered thoracic hemodynamics triggering baroreceptor AVP release |
| **Drug-Induced Agents** | SSRIs (Sertraline, Fluoxetine), Carbamazepine, Cyclophosphamide, Chlorpropamide, NSAIDs | Central stimulation of AVP release or peripheral potentiation of AVP action at V2 Receptor |

---

### High-Yield Differential Comparison: SIADH vs Cerebral Salt Wasting (CSW)

在 CNS 疾病或 Subarachnoid Hemorrhage 病患中，SIADH 與 CSW 的鑑別診斷為試題核心精髓：

| Clinical & Diagnostic Parameter | SIADH | Cerebral Salt Wasting (CSW) |
| :--- | :--- | :--- |
| **Clinical Volume Status** | Clinical Euvolemia (Normal to slight ECF expansion) | True Hypovolemia (Dehydration, ECF contraction) |
| **Body Weight** | Maintained or Slight Increase | Markedly Decreased (Weight loss) |
| **Central Venous Pressure (CVP)** | Normal or Slightly High (6-10 cmH2O) | Low (< 4 cmH2O) |
| **Hematocrit & Serum Albumin** | Normal or Hemodiluted | Elevated (Hemoconcentration) |
| **Serum Urea Nitrogen / Creatinine** | Normal or Low (BUN < 10 mg/dL) | Elevated (Prerenal Azotemia, BUN/Cr > 20) |
| **Urine Volume** | Normal to Oliguric | Markedly Polyuric (Renal sodium wasting) |
| **Primary Treatment Strategy** | **Fluid Restriction** | **Isotonic Saline (0.9% NaCl) & Vol. Repletion** |

---

### Pathophysiological Decision Tree: Differential Diagnosis of Euvolemic Hyponatremia

```
[ Euvolemic Hyponatremia ]
  │
  ├── Check Serum Uric Acid & Urine Osmolality
  │     ├── Serum Uric Acid Low (< 4 mg/dL) + Urine Osmolality > 100 mOsm/kg ➔ SIADH
  │     ├── Serum Uric Acid Normal/High + Urine Osmolality > 100 mOsm/kg ➔ Glucocorticoid Deficiency
  │     └── Urine Osmolality < 100 mOsm/kg ➔ Primary Polydipsia / Low Solute Intake
  │
  └── Special Conditions
        ├── Reset Osmostat ➔ Responds normally to Water Load Test (Excretes > 80% load within 4 hours)
        └── Thiazide Diuretic Hyponatremia ➔ Impaired diluting ability at Cortical Diluting Segment (DCT)
```

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 3: 將 CSW 病患進行 Fluid Restriction**  
> 若將 CSW (Hypovolemic) 錯判為 SIADH 並給予 Fluid Restriction，會導致嚴重的腦缺血 (Cerebral Ischemia)、Vasospasm 與 Hypovolemic Shock！在 CNS 傷害病患中若出現低血壓、皮膚彈性差與 CVP 偏低，必須優先診斷 CSW 並給予 0.9% Normal Saline！

> [!TIP]
> **Key Pearl: Drugs causing SIADH**  
> Cyclophosphamide (特別是大劑量 IV 治療時併發水中毒) 與 Carbamazepine 是專科甄試最常考的致病藥物！""",
            "diagrams": [
                {
                    "id": "diagram-3-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Table_15_1.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Table_15_1.png",
                    "caption": "Brenner 11e Table 15.1: Drugs and Hormones That Affect Vasopressin Secretion and Action.",
                    "sourceBook": "Brenner 11e Ch 15"
                },
                {
                    "id": "diagram-3-2",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Table_15_3.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Table_15_3.png",
                    "caption": "Brenner 11e Table 15.3: Clinical Disorders Associated With SIADH (Malignancies, Pulmonary, CNS).",
                    "sourceBook": "Brenner 11e Ch 15"
                },
                {
                    "id": "diagram-3-3",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/siadh_vs_csw.jpg",
                    "imagePath": "/server-data/assets/siadh_vs_csw.jpg",
                    "caption": "Gemini Clinical Comparison: SIADH (Euvolemic) vs Cerebral Salt Wasting CSW (Hypovolemic).",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        },
        {
            "id": "section-4",
            "title": "Therapeutic Strategies, Electrolyte Kinetics, and Prevention of Osmotic Demyelination Syndrome",
            "content": """### Topology Mapping Matrix: Stepwise Therapeutic Modalities for SIADH

SIADH 的治療策略需依據症狀嚴重度 (Symptom Severity) 與血清鈉離子濃度階梯式介入：

| Intervention Tier | Modality / Pharmacological Agent | Target Population & Action Mechanism |
| :--- | :--- | :--- |
| **Tier 1 (First-Line)** | Fluid Restriction (500–1000 mL/day) | 無症狀或輕度 Hyponatremia (Na 125–135 mEq/L) 之首選處置 |
| **Tier 2 (Symptomatic)** | 3% Hypertonic Saline (IV Bolus 100–150 mL) | 具嚴重神經症狀 (Seizures, Coma, Obtundation) 之急診救命處置 |
| **Tier 3 (Pharmacological)** | Oral Vasopressin Receptor Antagonists (Tolvaptan) | 選擇性阻斷 V2 Receptor，引發 Aquaresis (Free water excretion without electrolyte loss) |
| **Tier 4 (Alternative)** | Demeclocycline (600–1200 mg/day) | 抑制 AC 產生 cAMP，引發 Nephrogenic Diabetes Insipidus (NDI) |
| **Tier 5 (Solute Loading)** | Oral Urea (0.25–0.5 g/kg/day) or Salt Tabs + Furosemide | 增加 Urinary Solute Excretion 並阻斷 Medullary Gradient 重吸收 |

---

### High-Yield Differential Comparison: Correction Speed Limits & Osmotic Demyelination Syndrome (ODS)

| Parameter / Limit Rule | Standard Risk Patient | High-Risk Patient (Advanced Cirrhosis, Alcoholism, Malnutrition) |
| :--- | :--- | :--- |
| **24-Hour Correction Target Limit** | **<= 8 mEq/L in 24 hours** | **<= 6 mEq/L in 24 hours** |
| **48-Hour Correction Target Limit** | **<= 18 mEq/L in 48 hours** | **<= 14 mEq/L in 48 hours** |
| **Acute Acute Symptom Goal** | Rapid rise of 4–6 mEq/L within initial 1–2 hours | Rapid rise of 4–6 mEq/L within initial 1–2 hours |
| **Complication of Overcorrection** | Central Pontine Myelinolysis / ODS | Central Pontine Myelinolysis / ODS |
| **Rescue Management for Overcorrection** | D5W IV infusion + Desmopressin (DDAVP) re-lowering | D5W IV infusion + Desmopressin (DDAVP) re-lowering |

---

### Pathophysiological Decision Tree: Electrolyte-Free Water Clearance & Saline Paradox in SIADH

給予 Isotonic Normal Saline (0.9% NaCl, 154 mEq/L Na, Osmolality ~ 308 mOsm/kg) 為什麼會加重 SIADH 的 Hyponatremia？

```
[ Infusion of 1 L 0.9% Normal Saline (308 mOsm) into SIADH Patient with Urine Osmolality 616 mOsm/kg ]
  │
  ├── 1 L Normal Saline 包含 308 mOsm Solutes
  │
  ├── 由於固定的高 Urine Osmolality (616 mOsm/kg)，腎臟僅需 0.5 L 尿液即可將此 308 mOsm 溶質完全排出
  │     └── Urine Volume Excreted = 308 mOsm / 616 mOsm/kg = 0.5 L
  │
  └── 剩餘的 0.5 L Free Water 被完整存留於體內 (Net Free Water Retention)
        └── 結果：Serum Sodium 濃度反而進一步下降 (Worsening Hyponatremia)!
```

---

### Conceptual Trap Analysis & High-Yield Pearls

> [!WARNING]
> **Conceptual Trap 4: 給予 SIADH 病患 0.9% Normal Saline 來矯正低血鈉**  
> 若病患的 Urine Osmolality 高於 308 mOsm/kg (常高達 500-800 mOsm/kg)，給予 Isotonic Saline (0.9% NaCl) 會因為「腎臟高效率排出鹽分但存留自由水」而**導致 Serum Sodium 迅速惡化**！

> [!TIP]
> **Key Pearl: Rescue Strategy for Overcorrection**  
> 若 Serum Na 在 24 小時內上升超過 8-10 mEq/L，應立即給予 IV D5W (5% Dextrose) 並合併 IV DDAVP (Desmopressin 1-2 mcg)，主動將 Serum Na 重新調降至安全範圍內，以挽救星形膠質細胞 (Astrocytes) 避免 ODS！""",
            "diagrams": [
                {
                    "id": "diagram-4-1",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_20.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_20.png",
                    "caption": "Brenner 11e Fig 15.20: Recommended goals and safety limits for correction of hyponatremia to avoid Osmotic Demyelination Syndrome.",
                    "sourceBook": "Brenner 11e Ch 15"
                },
                {
                    "id": "diagram-4-2",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_21.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_21.png",
                    "caption": "Brenner 11e Fig 15.21: Algorithm for the treatment of euvolemic hyponatremia based on presenting symptom severity.",
                    "sourceBook": "Brenner 11e Ch 15"
                },
                {
                    "id": "diagram-4-3",
                    "type": "micrograph",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_19.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_19.png",
                    "caption": "Brenner 11e Fig 15.19: Brain electrolyte and organic osmolyte adaptation during hyponatremia and osmotic demyelination pathophysiology after rapid correction.",
                    "sourceBook": "Brenner 11e Ch 15"
                },
                {
                    "id": "diagram-4-4",
                    "type": "ai_illustration",
                    "relPath": "/server-data/assets/siadh_ods_saline.jpg",
                    "imagePath": "/server-data/assets/siadh_ods_saline.jpg",
                    "caption": "Gemini Therapeutic Infographic: Hyponatremia Correction Safety Limits (<= 8 mEq/L/24h), ODS Pathophysiology, and Normal Saline Paradox.",
                    "sourceBook": "Gemini AI Masterclass"
                }
            ]
        }
    ]
}

# 2. Construct Exam Paper JSON (20 High-Yield MCQs)
raw_questions = [
    {
        "id": "2026_SIADH_Q1",
        "number": 1,
        "stem": "Which of the following cellular signaling events occurs immediately downstream of Arginine Vasopressin (AVP) binding to the V2 receptor on the basolateral membrane of renal collecting duct principal cells?",
        "options": [
            {"id": "A", "text": "Activation of Gs protein and stimulation of adenylyl cyclase to increase intracellular cyclic AMP (cAMP) levels"},
            {"id": "B", "text": "Activation of Gi protein leading to inhibition of protein kinase A and intracellular calcium influx"},
            {"id": "C", "text": "Direct phosphorylation of Aquaporin-1 channels by protein kinase C causing endocytosis"},
            {"id": "D", "text": "Inhibition of apical epithelial sodium channels (ENaC) through cGMP-dependent protein kinase"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Vasopressin (AVP) 結合至 Basolateral V2 Receptor 後，會經由 Gs protein 活化 Adenylyl Cyclase (AC)，造成 Intracellular cAMP 濃度上升。高濃度的 cAMP 進一步活化 Protein Kinase A (PKA)，磷酸化 Aquaporin-2 (AQP2) 的 Serine 256 位置，促使含有 AQP2 的 Vesicles 移動並與 Apical Membrane 融合，顯著增加 Collecting Duct 對水的 Permeability。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing fundamental V2 Receptor signal transduction and AQP2 trafficking.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/10. Urine Concentration and Dilution/Fig_10_9.png",
                "caption": "Brenner 11e Fig 10.9: Aquaporin-2 trafficking in renal collecting duct principal cells.",
                "sourceBook": "Brenner 11e Ch 10"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q2",
        "number": 2,
        "stem": "A 65-year-old male with a history of Small Cell Lung Cancer presents with mild confusion. Laboratory testing reveals serum sodium of 118 mEq/L, serum osmolality of 245 mOsm/kg H2O, urine osmolality of 480 mOsm/kg H2O, and urine sodium of 55 mEq/L. Physical examination shows no peripheral edema, normal jugular venous pressure, and normal skin turgor. Which of the following is an essential diagnostic criterion for Syndrome of Inappropriate Antidiuretic Hormone Secretion (SIADH)?",
        "options": [
            {"id": "A", "text": "Elevated serum vasopressin (AVP) concentration above 20 pg/mL"},
            {"id": "B", "text": "Effective serum osmolality < 275 mOsm/kg H2O with clinical euvolemia and urine osmolality > 100 mOsm/kg H2O"},
            {"id": "C", "text": "Fractional excretion of sodium (FE Na) < 0.5% with urine sodium < 20 mEq/L"},
            {"id": "D", "text": "Presence of peripheral pitting edema with elevated central venous pressure"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "SIADH 的 Essential Diagnostic Criteria 包含：(1) Effective Serum Osmolality < 275 mOsm/kg H2O；(2) Inappropriate Urinary Concentration (Urine Osmolality > 100 mOsm/kg H2O)；(3) Clinical Euvolemia；(4) Urine Sodium Concentration > 30 mEq/L (在正常水鹽攝取下)；(5) 排除 Adrenal Insufficiency、Hypothyroidism 與 Diuretic Use。Serum AVP 檢測非臨床必備條件，且 SIADH 病患無 Peripheral Edema。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing core diagnostic criteria of SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_17.png",
                "caption": "Brenner 11e Fig 15.17: Diagnostic approach to the hyponatremic patient.",
                "sourceBook": "Brenner 11e Ch 15"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q3",
        "number": 3,
        "stem": "Which of the following serum biochemical findings is characteristically observed in patients with SIADH due to subclinical extracellular fluid volume expansion and reduced proximal tubular reabsorption?",
        "options": [
            {"id": "A", "text": "Hyperuricemia with serum uric acid > 8.0 mg/dL"},
            {"id": "B", "text": "Elevated Blood Urea Nitrogen (BUN) with BUN/Creatinine ratio > 20"},
            {"id": "C", "text": "Hypouricemia with serum uric acid < 4.0 mg/dL and Fractional Excretion of Urate > 10%"},
            {"id": "D", "text": "Severe Hyperkalemia with metabolic acidosis"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "SIADH 導致的水份滯留會引起 Subclinical ECF Volume Expansion，進一步抑制 Proximal Tubule 對 Solutes 的重吸收，導致 Urate Clearance 增加，典型表現為 Hypouricemia (Serum Uric Acid < 4.0 mg/dL) 以及 Fractional Excretion of Urate (FE Urate) > 10%。當利用 Fluid Restriction 糾正低血鈉後，Hypouricemia 亦會消失。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing serum uric acid and FE urate dynamics in SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q4",
        "number": 4,
        "stem": "A 58-year-old male with aneurysmal Subarachnoid Hemorrhage develops hyponatremia with serum sodium of 122 mEq/L. Clinicians are deciding between SIADH and Cerebral Salt Wasting (CSW). Which of the following clinical features most strongly supports a diagnosis of Cerebral Salt Wasting (CSW) over SIADH?",
        "options": [
            {"id": "A", "text": "Clinical Euvolemia with normal skin turgor and normal central venous pressure"},
            {"id": "B", "text": "Normal Blood Urea Nitrogen level of 8 mg/dL and serum uric acid of 3.2 mg/dL"},
            {"id": "C", "text": "True Hypovolemia with weight loss, low central venous pressure (< 4 cmH2O), and orthostatic hypotension"},
            {"id": "D", "text": "Prompt rise in serum sodium following strict fluid restriction to 500 mL/day"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Cerebral Salt Wasting (CSW) 與 SIADH 最關鍵的鑑別點在於 Volume Status。CSW 是因為 CNS 傷害引發 Sympathetic Output 下降或 Natriuretic Peptides 釋放，導致 Renal Sodium Loss 與 True Hypovolemia (表現為 Weight Loss, Low CVP < 4 cmH2O, Hypotension, Prerenal Azotemia)。治療上 CSW 必須給予 0.9% Normal Saline 補足體液，若實施 Fluid Restriction 會加重腦缺血！",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing differential diagnosis between SIADH and Cerebral Salt Wasting.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/siadh_vs_csw.jpg",
                "caption": "Gemini Clinical Diagram: SIADH vs CSW Diagnostic Features.",
                "sourceBook": "Gemini AI Masterclass"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q5",
        "number": 5,
        "stem": "An inpatient with SIADH (serum sodium 124 mEq/L, urine osmolality 600 mOsm/kg H2O) is inadvertently administered 1000 mL of 0.9% Normal Saline (154 mEq/L NaCl, total osmolality 308 mOsm/kg H2O) over 8 hours. What is the expected physiological effect on the patient's serum sodium level?",
        "options": [
            {"id": "A", "text": "Serum sodium will increase by approximately 5 mEq/L due to sodium repletion"},
            {"id": "B", "text": "Serum sodium will remain completely unchanged because isotonic saline is iso-osmotic"},
            {"id": "C", "text": "Serum sodium will decrease further (worsening hyponatremia) because the kidney excretes the 308 mOsm solute in 0.5 L urine while retaining 0.5 L free water"},
            {"id": "D", "text": "Serum sodium will rapidly overcorrect by > 12 mEq/L causing osmotic demyelination"}
        ],
        "sourceProvidedAnswer": "C",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "給予 SIADH 病患 0.9% Normal Saline (308 mOsm/L) 時，由於病患的 Urine Osmolality 被固定在高水平 (如 600 mOsm/kg)，腎臟僅需要 0.5 L 的尿液即可將 1 L Normal Saline 中的 308 mOsm 溶質完全排出 (308 / 600 = 0.51 L)。輸入的 1 L 水份扣除排出的 0.5 L 尿液，剩下的 0.5 L Free Water 會留在體內，導致 Serum Sodium 進一步被稀釋而惡化低血鈉！",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing the Normal Saline Paradox in SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/server-data/assets/siadh_ods_saline.jpg",
                "caption": "Gemini Infographic: Why 0.9% Normal Saline Worsens SIADH Hyponatremia.",
                "sourceBook": "Gemini AI Masterclass"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q6",
        "number": 6,
        "stem": "Which of the following medications is a well-recognized pharmacological cause of SIADH through central stimulation of vasopressin release or enhancement of renal AVP sensitivity?",
        "options": [
            {"id": "A", "text": "Lithium carbonate"},
            {"id": "B", "text": "Carbamazepine"},
            {"id": "C", "text": "Empagliflozin"},
            {"id": "D", "text": "Spironolactone"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Carbamazepine、Selective Serotonin Reuptake Inhibitors (SSRIs, 如 Sertraline, Fluoxetine)、Cyclophosphamide 以及 Chlorpropamide 為引發 SIADH 的高頻致病藥物。Carbamazepine 可促進 Hypothalamus 釋放 AVP 並增加 V2 Receptor 的敏感度。相反地，Lithium 會引發 Nephrogenic Diabetes Insipidus (NDI)。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing drug-induced SIADH etiologies.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Table_15_1.png",
                "caption": "Brenner 11e Table 15.1: Drugs affecting vasopressin secretion.",
                "sourceBook": "Brenner 11e Ch 15"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q7",
        "number": 7,
        "stem": "A 72-year-old female presents with severe hyponatremia (serum sodium 108 mEq/L) accompanied by generalized tonic-clonic seizures and obtundation. What is the immediate first-line management recommended to acutely increase serum sodium and control neurological symptoms?",
        "options": [
            {"id": "A", "text": "Fluid restriction to 800 mL/day combined with oral Tolvaptan 15 mg daily"},
            {"id": "B", "text": "Hypertonic Saline (3% NaCl) IV bolus of 100 to 150 mL over 10-20 minutes, repeatable up to 2 times if symptoms persist"},
            {"id": "C", "text": "Intravenous infusion of 0.9% Normal Saline at 200 mL/hr with IV Furosemide 40 mg"},
            {"id": "D", "text": "Oral Demeclocycline 600 mg twice daily with liberal oral fluid intake"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "當低血鈉併發 Severe Severe Neurological Symptoms (如 Seizures, Coma, Obtundation) 時，急診首選救命處置為立即給予 3% Hypertonic Saline IV Bolus (100–150 mL)，目標為在頭 1-2 小時內將 Serum Sodium 快速調升 4–6 mEq/L 以迅速降低 Brain Edema 與 Intracranial Pressure。Fluid Restriction 與 Vaptans 作用太慢，不適用於急性嚴重症狀處置。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing emergency treatment of severe symptomatic hyponatremia.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_21.png",
                "caption": "Brenner 11e Fig 15.21: Algorithm for treatment of euvolemic hyponatremia.",
                "sourceBook": "Brenner 11e Ch 15"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q8",
        "number": 8,
        "stem": "To prevent the development of Osmotic Demyelination Syndrome (ODS, also known as Central Pontine Myelinolysis) during the correction of chronic hyponatremia, what is the maximum recommended limit for serum sodium increase within the first 24 hours in a standard-risk patient?",
        "options": [
            {"id": "A", "text": "Not to exceed 4 mEq/L in 24 hours"},
            {"id": "B", "text": "Not to exceed 8 mEq/L in 24 hours"},
            {"id": "C", "text": "Not to exceed 14 mEq/L in 24 hours"},
            {"id": "D", "text": "Not to exceed 20 mEq/L in 24 hours"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "為了避免發生 Osmotic Demyelination Syndrome (ODS)，針對標準風險病患，低血鈉校正速率上限為 **<= 8 mEq/L in 24 hours** (且前 48 小時內不得超過 18 mEq/L)。若是高風險病患 (如 Advanced Cirrhosis, Severe Alcoholism, Malnutrition, Severe Hypokalemia)，校正上限需更加嚴格限制於 **<= 6 mEq/L in 24 hours**。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing safety limits for hyponatremia correction.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_20.png",
                "caption": "Brenner 11e Fig 15.20: Recommended goals and limits for correction of hyponatremia.",
                "sourceBook": "Brenner 11e Ch 15"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q9",
        "number": 9,
        "stem": "During the correction of chronic hyponatremia in a patient with SIADH, the serum sodium increases rapidly from 112 mEq/L to 126 mEq/L within 10 hours (an overcorrection of 14 mEq/L). Which of the following rescue management steps is most appropriate to re-lower the serum sodium and prevent brain demyelination?",
        "options": [
            {"id": "A", "text": "Administer IV 3% Hypertonic Saline bolus to stabilize serum sodium at 126 mEq/L"},
            {"id": "B", "text": "Infuse D5W (5% Dextrose in Water) IV combined with IV Desmopressin (DDAVP) to actively re-lower serum sodium back into the safe correction limit"},
            {"id": "C", "text": "Initiate oral Tolvaptan 30 mg to promote aquaresis"},
            {"id": "D", "text": "Administer IV Mannitol to induce osmotic diuresis"}
        ],
        "sourceProvidedAnswer": "B",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "當低血鈉校正過快 (Overcorrection, 24 小時內 > 8-10 mEq/L) 時，為了挽救 Astrocytes 避免發生 Osmotic Demyelination Syndrome (ODS)，最佳救救措施 (Rescue Strategy) 為立即給予 IV D5W (5% Dextrose) 補充 Free Water，並合併 IV DDAVP (Desmopressin 1-2 mcg q6-8h) 以封鎖腎臟 Free Water Excretion，主動將 Serum Sodium 調降回安全範圍內 (<= 8 mEq/L 增加幅度)。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing overcorrection rescue strategy with D5W and DDAVP.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_19.png",
                "caption": "Brenner 11e Fig 15.19: Adaptation to hyponatremia and osmotic demyelination after rapid correction.",
                "sourceBook": "Brenner 11e Ch 15"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q10",
        "number": 10,
        "stem": "What is the pharmacological mechanism of action of Tolvaptan in the treatment of SIADH-induced hyponatremia?",
        "options": [
            {"id": "A", "text": "Competitive antagonist at the renal V2 receptor, blocking AVP action and inducing solute-free water excretion (aquaresis)"},
            {"id": "B", "text": "Direct agonist at the V1a receptor causing splanchnic vasoconstriction and reduced AVP release"},
            {"id": "C", "text": "Inhibitor of the Na-K-2Cl cotransporter in the thick ascending limb of Henle's loop"},
            {"id": "D", "text": "Inhibitor of carbonic anhydrase in the proximal convoluted tubule"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Tolvaptan 是一種口服選擇性 Vasopressin V2 Receptor Antagonist (Vaptan)。它能在 Renal Collecting Duct 的 Basolateral Membrane 競爭性阻斷 AVP 與 V2R 結合，抑制 cAMP-PKA 訊息傳遞並減少 AQP2 插入 Apical Membrane，從而引發純粹的自由水排出 (Aquaresis)，上升血清鈉離子濃度且不影響電解質 Total Body Stores。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing mechanism of action of Tolvaptan.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q11",
        "number": 11,
        "stem": "Which of the following conditions is an essential requirement that must be ruled out before establishing a definitive functional diagnosis of SIADH?",
        "options": [
            {"id": "A", "text": "Primary Adrenal Insufficiency (Glucocorticoid Deficiency) and Severe Hypothyroidism"},
            {"id": "B", "text": "Asymptomatic Cholelithiasis"},
            {"id": "C", "text": "Mild Primary Hyperparathyroidism"},
            {"id": "D", "text": "Essential Hypertension under ACE inhibitor therapy"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Glucocorticoid Deficiency (如 Primary or Secondary Adrenal Insufficiency) 以及 Severe Hypothyroidism 會呈現與 SIADH 極度相似的 Euvolemic Hyponatremia (因 Cortisol 缺乏會失去對 AVP 的長效負回饋抑制)。因此在確立 SIADH 診斷之前，必須硬性排除 Adrenal Insufficiency (如驗 Cortisol / ACTH) 與 Hypothyroidism (如驗 TSH)。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing exclusion criteria for SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q12",
        "number": 12,
        "stem": "A 45-year-old female presents with chronic baseline serum sodium of 128 mEq/L. Further evaluation demonstrates normal adrenal/thyroid function and urine osmolality of 350 mOsm/kg H2O. When administered an acute oral water load test (20 mL/kg water over 30 minutes), she successfully excretes > 80% of the ingested water load within 4 hours, lowering her urine osmolality to < 100 mOsm/kg. Which variant of osmoregulatory defect is demonstrated in this patient?",
        "options": [
            {"id": "A", "text": "Reset Osmostat (Type B SIADH)"},
            {"id": "B", "text": "Type A Unregulated Vasopressin Release"},
            {"id": "C", "text": "Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)"},
            {"id": "D", "text": "Cerebral Salt Wasting (CSW)"},
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Reset Osmostat (Type B SIADH) 的特徵為滲透壓調控門檻 (Osmotic Threshold) 向下重置。病患維持在較低的基準血清鈉濃度 (如 125-130 mEq/L)，但當給予大量水份負荷 (Water Load Test) 使血鈉進一步下降時，Hypothalamus 仍能完全關閉 AVP 分泌並排出稀釋尿 (Urine Osmolality < 100 mOsm/kg)，順利排出 > 80% 的水份負荷。此型態無需特殊處置。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing Reset Osmostat physiology and water loading response.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q13",
        "number": 13,
        "stem": "Which antibiotic agent possesses pharmacological activity as an inhibitor of AVP-induced adenylyl cyclase activation in the renal collecting duct, and was historically used off-label to treat chronic SIADH?",
        "options": [
            {"id": "A", "text": "Demeclocycline"},
            {"id": "B", "text": "Vancomycin"},
            {"id": "C", "text": "Ciprofloxacin"},
            {"id": "D", "text": "Ceftriaxone"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Demeclocycline 是一種 Tetracycline 衍生物，能在 Collecting Duct 阻斷 AVP 誘導的 Adenylyl Cyclase 活化，從而引發 Partial Nephrogenic Diabetes Insipidus (NDI)，增加自由水排出。過去常用於 chronic SIADH 的藥物治療 (現多被 Vaptans 取代)。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing Demeclocycline mechanism of action in SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q14",
        "number": 14,
        "stem": "How does oral urea therapy (0.25 to 0.5 g/kg/day) effectively increase serum sodium concentration in patients with chronic SIADH?",
        "options": [
            {"id": "A", "text": "It induces an osmotic diuresis by increasing urinary solute excretion, thereby promoting electrolyte-free water clearance"},
            {"id": "B", "text": "It directly stimulates aldosterone secretion from the adrenal zona glomerulosa"},
            {"id": "C", "text": "It blocks V2 receptors on the basolateral membrane of principal cells"},
            {"id": "D", "text": "It converts into sodium chloride in the proximal tubule"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "口服 Urea (0.25-0.5 g/kg/day) 在體內經由腎臟過濾後，會增加 Urine Solute Excretion，在 Medullary Collecting Duct 引發 Osmotic Diuresis，強迫帶走自由水 (Electrolyte-Free Water Clearance)，從而有效調升血清鈉離子濃度，為無效或無法耐受 Fluid Restriction 病患之安全替代方案。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing mechanism of oral urea in SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q15",
        "number": 15,
        "stem": "A patient with mild asymptomatic SIADH secondary to localized pneumonia has serum sodium of 130 mEq/L. What is the recommended first-line therapeutic intervention?",
        "options": [
            {"id": "A", "text": "Fluid restriction to 500-1000 mL/day"},
            {"id": "B", "text": "Immediate 3% Hypertonic Saline bolus"},
            {"id": "C", "text": "Intravenous Desmopressin (DDAVP)"},
            {"id": "D", "text": "High-dose IV Dextrose 5% in Water"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "對於無症狀或僅有輕微低血鈉 (Serum Na 125-135 mEq/L) 的 SIADH 病患，首選且最安全的處置為限制液體攝取 (Fluid Restriction 500-1000 mL/day)，每日水分攝取量應設定為低於每日預估尿量 500 mL。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing first-line conservative management of SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q16",
        "number": 16,
        "stem": "Which of the following primary pulmonary conditions is a well-established cause of SIADH leading to non-osmotic vasopressin release?",
        "options": [
            {"id": "A", "text": "Bacterial Pneumonia and Pulmonary Tuberculosis"},
            {"id": "B", "text": "Simple Pneumothorax without tension"},
            {"id": "C", "text": "Mild Allergic Asthma"},
            {"id": "D", "text": "Idiopathic Pulmonary Fibrosis without hypoxia"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "肺部感染與疾病 (如 Bacterial Pneumonia, Pulmonary Tuberculosis, Lung Abscess, ARDS) 是引發 SIADH 的常考原因。其機制涉及肺部局部 Hypoxia/Hypercapnia 以及胸腔內壓力變化 (如 Mechanical Ventilation PEEP)，干擾 Baroreceptors 進而促使 Central AVP 非適當釋放。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing pulmonary causes of SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Table_15_3.png",
                "caption": "Brenner 11e Table 15.3: Disorders associated with SIADH.",
                "sourceBook": "Brenner 11e Ch 15"
            }
        ],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q17",
        "number": 17,
        "stem": "Why does combining oral Sodium Chloride tablets with a Loop Diuretic (such as Furosemide) help correct hyponatremia in SIADH patients?",
        "options": [
            {"id": "A", "text": "Furosemide disrupts the medullary osmotic gradient and impairs urinary concentrating ability while salt tabs supply solute"},
            {"id": "B", "text": "Furosemide stimulates V2 receptors to enhance solute reabsorption"},
            {"id": "C", "text": "Furosemide decreases urinary sodium excretion while salt tabs induce free water absorption"},
            {"id": "D", "text": "Furosemide inhibits AVP release directly from the posterior pituitary gland"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Loop Diuretics (如 Furosemide) 能抑制 Thick Ascending Limb 的 NKCC2 輸送體，破壞 Medullary Interstitial Osmotic Gradient，使 Collecting Duct 即使在 AVP 存在下也無法將尿液濃縮至極致 (降低 Urine Osmolality)；配合 Oral Salt Tablets 補充溶質，能顯著促進 Electrolyte-Free Water Excretion，從而有效改善 SIADH 低血鈉。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing loop diuretic plus salt tablet therapy mechanism.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q18",
        "number": 18,
        "stem": "What key safety warning is associated with the clinical use of Tolvaptan, prompting the US FDA to restrict its continuous duration of use to a maximum of 30 days?",
        "options": [
            {"id": "A", "text": "Potential for severe Hepatotoxicity and liver injury"},
            {"id": "B", "text": "High incidence of acute pulmonary fibrosis"},
            {"id": "C", "text": "Irreversible nephrocalcinosis and nephrolithiasis"},
            {"id": "D", "text": "Severe hypercalcemia and metabolic alkalosis"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "Tolvaptan 的主要 Safety Warning 為潛在的 Hepatotoxicity (肝臟毒性 與 Transaminase 上升)。因此美國 FDA 規定使用 Tolvaptan 期間需定期監測 肝功能 (LFTs)，且連續使用時間不得超過 30 天，同時禁用於已有 Underlying Liver Disease (如 Cirrhosis) 的病患。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing FDA black box warning and safety restrictions for Tolvaptan.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q19",
        "number": 19,
        "stem": "A 68-year-old male presenting with SIADH has a baseline urine osmolality of 750 mOsm/kg H2O. Which of the following lab findings is most consistent with the expected renal response in SIADH?",
        "options": [
            {"id": "A", "text": "Urine Sodium > 30 mEq/L and Serum Osmolality < 275 mOsm/kg H2O"},
            {"id": "B", "text": "Urine Sodium < 10 mEq/L and Serum Osmolality > 295 mOsm/kg H2O"},
            {"id": "C", "text": "Fractional Excretion of Sodium (FE Na) < 0.1% with Serum Uric Acid > 9.0 mg/dL"},
            {"id": "D", "text": "Urine Osmolality < 80 mOsm/kg H2O during fluid restriction"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "SIADH 典型的實驗室數據包含：(1) Low Serum Osmolality (< 275 mOsm/kg)；(2) High Urine Osmolality (> 100 mOsm/kg，本題為 750 mOsm/kg)；(3) High Urine Sodium (> 30 mEq/L)；(4) FE Na > 1% 且 FE Urate > 10% (Hypouricemia)。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing lab findings pattern recognition in SIADH.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [],
        "nlmResponses": []
    },
    {
        "id": "2026_SIADH_Q20",
        "number": 20,
        "stem": "In the pathological development of Osmotic Demyelination Syndrome (ODS) triggered by overly rapid correction of severe hyponatremia, which central nervous system cell type suffers acute shrinkage and apoptosis due to loss of intracellular organic osmolytes?",
        "options": [
            {"id": "A", "text": "Astrocytes and Oligodendrocytes in the central pons"},
            {"id": "B", "text": "Purkinje cells in the cerebellar cortex"},
            {"id": "C", "text": "Ependymal cells lining the lateral ventricles"},
            {"id": "D", "text": "Microglial cells in the olfactory bulb"}
        ],
        "sourceProvidedAnswer": "A",
        "sourceAnswerStatus": "provided",
        "sourceExplanation": "在大腦適應慢性低血鈉時，Astrocytes 會將細胞內的 Organic Osmolytes (如 Myo-inositol, Glutamine, Taurine) 排出以維持細胞體積。若突然快速調升血清滲透壓，Astrocytes 無法及時重新合成並積聚 Organic Osmolytes，導致大腦細胞急遽脫水皺縮 (Cellular Shrinkage)，引發 Blood-Brain Barrier (BBB) 破裂、Astrocytes 與 Oligodendrocytes 凋亡，最終導致 Central Pontine Myelinolysis / Osmotic Demyelination Syndrome (ODS)。",
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "reconciliationNotes": "High confidence question testing cellular pathophysiology of Osmotic Demyelination Syndrome.",
        "qcVerified": False,
        "qcStatus": "PENDING_QC",
        "resolvedImages": [
            {
                "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_19.png",
                "caption": "Brenner 11e Fig 15.19: Osmotic demyelination syndrome cellular pathophysiology.",
                "sourceBook": "Brenner 11e Ch 15"
            }
        ],
        "nlmResponses": []
    }
]

paper_data = {
    "id": PAPER_ID,
    "title": TITLE,
    "sourceCategory": CATEGORY,
    "year": 2026,
    "questionCount": len(raw_questions),
    "questions": raw_questions
}

# Write files
os.makedirs(os.path.dirname(TUTORIAL_PATH), exist_ok=True)
with open(TUTORIAL_PATH, "w", encoding="utf-8") as f:
    json.dump(tutorial_data, f, ensure_ascii=False, indent=2)

with open(PAPER_PATH, "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated tutorial JSON at: {TUTORIAL_PATH}")
print(f"Successfully generated paper JSON at: {PAPER_PATH}")

import json
import os

output_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials/2026_KMU_Clinical_Exam_Prep_Tutorial.json'

tutorial_data = {
  'id': '2026_KMU_Clinical_Exam_Prep_Tutorial',
  'paperId': '2026 高醫臨床考訓',
  'title': '2026 高醫臨床考訊重點：腎臟專科高階主題式備考講堂',
  'sourceCategory': '2026 年重點轉化',
  'year': '2026',
  'updatedAt': '2026-07-29T15:00:00Z',
  'modules': [
    {
      'moduleId': 'mod_transplant_immunobiology',
      'moduleTitle': 'Module 1: Transplant Immunobiology, Desensitization & Chronic AMR',
      'sections': [
        {
          'heading': 'Desensitization Protocols in Living Donor Kidney Transplantation & Chronic Antibody-Mediated Rejection',
          'diagrams': [
            {
              'id': 'table_70_8_sec1',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Table_70_8_part1.png',
              'path': '/server-data/assets/Table_70_8_part1.png',
              'sourceBook': 'Brenner 11e Ch 70',
              'caption': 'Brenner 11e Table 70.8: Banff Diagnostic Categories for Kidney Transplant Histopathology (Active ABMR & Chronic Active ABMR Criteria).'
            },
            {
              'id': 'kdigo_fig1_sec1',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Fig_1.png',
              'path': '/server-data/assets/Fig_1.png',
              'sourceBook': 'KDIGO 2009 Transplant Guideline',
              'caption': 'KDIGO Transplant Recipient Management Algorithm for Immunosuppression and Allograft Monitoring.'
            },
            {
              'id': 'ai_transplant_sec1',
              'type': 'ai_illustration',
              'imagePath': '/server-data/assets/transplant_desensitization_camr.jpg',
              'path': '/server-data/assets/transplant_desensitization_camr.jpg',
              'caption': 'AI High-Resolution Illustration: Plasmapheresis Desensitization Mechanism & Peritubular Capillary Basement Membrane Multilayering (PTCML) with Linear C4d Staining.'
            }
          ],
          'keyTerms': [
            'Desensitization',
            'Plasmapheresis',
            'ABO-incompatible transplant',
            'ABO-compatible transplant',
            'Donor-Specific Antibody',
            'Chronic Antibody-Mediated Rejection',
            'Peritubular Capillary Basement Membrane Multilayering',
            'C4d Complement Staining',
            'Banff Classification'
          ],
          'content': """[權威文獻對照: Brenner 11e Ch 70 & KDIGO 2009 Transplant Guideline]

### 核心觀念解析：Living-Donor Kidney Transplantation 抗體清除與 Desensitization 原則

在 **Living-donor kidney transplantation** 領域，當捐贈者與受贈者存在 **ABO-incompatibility** 或受贈者體內存有高滴度 **Donor-Specific Antibody (DSA)** 時，必須實施嚴密的 **Desensitization protocol** 以防止發生 **Hyperacute rejection** 與 **Acute antibody-mediated rejection (ABMR)**。

根據 **American Society for Apheresis (ASFA)** 與 **KDIGO guidelines** 指引：
1. **Plasmapheresis (Therapeutic Plasma Exchange, TPE)** 搭配 **Intravenous Immunoglobulin (IVIG)** 於 **ABO-incompatible kidney transplantation** 屬於 **Category I indication**。
2. 對於 **ABO-compatible kidney transplantation** 但受贈者 **Crossmatch positive** 或具有高敏感化 **DSA** 之患者，執行 **Plasmapheresis** 進行 **Desensitization** 同樣列為 **Category I indication**。

這項臨床規範確立了不論是 **ABO-incompatibility** 或是 **HLA pre-sensitization**，**Plasmapheresis** 均為移除循環中預存抗體、降低 **Titer** 的核心前置處置手段。

---

### Chronic Antibody-Mediated Rejection (cAMR) 之病理診斷與 Banff 診斷標準門閥

**Chronic antibody-mediated rejection (cAMR)** 為導致 **Allograft** 長期失能 (**Late chronic allograft loss**) 的主因。其病理特徵為 **Microvascular endothelium** 長期受到低滴度 **DSA** 與 **Complement system** 的持續性微量傷害，引發 **Endothelial cell** 反覆損傷與修復。

#### 1. Peritubular Capillary Basement Membrane Multilayering (PTCML)
在 **Transmission Electron Microscopy (TEM)** 下，**Peritubular capillary (PTC)** 內皮下基底膜呈現多層次結構。
- **Banff classification** 嚴格規定：**只有 Severe PTCML（於 TEM 下觀察到 7 層或以上之 Multilayering）** 方能作為符合 **Chronicity criteria of AMR** 的病理診斷指標。輕微或中度重層化不具備單獨診斷 **cAMR** 之特徵強度。

#### 2. Linear C4d Staining 替代效應
**C4d** 為 **Complement activation** 之 **Classical pathway** 中 **C4b** 裂解後共價結合於組織的副產物。當臨床上受血清學技術限制無法直接測定 **DSA** 或 **DSA** 呈現隱匿性時，**Banff criteria** 許可在 **PTC** 觀察到強烈且連續的 **Linear C4d immunofluorescence/immunohistochemistry staining** 時，作為代表 **Current or recent antibody-mediated complement activation** 的替代分子標記（**Substitute for DSA**）。

---

### Dynamic Feature / Receptor / Pathway Mapping Matrix

| Target | Receptor / Pathway | Category / Criteria | Clinical Significance & Pitfall |
| :--- | :--- | :--- | :--- |
| **ABO-incompatible TPE** | Anti-A / Anti-B Isohemagglutinin removal | **Category I Indication** | 移植前必須將 Isohemagglutinin titer 降至 <= 1:8 |
| **ABO-compatible (Positive XM)** | Anti-HLA Pre-formed DSA removal | **Category I Indication** | TPE 結合 IVIG 可有效抑制 Complement-dependent cytotoxicity |
| **Severe PTCML** | TEM >= 7 layers of peritubular basement membrane | **Banff Chronicity Criterion** | 僅有 Severe (>= 7 layers) 符合診斷，Mild/Moderate 不得計算 |
| **Linear C4d in PTC** | Classical complement cascade activation | **DSA Surrogate Marker** | 微血管壁線性 C4d 沉積可直接替代 DSA 陰性之缺口 |

---

### High-Yield Differential Comparison: Rejection Histopathology

| Feature | Acute TCMR | Active ABMR | Chronic Active ABMR (cAMR) |
| :--- | :--- | :--- | :--- |
| **Target Cells** | Tubular epithelial cells & Interstitium | Microvascular endothelium (Glomerular & PTC) | Peritubular capillary & Glomerular basement membranes |
| **Histopathology** | Tubulitis (t >= 1), Interstitial inflammation (i >= 1) | Microvascular inflammation (g+ptc >= 2), Intracapillary thrombi | **Severe PTCML** (>= 7 layers), Transplant glomerulopathy (cg > 0) |
| **C4d Staining** | Negative | Positive or Negative (C4d-negative ABMR) | Diffuse linear PTC C4d staining |
| **Primary Mediators** | Cytotoxic T lymphocytes (CD8+) & Macrophages | Anti-HLA or anti-ABO **Donor-Specific Antibodies (DSA)** | Persistent low-titer DSA causing chronic endothelial injury |

---

### Pathophysiological Decision Trees

Pre-transplant Positive Crossmatch / High DSA / ABO-Incompatibility
  └─► Execute Plasmapheresis (TPE) + IVIG Desensitization (Category I Indication)
        └─► Deplete circulating Anti-ABO & Anti-HLA Antibodies (Titer <= 1:8)
              └─► Prevent Hyperacute & Early Active ABMR

Post-transplant Persistent Low-Titer DSA / Endothelial Microinjury
  ├─► Classical Complement Pathway Activation ──► Linear C4d Deposition in PTC
  │                                                     └─► Can substitute for DSA in Banff Diagnosis
  │
  └─► Repeated Microvascular Endothelial Injury & Repair
        └─► Basement Membrane Multilayering ──► Severe PTCML (>= 7 layers on TEM)
                                                     └─► Structural Diagnostic Criterion for cAMR

---

### Conceptual Trap Analysis

1. **Category Classification Trap**：臨床常誤以為只有 **ABO-incompatible** 才屬於 **Category I** 適應症。事實上，**ABO-compatible** 但 **Crossmatch positive / High DSA** 執行 **Plasmapheresis** 同樣屬於 **Category I**。
2. **TEM Layer Quantification Trap**：**Banff criteria** 對於 **PTCML** 的計算非常嚴格，任何少於 **7 layers** 的基底膜重層化均不符合 **cAMR** 的結構診斷標準。
3. **C4d-Negative ABMR Trap**：雖然 **Linear C4d** 可以作為 **DSA** 的替代指標，但非補體依賴性抗體作用機制或 **NK cell-mediated ADCC** 亦可引發 **C4d-negative ABMR**，不可將 **C4d negative** 直接等同於排除 **ABMR**。"""
        }
      ]
    },
    {
      'moduleId': 'mod_endocrine_hypertension',
      'moduleTitle': 'Module 2: Endocrine Hypertension & Mineral Transport Signaling',
      'sections': [
        {
          'heading': 'Adrenal Vein Sampling (AVS) Dynamics & Tumor-Induced Osteomalacia (TIO) Phosphatonin Pathways',
          'diagrams': [
            {
              'id': 'fig_17_9_sec2',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Fig_17_9.png',
              'path': '/server-data/assets/Fig_17_9.png',
              'sourceBook': 'Brenner 11e Ch 17',
              'caption': 'Brenner 11e Fig 17.9: Diagnostic Algorithm in Primary Aldosteronism and Adrenal Vein Sampling (AVS) Interpretation.'
            },
            {
              'id': 'fig_7_10_sec2',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Fig_7_10.png',
              'path': '/server-data/assets/Fig_7_10.png',
              'sourceBook': 'Brenner 11e Ch 07',
              'caption': 'Brenner 11e Fig 7.10: Proximal Tubule Phosphate Transport Regulation by FGF23 and NaPi-2a/NaPi-2c Cotransporters.'
            },
            {
              'id': 'ai_endocrine_sec2',
              'type': 'ai_illustration',
              'imagePath': '/server-data/assets/avs_and_tio_fgf23.jpg',
              'path': '/server-data/assets/avs_and_tio_fgf23.jpg',
              'caption': 'AI Illustration: Adrenal Vein Sampling Post-Cosyntropin A/C Ratio Cut-off (4:1) & TIO FGF23 Phosphatonin Cascade.'
            }
          ],
          'keyTerms': [
            'Adrenal Vein Sampling',
            'Primary Aldosteronism',
            'Aldosterone-to-Cortisol Ratio',
            'Cosyntropin Stimulation Test',
            'Tumor-Induced Osteomalacia',
            'FGF23',
            'Phosphatonin',
            'TmP/GFR',
            'Burosumab',
            'Cinacalcet'
          ],
          'content': """[權威文獻對照: Brenner 11e Ch 12, Ch 17 & Ch 07]

### 核心觀念解析：Adrenal Vein Sampling (AVS) 側化判定標準

在 **Primary Aldosteronism (PA)** 的診斷流程中，當 **Aldosterone-to-Renin Ratio (ARR)** 陽性且確認過量分泌後，為了區分 **Unilateral Aldosterone-Producing Adenoma (APA)** 與 **Bilateral Adrenal Hyperplasia (BAH)**，**Adrenal Vein Sampling (AVS)** 為黃金標準指標。

為了消除靜脈血流稀釋效應與採樣瞬時波動，必須使用 **Cortisol** 來校正 **Aldosterone** 濃度，計算出 **Aldosterone-to-Cortisol (A/C) ratio**：
1. **Cannulation Selectivity Index**：以 **Adrenal Vein Cortisol / Inferior Vena Cava (IVC) Cortisol** 評估成功導管插管。在 **Cosyntropin (ACTH 1-24) stimulation** 後，比值需 >= 5:1；未刺激前需 >= 3:1。
2. **Lateralization Index (Positive Cut-off Value)**：經過 **Cosyntropin stimulation** 之後，高分泌側與低分泌側的 **A/C ratio** 側化比值黃金截斷值為 **1:4 (Dominant to Non-dominant ratio >= 4:1)**。若達到 **4:1** 標示為單側病變，指示單側 **Adrenalectomy**。

---

### Tumor-Induced Osteomalacia (TIO) 生化診斷與 Phosphatonin 分子病理

**Tumor-Induced Osteomalacia (TIO)**（又稱 **Oncogenic Osteomalacia**）是一種由 **Phosphaturic Mesenchymal Tumor (PMT)** 過度分泌 **Phosphatonins** 引發的罕見 **Paraneoplastic syndrome**。

#### 1. Phosphatonin 家族與 Sclerostin 的差異
**Phosphatonins** 為能促進腎臟排磷、抑制 **Active Vitamin D** 合成的體液因子，包括：
- **FGF23 (Fibroblast Growth Factor 23)**：主要致病因子。
- **MEPE (Matrix Extracellular Phosphoglycoprotein)**
- **sFRP4 (Secreted Frizzled-Related Protein 4)**
- **FGF7**
- **重要鑑別陷阱**：**Sclerostin (SOST)** 為 **Osteocyte** 分泌抑制 **Wnt/beta-catenin pathway** 的調節因子，**不屬於 Phosphatonin 家族**！

#### 2. 生化病理學與計算指標
**FGF23** 作用於 **Proximal tubule** 的 **FGFR1/Klotho receptor complex**，引發：
- 下調 **NaPi-2a (SLC34A1)** 與 **NaPi-2c (SLC34A3)** 共運體，導致大量 **Renal phosphate wasting**。
- 抑制 **1-alpha-hydroxylase (CYP27B1)** 並活化 **24-hydroxylase (CYP24A1)**，導致 **Serum 1,25(OH)2D3** 異常偏低或不適當的正常。
- 臨床需計算 **Fractional Excretion of Phosphate (FePi)** 與 **TmP/GFR (Tubular Maximum Reabsorption of Phosphate per GFR)**。**TmP/GFR** 顯著降低為診斷 **Renal phosphate wasting** 的核心依據。

#### 3. 治療戰略演進
- 首選治療：外科精準完整切除 **PMT**。
- 藥物治療：補充 **Oral phosphate** 搭配 **Calcitriol** 或 **Cinacalcet**。
- 標靶突破：**Burosumab**（**Monoclonal IgG1 anti-FGF23 antibody**）已於 **2020 年獲 FDA 批准** 用於無法切除或定位失敗之 **TIO** 患者。

---

### Dynamic Feature / Receptor / Pathway Mapping Matrix

| Factor / Test | Target | Marker / Ratio | Diagnostic Threshold |
| :--- | :--- | :--- | :--- |
| **Post-ACTH AVS** | Adrenal cortex microcirculation | **A/C Ratio Lateralization** | **Dominant:Non-dominant ratio >= 4:1** |
| **FGF23 Pathway** | Proximal Tubule (PT) FGFR1/Klotho | **NaPi-2a / NaPi-2c Downregulation** | **TmP/GFR 顯著下降** (Phosphate Wasting) |
| **1-alpha-Hydroxylase** | PT Mitochondria CYP27B1 | **Suppressed 1,25(OH)2D3** | 低血磷但 1,25(OH)2D 不適當低下 |
| **Burosumab** | Circulating active FGF23 | **Monoclonal IgG1 Anti-FGF23** | **2020 FDA Approved for TIO** |

---

### High-Yield Differential Comparison: Hypophosphatemic Disorders

| Disorder | FGF23 Level | Serum Calcium | Serum 1,25(OH)2D | Etiology |
| :--- | :--- | :--- | :--- | :--- |
| **TIO (Oncogenic)** | 異常升高 (High) | Normal or Low | Low / Inappropriately Normal | Acquired (Phosphaturic Mesenchymal Tumor) |
| **XLH (X-linked)** | 升高 (High) | Normal | Low / Inappropriately Normal | X-linked dominant (PHEX gene mutation) |
| **ADHR** | 升高 (High) | Normal | Low / Inappropriately Normal | Autosomal dominant (FGF23 cleavage site mutation) |
| **ARHR** | 升高 (High) | Normal | Low / Inappropriately Normal | Autosomal recessive (DMP1, ENPP1, FAM20C mutations) |
| **HPRH** | **Normal / Suppressed** | Normal | **Markedly Elevated** | Autosomal recessive (SLC34A3/NaPi-2c mutation) |

---

### Pathophysiological Decision Trees

Primary Aldosteronism Diagnostic Protocol
  └─► Positive ARR & Confirmatory Suppression Test
        └─► Perform Adrenal Vein Sampling (AVS) with Cosyntropin Stimulation
              ├─► Post-ACTH A/C Ratio Lateralization >= 4:1 ──► Unilateral APA ──► Adrenalectomy
              └─► Post-ACTH A/C Ratio Lateralization < 4:1 ──► Bilateral BAH ──► MRA (Spironolactone)

Tumor-Induced Osteomalacia (TIO) Pathophysiology
  └─► PMT Secretes Excessive FGF23 (Phosphatonin)
        ├─► Downregulates NaPi-2a/NaPi-2c in Proximal Tubule ──► Reduced TmP/GFR ──► Severe Hypophosphatemia
        └─► Inhibits CYP27B1 (1-alpha-hydroxylase) ──► Low 1,25(OH)2D3 ──► Impaired Intestinal Calcium/Phosphate Absorption

Treatment Protocol: Surgical PMT Resection or Anti-FGF23 Antibody (Burosumab - 2020 FDA Approved)

---

### Conceptual Trap Analysis

1. **AVS Lateralization Cut-off Trap**：未經過 **Cosyntropin** 刺激前，部分文獻允許 **2:1** 或 **3:1**；但**經過 Cosyntropin 刺激後，黃金側化截斷值一律為 4:1 (Dominant/Non-dominant A/C ratio >= 4:1)**。
2. **Phosphatonin Family Inclusion Trap**：考題常將 **Sclerostin** 混入選項中問何者屬於 **Phosphatonin**。**Sclerostin 不是 Phosphatonin**，真正的 **Phosphatonins** 包括 **FGF23, MEPE, sFRP4, FGF7**。
3. **Calcitriol Level in TIO Trap**：在嚴重低血磷下，正常生理反應應刺激 **1-alpha-hydroxylase** 使 **1,25(OH)2D3** 顯著上升。但 **TIO** 患者的 **1,25(OH)2D3** 卻呈現不適當的正常或下降，此為 **FGF23** 抑制作用的證明。"""
        }
      ]
    },
    {
      'moduleId': 'mod_inherited_structural',
      'moduleTitle': 'Module 3: Inherited Tubular Defects, Tumor Syndromes & Anatomical Anomalies',
      'sections': [
        {
          'heading': 'Tuberous Sclerosis Complex (TSC), FHHNC Claudin Mutations & Horseshoe Kidney Biopsy Safety',
          'diagrams': [
            {
              'id': 'fig_45_11_sec3',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Fig_45_11.png',
              'path': '/server-data/assets/Fig_45_11.png',
              'sourceBook': 'Brenner 11e Ch 45',
              'caption': 'Brenner 11e Fig 45.11: Tuberous Sclerosis Complex (TSC) Bilateral Renal Angiomyolipoma (AML) Histopathology and Abdominal CT.'
            },
            {
              'id': 'fig_44_1_sec3',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Fig_44_1.png',
              'path': '/server-data/assets/Fig_44_1.png',
              'sourceBook': 'Brenner 11e Ch 44',
              'caption': 'Brenner 11e Fig 44.1: Paracellular Divalent Cation Transport in Thick Ascending Limb (TAL) mediated by Claudin-16 (Paracellin-1) and Claudin-19.'
            },
            {
              'id': 'fig_26_1_sec3',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Fig_26_1.png',
              'path': '/server-data/assets/Fig_26_1.png',
              'sourceBook': 'Brenner 11e Ch 26',
              'caption': 'Brenner 11e Fig 26.1: Diagnostic Evaluation and Relative Contraindications for Percutaneous Renal Biopsy.'
            },
            {
              'id': 'ai_inherited_sec3',
              'type': 'ai_illustration',
              'imagePath': '/server-data/assets/tsc_fhhnc_horseshoe.jpg',
              'path': '/server-data/assets/tsc_fhhnc_horseshoe.jpg',
              'caption': 'AI Illustration: TSC Renal AML Pathogenesis, FHHNC CLDN16/19 Tight Junction Defects & Horseshoe Kidney Fusion Dynamics.'
            }
          ],
          'keyTerms': [
            'Tuberous Sclerosis Complex',
            'Angiomyolipoma',
            'TSC1',
            'TSC2',
            'mTOR Inhibitor',
            'FHHNC',
            'Claudin-16',
            'Claudin-19',
            'Nephrocalcinosis',
            'Horseshoe Kidney',
            'Renal Biopsy Contraindications'
          ],
          'content': """[權威文獻對照: Brenner 11e Ch 45, Ch 44 & Ch 26]

### 核心觀念解析：Tuberous Sclerosis Complex (TSC) 之腎臟病變與臨床特徵

**Tuberous Sclerosis Complex (TSC)** 為體染色體顯性遺傳性疾病，由 **TSC1 (Hamartin)** 或 **TSC2 (Tuberin)** 基因突變引發 **mTOR pathway** 過度活化。

#### 1. 腎臟特徵與死因位移
- 腎臟主要病變為雙側多發性 **Angiomyolipoma (AML)**、**Renal Cysts** 與 **Renal Cell Carcinoma (RCC)**。
- **Death Causes Priority**：在童年時期主要死因為 **Central Nervous System (CNS)** 病變（如 **Subependymal Giant Cell Astrocytoma, SEGA** 或 **Status epilepticus**）；但在成年時期，**Renal disease (ESRD or AML hemorrhage)** 已躍升為最主要的死因 (**Leading cause of death: CNS ──► Renal**)。

#### 2. Estrogen 相關性與懷孕風險
**AML** 組織表達高濃度 **Estrogen** 與 **Progesterone receptors**。女性在懷孕期間因為 **Estrogen** 濃度劇升，**AML 體積會快速增大**，大幅增加破裂出血與 **Lymphangioleiomyomatosis (LAM)** 惡化風險。

#### 3. 手術與介入適應症及嗜鉻細胞瘤之鑑別
- **Intervention indications**：**AML 直徑 > 4 cm**、**Aneurysm size > 5 mm**、持續性性疼痛或急性自發性破裂出血（首選 **Transcatheter Arterial Embolization, TAE**；無症狀 > 3 cm 首選 **mTOR inhibitor (Everolimus)**）。
- **關鍵鑑別鐵律**：**TSC 患者絕對不會出現 Pheochromocytoma**！具有 **Pheochromocytoma** 表現的遺傳症候群為 **VHL (Von Hippel-Lindau)**、**NF1 (Neurofibromatosis type 1)** 與 **MEN2**。

---

### Familial Hypomagnesemia with Hypercalciuria and Nephrocalcinosis (FHHNC)

**FHHNC** 是一種嚴重且罕見的 **Autosomal Recessive (AR)** Renal tubular遺傳疾病，病因為 **Thick Ascending Limb (TAL)** 緊密連接 (**Tight junction**) 蛋白質突變。

#### 1. Claudin-16 (Paracellin-1) 與 Claudin-19 分子遺傳
- **Type 1 FHHNC**：由 **CLDN16 (Claudin-16 / Paracellin-1)** 突變引起。
- **Type 2 FHHNC**：由 **CLDN19 (Claudin-19)** 突變引起。**Claudin-19** 同時表達於腎臟 **TAL** 與眼部 **Retinal pigment epithelium**。因此 **Type 2 FHHNC 特徵為合併嚴重的 Ocular symptoms (e.g., severe myopia, nystagmus, macular coloboma)**。

#### 2. 生化與臨床特徵
- **Inappropriately High PTH**：患者即使血鈣正常或低偏，**PTH** 水準仍呈現不適當的顯著升高。
- **Treatment Resistance**：長期口服大劑量 **Magnesium** 補充**無法使血鎂濃度恢復正常**，且多數患者在青少年期即快速進展至 **Progressive CKD / ESRD**。

---

### Horseshoe Kidney 與 Percutaneous Renal Biopsy 安全評估

**Horseshoe Kidney** 為最常見的腎臟融合發育異常，**Bilateral lower renal poles** 在 **Aorta** 前交叉融合形成 **Isthmus**。
- **Percutaneous Renal Biopsy Safety**：對於 **Horseshoe kidney** 患者，由於解剖位置異常與血管走位扭曲（常伴隨多重異位 **Renal arteries**），**Percutaneous renal biopsy** 具有極高血管損傷與出血風險，列為 **Relative Contraindication**。

---

### Dynamic Feature / Receptor / Pathway Mapping Matrix

| Disorder | Gene / Protein | Inheritance | Key Hallmark |
| :--- | :--- | :--- | :--- |
| **TSC** | TSC1 (Hamartin) / TSC2 (Tuberin) | Autosomal Dominant | 成人主要死因為 **Renal**；**No Pheochromocytoma** |
| **FHHNC Type 1** | CLDN16 (Claudin-16) | Autosomal Recessive | Magnesium & Calcium reabsorption impairment, **Nephrocalcinosis**, 高 **PTH** |
| **FHHNC Type 2** | CLDN19 (Claudin-19) | Autosomal Recessive | 腎臟病變**合併 Ocular symptoms (Coloboma, Myopia)** |
| **Horseshoe Kidney** | Lower pole fusion (Aberrant vessels) | Congenital Anomaly | **Renal Biopsy Relative Contraindication** |

---

### High-Yield Differential Comparison: Hereditary Syndromes with Renal Tumors

| Syndrome | Gene | Renal Lesions | Pheochromocytoma | Extrarenal Features |
| :--- | :--- | :--- | :--- | :--- |
| **TSC** | TSC1, TSC2 | Bilateral **Angiomyolipoma (AML)**, Cysts, RCC | **NO (Absolute Zero)** | Facial angiofibromas, Cardiac rhabdomyoma, LAM |
| **VHL** | VHL | Clear cell RCC, Pancreatic/Renal Cysts | **YES (Common)** | Hemangioblastoma (Retina/CNS), Endolymphatic tumor |
| **BHD (Birt-Hogg-Dubé)** | FLCN (Folliculin) | Chromophobe RCC, Hybrid Oncocytic Tumors | **NO** | Fibrofolliculomas, Spontaneous pneumothorax |
| **NF1** | NF1 (Neurofibromin) | Renal artery stenosis, Rare RCC | **YES** | Café-au-lait spots, Neurofibromas, Lisch nodules |

---

### Pathophysiological Decision Trees

Tuberous Sclerosis Complex (TSC) Adult Complication Progression
  └─► Loss of TSC1/TSC2 Complex ──► Hyperactive mTOR Signaling
        ├─► Renal Angiomyolipoma (AML) Expansion (Estrogen accelerated in Pregnancy)
        │     ├─► Size > 4 cm / Aneurysm > 5 mm ──► High Rupture Bleeding Risk
        │     │                                       └─► TAE or mTOR Inhibitor (Everolimus)
        │     └─► Renal Failure & Hemorrhage ──► Adult Leading Cause of Death
        └─► NO Pheochromocytoma (Distinguish from VHL/NF1)

FHHNC Pathogenesis (CLDN16 / CLDN19 Mutations)
  └─► Disruption of Tight Junction Paracellular Pore in Thick Ascending Limb (TAL)
        ├─► Severe Urinary Magnesium & Calcium Wasting ──► Nephrocalcinosis & CKD Progression
        └─► Secondary High PTH (Unresponsive to Long-Term Oral Mg Supplementation)

If CLDN19 Mutation (Type 2) ──► Retinal Pigment Epithelium Defect ──► Ocular Manifestations (Myopia, Coloboma)

---

### Conceptual Trap Analysis

1. **TSC Tumor Association Trap**：高頻考題常混淆 **TSC** 與 **VHL** 的腫瘤表現。**TSC 絕無 Pheochromocytoma**；若題目提及腎腫瘤伴隨 **Pheochromocytoma**，正解必為 **VHL** 或 **NF1**。
2. **FHHNC Oral Mg Response Trap**：臨床常直覺認為補鎂即可修正 **FHHNC** 的低血鎂。但事實上 **Long-term oral Mg administration does NOT normalize serum Mg2+ levels**，腎臟流失無法關閉。
3. **CLDN16 vs CLDN19 Ocular Trap**：**Type 1 (CLDN16)** 僅有 **Nephrocalcinosis** 表現；唯有 **Type 2 (CLDN19)** 才具有 **Ocular symptoms**（如 **Macular coloboma**）。"""
        }
      ]
    },
    {
      'moduleId': 'mod_infectious_dialysis_pitfalls',
      'moduleTitle': 'Module 4: Infectious Nephrology, Peritoneal Dialysis Sclerosis & Laboratory Artifacts',
      'sections': [
        {
          'heading': 'Genitourinary Tuberculosis, Encapsulating Peritoneal Sclerosis (EPS) & Pseudohyperkalemia Artifacts',
          'diagrams': [
            {
              'id': 'fig_35_1_sec4',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Fig_35_1.png',
              'path': '/server-data/assets/Fig_35_1.png',
              'sourceBook': 'Brenner 11e Ch 35',
              'caption': 'Brenner 11e Fig 35.1: Granulomatous Tubulointerstitial Nephritis and Autonephrectomy Pathology in Genitourinary Tuberculosis.'
            },
            {
              'id': 'fig_64_2_sec4',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Fig_64_2.png',
              'path': '/server-data/assets/Fig_64_2.png',
              'sourceBook': 'Brenner 11e Ch 64',
              'caption': 'Brenner 11e Fig 64.2: Encapsulating Peritoneal Sclerosis (EPS) Peritoneal Fibrosis, Intestinal Cocooning & Calcification.'
            },
            {
              'id': 'table_17_3_sec4',
              'type': 'micrograph',
              'imagePath': '/server-data/assets/Table_17_3.png',
              'path': '/server-data/assets/Table_17_3.png',
              'sourceBook': 'Brenner 11e Ch 17',
              'caption': 'Brenner 11e Table 17.3: Correlation Between Serum Potassium Concentration and Electrocardiographic (ECG) Changes.'
            },
            {
              'id': 'ai_pitfalls_sec4',
              'type': 'ai_illustration',
              'imagePath': '/server-data/assets/tb_eps_pseudohyperkalemia.jpg',
              'path': '/server-data/assets/tb_eps_pseudohyperkalemia.jpg',
              'caption': 'AI Illustration: Genitourinary TB Putty Kidney Cascade, EPS Intestinal Cocooning & Pseudohyperkalemia Fragile Cell Lysis.'
            }
          ],
          'keyTerms': [
            'Genitourinary Tuberculosis',
            'Autonephrectomy',
            'Putty Kidney',
            'Calyceal Clubbing',
            'Encapsulating Peritoneal Sclerosis',
            'Peritoneal Calcification',
            'Pseudohyperkalemia',
            'Fragile Leukocytes',
            'Pneumatic Tube Transport'
          ],
          'content': """[權威文獻對照: Brenner 11e Ch 35, Ch 64 & Ch 17]

### 核心觀念解析：Genitourinary Tuberculosis (GU TB) 之影像與病理病程

**Genitourinary Tuberculosis (GU TB)** 為 **Extrapulmonary tuberculosis** 常見型態。**Mycobacterium tuberculosis** 經血行播散至 **Renal cortex**，形成 **Granulomas** 與 **Caseous necrosis**。

#### 1. 影像學與自然病程
- **Calyceal Clubbing & Ureteral Strictures**：結核性 **Granulomas** 潰破至 **Renal pelvis** 引發 **Fibrotic strictures**，影像學呈現典型的 **Calyceal clubbing** 與 **Renal pelvis / Ureter dilation**。
- **Autonephrectomy (Putty Kidney)**：嚴重 **Calyceal dilation** 與皮質破壞最終導致腎臟完全乾酪化與緻密鈣化失能，稱為 **Autonephrectomy (Putty kidney)**。此現象發生於 **23% 至 33% 的 GU TB 患者**。
- **Renal Failure Incidence**：結核所致之 **Renal failure** 發生率為 **1% 至 10%**。

---

### Encapsulating Peritoneal Sclerosis (EPS)

**Encapsulating Peritoneal Sclerosis (EPS)** 為 **Peritoneal Dialysis (PD)** 最嚴重且高致死率的併發症。

#### 1. 腹膜病理與 Intestinal Cocooning
長期的 **PD** 暴露（高糖透析液、酸性環境、**GDPs**）或反覆 **Peritonitis** 引發腹膜慢性發炎與纖維化。極厚的增生纖維膜將 **Small bowel** 包覆，形成 **Intestinal cocooning**。

#### 2. KUB 放射線學特徵
**KUB** 或 **CT** 顯示特徵性的 **Peritoneal calcification**（腹膜牆壁呈廣泛薄板狀或瀰漫性鈣化沉積），伴隨 **Bowel obstruction** 與腸壁增厚。

---

### Pseudohyperkalemia 生化偽影機制

**Pseudohyperkalemia** 定義為體外測得的 **Serum potassium** 顯著升高，但體內真實 **In vivo plasma potassium** 正常，且患者 **12-lead ECG 完全正常（無 Peaked T waves, QRS widening 或 PR prolongation）**。

#### 1. 致病因素
- **Fragile Leukocytosis**：嚴重白血球過高（如 **Chronic Lymphocytic Leukemia, CLL** 或 **Acute Leukemia**, WBC > 50,000-100,000/uL）。白血病細胞極度脆弱，在 **Venipuncture** 抽血、**Pneumatic tube transport** 氣動傳輸震盪、或 **Centrifugation** 離心過程中細胞破裂，釋放出大量細胞內鉀離子。
- **Thrombocytosis & Hemolysis**：血小板 > 500,000/uL（凝血過程釋放鉀）或體外溶血。

#### 2. 處置與防範鐵律
當 **Serum potassium** 異常高但 **ECG** 完全正常時：
- 必須使用 **Heparinized blood tube (Plasma potassium)** 採血。
- **禁止使用 Pneumatic tube transport 輸送**，需專人手提送檢，並避免劇烈搖晃。

---

### Dynamic Feature / Receptor / Pathway Mapping Matrix

| Complication / Artifact | Pathophysiology | Hallmark & Rate | Management Mandate |
| :--- | :--- | :--- | :--- |
| **GU TB (Putty Kidney)** | Caseous necrosis & Strictures | **Autonephrectomy (23-33%)**; Renal failure (1-10%) | CT 見 Calyceal clubbing & 廣泛鈣化 |
| **EPS** | Chronic peritoneal inflammation | **Peritoneal calcification** & Cocooning | KUB 可見薄板狀 Peritoneal calcification |
| **Pseudohyperkalemia** | Fragile leukemic cell lysis in vitro | Serum K+ 升高但 **ECG 100% 正常** | 採用 **Plasma K+** (Heparin) 且**禁用 Pneumatic transport** |

---

### High-Yield Differential Comparison: Pseudohyperkalemia vs True Hyperkalemia

| Parameter | Pseudohyperkalemia | True Hyperkalemia |
| :--- | :--- | :--- |
| **12-lead ECG** | **100% Normal (No Peaked T waves)** | **Tall Peaked T waves, QRS widening, Sine wave** |
| **Serum K+ vs Plasma K+** | Serum K+ 比 Plasma K+ 高 > 0.5 mmol/L | Serum K+ 與 Plasma K+ 均一致升高 |
| **Associated Cytopenia / Cytosis** | **Fragile Leukemia WBC > 50,000/uL**, Platelets > 500k | 無特定血球破裂關聯（多為 CKD/AKI/RAASi） |
| **Pneumatic transport Impact** | **Pneumatic transport 後 K+ 顯著飆高** | Pneumatic transport 前後 K+ 無顯著變化 |

---

### Pathophysiological Decision Trees

Genitourinary TB Natural Progression
  └─► Mycobacterium tuberculosis Renal Cortical Seeding
        └─► Caseous Necrosis & Granulomatous Inflammation
              └─► Ureteral Stricture & Calyceal Clubbing
                    └─► Autonephrectomy (Putty Kidney) (23% - 33% of cases)
                          └─► Progressive Renal Failure (1% - 10% of cases)

Pseudohyperkalemia Diagnostic & Handling Algorithm
  └─► Elevated Lab Serum K+ (> 6.0 mmol/L) with Completely Normal ECG
        ├─► Check WBC count (Look for Fragile Leukemic Cells / CLL)
        └─► Re-draw Blood with Heparinized Plasma Tube
              ├─► DO NOT use Pneumatic Tube Transport (Manual transport only)
              └─► Measured Plasma K+ Normal ──► Confirms Pseudohyperkalemia (Avoid Aggressive Treatment)

---

### Conceptual Trap Analysis

1. **GU TB Autonephrectomy Rate Trap**：考題常考 **Autonephrectomy** 的發生比例。**Putty kidney / Autonephrectomy** 發生於 **23-33%** 的患者，而 **Renal failure** 發生於 **1-10%** 的患者，兩數字不可錯置。
2. **Pseudohyperkalemia Treatment Trap**：當發現極高血鉀報告時，未核對 **ECG** 即急躁給予 **Calcium gluconate** 或 **Insulin/Glucose** 治療，可能引發實質低血鉀。**只要 ECG 正常且 WBC 顯著升高，必須優先排除 Pseudohyperkalemia**。
3. **Pneumatic Tube Transport Trap**：傳統抽血以氣動管送檢，在 **Leukocytosis** 患者會造成劇烈物理剪力破壞白血球，大幅加重 **Pseudohyperkalemia**。必須改為人工專人送檢。"""
        }
      ]
    }
  ]
}

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(tutorial_data, f, indent=2, ensure_ascii=False)

print('Successfully updated tutorial JSON with 100% pure English medical terms and English parentheses.')

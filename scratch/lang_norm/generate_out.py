import json

input_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/lang_norm/vghtpe_b1_in.json"
output_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/lang_norm/vghtpe_b1_out.json"

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

normalized_explanations = {
    "q1": """### 1. Answer Determination
正確答案為 **(D)**。

### 2. Mechanism & Rationale
在正常健康 `uncomplicated pregnancy` 期間，`renal hemodynamics` 發生顯著適應性改變：
- **Effective Renal Plasma Flow (ERPF / RPF)**：在 `first trimester` 與 `second trimester` 迅速上升，`peak` 可達 `baseline` 的 50%–80%。
- **Glomerular Filtration Rate (GFR)**：由於 `RPF` 增加及 `ultrafiltration coefficient` 適應，`GFR` 上升約 40%–50% (在 150–200 mL/min 之間)，導致 `serum creatinine` 生理性下降至 0.4–0.5 mg/dL。
- **Filtration Fraction (FF = GFR / RPF)**：由於 `RPF` 的增幅等於或大於 `GFR` 的增幅，`filtration fraction` 保持相對穩定或呈微幅下降。因此 (D) 選項完全正確。

### 3. Distractor Analysis
- **(C) 錯誤**：`Filtration fraction` 並未顯著上升 50%，主因在於 `RPF` 的增加比例並未落後於 `GFR`。
- **(A) 錯誤**：`gestation` 期間在 `vasodilatory factors` (如 `progesterone`、`relaxin`、`nitric oxide`) 的作用下，`systemic vascular resistance` (SVR) 顯著下降，導致 `mean arterial pressure` (MAP) 下降約 10 mmHg，並在 `second trimester` 達到 `nadir`，而非上升。
- **(B) 錯誤**：`gestation` 期間 `serum sodium` 下降 4–5 mEq/L (達到約 134–136 mEq/L) 是因為中樞 `reset osmostat` (`osmotic threshold` 下降)，而非 `renal tubule` 流失 `sodium` (`sodium wasting`)。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **Normal Pregnancy vs. Preeclampsia Hemodynamics**：
  - **Normal Pregnancy**：`SVR` 下降、`MAP` 下降 10 mmHg、`GFR` 增加 40–50%、`serum creatinine` 下降至 0.4–0.5 mg/dL。
  - **Preeclampsia**：`SVR` 異常升高、`MAP` 顯著上升、`GFR` 因 `glomerular endotheliosis` 而下降、`serum creatinine` 回升或高於 1.1 mg/dL。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 48 (Pregnancy and Kidney Disease):
  - `Table 48.1: Physiologic Changes in Pregnancy`
  - `Fig 48.1: Changes in mean arterial pressure in normal pregnancy`
  - `Fig 48.4: Effect of pregnancy on glomerular filtration rate (GFR) and effective renal plasma flow (ERPF)`""",

    "q2": """### 1. Answer Determination
正確答案為 **(A)**。

### 2. Mechanism & Rationale
在 `normal pregnancy` 期間，受 `human chorionic gonadotropin (hCG)` 與 `relaxin` 的調控：
- `hypothalamus` 的 `osmotic set point` 下降約 10 mOsm/kg。
- `serum osmolality` 基準點由 `non-pregnant state` 的 ~280 mOsm/kg 下降至 ~270 mOsm/kg。
- 當 `serum osmolality` 低於 270 mOsm/kg 時才抑制 `arginine vasopressin (AVP)` 的釋放，同時 `thirst threshold` 也同步下調。這被稱為 **Reset Osmostat**，導致正常的 `physiological hypotonicity` 與 `physiological hyponatremia` (`serum sodium` 下降 4–5 mEq/L，常介於 133–137 mEq/L)。因此 (A) 為最佳機制解釋。

### 3. Distractor Analysis
- **(D) 錯誤**：`inferior vena cava` 受壓主要影響 `lower extremity venous return` 及引起 `peripheral edema`，並非 `reset osmostat` 造成 `hyponatremia` 與 `hypotonicity` 的主因。
- **(C) 錯誤**：`placenta` 產生的 `vasopressinase` 增加會加速 `AVP` 代謝，在極少數情況下造成 `gestational diabetes insipidus`，臨床表現為 `polyuria` 與 `hypernatremia` / `hyperosmolality`，而非 `asymptomatic physiological hypotonicity`。
- **(B) 錯誤**：`hCG` 並不會抑制 `proximal tubule` 對 `sodium` 與 `bicarbonate` 的 `reabsorption`；`gestation` 期間 `HCO3-` 下降是為了適應 `progesterone` 刺激 `respiratory center` 引發 `hyperventilation` (血中 `pCO2` 下降 10 mmHg) 的代償反應。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **Reset Osmostat vs. SIADH**：
  - **Reset Osmostat**：`serum sodium` 維持在 133–137 mEq/L 之間的微低狀態，且對 `water load` 給予或限制能正常排出 `dilute urine` 與 `concentrated urine`，為正常 `gestational physiology` 變化。
  - **SIADH**：`serum sodium` 進行性下降，`urine osmolality` 異常高於 `serum osmolality`，為病理狀態。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 48 (Pregnancy and Kidney Disease):
  - `Table 48.1: Physiologic Changes in Pregnancy` (Osmolality decreases to a new osmotic set point of ~270 mOsm/kg, Sodium decreases by 4-5 mEq/L)""",

    "q3": """### 1. Answer Determination
正確答案為 **(A)**。

### 2. Mechanism & Rationale
`Preeclampsia` 的核心病理為 `placental vascular remodeling` 不良 (`shallow cytotrophoblast invasion`) 導致 `placental ischemia` 與 `angiogenic imbalance`：
- **Risk / Anti-angiogenic Markers**：`hypoxic placenta` 大量分泌 `soluble fms-like tyrosine kinase-1 (sFlt1)` 與 `soluble endoglin (sEng)` 入 `maternal blood` 中，濃度顯著**升高**。`first trimester` 由 `placenta` 分泌的 `placental protein 13 (PP-13)` 則顯著**降低** (與後續 `preeclampsia` 發生相關)。
- **Protective / Pro-angiogenic Marker**：`Placental growth factor (PlGF)` 在 `healthy pregnancy` 中應保持高濃度；但在 `preeclampsia` 病患中，高濃度的 `sFlt1` 會結合並螯合 `PlGF`，導致血液中 `free PlGF` 濃度顯著**下降**，使 `sFlt1 / PlGF ratio` 大幅升高。因此 (A) 符合正確標記模式。

### 3. Distractor Analysis
- **(B) 錯誤**：標記變化方向完全顛倒。
- **(C) 錯誤**：`PlGF` 與 `PP-13` 為 `pro-angiogenic factors` 或正常 `placental markers`，而非 `anti-angiogenic mediators`。
- **(D) 錯誤**：`sFlt1 / PlGF ratio` 在 `preeclampsia` 發作前數週即顯著**升高** (而非降低)，是臨床極具價值的排除與預測指標 (如 `PROMISS` / `sFlt-1:PlGF ratio` 檢測)。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **sFlt1 vs. PlGF in Clinical Prediction**：
  - **Normal Pregnancy**：`PlGF` 隨 `gestation` 上升，`sFlt1` 低值，`sFlt1/PlGF ratio` 低。
  - **Preeclampsia**：`sFlt1` 暴增，`free PlGF` 被螯合下降，`sFlt1/PlGF ratio` 顯著升高 (> 38 用於 1 週內排除 `preeclampsia`，高比值用於評估 4 週內臨床發作與併發症風險)。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 48 (Pregnancy and Kidney Disease):
  - `Fig 48.8: Placental dysfunction and endothelial dysfunction in the pathogenesis of preeclampsia`
  - `Fig 48.10: Proposed mechanism of soluble fms-like tyrosine kinase-1 (sFlt1)-induced endothelial dysfunction`
  - `Fig 48.11: Concentrations of soluble fms-like tyrosine kinase-1 (sFlt1) in preeclampsia and normal pregnancy`
  - `Fig 48.12: Concentrations of placental growth factor (PlGF) in preeclampsia and normal pregnancy`""",

    "q4": """### 1. Answer Determination
正確答案為 **(C)**。

### 2. Mechanism & Rationale
`sFlt1 (soluble fms-like tyrosine kinase-1)` 是由 `Flt1 (VEGF receptor-1)` 基因 `alternative splicing` 產生的 `soluble extracellular receptor truncated protein`：
- 含有 intact 的 `VEGF` 與 `PlGF` binding `domain`，但缺乏 `transmembrane domain` 與 `intracellular tyrosine kinase domain`。
- 在 `maternal blood` 中過量存在時，`sFlt1` 扮演「分子吸塵器」的角色，大量結合並螯合 `free VEGF` 與 `PlGF` (`sequestration`)。
- 這阻斷了 `endothelial cell surface receptors` 的生理性信號傳導，損害內皮自我修復與存活，在 `kidney` 典型表現為 **Glomerular Endotheliosis** (`glomerular endothelial cell swelling`、`subendothelial space expansion` 及 `capillary lumen occlusion`)，並引發 `proteinuria` 與 `hypertension`。因此 (C) 完全正確。

### 3. Distractor Analysis
- **(D) 錯誤**：`sFlt1` 與 `aldosterone` 無競爭抑制關係，也不會引起 `salt-wasting nephropathy`。
- **(B) 錯誤**：`sFlt1` 阻斷 `VEGF` 信號傳導會導致 `eNOS` 活性**下降**、`NO` 與 `prostacyclin (PGI2)` 減少，從而引起 `vasoconstriction` 而非 `vasodilation`。
- **(A) 錯誤**：`sFlt1` 不會降解 `extracellular matrix`，其導致的是 `spiral artery stenosis` 與高阻力低灌流 (`high resistance and hypoperfusion`)。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **Glomerular Endotheliosis Pathognomonic Feature**:
  - `Preeclampsia` 在 `renal biopsy` 下的特徵性病理變化為 **Glomerular Endotheliosis** (`endothelial intracellular swelling droplets`, `subendothelial deposits`, `podocyte foot processes` 相對保留)，其根本病因為 `sFlt1` 抑制 `VEGF` 引起的 `endothelial injury`。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 48 (Pregnancy and Kidney Disease):
  - `Fig 48.9: Glomerular endotheliosis`
  - `Fig 48.10: Proposed mechanism of soluble fms-like tyrosine kinase-1 (sFlt1)-induced endothelial dysfunction`""",

    "q5": """### 1. Answer Determination
正確答案為 **(D)**。

### 2. Mechanism & Rationale
`end-stage kidney disease` (ESKD) `hemodialysis` 患者懷孕時，處方調整的三大黃金原則為：
1. **Intensive Dialysis**：每週透析時數應大幅提升至 **≥37 小時/週** (甚至 `daily dialysis` 或 `nocturnal dialysis`)，使 `predialysis BUN` 維持在 **< 35–45 mg/dL** 降至接近生理濃度。這能顯著降低 `polyhydramnios` 劑量效應，使 `live birth rate` 提升至 80%–90% 以上。
2. **Hemoglobin Target**：目標控制在 **10–11 g/dL**，防止嚴重 `anemia` 引發 `fetal hypoxia`，同時避免 `ESA` 使用過量引起 `hypertension`。
3. **Gradual Dry Weight Gain**：`second and third trimesters` 應每週循序漸進增加 `dry weight` 約 **0.3–0.5 kg/week**，以包含 `fetus`、`placenta` 與 `amniotic fluid` 的生理成長，避免過度 `ultrafiltration` 致 `maternal intravascular volume depletion` 與 `placental hypoperfusion`。因此 (D) 完全正確。

### 3. Distractor Analysis
- **(C) 錯誤**：減少 `dialysis frequency` 會使 `BUN` 積聚 (> 80 mg/dL)，嚴重損害 `fetal outcome`，增加 `intrauterine fetal demise` 與 `extreme prematurity` 風險。
- **(A) 錯誤**：維持嚴格靜止的 `dry weight` 會忽略 `gestation` 期間 `fetus` 與 `uterus` 的重量增長，導致臨床 `over-ultrafiltration` 與 `fetal growth restriction`。
- **(B) 錯誤**：`hemoglobin` 目標為 10–11 g/dL；過高 (`Hb > 14 g/dL`) 會增加 `blood viscosity`、`thrombosis` 與 `maternal hypertension` 發作。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **Dialysis Prescription in Pregnancy High-Yield Summary**：
  - **Weekly Duration**：`≥37 hours/week` (6-7 sessions/week nocturnal or long daily).
  - **BUN Goal**：`< 35-45 mg/dL` (predialysis).
  - **Hb Goal**：`10-11 g/dL`.
  - **Dry Weight Adjustment**：`+ 0.3-0.5 kg/week` in 2nd/3rd trimesters.
  - **Dialysate Calcium & Potassium**：適當調整以防止 `hypocalcemia` 或 `hypokalemia`。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 48 (Pregnancy and Kidney Disease):
  - `Fig 48.14: Antenatal care in women with chronic kidney disease`
  - `Section: End-Stage Kidney Disease and Dialysis in Pregnancy`""",

    "q6": """### 1. Answer Determination
正確答案為 **(C)**。

### 2. Mechanism & Rationale
對於 `kidney transplantation` 後擬懷孕的女性患者：
- **Mycophenolate Mofetil (MMF / MPA)** 具有強烈的 `teratogenicity` (`teratogenic`)，可導致耳部、面部、心臟及肢體等 `congenital malformations` 與 `early spontaneous abortion`。
- 指引規範在受孕前必須提前**停用 MMF**，並轉換為安全的替代 `immunosuppressants` 如 **Azathioprine** (且通常於受孕前至少 6 週完成換藥並監測 `graft function` 與 `drug concentration`)。
- **Tacrolimus** 與 **Prednisone** 在 `gestation` 期間相對安全，但因孕期 `volume expansion` 與 `increased metabolism`，需頻繁監測 `tacrolimus trough level` 並調整劑量。因此 (C) 完全原則與建議一致。

### 3. Distractor Analysis
- **(B) 錯誤**：完全停用 `immunosuppressants` 會引發嚴重的 `acute graft rejection` (`acute rejection`)，可致 `graft loss` 與 `maternal life-threatening risk`。
- **(A) 錯誤**：`MMF` 為 `gestation` 期間極高風險 `contraindicated medication`，與 `tacrolimus` 濃度低否無關。
- **(D) 錯誤**：`kidney transplant recipient` 若移植已滿 1–2 年、`graft function` 穩定 (`serum creatinine < 1.5 mg/dL`)、無顯著 `proteinuria` 與 `hypertension`，且藥物已調整為安全處方，可以安全懷孕。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **Immunosuppressives Safety Category in Pregnancy**：
  - **Safe**：`Prednisone`, `Azathioprine` (< 2 mg/kg/day), `Tacrolimus`, `Cyclosporine` (須常規追蹤 `trough level`)。
  - **Contraindicated / Teratogenic**：`Mycophenolate Mofetil (MMF)`, `Mycophenolic Acid (MPA)`, `Sirolimus / Everolimus (mTOR inhibitors)`。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 48 (Pregnancy and Kidney Disease):
  - `Table 48.7: Immunosuppressive Medications in Pregnancy` (Mycophenolate mofetil is contraindicated in pregnancy; Azathioprine considered safe)
  - `Fig 48.15: Pregnancies in kidney transplant recipients worldwide`""",

    "q7": """### 1. Answer Determination
正確答案為 **(C)**。

### 2. Mechanism & Rationale
在 **nephrotic syndrome** 所致的 **hypoalbuminemia** 患者中，使用 **furosemide** 等 **loop diuretics** 產生 **diuretic resistance** 的核心機轉如下：
1. **Intravascular Delivery Deficit**：**Furosemide** 在 `plasma` 中高達 95–99% 與 **albumin** 結合。`plasma protein` 降低時，有效輸送至 `kidney` 的藥物總量減少，且過濾至 **proximal tubule** 外的 **furosemide** `volume of distribution` 擴大，導致到達 **basolateral membrane** 之 **organic anion transporters (OAT1/OAT3)** 的藥物量不足。
2. **Luminal Protein Binding**：**Nephrotic syndrome** 患者在 **glomerular filtration barrier** 嚴重受損下，大量 **albumin** 漏出至 **tubular lumen** 內。自 **basolateral OAT** 分泌進 **tubular lumen** 的 **furosemide**，在 **tubular lumen** 內與漏出的 **albumin** 發生強烈結合，形成 **furosemide-albumin complex**。此結合態的 **furosemide** 無法作用於 **thick ascending limb (TAL)** 的 **NKCC2 (Na-K-2Cl cotransporter)**，導致藥效被大幅中和，呈現 **diuretic resistance**。因此 (C) 為最核心與具體之機制解析。

### 3. Distractor Analysis
- **(B) 錯誤**：**Furosemide** 主要是經由 **basolateral OAT1/OAT3** 分泌進入 **tubular lumen**，而非被 **proximal tubule** 嚴重 `reabsorption`。
- **(D) 錯誤**：**Hypoalbuminemia** 並不會導致 **furosemide** 在 **S1 segment** 發生 `accelerated metabolic degradation`。
- **(A) 錯誤**：**Albumin** 係促進 **furosemide** 輸送至 **OAT**，並非 **OAT1/OAT3** 的抑制劑，**hypoalbuminemia** 不會使 **luminal secretion** 增加。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **Furosemide Secretion & Binding Site**：作用點在 **luminal side** 的 **NKCC2**。必定先經由 **basolateral OAT1/OAT3** 分泌至 **tubular lumen**。
- **Hypoalbuminemia in Nephrotic Syndrome**：若使用 **furosemide** 效果不佳，臨床可考量將 **furosemide** 與 **hyperoncotic albumin (20%)** `intravenous co-infusion`，以提升 **intravascular binding** 與 **renal blood flow** 輸送，但最根本關鍵仍為克服 **luminal protein binding** 與 **distal reabsorption**。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 50: "Diuretics" -> Section: "Pharmacokinetics of Loop Diuretics" & "Diuretic Resistance in Nephrotic Syndrome".""",

    "q8": """### 1. Answer Determination
正確答案為 **(A)**。

### 2. Mechanism & Rationale
**Diuretic Braking Phenomenon** 是指長期或連續使用 **loop diuretics** 後，隨著 `volume depletion` 與 **distal sodium delivery** 增加，引發 **distal convoluted tubule (DCT)** 與 **collecting duct** 發生結構性 **hypertrophy** 與 **hyperplasia**，同時活化 **RAAS** 與 **sympathetic nervous system**，導致 **distal tubule** 對 `sodium` 的 `reabsorption` 顯著增強，抵銷了 **loop diuretic** 的 `diuretic effect`。
應對 **braking phenomenon** 與 **diuretic resistance** 的標準核心策略包括：
1. **Sequential Nephron Blockade**：併用 **thiazide** 或 **thiazide-like diuretics** (如 **metolazone**, **chlorothiazide**)，抑制肥大的 **DCT** 之 **NCC cotransporter**。
2. **Strict Dietary Sodium Restriction**：防止利尿劑藥效過去後的 **post-diuretic sodium retention**。
3. **Correction of Metabolic Acidosis**：**Metabolic acidosis** 會降低 **OAT** 的轉運效率，矯正 **metabolic acidosis** 可恢復 **furosemide** 的 **luminal secretion** 效率。因此 (A) 為最適當處置。

### 3. Distractor Analysis
- **(B) 錯誤**：增加 `high-sodium diet` 會提供大量 `sodium` 供 **distal tubule** `reabsorption`，完全破壞 `negative sodium balance`。
- **(C) 錯誤**：**NSAIDs** (如 indomethacin) 會抑制腎臟 **prostaglandins (PGE2/PGI2)** 產生的 `vasodilatory effect`，並競爭 **OAT1/OAT3** `transporters`，進而**降低** **furosemide** 的 **luminal secretion** 與 `diuretic effect`，嚴禁用於解救 **diuretic resistance**。
- **(D) 錯誤**：`oral` **furosemide** `bioavailability` 平均僅約 50%，且在 `heart failure` `intestinal edema` 時吸收更差，將 `intravenous dose` 改為半量 `oral` 會嚴重惡化 `diuretic effect`。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **Braking Phenomenon vs. True Diuretic Resistance**：Braking 是 `normal physiological compensatory mechanism` (避免過度 `dehydration`)；當產生病理阻抗時，首選 **Combination Diuretic Therapy (Metolazone + Loop Diuretic)**。
- **NSAIDs Impact on Diuretics**：**NSAIDs** 是引發 **loop diuretic resistance** 的常見外因性藥物。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 50: "Diuretics" -> Section: "Diuretic Resistance and the Braking Phenomenon" (Fig. 50.10).""",

    "q9": """### 1. Answer Determination
正確答案為 **(B)**。

### 2. Mechanism & Rationale
**Thiazide-Induced Hyponatremia (TIH)** 的臨床與生理學特徵如下：
1. **Rapid Onset**：典型 TIH 多發生於開始服藥或增加劑量的 **within 14 days**。
2. **Weight Gain & Water Retention**：臨床上 TIH 患者的表型常類似 **SIADH** (euvolemic / mild hypervolemic)，常伴隨 **body weight gain**，此乃因為 **Thiazides** 抑制 **cortical diluting segment** 的 **NCC**，損害了 `kidney` 排出 `dilute urine` (**free water excretion**) 的能力，但保留了 **medullary concentrating ability**，導致 `water retention` 於體內。因此 (B) 陳述完全正確。

### 3. Distractor Analysis
- **(A) 錯誤**：TIH 主要非極度 **hypovolemic volume depletion**，臨床常伴隨 **body weight gain** 與 **free water retention**，非純粹大量 `sodium loss` 導致的 `weight loss`。
- **(C) 錯誤**：部分 TIH 患者的 `serum` **AVP** 確實未被適當抑制，但最新研究證實 TIH 亦可透過 **SLCO2A1 / PGT** 與 **PGE2** 途徑，發生 **AVP-independent** 的 **AQP2** `water reabsorption`，非所有患者 AVP 皆被完全抑制。
- **(D) 錯誤**：TIH 發病於用藥 **within 14 days**，非 6 個月以上的長期慢沉澱。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **Thiazide vs. Loop Diuretic in Hyponatremia**：**Loop diuretics** 破壞 **medullary hypertonic gradient**，同時損害 **concentrating and diluting capacity**，故較少引起 **severe hyponatremia**；**Thiazides** 僅損害 **diluting capacity** (cortical TAL/DCT) 而保留 **medullary concentrating capacity**，極易引起嚴重 **hyponatremia**。
- **Clinical Presentation of TIH**：老年女性、低 BMI、高齡為 `high-risk population`，多數呈現體重微幅增加之 **euvolemic hyponatremia**。

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 15: "Disorders of Water Balance" -> Section: "Drug-Induced Hyponatremia: Thiazides".""",

    "q10": """### 1. Answer Determination
正確答案為 **(C)**。

### 2. Mechanism & Rationale
**SLCO2A1** 基因編碼 **solute carrier organic anion transporter family member 2A1**，亦即 **prostaglandin transporter (PGT)**。
1. **PGT Function & Mutation**：**PGT** 負責細胞對 **Prostaglandin E2 (PGE2)** 的攝取與清除。當 **SLCO2A1** 基因發生 **single nucleotide polymorphism (SNP) / loss of function** 時，**PGT** 功能受損，導致 **PGE2** 的 `cellular uptake` 與 `metabolic clearance rate` 下降，進而使 **urinary PGE2** 濃度顯著升高。
2. **AVP-Independent AQP2 Trafficking**：`luminal` 與組織中升高的 **PGE2** 作用於 **collecting duct principal cells** 的 **EP2 / EP4 receptors**，刺激 **Aquaporin-2 (AQP2)** 穿膜並翻轉移位至 **apical membrane**，在 **AVP-independent** 的情況下大大增加了 `water reabsorption`，從而誘發極嚴重的 **hyponatremia**。因此 (C) 為精準正確之機制解析。

### 3. Distractor Analysis
- **(A) 錯誤**：**SLCO2A1** 變異是減弱 **PGE2** 的清除與攝取，導致 `extracellular` 與 `urinary` **PGE2 升高**，非減少產量。
- **(B) 錯誤**：**NCC** 係由 **SLC12A3** 基因編碼，非 **SLCO2A1**。
- **(D) 錯誤**：**SLCO2A1** 編碼的是 **prostaglandin transporter (PGT)**，非 **V2 receptor**。

### 4. Exam Differential Diagnosis & High-Yield Comparisons
- **SLCO2A1 & TIH Key High-Yield Summary**：
  - Gene: `SLCO2A1` (encodes PGT)
  - Biomarker: Urinary PGE2 升高
  - Mechanism: AVP-independent AQP2 apical trafficking
  - Timing: 用藥 2 週內發生
  - Phenotype: `weight gain / fluid retention`

### 5. Citations & References
- *Brenner & Rector's The Kidney, 11th Edition*, Chapter 15: "Disorders of Water Balance" -> Section: "Genetics of Thiazide-Induced Hyponatremia (SLCO2A1/PGT)"."""
}

for q in data:
    qid = q['id']
    if qid in normalized_explanations:
        q['sourceExplanation'] = normalized_explanations[qid]

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved output to", output_path)

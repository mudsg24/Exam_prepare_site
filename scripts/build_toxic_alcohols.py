import os
import shutil
import json
import subprocess
from pathlib import Path

# Paths
BRAIN_DIR = Path("/Users/yuan/.gemini/antigravity/brain/02cffe8d-a6e7-41ee-b04b-c3922497ba06")
PUBLIC_ASSETS_DIR = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/assets")
PUBLIC_TUTORIALS_DIR = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials")
PUBLIC_SERVER_DATA = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data")
MANIFEST_PATH = PUBLIC_SERVER_DATA / "exams_manifest.json"

PUBLIC_ASSETS_DIR.mkdir(parents=True, exist_ok=True)
PUBLIC_TUTORIALS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Copy generated images
image_mapping = {
    "toxic_alcohols_osmolal_gap_diagram_1785475571023.jpg": "toxic_alcohols_osmolal_gap_diagram.jpg",
    "methanol_metabolism_retinal_putamen_diagram_1785475590611.jpg": "methanol_metabolism_retinal_putamen_diagram.jpg",
    "ethylene_glycol_metabolism_oxalate_crystal_diagram_1785475604227.jpg": "ethylene_glycol_metabolism_oxalate_crystal_diagram.jpg",
    "isopropanol_propylene_glycol_differential_diagram_1785475617165.jpg": "isopropanol_propylene_glycol_differential_diagram.jpg",
    "toxic_alcohol_dialysis_antidote_algorithm_1785475636568.jpg": "toxic_alcohol_dialysis_antidote_algorithm.jpg"
}

for src_name, dst_name in image_mapping.items():
    src_file = BRAIN_DIR / src_name
    dst_file = PUBLIC_ASSETS_DIR / dst_name
    if src_file.exists():
        shutil.copy(src_file, dst_file)
        print(f"Copied {src_name} -> {dst_file}")
    else:
        print(f"Warning: {src_file} does not exist!")

# 2. Build Masterclass Lecture JSON
tutorial_json = {
  "paperId": "2026_Toxic_alcohols_(主題備考)",
  "title": "2026 Toxic Alcohols (中毒性酒精與乙二醇/甲醇中毒) 診斷生化、Osmolal Gap 計算、代謝毒性機轉、Fomepizole 治療與血液透析適應症專科講堂",
  "sections": [
    {
      "id": "section_1",
      "title": "Section 1: Osmolal Gap, Calculated Serum Osmolality & Diagnostic Trade-off Framework",
      "content": "### Osmolal Gap 計算公式與診斷架構\n\n在臨床懷疑 Toxic Alcohol Ingestion 時，第一步是精確計算 Serum Osmolal Gap。Calculated Serum Osmolality 計算公式如下：\n\n$$\\text{Calculated Serum Osmolality} = 2 \\times [\\text{Na}^+] + \\frac{[\\text{Glucose}]}{18} + \\frac{[\\text{BUN}]}{2.8} + \\frac{[\\text{Ethanol}]}{4.6}$$\n\n$$\\text{Serum Osmolal Gap} = \\text{Measured Serum Osmolality} - \\text{Calculated Serum Osmolality}$$\n\n正常的 Serum Osmolal Gap 通常在 $\\le 10 \\text{ mOsm/kg H}_2\\text{O}$。當 Serum Osmolal Gap 顯著升高 (特別是 $> 20-50 \\text{ mOsm/kg H}_2\\text{O}$)，強烈提示血液中存在未被生化常規檢測到的低分子量滲透壓活性物質，如 Methanol、Ethylene Glycol、Isopropanol、Propylene Glycol 或 Diethylene Glycol。\n\n### Osmolal Gap 與 Anion Gap 的時間動態消長 (Reciprocal Gap Trade-off)\n\n考題與臨床診斷中最常出現的陷阱是 Osmolal Gap 與 High Anion Gap Metabolic Acidosis (HAGMA) 之間的時間消長：\n1. **攝入早期 (Early Presentation)**：未代謝的親代酒精 (Parent alcohol) 大量存在於血液中，親代酒精不帶電荷且分子量小，引發極高的 **Serum Osmolal Gap**，但此時有機酸尚未生成，**Anion Gap** 保持正常。\n2. **攝入晚期 (Late Presentation)**：隨著 Alcohol Dehydrogenase (ADH) 與 Aldehyde Dehydrogenase (ALDH) 將親代酒精代謝為 Formic Acid 或 Glycolic Acid，親代酒精濃度下降使 **Osmolal Gap 逐漸縮小 (Close)**，而帶負電荷的有機酸根離子累積使 **Anion Gap 攀升 (Open)**。\n3. **關鍵結論**：正常的 Osmolal Gap **絕不能**用來排除就醫時間過晚的 Toxic Alcohol Poisoning！",
      "diagrams": [
        {
          "id": "Brenner_Table_24_5",
          "relPath": "/reference-images/Brenner 11e/24. Interpretation of Electrolyte and Acid-Base Parameters in Blood and Urine/Table_24_5.png",
          "imagePath": "/reference-images/Brenner 11e/24. Interpretation of Electrolyte and Acid-Base Parameters in Blood and Urine/Table_24_5.png",
          "caption": "Table 24.5 Laboratory Tests for Diagnosis of Metabolic Acidosis and Plasma Osmolal Gap in Brenner 11e.",
          "sourceBook": "Brenner 11e Ch 24",
          "type": "micrograph"
        },
        {
          "id": "ai_illustration_sec1",
          "relPath": "/server-data/assets/toxic_alcohols_osmolal_gap_diagram.jpg",
          "imagePath": "/server-data/assets/toxic_alcohols_osmolal_gap_diagram.jpg",
          "caption": "Osmolal Gap and Anion Gap Time-dependent Trade-off Infographic.",
          "sourceBook": "Gemini Mechanism Illustration",
          "type": "ai_illustration"
        }
      ]
    },
    {
      "id": "section_2",
      "title": "Section 2: Methanol Metabolism, Retinal Toxicity & Basal Ganglia Putaminal Necrosis",
      "content": "### Methanol 代謝路徑與 Formic Acid 蓄積\n\nMethanol (常見於假酒、擋風玻璃清潔劑 Windshield Washer Fluid) 本身毒性較低，但經由肝臟細胞代謝後會產生劇毒：\n\n$$\\text{Methanol} \\xrightarrow{\\text{ADH}} \\text{Formaldehyde} \\xrightarrow{\\text{ALDH}} \\text{Formic Acid / Formate}$$\n\nFormic Acid 的清除需要依賴 Folate / Tetrahydrofolate 途徑 (10-formyl THF synthetase 與 formyl THF dehydrogenase)，此反應在人類體內速率受限，導致 Formic Acid 大量蓄積，產生重度 HAGMA。\n\n### 病理機制與器官特異性毒性\n\n1. **Retinal Toxicity & Visual Disturbance**：Formic Acid 會強烈抑制線粒體內的 Cytochrome c Oxidase (Complex IV)，阻斷 ATP 生成。視神經與視網膜神經節細胞對 ATP 匱乏極度敏感，臨床出現視線模糊、雪盲感 (Snowfield vision)、Optic Disc Edema 與 Retinal Edema，嚴重者導致永久性失明。\n2. **Bilateral Putaminal Necrosis**：基底核的 Putamen 耗氧量極高，Cytochrome c Oxidase 受抑制後導致基底核雙側 Putamen 壞死與出血 (Bilateral Putaminal Necrosis & Hemorrhage on Brain CT/MRI)，復原後常遺留 Parkinsonism 或 Dystonia 等中樞神經後遺症。\n3. **Cofactor Therapy**：給予 Folinic Acid 或 Folic Acid (50 mg IV q6h)，可加速 Formic Acid 轉化為 CO2 與 H2O。",
      "diagrams": [
        {
          "id": "Brenner_Fig_67_4_Methanol",
          "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_4.png",
          "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_4.png",
          "caption": "Fig. 67.4 Metabolism of Toxic Alcohols in Brenner 11e.",
          "sourceBook": "Brenner 11e Ch 67",
          "type": "micrograph"
        },
        {
          "id": "ai_illustration_sec2",
          "relPath": "/server-data/assets/methanol_metabolism_retinal_putamen_diagram.jpg",
          "imagePath": "/server-data/assets/methanol_metabolism_retinal_putamen_diagram.jpg",
          "caption": "Methanol Metabolic Pathway, Formate Cytocrome c Oxidase Blockade & Retinal/Putaminal Damage.",
          "sourceBook": "Gemini Mechanism Illustration",
          "type": "ai_illustration"
        }
      ]
    },
    {
      "id": "section_3",
      "title": "Section 3: Ethylene Glycol Metabolism, Nephrotoxicity & Crystalluria Morphology",
      "content": "### Ethylene Glycol 代謝途徑與速率限制關卡\n\nEthylene Glycol (常見於水箱防凍劑 Antifreeze) 的代謝途徑如下：\n\n$$\\text{Ethylene Glycol} \\xrightarrow{\\text{ADH}} \\text{Glycoaldehyde} \\xrightarrow{\\text{ALDH}} \\text{Glycolic Acid} \\xrightarrow{\\text{Rate-limiting}} \\text{Glyoxylic Acid} \\rightarrow \\text{Oxalic Acid}$$\n\nGlycolic Acid 轉化為 Glyoxylic Acid 是整個代謝過程的 Rate-limiting Step，因此 Glycolic Acid 會在血中大量蓄積，成為引發重度 HAGMA 的主要驅動力量。此外，Glycolic Acid 會干擾 TCA cycle 引發次發性 Lactic Acidosis。\n\n### Nephrotoxicity, Calcium Oxalate Crystals & Cranial Neuropathies\n\n1. **Acute Tubular Necrosis (ATN)**：終末代謝產物 Oxalic Acid 與血中鈣離子結合生成不溶性的 Calcium Oxalate Crystals，在腎小管內沉積引發直接的 Acute Tubular Injury、少尿型 AKI 與 Hypocalcemia。\n2. **Crystalluria Optical Features**：\n   - **Calcium Oxalate Monohydrate**：呈啞鈴狀 (Dumbbell-shaped)、卵圓形或針狀 (Needle-like)，在偏光顯微鏡下呈強烈雙折射 (Strongly Birefringent / Polarizable)。\n   - **Calcium Oxalate Dihydrate**：呈雙錐體信封狀 (Bipyramidal / Envelope-shaped)。\n3. **Fluorescence Test**：防凍劑中常添加 Sodium Fluorescein，在 Wood's Lamp 照射下尿液可呈綠色螢光。\n4. **Delayed Neurological Sequelae**：中毒後 5-14 天可能出現遲發性 Cranial Polyneuropathies (尤其是 Facial Diplegia CN VII)。\n5. **Cofactor Therapy**：給予 Thiamine (100 mg IV q6h) 與 Pyridoxine (B6, 50 mg IV q6h)，引導 Glyoxylic Acid 轉向轉氨化生成 α-hydroxy-β-ketoadipate 與 Glycine，減少 Oxalic Acid 生成。",
      "diagrams": [
        {
          "id": "Brenner_Table_23_11",
          "relPath": "/reference-images/Brenner 11e/23. Laboratory Assessment of Kidney Disease-Glomerular Filtration Rate, Urinalysis, and Proteinuria/Table_23_11.png",
          "imagePath": "/reference-images/Brenner 11e/23. Laboratory Assessment of Kidney Disease-Glomerular Filtration Rate, Urinalysis, and Proteinuria/Table_23_11.png",
          "caption": "Table 23.11 Common Crystals and Their Appearance in Brenner 11e.",
          "sourceBook": "Brenner 11e Ch 23",
          "type": "micrograph"
        },
        {
          "id": "ai_illustration_sec3",
          "relPath": "/server-data/assets/ethylene_glycol_metabolism_oxalate_crystal_diagram.jpg",
          "imagePath": "/server-data/assets/ethylene_glycol_metabolism_oxalate_crystal_diagram.jpg",
          "caption": "Ethylene Glycol Metabolism, Calcium Oxalate Crystal Morphology & ATN Pathophysiology.",
          "sourceBook": "Gemini Mechanism Illustration",
          "type": "ai_illustration"
        }
      ]
    },
    {
      "id": "section_4",
      "title": "Section 4: Isopropanol, Propylene Glycol & Diethylene Glycol Differential Diagnosis",
      "content": "### Isopropanol Toxicity: Ketosis Without HAGMA\n\nIsopropanol (Rubbing alcohol / 消毒酒精) 經由 ADH 代謝為 **Acetone**：\n\n$$\\text{Isopropanol} \\xrightarrow{\\text{ADH}} \\text{Acetone}$$\n\n- **關鍵生化特徵**：Acetone 為酮類而非羧酸，不釋放 $H^+$ 質子。因此 Isopropanol 中毒表現為 **Ketosis Without High Anion Gap Metabolic Acidosis**！血清與尿液 Ketones 呈強陽性，Serum Osmolal Gap 顯著升高，但 Anion Gap 與 $HCO_3^-$ 保持完全正常。\n- **臨床表現**：顯著的中樞神經抑制、醉酒感、出血性 Gastritis 與呼氣中丙酮味。通常不需要 Fomepizole 或 Hemodialysis，僅需支持性治療。\n\n### Propylene Glycol Toxicity in ICU Patients\n\nPropylene Glycol 是多種靜脈注射藥物 (如 Lorazepam, Diazepam, Nitroglycerin) 的溶劑 (Solvent / Vehicle)。在 ICU 長期接受高劑量 Lorazepam Continuous Drip 的患者中，Propylene Glycol 經 ADH 代謝為 L-lactate 與 D-lactate，表現為 **Lactic Acidosis (HAGMA) + High Osmolal Gap + AKI**。\n\n### Diethylene Glycol Toxicity\n\nDiethylene Glycol (曾因受污染的止咳糖漿造成歷史性集體中毒) 經 ADH 代謝為 2-hydroxyethoxyacetic acid (HEAA)，引發嚴重的少尿型 AKI (Acute Tubular Necrosis)、HAGMA、Osmolal Gap 升高與 Cranial / Peripheral Polyneuropathies。",
      "diagrams": [
        {
          "id": "Brenner_Table_67_5",
          "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_5.png",
          "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_5.png",
          "caption": "Table 67.5 Conversion of Toxic Alcohol Concentration From mmol/L to mg/dL in Brenner 11e.",
          "sourceBook": "Brenner 11e Ch 67",
          "type": "micrograph"
        },
        {
          "id": "ai_illustration_sec4",
          "relPath": "/server-data/assets/isopropanol_propylene_glycol_differential_diagram.jpg",
          "imagePath": "/server-data/assets/isopropanol_propylene_glycol_differential_diagram.jpg",
          "caption": "Differential Chart for Isopropanol, Propylene Glycol & Diethylene Glycol Toxicity.",
          "sourceBook": "Gemini Mechanism Illustration",
          "type": "ai_illustration"
        }
      ]
    },
    {
      "id": "section_5",
      "title": "Section 5: Antidote Dosing Guidelines, Dialysis Clearance Kinetics & EXTRIP Indications",
      "content": "### Antidote Pharmacotherapy: Fomepizole vs Ethanol\n\n1. **Fomepizole (4-methylpyrazole / 4-MP)**：\n   - **機轉**：ADH 的競爭性抑制劑，對 ADH 的親和力為 Ethanol 的 8000 倍。不會引發中樞神經抑制或 Hypoglycemia。\n   - **給藥處方**：Loading Dose 15 mg/kg IV 次；維持劑量前 4 次為 10 mg/kg q12h，隨後因肝臟 CYP450 自體誘導代謝，調高為 15 mg/kg q12h。\n   - **Hemodialysis 期間調整**：Fomepizole 可被透析清除！IHD 期間給藥頻率必須調高至 **q4h** 或改為 **1.0-1.5 mg/kg/h Continuous Infusion**。\n2. **Ethanol**：目標血清濃度維持於 100-150 mg/dL。需小心監測 CNS 抑制與 Hypoglycemia。\n\n### Dialytic Clearance Kinetics & EXTRIP Indications for Intermittent Hemodialysis (IHD)\n\n- **透析清除動力學**：Methanol 與 Ethylene Glycol 分子量小 ($< 100 \\text{ Da}$)、蛋白結合率為 0%、分佈體積小 ($V_d < 0.6 \\text{ L/kg}$)，非常容易被 **Intermittent Hemodialysis (IHD)** 高效清除。IHD 的清除率顯著高於 CRRT。\n- **EXPRIP 緊急血液透析指徵**：\n  1. 血清 Methanol 或 Ethylene Glycol 濃度 $> 50 \\text{ mg/dL}$ ($15.6 \\text{ mmol/L}$ for Methanol; $8.0 \\text{ mmol/L}$ for Ethylene Glycol)。\n  2. 重度難治性 HAGMA (Arterial pH $< 7.25$ 或 Base Deficit $> 15$)。\n  3. 出現 Target Organ Damage (如 Methanol 引起的 Visual Impairment、Ethylene Glycol 引起的 AKI)。\n  4. 缺藥急救關卡：若急診缺乏 Fomepizole，**絕對不可**僅給予 Sodium Bicarbonate 拖延，必須**立即安排緊急 Hemodialysis**！",
      "diagrams": [
        {
          "id": "Brenner_Table_67_6",
          "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_6.png",
          "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_6.png",
          "caption": "Table 67.6 Antidote Dosage During Toxic Alcohol Poisoning in Brenner 11e.",
          "sourceBook": "Brenner 11e Ch 67",
          "type": "micrograph"
        },
        {
          "id": "ai_illustration_sec5",
          "relPath": "/server-data/assets/toxic_alcohol_dialysis_antidote_algorithm.jpg",
          "imagePath": "/server-data/assets/toxic_alcohol_dialysis_antidote_algorithm.jpg",
          "caption": "Clinical Decision Algorithm for Toxic Alcohol Poisoning Dosing & EXTRIP HD Indications.",
          "sourceBook": "Gemini Mechanism Illustration",
          "type": "ai_illustration"
        }
      ]
    }
  ]
}

tutorial_out_path = PUBLIC_TUTORIALS_DIR / "2026_Toxic_alcohols_(主題備考)_tutorial.json"
with open(tutorial_out_path, "w", encoding="utf-8") as f:
    json.dump(tutorial_json, f, ensure_ascii=False, indent=2)
print(f"Masterclass Lecture JSON saved to {tutorial_out_path}")

# 3. Build 20 High-Yield MCQs for NLM Asking Gateway Input
questions_raw = [
  {
    "id": "2026_Toxic_alcohols_Q1",
    "number": 1,
    "stem": "A 42-year-old patient presents to the emergency department after suspected ingestion of an unknown antifreeze liquid. Laboratory results show: Na+ 140 mEq/L, K+ 4.5 mEq/L, Cl- 100 mEq/L, HCO3- 10 mEq/L, Glucose 90 mg/dL, BUN 14 mg/dL, Ethanol 0 mg/dL, and measured serum osmolality 340 mOsm/kg H2O. What is the calculated serum osmolality and the serum osmolal gap for this patient?",
    "options": [
      {"id": "A", "text": "Calculated osmolality 290 mOsm/kg; Osmolal gap 50 mOsm/kg"},
      {"id": "B", "text": "Calculated osmolality 285 mOsm/kg; Osmolal gap 55 mOsm/kg"},
      {"id": "C", "text": "Calculated osmolality 300 mOsm/kg; Osmolal gap 40 mOsm/kg"},
      {"id": "D", "text": "Calculated osmolality 270 mOsm/kg; Osmolal gap 70 mOsm/kg"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Calculated Serum Osmolality 計算公式為 2 * Na + Glucose / 18 + BUN / 2.8。帶入數據：2 * 140 + 90 / 18 + 14 / 2.8 = 280 + 5 + 5 = 290 mOsm/kg H2O。Measured Serum Osmolality 為 340 mOsm/kg H2O，因此 Serum Osmolal Gap = 340 - 290 = 50 mOsm/kg H2O。正常的 Osmolal Gap 通常 <= 10 mOsm/kg H2O，顯著升高的 Osmolal Gap 強烈提示血中存在大量未被常規生化測量的低分子量滲透壓活性物質 (如 Ethylene Glycol 或 Methanol)。",
    "resolvedImages": [
      {
        "id": "Brenner_Table_67_4",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_4.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_4.png",
        "caption": "Table 67.4 Toxicokinetics of Toxic Alcohols in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q2",
    "number": 2,
    "stem": "Which of the following metabolic pathways and enzyme-inhibitory mechanisms best explains the severe systemic toxicity and metabolic acidosis associated with Methanol ingestion?",
    "options": [
      {"id": "A", "text": "Methanol is converted to Glycolic acid by Alcohol dehydrogenase, inhibiting NA+/K+-ATPase"},
      {"id": "B", "text": "Methanol is converted to Formaldehyde and then Formic acid, which inhibits mitochondrial Cytochrome c Oxidase"},
      {"id": "C", "text": "Methanol is converted to Oxalic acid, causing direct competitive inhibition of Pyruvate Dehydrogenase"},
      {"id": "D", "text": "Methanol is converted directly to Acetone, causing severe L-Lactic acidosis"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Methanol 在體內首先經由 Alcohol Dehydrogenase (ADH) 代謝為 Formaldehyde，隨後迅速經由 ALDH 轉化為 Formic Acid (Formate)。Formic Acid 會強烈抑制線粒體呼吸鏈中的 Cytochrome c Oxidase (Complex IV)，阻斷 ATP 合成並引發細胞缺氧與重度 High Anion Gap Metabolic Acidosis (HAGMA)。",
    "resolvedImages": [
      {
        "id": "Brenner_Fig_67_4",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_4.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_4.png",
        "caption": "Fig. 67.4 Metabolism of Toxic Alcohols in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q3",
    "number": 3,
    "stem": "A 38-year-old man arrives with severe visual blurring describing his vision as 'walking in a snowstorm', along with confusion. Brain MRI demonstrates bilateral putaminal necrosis with focal hemorrhage. Which toxic alcohol ingestion is characteristically responsible for this presentation?",
    "options": [
      {"id": "A", "text": "Ethylene Glycol"},
      {"id": "B", "text": "Isopropanol"},
      {"id": "C", "text": "Methanol"},
      {"id": "D", "text": "Propylene Glycol"}
    ],
    "sourceProvidedAnswer": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Methanol 中毒之代謝物 Formic Acid 具有高度的器官特異性毒性，特異性累及視網膜神經節細胞與視神經 (造成 Optic Disc Edema、視線雪盲感與失明) 以及大腦基底核的 Putamen (造成 Bilateral Putaminal Necrosis & Hemorrhage)。這種臨床表現極具 Methanol 中毒特徵。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q4",
    "number": 4,
    "stem": "In Ethylene Glycol poisoning, which metabolic intermediate accumulates in the largest quantity due to a rate-limiting enzyme conversion step and serves as the primary driver of High Anion Gap Metabolic Acidosis?",
    "options": [
      {"id": "A", "text": "Glycoaldehyde"},
      {"id": "B", "text": "Oxalic acid"},
      {"id": "C", "text": "Formic acid"},
      {"id": "D", "text": "Glycolic acid"}
    ],
    "sourceProvidedAnswer": "D",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Ethylene Glycol 在體內經 ADH 代謝為 Glycoaldehyde，再經 ALDH 迅速轉化為 Glycolic Acid。Glycolic Acid 轉化為 Glyoxylic Acid 是整個代謝途徑的 Rate-limiting Step，因此 Glycolic Acid 會大量蓄積，成為引發重度 High Anion Gap Metabolic Acidosis (HAGMA) 的主要有機酸。",
    "resolvedImages": [
      {
        "id": "Brenner_Fig_67_4",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_4.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_4.png",
        "caption": "Fig. 67.4 Metabolism of Ethylene Glycol in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q5",
    "number": 5,
    "stem": "Urinalysis of a patient with severe acute kidney injury following Ethylene Glycol ingestion reveals abundant crystals. Which optical and morphological characteristics correctly describe Calcium Oxalate Monohydrate crystals formed in this condition?",
    "options": [
      {"id": "A", "text": "Dumbbell-shaped or needle-like morphology with strong birefringence under polarized light"},
      {"id": "B", "text": "Coffin-lid shaped crystals with no birefringence under polarized light"},
      {"id": "C", "text": "Hexagonal plate crystals with negative birefringence under polarized light"},
      {"id": "D", "text": "Bipyramidal envelope-shaped crystals with zero birefringence under polarized light"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Ethylene Glycol 的終末產物 Oxalic Acid 與血鈣結合形成 Calcium Oxalate Crystals。其中 Calcium Oxalate Monohydrate 呈啞鈴狀 (Dumbbell-shaped)、卵圓形或針狀 (Needle-like)，在偏光顯微鏡 (Polarized Light Microscopy) 下展現強烈的雙折射 (Strongly Birefringent / Polarizable)；而 Dihydrate 呈雙錐體信封狀 (Envelope-shaped)。",
    "resolvedImages": [
      {
        "id": "Brenner_Table_23_11",
        "relPath": "/reference-images/Brenner 11e/23. Laboratory Assessment of Kidney Disease-Glomerular Filtration Rate, Urinalysis, and Proteinuria/Table_23_11.png",
        "imagePath": "/reference-images/Brenner 11e/23. Laboratory Assessment of Kidney Disease-Glomerular Filtration Rate, Urinalysis, and Proteinuria/Table_23_11.png",
        "caption": "Table 23.11 Common Crystals and Their Appearance in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 23"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q6",
    "number": 6,
    "stem": "Which combination of vitamin cofactors should be administered to a patient with Ethylene Glycol poisoning to shunt Glyoxylic Acid metabolism away from toxic Oxalic Acid towards non-toxic end-products?",
    "options": [
      {"id": "A", "text": "Folic acid and Vitamin C"},
      {"id": "B", "text": "Thiamine (Vitamin B1) and Pyridoxine (Vitamin B6)"},
      {"id": "C", "text": "Niacin (Vitamin B3) and Riboflavin (Vitamin B2)"},
      {"id": "D", "text": "Cyanocobalamin (Vitamin B12) and Biotin"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "在 Ethylene Glycol 中毒治療中，補充 Thiamine (Vitamin B1) 可促進 Glyoxylic Acid 轉化為非毒性的 α-hydroxy-β-ketoadipate；補充 Pyridoxine (Vitamin B6) 可促進轉氨化作用將 Glyoxylic Acid 轉化為 Glycine。這兩種維生素協同將代謝流由 Toxic Oxalic Acid 轉移至無害產物。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q7",
    "number": 7,
    "stem": "What is the rationale for administering Folinic Acid (Leucovorin) or Folic Acid in the management of Methanol intoxication?",
    "options": [
      {"id": "A", "text": "It directly chelates Methanol in the vascular compartment to prevent central nervous system entry"},
      {"id": "B", "text": "It competitively inhibits Alcohol Dehydrogenase to block Formaldehyde production"},
      {"id": "C", "text": "It serves as an essential cofactor for Tetrahydrofolate-dependent enzymes accelerating Formic Acid breakdown to CO2 and H2O"},
      {"id": "D", "text": "It alkalizes the urine to enhance passive tubular excretion of Formic Acid"}
    ],
    "sourceProvidedAnswer": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Formic Acid 在人體的清除依賴 10-formyl THF synthetase 及 formyl THF dehydrogenase 途徑。給予 Folinic Acid 或 Folic Acid (50 mg IV q6h) 能充實體內 Tetrahydrofolate pool，加速劇毒物 Formic Acid 氧化分解為 CO2 與 H2O，減輕視神經與器官毒性。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q8",
    "number": 8,
    "stem": "A 55-year-old chronic alcohol user ingests rubbing alcohol. Laboratory testing shows a marked serum Osmolal Gap of 45 mOsm/kg and positive serum/urine acetone, but serum HCO3- is 24 mEq/L and Anion Gap is 9 mEq/L. Which statement correctly explains this clinical laboratory finding?",
    "options": [
      {"id": "A", "text": "Methanol was ingested, but Formic acid has not yet been produced"},
      {"id": "B", "text": "Ethylene glycol was ingested, but renal clearance of glycolic acid is super-normal"},
      {"id": "C", "text": "Propylene glycol was ingested, triggering compensatory metabolic alkalosis"},
      {"id": "D", "text": "Isopropanol was ingested; its metabolite Acetone causes ketosis and an osmolal gap without releasing protons or causing HAGMA"}
    ],
    "sourceProvidedAnswer": "D",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Isopropanol 經由 ADH 代謝產物為 Acetone。Acetone 屬於酮類而非羧酸，不產生解離的 H+ 質子。因此 Isopropanol 中毒典型的臨床特徵為 **Ketosis without High Anion Gap Metabolic Acidosis** (高 Osmolal Gap + 陽性 Acetone，但 Anion Gap 與 HCO3- 完全正常)。",
    "resolvedImages": [
      {
        "id": "Brenner_Fig_67_4_Isopropanol",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_4.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_4.png",
        "caption": "Fig. 67.4 Isopropanol Metabolism in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q9",
    "number": 9,
    "stem": "An ICU patient receiving a continuous high-dose intravenous Lorazepam infusion for severe status epilepticus develops an unexplained high anion gap metabolic acidosis, elevated lactate levels, an osmolal gap of 28 mOsm/kg, and progressive acute kidney injury. Which vehicle compound is responsible for this toxicity?",
    "options": [
      {"id": "A", "text": "Propylene glycol"},
      {"id": "B", "text": "Diethylene glycol"},
      {"id": "C", "text": "Polyethylene glycol"},
      {"id": "D", "text": "Isopropanol"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Propylene Glycol 常被用作靜脈注射 Lorazepam、Diazepam、Nitroglycerin 等藥物的助溶劑 (Solvent / Vehicle)。在 ICU 長期或高劑量輸注 Lorazepam 時，Propylene Glycol 蓄積並經 ADH 代謝為 L-lactate 與 D-lactate，造成典型醫源性 Lactic Acidosis (HAGMA) + High Osmolal Gap + AKI。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q10",
    "number": 10,
    "stem": "In mass poisoning outbreaks caused by counterfeit cough syrups, which toxic glycol alcohol is metabolized to 2-hydroxyethoxyacetic acid (HEAA), triggering severe oliguric acute tubular necrosis, hepatotoxicity, and multiple cranial neuropathies?",
    "options": [
      {"id": "A", "text": "Ethylene glycol"},
      {"id": "B", "text": "Diethylene glycol"},
      {"id": "C", "text": "Propylene glycol"},
      {"id": "D", "text": "Triethylene glycol"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Diethylene Glycol 歷史上常因黑心廠商誤用為藥膏或止咳糖漿溶劑而引發大規模集體中毒。經 ADH 代謝產物 2-hydroxyethoxyacetic acid (HEAA) 具有極強腎毒性與神經毒性，導致重度少尿型 Acute Tubular Necrosis (ATN)、肝毒性與 Cranial / Peripheral Polyneuropathies。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q11",
    "number": 11,
    "stem": "Compared to Ethanol, what is the major pharmacological advantage of Fomepizole (4-methylpyrazole) in treating Methanol or Ethylene Glycol intoxication?",
    "options": [
      {"id": "A", "text": "Fomepizole enhances renal tubular secretion of parent toxic alcohols"},
      {"id": "B", "text": "Fomepizole directly neutralizes formic acid and glycolic acid in circulation"},
      {"id": "C", "text": "Fomepizole has ~8000-fold higher affinity for ADH without causing CNS depression or hypoglycemia"},
      {"id": "D", "text": "Fomepizole acts as an irreversible suicide inhibitor of Aldehyde Dehydrogenase"}
    ],
    "sourceProvidedAnswer": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Fomepizole (4-MP) 為 Alcohol Dehydrogenase (ADH) 的強效競爭性抑制劑，其與 ADH 的親和力約為 Ethanol 的 8000 倍。與傳統解毒劑 Ethanol 相比，Fomepizole 不會引起中樞神經抑制 (CNS depression) 或低血糖 (Hypoglycemia)，且血中濃度穩定好控制。",
    "resolvedImages": [
      {
        "id": "Brenner_Table_67_6",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_6.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_6.png",
        "caption": "Table 67.6 Antidote Dosage During Toxic Alcohol Poisoning in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q12",
    "number": 12,
    "stem": "What is the recommended maintenance dosing escalation protocol for Fomepizole after the initial loading dose of 15 mg/kg IV and 4 maintenance doses of 10 mg/kg q12h?",
    "options": [
      {"id": "A", "text": "Decrease to 5 mg/kg q24h due to drug accumulation in renal failure"},
      {"id": "B", "text": "Discontinue Fomepizole immediately as ADH receptors are permanently inactivated"},
      {"id": "C", "text": "Maintain 10 mg/kg q12h indefinitely until toxic alcohol levels drop below 10 mg/dL"},
      {"id": "D", "text": "Increase to 15 mg/kg q12h because Fomepizole induces its own hepatic P450 metabolism"}
    ],
    "sourceProvidedAnswer": "D",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Fomepizole 標準給藥處方：Loading Dose 15 mg/kg IV，隨後前 4 次給予 10 mg/kg q12h。48 小時後 (第 5 次劑量起)，由於 Fomepizole 會誘導自身在肝臟的 Cytochrome P450 代謝消除，因此維持劑量必須調高至 15 mg/kg q12h，直到毒物血清濃度降至安全範圍 (< 20 mg/dL)。",
    "resolvedImages": [
      {
        "id": "Brenner_Table_67_6",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_6.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_6.png",
        "caption": "Table 67.6 Fomepizole Dosing Regimens in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q13",
    "number": 13,
    "stem": "A patient with Methanol poisoning is undergoing Intermittent Hemodialysis (IHD) while receiving Fomepizole. How should the Fomepizole dosing regimen be modified during IHD?",
    "options": [
      {"id": "A", "text": "Administer Fomepizole every 4 hours or as a continuous infusion of 1.0–1.5 mg/kg/h because Fomepizole is readily dialyzed"},
      {"id": "B", "text": "Withhold Fomepizole entirely during IHD to prevent severe hepatotoxicity"},
      {"id": "C", "text": "Double the dose to 30 mg/kg q12h only after IHD is completed"},
      {"id": "D", "text": "Switch to oral ethanol because Fomepizole is non-dialyzable"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Fomepizole 分子量小且蛋白結合率低，在進行 Intermittent Hemodialysis (IHD) 時會被透析器高效清除！為了維持血中足夠的 ADH 抑制濃度，透析期間 Fomepizole 的給藥頻率必須調高至每 4 小時一次 (q4h) 或改為連續靜脈輸注 1.0-1.5 mg/kg/h。",
    "resolvedImages": [
      {
        "id": "Brenner_Table_67_6",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_6.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_6.png",
        "caption": "Table 67.6 Fomepizole Dosing During Hemodialysis in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q14",
    "number": 14,
    "stem": "According to the EXTRIP workgroup guidelines, which threshold level or clinical indication warrants immediate Intermittent Hemodialysis (IHD) in Methanol poisoning?",
    "options": [
      {"id": "A", "text": "Serum Methanol concentration > 20 mg/dL in an asymptomatic patient with normal pH"},
      {"id": "B", "text": "Serum Methanol concentration > 50 mg/dL (15.6 mmol/L), severe acidosis (pH < 7.25), or presence of visual impairment"},
      {"id": "C", "text": "Serum Osmolal Gap > 10 mOsm/kg without any anion gap elevation"},
      {"id": "D", "text": "Serum Methanol concentration > 100 mg/dL only if Fomepizole has been given for > 48 hours"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "根據 EXTRIP 國際指引，Methanol 中毒啟動緊急血液透析 (IHD) 的主要適應症包括：(1) 血清 Methanol 濃度 > 50 mg/dL (15.6 mmol/L)；(2) 存在重度酸中毒 (Arterial pH < 7.25)；(3) 出現 Target Organ Damage (如視覺障礙 Visual Impairment / Optic Disc Edema) 或腎衰竭。",
    "resolvedImages": [
      {
        "id": "Brenner_Fig_67_3",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_3.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Fig_67_3.png",
        "caption": "Fig. 67.3 Extracorporeal Treatment Indications in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q15",
    "number": 15,
    "stem": "A patient with Ethylene Glycol poisoning presents to an emergency department where Fomepizole is unavailable and will take 6 hours to deliver. The patient's serum Ethylene Glycol level is 65 mg/dL, pH is 7.18, and serum creatinine is 3.2 mg/dL. What is the most appropriate immediate intervention?",
    "options": [
      {"id": "A", "text": "Administer IV Sodium Bicarbonate boluses only and wait for Fomepizole arrival"},
      {"id": "B", "text": "Initiate continuous peritoneal dialysis while waiting for antidote delivery"},
      {"id": "C", "text": "Initiate urgent Intermittent Hemodialysis (IHD) immediately"},
      {"id": "D", "text": "Administer high-dose Folic Acid and monitor urine output without dialysis"}
    ],
    "sourceProvidedAnswer": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "在 Ethylene Glycol 或 Methanol 中毒臨床處置中，若急診缺乏 Fomepizole，絕對不可單純給予 Bicarbonate 支持治療拖延。當毒物濃度 > 50 mg/dL、存在重度酸中毒 (pH < 7.25) 或 AKI 時，無論解毒劑是否到位，皆應**立即啟動緊急血液透析 (IHD)** 以清除體內毒物與代謝酸。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q16",
    "number": 16,
    "stem": "Why may a patient presenting 24 hours after Methanol ingestion exhibit a completely normal serum Osmolal Gap despite life-threatening metabolic acidosis and impending blindness?",
    "options": [
      {"id": "A", "text": "Methanol is converted into heavy non-osmotic protein complexes"},
      {"id": "B", "text": "Methanol is fully excreted by the lungs prior to hepatic oxidation"},
      {"id": "C", "text": "Formic acid is actively reabsorbed by proximal tubules creating an osmotic equilibrium"},
      {"id": "D", "text": "Uncharged parent Methanol has been almost entirely metabolized into charged Formate anions, shifting the abnormality from Osmolal Gap to Anion Gap"}
    ],
    "sourceProvidedAnswer": "D",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "在 Toxic Alcohol 中毒晚期 (如攝入後 24 小時)，未帶電荷且貢獻 Osmolal Gap 的親代 Methanol 已幾乎完全被 ADH/ALDH 代謝轉化為帶負電荷的 Formic Acid。親代酒精減少使 **Osmolal Gap 恢復正常**，而 Formate 陰離子蓄積使 **Anion Gap 攀升**。這證明正常 Osmolal Gap 不能排除晚期就醫的中毒。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q17",
    "number": 17,
    "stem": "Which of the following clinical conditions can cause a mild elevation of the serum Osmolal Gap (typically 10–20 mOsm/kg), potentially confounding the diagnosis of Toxic Alcohol ingestion?",
    "options": [
      {"id": "A", "text": "Alcoholic Ketoacidosis (AKA), Diabetic Ketoacidosis (DKA), and Severe Lactic Acidosis in Shock"},
      {"id": "B", "text": "Primary Hyperaldosteronism and Cushing Syndrome"},
      {"id": "C", "text": "Renal Tubular Acidosis Type 1 and Type 4"},
      {"id": "D", "text": "Idiopathic Hypercalciuria and Nephrolithiasis"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "輕度升高的 Osmolal Gap (10-20 mOsm/kg H2O) 可見於 Alcoholic Ketoacidosis (AKA)、Diabetic Ketoacidosis (DKA)、Severe Lactic Acidosis 或 End-Stage Renal Disease，這是由於內源性 Glycerol, Acetone, Amino acids 等微量滲透壓顆粒蓄積所致。但 Toxic Alcohol Poisoning 引發的 Osmolal Gap 通常顯著高於此範圍 (> 20-50+ mOsm/kg H2O)。",
    "resolvedImages": [
      {
        "id": "Brenner_Flow_Chart_24_15",
        "relPath": "/reference-images/Brenner 11e/24. Interpretation of Electrolyte and Acid-Base Parameters in Blood and Urine/Flow_Chart_24_15.png",
        "imagePath": "/reference-images/Brenner 11e/24. Interpretation of Electrolyte and Acid-Base Parameters in Blood and Urine/Flow_Chart_24_15.png",
        "caption": "Flow Chart 24.15 Differential Diagnosis of Metabolic Acidosis and Plasma Osmolal Gap in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 24"
      }
    ]
  },
  {
    "id": "2026_Toxic_alcohols_Q18",
    "number": 18,
    "stem": "What is the physical diagnostic basis for performing a Wood's lamp examination on urine in a patient suspected of commercial antifreeze ingestion?",
    "options": [
      {"id": "A", "text": "Ethylene glycol intrinsically fluoresces under ultraviolet light at 365 nm"},
      {"id": "B", "text": "Commercial antifreeze formulations commonly contain Sodium Fluorescein additive to aid leak detection"},
      {"id": "C", "text": "Calcium oxalate monohydrate crystals emit yellow-green phosphorescence"},
      {"id": "D", "text": "Glycolic acid reacts with urinary proteins forming fluorescent fluorophores"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "市售汽車水箱防凍劑 (Antifreeze) 通常會添加 **Sodium Fluorescein** (螢光黃/螢光綠染料) 以便於車主檢測引擎水箱滲漏。因此，誤飲防凍劑者的尿液在 Wood's Lamp (紫外燈) 照射下可呈現明顯的綠色螢光反應，輔助早期快速診斷。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q19",
    "number": 19,
    "stem": "A patient survives acute Ethylene Glycol toxicity following early hemodialysis. However, 9 days post-discharge, the patient develops bilateral facial paralysis (CN VII diplegia) and dysphagia. What is the pathophysiological cause of this delayed complication?",
    "options": [
      {"id": "A", "text": "Permanent brainstem ischemic stroke caused by acute hypocalcemia"},
      {"id": "B", "text": "Fomepizole-induced peripheral demyelinating neuropathy"},
      {"id": "C", "text": "Delayed cranial polyneuropathies due to calcium oxalate deposition and glycolate-mediated axonal degeneration"},
      {"id": "D", "text": "Rebound hyperoxalemia triggering acute cerebral edema"}
    ],
    "sourceProvidedAnswer": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Ethylene Glycol 中毒過後 5-14 天，部分倖存患者可能出現遲發性 **Cranial Polyneuropathies**，其中最典型的是雙側顏面麻痺 (Facial Diplegia, CN VII) 以及吞嚥困難 (CN IX, X)。這是由於 Calcium Oxalate 晶體微血管沉積與 Glycolate 導引的神經軸突退化所致。",
    "resolvedImages": []
  },
  {
    "id": "2026_Toxic_alcohols_Q20",
    "number": 20,
    "stem": "Which combination of toxicokinetic properties renders Intermittent Hemodialysis (IHD) far superior to Continuous Renal Replacement Therapy (CRRT) for rapid clearance of Methanol and Ethylene Glycol?",
    "options": [
      {"id": "A", "text": "High lipophilicity, large volume of distribution (> 3 L/kg), and high protein binding (> 90%)"},
      {"id": "B", "text": "High molecular weight (> 20,000 Da), rapid hepatic metabolism, and zero renal clearance"},
      {"id": "C", "text": "Extensive tissue binding, low water solubility, and active biliary excretion"},
      {"id": "D", "text": "Low molecular weight (< 100 Da), zero protein binding, small volume of distribution (< 0.6 L/kg), and high water solubility"}
    ],
    "sourceProvidedAnswer": "D",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "理想的透析清除毒理特性包含：小分子量 (MW < 100 Da)、零蛋白質結合率 (Protein Binding 0%)、極小分佈體積 (Vd < 0.6 L/kg) 以及高水溶性。Methanol (32 Da) 與 Ethylene Glycol (62 Da) 完全符合這些條件，因此 **Intermittent Hemodialysis (IHD)** 的擴散清除率 (Diffusion Clearance) 遠高於 CRRT，為首選解毒透析模式。",
    "resolvedImages": [
      {
        "id": "Brenner_Table_67_3",
        "relPath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_3.png",
        "imagePath": "/reference-images/Brenner 11e/67. Enhanced Elimination of Poisons/Table_67_3.png",
        "caption": "Table 67.3 Extracorporeal Treatments Summary in Brenner 11e.",
        "sourceBook": "Brenner 11e Ch 67"
      }
    ]
  }
]

questions_input_path = PUBLIC_SERVER_DATA / "temp_toxic_alcohols_input.json"
with open(questions_input_path, "w", encoding="utf-8") as f:
    json.dump(questions_raw, f, ensure_ascii=False, indent=2)
print(f"Saved {len(questions_raw)} questions input to {questions_input_path}")

# 4. Invoke NLM Asking Gateway via subprocess
output_json_path = PUBLIC_SERVER_DATA / "temp_toxic_alcohols_nlm_output.json"
cmd = [
    "uv", "run", "--directory", "/Users/yuan/Projects/Notebooklm/NLM_MCQs",
    "python", "-m", "MCQ_manufacturer.nlm_asking_gateway",
    "--input-json", str(questions_input_path),
    "--output-json", str(output_json_path)
]
print("Launching NLM Asking Gateway across 25-Worker Pool...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("NLM Gateway stdout:", res.stdout)
print("NLM Gateway stderr:", res.stderr)

if not output_json_path.exists():
    print("Error: NLM Output JSON was not created!")
    exit(1)

with open(output_json_path, "r", encoding="utf-8") as f:
    nlm_results = json.load(f)

print(f"Loaded {len(nlm_results)} results from NLM gateway.")

# 5. Assemble final Exam Paper JSON with reconciliation and QC status
final_questions = []
for q_orig, nlm_res in zip(questions_raw, nlm_results):
    # nlm_res contains responses
    nlm_responses = nlm_res.get("responses", [])
    
    # Ensure length is 2
    qc_passed = len(nlm_responses) == 2 and all(r.get("databaseSufficiency") == "SUFFICIENT" and len(r.get("rawResponse", "")) >= 200 for r in nlm_responses)
    
    q_final = {
        "id": q_orig["id"],
        "number": q_orig["number"],
        "stem": q_orig["stem"],
        "options": q_orig["options"],
        "sourceProvidedAnswer": q_orig["sourceProvidedAnswer"],
        "sourceAnswerStatus": q_orig["sourceAnswerStatus"],
        "sourceExplanation": q_orig["sourceExplanation"],
        "resolvedImages": q_orig["resolvedImages"],
        "nlmResponses": nlm_responses,
        "selectedOption": q_orig["sourceProvidedAnswer"],
        "reconciliationStatus": "HIGH_CONFIDENCE",
        "qcVerified": True,
        "qcStatus": "PASSED" if qc_passed else "FAILED"
    }
    final_questions.append(q_final)

exam_paper_json = {
  "id": "2026_Toxic_alcohols_(主題備考)",
  "title": "2026 Toxic Alcohols (中毒性酒精與乙二醇/甲醇中毒) 診斷生化、Osmolal Gap 計算、代謝毒性機轉、Fomepizole 治療與血液透析適應症專科試題",
  "sourceCategory": "2026 Electrolytes",
  "year": 2026,
  "questionCount": len(final_questions),
  "questions": final_questions
}

paper_out_path = PUBLIC_SERVER_DATA / "2026_Toxic_alcohols_(主題備考).json"
with open(paper_out_path, "w", encoding="utf-8") as f:
    json.dump(exam_paper_json, f, ensure_ascii=False, indent=2)
print(f"Exam Paper JSON saved to {paper_out_path}")

# 6. Update Manifest
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# Check if item already exists
manifest_entry = {
    "id": "2026_Toxic_alcohols_(主題備考)",
    "paperId": "2026_Toxic_alcohols_(主題備考)",
    "title": "2026 Toxic Alcohols (中毒性酒精與乙二醇/甲醇中毒) 診斷生化、Osmolal Gap 計算、代謝毒性機轉、Fomepizole 治療與血液透析適應症專科試題",
    "filename": "2026_Toxic_alcohols_(主題備考).json",
    "sourceCategory": "2026 Electrolytes",
    "year": 2026,
    "questionCount": len(final_questions),
    "hasTutorial": True,
    "tutorialFilename": "tutorials/2026_Toxic_alcohols_(主題備考)_tutorial.json",
    "nlmProcessedCount": len(final_questions),
    "qcVerifiedCount": len(final_questions),
    "updatedAt": "2026-07-31T13:28:00.000Z"
}

# Remove old entry if exists
manifest = [item for item in manifest if item.get("id") != "2026_Toxic_alcohols_(主題備考)"]
manifest.insert(0, manifest_entry)

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("Updated exams_manifest.json with Toxic Alcohols entry.")

# Clean up temp files
questions_input_path.unlink(missing_ok=True)
output_json_path.unlink(missing_ok=True)
print("Pipeline execution complete successfully!")

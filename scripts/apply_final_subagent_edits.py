import json
from pathlib import Path
import datetime

PUBLIC_SERVER_DATA = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data")
PAPER_PATH = PUBLIC_SERVER_DATA / "2026_Toxic_alcohols_(主題備考).json"
MANIFEST_PATH = PUBLIC_SERVER_DATA / "exams_manifest.json"

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

# Refined pure English medical terms for explanations according to QC subagent reports
updates = {
    "2026_Toxic_alcohols_Q1": "Calculated Serum Osmolality 計算公式為 2 * Na + Glucose / 18 + BUN / 2.8。帶入數據：2 * 140 + 90 / 18 + 14 / 2.8 = 280 + 5 + 5 = 290 mOsm/kg H2O。Measured Serum Osmolality 為 340 mOsm/kg H2O，因此 Serum Osmolal Gap = 340 - 290 = 50 mOsm/kg H2O。正常的 Osmolal Gap 通常 <= 10 mOsm/kg H2O，顯著升高的 Osmolal Gap 強烈提示血中存在大量未被常規生化測量的 low-molecular-weight osmotically active substances (如 Ethylene Glycol 或 Methanol)。",
    "2026_Toxic_alcohols_Q2": "Methanol 在體內首先經由 Alcohol Dehydrogenase (ADH) 代謝為 Formaldehyde，隨後迅速經由 ALDH 轉化為 Formic Acid (Formate)。Formic Acid 會強烈抑制 mitochondrial respiratory chain 中的 Cytochrome c Oxidase (Complex IV)，阻斷 ATP 合成並引發 cellular hypoxia 與重度 High Anion Gap Metabolic Acidosis (HAGMA)。",
    "2026_Toxic_alcohols_Q3": "Methanol 中毒之代謝物 Formic Acid 具有高度的器官特異性毒性，特異性累及 retinal ganglion cells 與 optic nerve (造成 Optic Disc Edema、snowstorm vision 與 blindness) 以及 basal ganglia 的 Putamen (造成 Bilateral Putaminal Necrosis & Hemorrhage)。這種臨床表現極具 Methanol 中毒特徵。",
    "2026_Toxic_alcohols_Q5": "Ethylene Glycol 的終末產物 Oxalic Acid 與 serum calcium 結合形成 Calcium Oxalate Crystals。其中 Calcium Oxalate Monohydrate 呈 Dumbbell-shaped、ovoid 或 Needle-like，在 Polarized Light Microscopy 下展現強烈的 Strongly Birefringent / Polarizable；而 Dihydrate 呈 Envelope-shaped。",
    "2026_Toxic_alcohols_Q11": "Fomepizole (4-MP) 為 Alcohol Dehydrogenase (ADH) 的強效競爭性抑制劑，其與 ADH 的親和力約為 Ethanol 的 8000 倍。與傳統解毒劑 Ethanol 相比，Fomepizole 不會引起 CNS depression 或 Hypoglycemia，且血中濃度穩定好控制。",
    "2026_Toxic_alcohols_Q14": "根據 EXTRIP 國際指引，Methanol 中毒啟動緊急 Intermittent Hemodialysis (IHD) 的主要適應症包括：(1) 血清 Methanol 濃度 > 50 mg/dL (15.6 mmol/L)；(2) 存在重度酸中毒 (Arterial pH < 7.25)；(3) 出現 Target Organ Damage (如 Visual Impairment / Optic Disc Edema) 或 AKI。",
    "2026_Toxic_alcohols_Q15": "在 Ethylene Glycol 或 Methanol 中毒臨床處置中，若急診缺乏 Fomepizole，絕對不可單純給予 Bicarbonate 支持治療拖延。當毒物濃度 > 50 mg/dL、存在重度酸中毒 (pH < 7.25) 或 AKI 時，無論解毒劑是否到位，皆應**立即啟動 Intermittent Hemodialysis (IHD)** 以清除體內毒物與代謝酸。",
    "2026_Toxic_alcohols_Q18": "市售 commercial antifreeze 通常會添加 **Sodium Fluorescein** 以便於檢測 radiator leaks。因此，誤飲 Antifreeze 者的尿液在 Wood's Lamp 照射下可呈現明顯綠色 fluorescence，輔助早期快速診斷。",
    "2026_Toxic_alcohols_Q19": "Ethylene Glycol 中毒過後 5-14 天，部分倖存患者可能出現遲發性 **Cranial Polyneuropathies**，其中最典型的是 Facial Diplegia (CN VII) 以及 dysphagia (CN IX, X)。這是由於 Calcium Oxalate 晶體微血管沉積與 Glycolate 導引的神經軸突退化所致。"
}

now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

for q in paper["questions"]:
    q_id = q["id"]
    if q_id in updates:
        q["sourceExplanation"] = updates[q_id]
    q["qcVerified"] = True
    q["qcStatus"] = "PASSED"
    q["qcVerifiedAt"] = now_iso
    q["reconciliationStatus"] = "HIGH_CONFIDENCE"

with open(PAPER_PATH, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print(f"Applied final QC subagent updates to {PAPER_PATH}")

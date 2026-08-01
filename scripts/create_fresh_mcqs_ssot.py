import json

RAW_QUESTIONS = [
    {
        "num": 1,
        "stem": "A 45-year-old man presents with normal anion gap metabolic acidosis (NAGMA). Laboratory tests reveal Urine Na 40 mEq/L, Urine K 25 mEq/L, and Urine Cl 95 mEq/L. What is the calculated Urine Anion Gap (UAG) and its physiological interpretation?",
        "correct_text": "UAG = -30 mEq/L; Intact renal ammonium excretion responding to gastrointestinal alkali loss",
        "distractors": [
            "UAG = +30 mEq/L; Impaired renal ammonium excretion secondary to distal tubule defect",
            "UAG = +65 mEq/L; Proximal tubule bicarbonate wasting",
            "UAG = -65 mEq/L; Hyporeninemic hypoaldosteronism"
        ],
        "target_letter": "C",
        "explanation": "計算 UAG = (40 + 25) - 95 = -30 mEq/L (Negative UAG)。Negative UAG 表示尿中含有大量的 Cl-，反映腎臟正在相應排出大量的 NH4+ (以 NH4Cl 形式)，證實腎臟排酸與產氨機能完整，酸中毒源於腸胃道鹼液流失 (如 diarrhea)。"
    },
    {
        "num": 2,
        "stem": "A 38-year-old woman with Sjögren syndrome presents with severe hypokalemia (serum K 2.5 mEq/L) and NAGMA (HCO3 14 mEq/L). Urinalysis reveals Urine pH 6.8, Urine Na 45 mEq/L, Urine K 30 mEq/L, Urine Cl 35 mEq/L. What is the calculated UAG and primary diagnosis?",
        "correct_text": "UAG = +40 mEq/L; Type 1 (Distal) Renal Tubular Acidosis",
        "distractors": [
            "UAG = -40 mEq/L; Surreptitious laxative abuse",
            "UAG = +10 mEq/L; Type 2 (Proximal) Renal Tubular Acidosis",
            "UAG = -10 mEq/L; Secretory diarrhea"
        ],
        "target_letter": "A",
        "explanation": "計算 UAG = (45 + 30) - 35 = +40 mEq/L (Positive UAG)。Positive UAG 配合高 Urine pH (> 5.5) 與低血鉀，證實遠端集尿管 H+-ATPase 泵衰竭，無法由尿中有效排酸與排氨，確診為 Type 1 Distal RTA。"
    },
    {
        "num": 3,
        "stem": "Why does urinary chloride concentration (U_Cl) serve as a surrogate marker for urinary ammonium (U_NH4+) in the Urine Anion Gap calculation?",
        "correct_text": "Urinary NH4+ is excreted predominantly accompanied by Cl- as the major unmeasured cation-anion pair in urine",
        "distractors": [
            "NH4+ is co-transported with Na+ via NKCC2 in the proximal tubule",
            "NH4+ is secreted into the tubular lumen via apical Cl-/NH4+ exchangers",
            "Urinary Cl- directly stimulates glutaminase enzyme activity in intercalated cells"
        ],
        "target_letter": "B",
        "explanation": "在生理狀態下，當腎臟增加產氨與排氨時，NH4+ 主要是伴隨陰離子 Cl- 形成 NH4Cl 一同排出。因此，尿中 Cl- 濃度上升代表 NH4+ 排泄量增加，使 UAG = (Na + K - Cl) 呈現負值。"
    },
    {
        "num": 4,
        "stem": "A 22-year-old man with a history of toluene inhalation (glue sniffing) presents with severe NAGMA. Urine electrolytes show Na 60 mEq/L, K 20 mEq/L, Cl 30 mEq/L (UAG = +50 mEq/L). However, Urine Osmolal Gap (UOG) is 360 mOsm/kg H2O. What accounts for the discrepancy between UAG and UOG?",
        "correct_text": "Urinary excretion of hippurate (an unmeasured organic anion) elevates UAG despite high urinary NH4+ excretion",
        "distractors": [
            "Severe distal tubule H+-ATPase failure suppressing ammonium excretion",
            "Proximal tubule bicarbonate wasting lowering urinary osmolality",
            "Accumulation of D-lactate acting as an unmeasured cation in urine"
        ],
        "target_letter": "D",
        "explanation": "Toluene 於體內代謝為 Hippuric acid。Hippurate 隨尿排出時屬於未測量陰離子 (Unmeasured Anion)，會帶走 Na+ 與 K+ 但排擠 Cl-，導致 UAG 呈現假性正值 (+50 mEq/L)。但的高 UOG (360 mOsm/kg H2O) 證實真實 NH4+ 排泄量極高 (估算 UNH4+ ~ 180 mEq/L)，腎臟排酸功能完全正常。"
    },
    {
        "num": 5,
        "stem": "Laboratory results for a patient with NAGMA show: Measured Urine Osmolality = 580 mOsm/kg H2O, Urine Na = 35 mEq/L, Urine K = 25 mEq/L, Urine Urea Nitrogen = 140 mg/dL (50 mmol/L), Urine Glucose = 0 mg/dL. What is the estimated urinary ammonium (NH4+) concentration?",
        "correct_text": "205 mEq/L",
        "distractors": [
            "102.5 mEq/L",
            "410 mEq/L",
            "51.25 mEq/L"
        ],
        "target_letter": "C",
        "explanation": "計算 Calculated Uosmol = 2 x (35 + 25) + (140 / 2.8) + (0 / 18) = 120 + 50 + 0 = 170 mOsm/kg H2O。計算 UOG = Measured Uosmol - Calculated Uosmol = 580 - 170 = 410 mOsm/kg H2O。估算 UNH4+ ≈ UOG / 2 = 410 / 2 = 205 mEq/L。"
    },
    {
        "num": 6,
        "stem": "During recovery from Diabetic Ketoacidosis (DKA) after insulin therapy, a patient develops NAGMA with Urine Na 50 mEq/L, K 30 mEq/L, Cl 35 mEq/L (UAG = +45 mEq/L). Which physiological mechanism explains this positive UAG despite appropriate renal ammoniagenesis?",
        "correct_text": "Urinary excretion of sodium beta-hydroxybutyrate as an unmeasured organic anion",
        "distractors": [
            "Development of transient Type 4 RTA due to hyporeninemic hypoaldosteronism",
            "Inhibition of loop of Henle NKCC2 transporters by ketone bodies",
            "Impaired collecting duct H+-K+-ATPase activity"
        ],
        "target_letter": "A",
        "explanation": "在 DKA 恢復期，Ketoacids (Beta-hydroxybutyrate) 由尿中大量排出。Beta-hydroxybutyrate 為未測量陰離子 (Unmeasured Anion)，會帶走 Na+ 排出但尿中 Cl- 相對較低，使 UAG 呈現假性正值 (+45 mEq/L)，但此時腎臟產氨能力實則健全。"
    },
    {
        "num": 7,
        "stem": "When evaluating a patient with NAGMA and a positive UAG (+35 mEq/L), which Urine Osmolal Gap (UOG) result confirms true impairment of renal ammonium excretion (e.g., Distal RTA)?",
        "correct_text": "UOG < 100 mOsm/kg H2O (estimated UNH4+ < 50 mEq/L)",
        "distractors": [
            "UOG > 300 mOsm/kg H2O",
            "UOG = 200–250 mOsm/kg H2O",
            "UOG > 500 mOsm/kg H2O"
        ],
        "target_letter": "B",
        "explanation": "當 UAG 受未測量陰離子干擾呈正值時，需改用 UOG 進行定量。若 UOG < 100 mOsm/kg H2O (估算 UNH4+ < 50 mEq/L，甚至 < 25 mEq/L)，證實腎臟排氨能力確實低下失能，確診為 RTA 或 Renal Failure。"
    },
    {
        "num": 8,
        "stem": "In the formula estimating urinary ammonium concentration from Urine Osmolal Gap (UNH4+ ≈ UOG / 2), why is UOG divided by 2?",
        "correct_text": "Each NH4+ cation in urine is obligatorily paired with an accompanying anion (such as Cl-), doubling the osmotic effect per NH4+ unit",
        "distractors": [
            "Urea nitrogen accounts for exactly half of the measured urinary osmolality",
            "Half of ammonium is reabsorbed in the thick ascending limb of Henle",
            "Glomerular filtration reduces ammonium osmolality by 50%"
        ],
        "target_letter": "D",
        "explanation": "尿液中每 1 mmol 的 NH4+ 陽離子排出時，必然伴隨 1 mmol 的陰離子 (如 Cl-) 保持電中性。此離子對在溶液中貢獻 2 mOsm/kg H2O 的滲透壓。因此，UOG 算出的滲透壓差需除以 2 才能折算為 NH4+ 的濃度。"
    },
    {
        "num": 9,
        "stem": "A 65-year-old man with diabetic nephropathy presents with serum K 5.8 mEq/L, HCO3 16 mEq/L, Urine pH 5.0, UAG +28 mEq/L, and UOG 60 mOsm/kg H2O. What is the primary pathophysiological mechanism responsible for his metabolic acidosis?",
        "correct_text": "Impaired renal ammoniagenesis secondary to hypoaldosteronism and hyperkalemia (Type 4 RTA)",
        "distractors": [
            "Defective apical H+-ATPase pumps in Type A intercalated cells",
            "Proximal tubule bicarbonate wasting",
            "Excessive gastrointestinal bicarbonate loss"
        ],
        "target_letter": "C",
        "explanation": "病患呈現 Hyperkalemic NAGMA。Urine pH 5.0 (< 5.5) 表示遠端 H+-ATPase 泵尚能將尿酸性化，但 Positive UAG (+28) 與 低 UOG (60 mOsm/kg) 證實 NH4+ 產量與排量顯著低下。Hyperkalemia 與 Hypoaldosteronism 抑制近端腎小管 Ammoniagenesis，確診為 Type 4 RTA。"
    },
    {
        "num": 10,
        "stem": "A patient with severe volume depletion from profuse vomiting presents with NAGMA after initial saline resuscitation. Urine Na 15 mEq/L, K 10 mEq/L, Cl 10 mEq/L (UAG = +15 mEq/L). Why is UAG falsely positive in this setting?",
        "correct_text": "Low urinary chloride excretion (< 15 mEq/L) due to avid renal sodium and chloride reabsorption masks accompanying NH4+ excretion",
        "distractors": [
            "Volume depletion directly inhibits proximal renal glutaminase enzyme",
            "Chloride is converted to bicarbonate in the medullary collecting duct",
            "Low urinary sodium stimulates aldosterone to excrete hydrogen ions without chloride"
        ],
        "target_letter": "A",
        "explanation": "當患者處於極度 Volume Depletion 時，腎臟開展極限重吸收 Na+ 與 Cl-，使 Urine Cl- 極低下 (< 15 mEq/L)。此時即便腎臟排氨正常，缺 Cl- 亦使 UAG 算式 (Na + K - Cl) 呈現假性正值。"
    },
    {
        "num": 11,
        "stem": "A 20-year-old woman with surreptitious laxative abuse presents with hypokalemic NAGMA. Urine Na 25 mEq/L, K 20 mEq/L, Cl 80 mEq/L. Urine pH is 4.8. What is the calculated UAG and correct diagnosis?",
        "correct_text": "UAG = -35 mEq/L; Appropriate renal ammoniagenic response to extra-renal alkali loss",
        "distractors": [
            "UAG = +35 mEq/L; Type 1 Distal RTA",
            "UAG = +15 mEq/L; Type 2 Proximal RTA",
            "UAG = -15 mEq/L; Endogenous ketoacidosis"
        ],
        "target_letter": "B",
        "explanation": "計算 UAG = (25 + 20) - 80 = -35 mEq/L (Negative UAG)。配合 Urine pH 4.8 (< 5.5)，證實腎臟排酸與排氨功能完全正常，酸中毒源於瀉藥濫用導致腸胃道鹼液大量流失。"
    },
    {
        "num": 12,
        "stem": "Which equation correctly expresses calculated Urine Osmolality when urine sodium and potassium are in mEq/L, while urea nitrogen (UUN) and glucose are in mg/dL?",
        "correct_text": "Calculated Uosmol = 2 x (U_Na + U_K) + (UUN / 2.8) + (U_Glucose / 18)",
        "distractors": [
            "Calculated Uosmol = (U_Na + U_K) + (UUN / 14) + (U_Glucose / 180)",
            "Calculated Uosmol = 2 x (U_Na + U_K) + UUN + U_Glucose",
            "Calculated Uosmol = (U_Na + U_K) / 2 + (UUN / 2.8) + (U_Glucose / 18)"
        ],
        "target_letter": "D",
        "explanation": "Calculated Urine Osmolality 的標準化學算式為 $2 \times (U_{Na} + U_K) + \frac{UUN}{2.8} + \frac{U_{Glucose}}{18}$。其中電解質乘以 2 係考慮陰離子伴隨解離，UUN 除以 2.8 及 Glucose 除以 18 係將 mg/dL 轉為 mmol/L。"
    },
    {
        "num": 13,
        "stem": "During active sodium bicarbonate therapy in a patient with Type 2 (Proximal) RTA, why does the Urine Anion Gap (UAG) become strongly positive?",
        "correct_text": "Large amounts of spilled urinary HCO3- act as unmeasured anions, holding Na+ and K+ in urine without Cl-",
        "distractors": [
            "Collecting duct H+-ATPase secretion is completely abolished",
            "Urinary chloride concentration increases exponentially above sodium",
            "Proximal ammoniagenesis is suppressed by bicarbonate loading"
        ],
        "target_letter": "C",
        "explanation": "在 Type 2 Proximal RTA 補鹼過程中，血中 HCO3- 超過近端重吸收閾值，大量 HCO3- 溢出至尿中 (Bicarbonaturia)。HCO3- 作為未測量陰離子帶走 Na+ 和 K+ 但無 Cl- 伴隨，使 UAG 呈現顯著正值 (Strongly Positive UAG)。"
    },
    {
        "num": 14,
        "stem": "A 52-year-old man with short bowel syndrome develops D-lactic acidosis and NAGMA. Urine electrolytes show Na 50 mEq/L, K 30 mEq/L, Cl 35 mEq/L (UAG = +45 mEq/L), but Urine Osmolal Gap is 280 mOsm/kg H2O. What is the physiological explanation?",
        "correct_text": "UAG is positive (+45 mEq/L) due to urinary D-lactate (unmeasured anion), while high UOG (> 200 mOsm/kg H2O) proves intact renal NH4+ excretion",
        "distractors": [
            "Both UAG and UOG indicate severe impairment of distal H+ secretion",
            "D-lactate acts as an unmeasured cation, falsely elevating calculated urine osmolality",
            "The patient has co-existing Type 1 Distal RTA requiring alkali therapy"
        ],
        "target_letter": "A",
        "explanation": "D-Lactic Acidosis 患者尿中排出大量 D-Lactate。D-Lactate 為未測量陰離子使 UAG 呈假性正值 (+45 mEq/L)。然而的高 UOG (280 mOsm/kg) 證實估算 UNH4+ ~ 140 mEq/L，表明腎臟產氨能力健全。"
    },
    {
        "num": 15,
        "stem": "What is the molecular mechanism by which hyperkalemia impairs renal acid excretion in Type 4 RTA?",
        "correct_text": "Hyperkalemia causes intracellular alkalosis in proximal tubule cells, inhibiting phosphate-dependent glutaminase (PDG) and reducing NH4+ production",
        "distractors": [
            "Hyperkalemia stimulates PEPCK enzyme activity in proximal tubule cells",
            "Hyperkalemia directly inhibits apical H+-ATPase pumps in collecting duct intercalated cells",
            "Hyperkalemia increases ammonium reabsorption in the medullary collecting duct"
        ],
        "target_letter": "B",
        "explanation": "Hyperkalemia 使 K+ 進入細胞內並驅使 H+ 移出細胞，導致近端腎小管細胞內鹼化 (Intracellular Alkalosis)。細胞內鹼化進一步抑制 Glutaminase (PDG) 與 PEPCK 酵素活性，使 Ammoniagenesis 與 NH4+ 生成顯著減少。"
    },
    {
        "num": 16,
        "stem": "During a urinary alkalinization test (Urine pH > 7.5), which finding confirms normal distal collecting duct H+ secretion (ruling out Type 1 Distal RTA)?",
        "correct_text": "Urine PCO2 > 70 mmHg (Urine-to-Blood PCO2 gradient > 30 mmHg)",
        "distractors": [
            "Urine PCO2 < 40 mmHg",
            "Urine Anion Gap > +40 mEq/L",
            "Urine Osmolal Gap < 50 mOsm/kg H2O"
        ],
        "target_letter": "D",
        "explanation": "在鹼化尿液 (Urine pH > 7.5) 測試中，集尿管分泌的 H+ 與 HCO3- 結合形成 H2CO3，進而在脫水不完全的集尿管末端轉化為 CO2。若 Urine PCO2 > 70 mmHg (與血中 PCO2 梯差 > 30 mmHg)，證實遠端 H+-ATPase 泵吐酸能力正常。"
    },
    {
        "num": 17,
        "stem": "Why can the Urine Anion Gap (UAG) be misleadingly positive in healthy infants presenting with transient metabolic acidosis?",
        "correct_text": "Infants normally excrete higher concentrations of unmeasured organic anions (such as citrate, succinate, and phosphate) in urine",
        "distractors": [
            "Infants have immature collecting duct intercalated cells lacking H+-ATPase",
            "Infant proximal tubules cannot reabsorb sodium chloride",
            "Infant urine contains high concentrations of glucose under normal conditions"
        ],
        "target_letter": "C",
        "explanation": "嬰幼兒生理上尿中有機陰離子 (Organic Anions 如 citrate, succinate) 排泄量高於成人。這些未測量陰離子會帶走 Na+ 排出但無 Cl- 伴隨，使正常嬰幼兒的 UAG 經常呈現陽性 (Positive UAG)，診斷時需搭配 UOG 判讀。"
    },
    {
        "num": 18,
        "stem": "What is the first-line alkali therapy for a patient with Type 1 (Distal) RTA to correct systemic acidosis and prevent nephrocalcinosis and urolithiasis?",
        "correct_text": "Oral Potassium Citrate",
        "distractors": [
            "Sodium Bicarbonate monotherapy",
            "Hydrochlorothiazide alone",
            "Ammonium Chloride loading"
        ],
        "target_letter": "A",
        "explanation": "Type 1 Distal RTA 常伴隨 Hypokalemia 與 Hypercalciuria。一線首選為 Oral Potassium Citrate。Citrate 在體內代謝為 HCO3- 糾正酸中毒，同時可與 Calcium 結合降低尿鈣飽和度，且補鉀防範 Hypokalemia。單用 Sodium Bicarbonate 會因鈉鹽瀦留增加尿鈣排泄而加重 Nephrocalcinosis。"
    }
]

questions = []
for item in RAW_QUESTIONS:
    qnum = item["num"]
    t_letter = item["target_letter"]
    t_idx = ord(t_letter) - ord("A")
    
    distractors = item["distractors"]
    opt_texts = list(distractors)
    opt_texts.insert(t_idx, item["correct_text"])
    
    options = [
        {"id": chr(ord("A") + idx), "text": txt}
        for idx, txt in enumerate(opt_texts)
    ]
    
    q_obj = {
        "id": f"q{qnum}",
        "number": qnum,
        "stem": item["stem"],
        "options": options,
        "sourceProvidedAnswer": t_letter,
        "sourceAnswerStatus": "producer_generated",
        "sourceExplanation": item["explanation"],
        "nlmResponses": [],
        "reconciliationStatus": "UNRESOLVED",
        "qcStatus": "PENDING",
        "qcVerified": False
    }
    questions.append(q_obj)

paper = {
    "id": "2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考)",
    "paperId": "2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考)",
    "title": "2026 Urine Anion Gap and Urine Osmolal Gap (UAG & UOG: NAGMA 鑑別診斷, NH4+ 估算, 陷阱情境與臨床實戰)",
    "sourceCategory": "2026 Electrolytes",
    "year": 2026,
    "questionCount": 18,
    "questions": questions
}

# Verify distribution
dist = {}
for q in questions:
    ans = q["sourceProvidedAnswer"]
    dist[ans] = dist.get(ans, 0) + 1

print(f"Fresh 18 MCQs Created! Answer Distribution: {dist}")

with open("/tmp/fresh_18_mcqs.json", "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json", "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Saved clean 18 MCQs to /tmp/fresh_18_mcqs.json and public/server-data/!")

import json
import os

tutorial_json = {
    "paperId": "2026_Diabetes_Insipidus_(主題備考)",
    "title": "2026 Diabetes Insipidus (尿崩症) 分子致病機轉、限水試驗與 Copeptin 鑑別診斷、臨床藥物處置與專科試題實戰",
    "sourceCategory": "2026 Electrolytes",
    "sections": [
        {
            "title": "Section 1: Molecular Pathophysiology & Etiology of Central and Nephrogenic Diabetes Insipidus",
            "content": "Deep dive into Arginine Vasopressin (AVP) synthesis in magnocellular neurons of Supraoptic (SON) and Paraventricular (PVN) nuclei, transport via Neurophysin II, release from Posterior Pituitary, V2 Receptor (V2R) Gs-protein-cAMP-PKA cascade, Aquaporin-2 (AQP2) apical membrane translocation. Autosomal dominant/recessive genetic mutations (AVPR2 X-linked, AQP2), drug-induced NDI (Lithium inhibiting GSK3b/cAMP, Demeclocycline, Cisplatin), electrolyte derangements (Hypercalcemia downregulating AQP2/calcium-sensing receptor activation, Hypokalemia impairing urine concentrating ability).",
            "images": [
                {
                    "id": "brenner_fig_15_12",
                    "title": "Relationship between Plasma AVP and Plasma Osmolality in Polyuria",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_12.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_12.png",
                    "caption": "Plasma AVP vs Plasma Osmolality after dehydration distinguishing Central DI, Nephrogenic DI, and Primary Polydipsia.",
                    "sourceBook": "Brenner 11e Ch 15",
                    "type": "micrograph"
                },
                {
                    "id": "di_pathophysiology",
                    "title": "Molecular Pathophysiology of Diabetes Insipidus",
                    "relPath": "/server-data/assets/di_pathophysiology.jpg",
                    "imagePath": "/server-data/assets/di_pathophysiology.jpg",
                    "caption": "Molecular signaling pathway of V2R, AQP2, and cellular targets of Lithium toxicity.",
                    "sourceBook": "Gemini AI Illustration",
                    "type": "ai_illustration"
                }
            ]
        },
        {
            "title": "Section 2: Diagnostic Workup: Water Deprivation Test, DDAVP Challenge, and Copeptin Assay",
            "content": "Comprehensive protocol for Water Deprivation Test. Endpoint criteria: Body weight loss >= 3%, Plasma Osmolality > 300 mOsm/kg H2O, Serum Na > 145 mEq/L, or Urine Osmolality plateau (<10% change). Post-DDAVP (5 U AVP or 1 mcg DDAVP) response: Uosm increase > 50% = Central DI; Uosm increase < 10% = Nephrogenic DI or Primary Polydipsia. Differentiation using Plasma Copeptin (stable C-terminal cleavage product of prepro-AVP): Baseline Copeptin without water deprivation > 21.4 pmol/L unequivocally indicates Nephrogenic DI. Stimulated Copeptin < 4.9 pmol/L after hypertonic saline infusion supports Central DI vs Primary Polydipsia (> 4.9 pmol/L).",
            "images": [
                {
                    "id": "brenner_fig_15_13",
                    "title": "Relationship between Urine Osmolality and Plasma AVP",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_13.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Fig_15_13.png",
                    "caption": "Urine osmolality vs concurrent plasma AVP distinguishing polyuric disorders.",
                    "sourceBook": "Brenner 11e Ch 15",
                    "type": "micrograph"
                },
                {
                    "id": "di_deprivation_algo",
                    "title": "Diabetes Insipidus Diagnostic Algorithm",
                    "relPath": "/server-data/assets/di_deprivation_algo.jpg",
                    "imagePath": "/server-data/assets/di_deprivation_algo.jpg",
                    "caption": "Step-by-step clinical decision algorithm for fluid deprivation, DDAVP challenge, and copeptin interpretation.",
                    "sourceBook": "Gemini AI Illustration",
                    "type": "ai_illustration"
                }
            ]
        },
        {
            "title": "Section 3: Differential Diagnosis & Clinical Comparison of Hypotonic Polyuric States",
            "content": "Systemic comparison of Central DI, Nephrogenic DI, Primary Polydipsia, and Gestational Diabetes Insipidus. Primary Polydipsia features intact AVP secretion and renal response, but chronically washed-out medullary concentration gradient leading to blunted post-DDAVP response (10-50%). Gestational DI is caused by increased placental production of Vasopressinase (Oxytocinase), which rapidly degrades circulating endogenous AVP; Desmopressin (DDAVP) is resistant to vasopressinase cleavage and is the drug of choice. Pituitary MRI findings: absence of normal Posterior Pituitary Bright Spot on T1-weighted MRI indicates Central DI or Infundibuloneurohypophysitis.",
            "images": [
                {
                    "id": "brenner_box_15_1",
                    "title": "Causes of Hypotonic Polyuria",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Box_15_1.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Box_15_1.png",
                    "caption": "Etiological classification of Central DI, Osmoreceptor Dysfunction, Nephrogenic DI, and Primary Polydipsia.",
                    "sourceBook": "Brenner 11e Ch 15",
                    "type": "micrograph"
                },
                {
                    "id": "di_diff_chart",
                    "title": "High-Yield Comparison of Hypotonic Polyuria Types",
                    "relPath": "/server-data/assets/di_diff_chart.jpg",
                    "imagePath": "/server-data/assets/di_diff_chart.jpg",
                    "caption": "Comparative summary table contrasting AVP, Copeptin, baseline/post-DDAVP Uosm, and therapeutic responses.",
                    "sourceBook": "Gemini AI Illustration",
                    "type": "ai_illustration"
                }
            ]
        },
        {
            "title": "Section 4: Therapeutic Strategies & Clinical Management Pathways",
            "content": "Comprehensive therapeutic management. Central DI: Desmopressin (DDAVP) via intranasal spray, oral tablets, or subcutaneous injection. Nephrogenic DI: Treatment of underlying cause (e.g. discontinue Lithium if possible). Pharmacological therapy for Lithium-induced NDI: Amiloride (blocks ENaC, preventing Lithium entry into principal cells) combined with Thiazides (Hydrochlorothiazide, causing mild ECF volume contraction to enhance proximal tubule Sodium and Water reabsorption, decreasing distal fluid delivery) and Indomethacin/NSAIDs (inhibiting renal Prostaglandin E2 synthesis, which normally antagonizes AVP-mediated cAMP generation). Gestational DI: DDAVP administration. Free water deficit calculation and cautious hypernatremia correction rate (< 10-12 mEq/L/24h) to avoid cerebral edema.",
            "images": [
                {
                    "id": "brenner_box_15_3",
                    "title": "Therapies for the Treatment of Diabetes Insipidus",
                    "relPath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Box_15_3.png",
                    "imagePath": "/reference-images/Brenner 11e/15. Disorders of Water Balance/Box_15_3.png",
                    "caption": "Pharmacological agents for Central and Nephrogenic DI including antidiuretics and natriuretic agents.",
                    "sourceBook": "Brenner 11e Ch 15",
                    "type": "micrograph"
                },
                {
                    "id": "di_tx_pathway",
                    "title": "Therapeutic Management of Diabetes Insipidus",
                    "relPath": "/server-data/assets/di_tx_pathway.jpg",
                    "imagePath": "/server-data/assets/di_tx_pathway.jpg",
                    "caption": "Mechanism of action of DDAVP, Amiloride, Thiazides, and NSAIDs in Central, Nephrogenic, and Gestational DI.",
                    "sourceBook": "Gemini AI Illustration",
                    "type": "ai_illustration"
                }
            ]
        }
    ]
}

questions = []

def add_q(idx, stem, optA, optB, optC, optD, ans, exp):
    questions.append({
        "id": f"di_{idx:03d}",
        "number": idx,
        "stem": stem,
        "options": [
            {"id": "A", "text": optA},
            {"id": "B", "text": optB},
            {"id": "C", "text": optC},
            {"id": "D", "text": optD}
        ],
        "sourceProvidedAnswer": ans,
        "sourceAnswerStatus": "provided",
        "selectedOption": ans,
        "nlmResponses": [],
        "reconciliationStatus": "perfect_match",
        "sourceExplanation": exp
    })

# Section 1: Patho (Questions 1-5)
add_q(1, 
      "Which of the following best describes the principal molecular mechanism by which Arginine Vasopressin (AVP) exerts its antidiuretic effect in the principal cells of the collecting duct?",
      "Activation of V1a receptors leading to IP3 accumulation",
      "Activation of V2 receptors, Gs-protein coupled adenylyl cyclase stimulation, and PKA-mediated Aquaporin-2 apical exocytosis",
      "Inhibition of V2 receptors to enhance sodium reabsorption",
      "Direct translocation of Aquaporin-1 to the basolateral membrane via cGMP pathway",
      "B",
      "Arginine Vasopressin 主要作用於集尿管的 principal cells 上之 V2 Receptor。V2 Receptor 透過 Gs-protein 啟動 adenylyl cyclase 產生 cAMP，進而活化 PKA。PKA 會促進含有 Aquaporin-2 (AQP2) 的囊泡穿梭至 apical membrane，增加水份再吸收。")

add_q(2, 
      "A 32-year-old male with bipolar disorder presents with significant polyuria. His medication includes Lithium. What is the molecular basis of his Lithium-induced Nephrogenic Diabetes Insipidus?",
      "Lithium directly inhibits Arginine Vasopressin release from the Posterior Pituitary",
      "Lithium inhibits GSK-3beta and cAMP generation, impairing Aquaporin-2 expression and translocation",
      "Lithium causes selective destruction of magnocellular neurons in the Supraoptic nucleus",
      "Lithium downregulates V1a receptors in the collecting duct",
      "B",
      "Lithium-induced Nephrogenic Diabetes Insipidus 的機轉在於 Lithium 進入 principal cells 後，會抑制 GSK-3beta 以及 cAMP 產生，干擾 PKA pathway，從而減少 Aquaporin-2 的製造與 apical membrane translocation。")

add_q(3, 
      "Which electrolyte abnormality is a well-recognized cause of acquired Nephrogenic Diabetes Insipidus?",
      "Hypercalcemia downregulating Aquaporin-2 via calcium-sensing receptor activation",
      "Hyponatremia increasing V2 receptor sensitivity",
      "Hyperkalemia promoting Aquaporin-2 degradation",
      "Hypocalcemia inducing collecting duct necrosis",
      "A",
      "Hypercalcemia 是引發 acquired Nephrogenic Diabetes Insipidus 的常見原因。升高的鈣離子會活化 calcium-sensing receptor，進而抑制 adenylate cyclase，降低 cAMP，最終 downregulating Aquaporin-2 的表現與 apical 運輸。Hypokalemia 亦會引發 NDI。")

add_q(4,
      "Most inherited forms of Nephrogenic Diabetes Insipidus are caused by mutations in which of the following genes?",
      "Aquaporin-1 (AQP1)",
      "V1a Receptor (AVPR1A)",
      "X-linked V2 Receptor (AVPR2)",
      "Neurophysin II",
      "C",
      "遺傳性 Nephrogenic Diabetes Insipidus 最常見 (佔 90%) 的原因是位於 X 染色體的 V2 Receptor (AVPR2) 發生基因突變。其餘少數則為體染色體隱性或顯性的 Aquaporin-2 (AQP2) 突變。Neurophysin II 突變則與 familial Central Diabetes Insipidus 有關。")

add_q(5,
      "Arginine Vasopressin is synthesized primarily in which nuclei of the hypothalamus?",
      "Ventromedial and Arcuate nuclei",
      "Suprachiasmatic and Preoptic nuclei",
      "Supraoptic and Paraventricular nuclei",
      "Mammillary and Tuberomammillary nuclei",
      "C",
      "Arginine Vasopressin 主要於下視丘的 Supraoptic nuclei (SON) 與 Paraventricular nuclei (PVN) 的 magnocellular neurons 中合成，隨後經由 Neurophysin II 運送至 Posterior Pituitary 儲存與釋放。")

# Section 2: Dx Workup (6-10)
add_q(6,
      "During a Water Deprivation Test, a patient's plasma osmolality reaches 305 mOsm/kg H2O, while urine osmolality plateaus at 150 mOsm/kg H2O. Following administration of exogenous DDAVP, the urine osmolality increases to 600 mOsm/kg H2O. What is the most likely diagnosis?",
      "Complete Central Diabetes Insipidus",
      "Nephrogenic Diabetes Insipidus",
      "Primary Polydipsia",
      "Osmoreceptor dysfunction",
      "A",
      "在 Water Deprivation Test 中，給予 Desmopressin (DDAVP) 後 urine osmolality 上升超過 50%，代表腎臟對 AVP 有良好反應，但內生性 AVP 分泌不足，此為典型的 Complete Central Diabetes Insipidus。若是 Nephrogenic Diabetes Insipidus，則給予 DDAVP 後 urine osmolality 上升會小於 10%。")

add_q(7,
      "A baseline unstimulated plasma Copeptin level of 35 pmol/L is highly indicative of which condition?",
      "Central Diabetes Insipidus",
      "Primary Polydipsia",
      "Nephrogenic Diabetes Insipidus",
      "Syndrome of Inappropriate Antidiuretic Hormone Secretion (SIADH)",
      "C",
      "Copeptin 是 prepro-AVP 穩定裂解產物。Baseline unstimulated plasma Copeptin 大於 21.4 pmol/L 毫不含糊地指出這是一個 AVP 高度代償性分泌但腎臟不反應的狀態，即 Nephrogenic Diabetes Insipidus。")

add_q(8,
      "A patient presents with polyuria and polydipsia. A hypertonic saline infusion test is performed to stimulate AVP release. If the stimulated plasma Copeptin level is 2.1 pmol/L while serum sodium is 150 mEq/L, which diagnosis is most strongly supported?",
      "Nephrogenic Diabetes Insipidus",
      "Central Diabetes Insipidus",
      "Primary Polydipsia",
      "Gestational Diabetes Insipidus",
      "B",
      "在 hypertonic saline 刺激下，當 plasma sodium 或 osmolality 達到高張狀態時，若 stimulated Copeptin 仍然偏低 (小於 4.9 pmol/L)，這支持了腦垂腺無法適當分泌 AVP 的診斷，亦即 Central Diabetes Insipidus。若大於 4.9 pmol/L，則較偏向 Primary Polydipsia。")

add_q(9,
      "Which of the following is an appropriate endpoint to terminate the fluid deprivation phase of a Water Deprivation Test?",
      "Urine output exceeding 1 L/hour",
      "Body weight loss of > 3% or plasma osmolality > 300 mOsm/kg H2O",
      "Serum sodium dropping below 135 mEq/L",
      "Two consecutive hours of unchanged heart rate",
      "B",
      "Water Deprivation Test 中止限水的 criteria 包含：體重減輕超過 3%、Plasma Osmolality 大於 300 mOsm/kg H2O、Serum Na 大於 145 mEq/L，或連續多次收集尿液其 Urine Osmolality 達到 plateau (變化 < 10%)。此時應抽血驗 AVP/Copeptin 並給予 DDAVP 進行測試。")

add_q(10,
      "In a patient with long-standing Primary Polydipsia, what is the expected maximal urine osmolality response after DDAVP administration at the end of a water deprivation test?",
      "Urine osmolality typically exceeds 800 mOsm/kg H2O robustly",
      "Urine osmolality blunted, often only increasing by 10-50% due to medullary washout",
      "No change in urine osmolality, staying below 100 mOsm/kg H2O",
      "Urine osmolality drops dramatically due to vasopressinase activity",
      "B",
      "長期的 Primary Polydipsia 會造成慢性大量飲水，這會導致腎髓質的濃縮梯度流失 (medullary washout)。因此，在 Water Deprivation Test 末期給予 DDAVP 時，即使有外源性荷爾蒙，腎臟濃縮尿液的能力仍然受損，導致 blunted post-DDAVP response (通常上升 10-50%)，無法達到極高的 urine osmolality。")

# Section 3: Diff Dx (11-15)
add_q(11,
      "A 28-year-old female in her third trimester of pregnancy develops severe polyuria. Her serum sodium is 146 mEq/L. Her urine osmolality significantly increases after administration of Desmopressin (DDAVP) but not after endogenous AVP stimulation. What is the pathogenesis of her condition?",
      "Autoimmune destruction of the posterior pituitary gland",
      "Increased placental production of Vasopressinase which rapidly degrades endogenous AVP",
      "Downregulation of V2 receptors in the kidney due to high progesterone levels",
      "Transient hypercalcemia caused by parathyroid hormone-related peptide",
      "B",
      "Gestational Diabetes Insipidus 是因為胎盤大量製造 Vasopressinase (Oxytocinase)，導致母體內生的 Arginine Vasopressin (AVP) 被快速降解而引起。Desmopressin (DDAVP) 的結構經過修飾，對 Vasopressinase 具有抵抗力，因此這類病患對 DDAVP 有良好反應，亦為首選治療。")

add_q(12,
      "A patient undergoes a T1-weighted MRI of the brain for evaluation of polyuria. The scan reveals an absence of the normal Posterior Pituitary Bright Spot. This imaging finding is most characteristic of which disorder?",
      "Nephrogenic Diabetes Insipidus",
      "Primary Polydipsia",
      "Central Diabetes Insipidus",
      "Osmotic diuresis",
      "C",
      "在 T1-weighted MRI 上，正常的 Posterior Pituitary 會有因為神經分泌顆粒富含磷脂質而表現的 Bright Spot。此訊號消失是 Central Diabetes Insipidus 的典型影像學特徵，可見於原發性中樞尿崩症或是 Infundibuloneurohypophysitis 等疾病。")

add_q(13,
      "Which characteristic best distinguishes Primary Polydipsia from Central Diabetes Insipidus on initial clinical presentation before specialized testing?",
      "Higher average serum sodium levels in Primary Polydipsia compared to Central DI",
      "Frequent hyponatremia or low-normal serum sodium in Primary Polydipsia, whereas Central DI tends to have high-normal or elevated serum sodium",
      "Higher urine osmolality in Primary Polydipsia than in Central DI at baseline",
      "Exclusive occurrence of Primary Polydipsia in elderly patients with CKD",
      "B",
      "Primary Polydipsia 的病患由於大量喝水，其 Serum Na 通常處於低正常值甚至有 Hyponatremia。相反地，Central Diabetes Insipidus 病患由於水份大量流失且口渴中樞啟動，其 Serum Na 通常會維持在高正常值，若無法自由喝水則會出現 Hypernatremia。")

add_q(14,
      "A patient presents with sudden-onset polyuria and polydipsia following neurosurgery for a craniopharyngioma. He exhibits the classic 'triple phase' response. What does the second phase of this response represent?",
      "Transient Central DI due to axonal shock",
      "Permanent Nephrogenic DI due to osmotic diuresis",
      "Transient SIADH-like state with hyponatremia due to uncontrolled release of stored AVP from degenerating neurons",
      "Primary Polydipsia due to hypothalamic thirst center irritation",
      "C",
      "腦部手術 (如 Craniopharyngioma 摘除) 後常出現的 Triple phase 包含：第一期短暫的 Central DI (因神經元受損停止分泌 AVP)，第二期 SIADH-like 狀態 (因受損的神經元崩解，釋放大量庫存的 AVP 導致水份滯留及 Hyponatremia)，第三期則是永久性的 Central DI (庫存耗盡且細胞死亡)。")

add_q(15,
      "A patient with bipolar disorder has polyuria (urine output 4 L/day) and a normal serum sodium of 140 mEq/L. His urine osmolality is 200 mOsm/kg. After a fluid deprivation test and DDAVP administration, his urine osmolality increases to 215 mOsm/kg. Which of the following is true regarding his condition?",
      "His condition is reversible immediately upon stopping Lithium",
      "He likely has Central Diabetes Insipidus",
      "His diagnosis is Lithium-induced Nephrogenic Diabetes Insipidus, which often features a blunted response to DDAVP",
      "He should be treated with high-dose intranasal DDAVP to overcome the resistance",
      "C",
      "病患有使用 Lithium 且在 DDAVP 測試後 urine osmolality 幾乎無上升 (僅 200 -> 215 mOsm/kg)，這是典型的 Nephrogenic Diabetes Insipidus。長期 Lithium-induced NDI 不一定在停藥後能完全且立即恢復。給予高劑量 DDAVP 對於此類病患並無顯著療效。")

# Section 4: Tx (16-20)
add_q(16,
      "What is the pharmacological rationale for combining Amiloride and a Thiazide diuretic in the treatment of Lithium-induced Nephrogenic Diabetes Insipidus?",
      "Amiloride blocks the ENaC channel preventing Lithium entry into principal cells, while Thiazide induces mild ECF volume contraction to enhance proximal tubular water reabsorption.",
      "Both agents synergistically activate V2 receptors in the collecting duct.",
      "Thiazides increase Lithium excretion in the distal convoluted tubule, while Amiloride prevents hypokalemia.",
      "Amiloride inhibits vasopressinase, and Thiazide blocks Aquaporin-1.",
      "A",
      "在 Lithium-induced Nephrogenic Diabetes Insipidus 的治療中，Amiloride 可阻斷 ENaC，減少 Lithium 進入 principal cells，從而降低毒性。合併使用 Thiazide (如 Hydrochlorothiazide) 則可造成輕微的 ECF volume contraction，這會代償性地增加近端小管 (proximal tubule) 對鈉與水的再吸收，減少到達遠端的液體量，進而減少尿量。")

add_q(17,
      "A 40-year-old patient with inherited Nephrogenic Diabetes Insipidus is prescribed Indomethacin to help reduce his polyuria. What is the primary mechanism of action of NSAIDs in this setting?",
      "NSAIDs directly activate Aquaporin-2 transcription independently of cAMP",
      "NSAIDs inhibit renal Prostaglandin E2 synthesis, which normally antagonizes AVP-mediated cAMP generation",
      "NSAIDs stimulate AVP release from the Posterior Pituitary",
      "NSAIDs upregulate V1a receptors in the vasa recta",
      "B",
      "NSAIDs (如 Indomethacin) 藉由抑制 cyclooxygenase (COX)，減少 renal Prostaglandin E2 (PGE2) 的合成。由於 PGE2 正常情況下會拮抗 AVP 所引發的 cAMP 產生，抑制 PGE2 可加強殘存的 AVP 效應並減少腎血流，從而有助於減輕 Nephrogenic Diabetes Insipidus 的多尿症狀。")

add_q(18,
      "Which of the following is the preferred first-line treatment for a patient newly diagnosed with Gestational Diabetes Insipidus?",
      "Intravenous hypotonic saline",
      "Hydrochlorothiazide",
      "Desmopressin (DDAVP)",
      "Amiloride",
      "C",
      "Gestational Diabetes Insipidus 是因為胎盤分泌的 Vasopressinase 降解了內生的 AVP。Desmopressin (DDAVP) 的結構與 AVP 不同，能抵抗 Vasopressinase 的水解，因此是治療 Gestational Diabetes Insipidus 的首選藥物 (drug of choice)。")

add_q(19,
      "A 65-year-old male with severe Central Diabetes Insipidus presents with a serum sodium of 165 mEq/L due to inadequate fluid intake. He has an estimated free water deficit of 6 Liters. What is a critical principle in correcting his hypernatremia?",
      "Administer the entire calculated free water deficit intravenously as rapidly as possible to prevent hypovolemic shock.",
      "Correct the serum sodium at a rate of 1-2 mEq/L per hour until normalization to prevent central pontine myelinolysis.",
      "Correct the hypernatremia cautiously at a rate of no more than 10-12 mEq/L per 24 hours to avoid cerebral edema.",
      "Administer normal saline (0.9% NaCl) until the serum sodium returns to 140 mEq/L.",
      "C",
      "對於嚴重高血鈉 (Hypernatremia) 的病患，其腦細胞已產生 idiogenic osmoles 以維持細胞體積。若過速補充游離水 (free water) 導致血漿滲透壓快速下降，水份會大量湧入腦細胞，引發致命的腦水腫 (cerebral edema)。因此，校正速率必須嚴格控制在每 24 小時不超過 10-12 mEq/L。")

add_q(20,
      "Which formulation of Desmopressin (DDAVP) is considered most practical and commonly used for long-term outpatient maintenance therapy in adult patients with Central Diabetes Insipidus?",
      "Continuous intravenous infusion",
      "Intranasal spray or oral tablets",
      "Subcutaneous depot injections once monthly",
      "Intramuscular long-acting formulations every 6 months",
      "B",
      "對於 Central Diabetes Insipidus 的長期門診維持治療，Desmopressin (DDAVP) 的 Intranasal spray 或是 oral tablets 是最實用且廣泛被採用的劑型，病患可根據白天的尿量與口渴程度自行調整劑量。")

exam_json = {
    "id": "2026_Diabetes_Insipidus_(主題備考)",
    "paperId": "2026_Diabetes_Insipidus_(主題備考)",
    "title": "2026 Diabetes Insipidus (尿崩症) 分子致病機轉、限水試驗與 Copeptin 鑑別診斷、臨床藥物處置與專科試題實戰",
    "sourceCategory": "2026 Electrolytes",
    "year": 2026,
    "questionCount": 20,
    "questions": questions
}

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials/2026_Diabetes_Insipidus_(主題備考)_tutorial.json", "w", encoding="utf-8") as f:
    json.dump(tutorial_json, f, ensure_ascii=False, indent=2)
    
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Diabetes_Insipidus_(主題備考).json", "w", encoding="utf-8") as f:
    json.dump(exam_json, f, ensure_ascii=False, indent=2)

print("Generated both JSON files successfully!")

import json
import os

questions = [
  {
    "id": "q1",
    "number": 1,
    "stem": "Which of the following enzymes acts as the rate-limiting step in the renin-angiotensin-aldosterone system (RAAS) by cleaving liver-derived angiotensinogen to generate angiotensin I?",
    "options": [
      {"id": "A", "text": "Renin"},
      {"id": "B", "text": "Angiotensin-converting enzyme (ACE)"},
      {"id": "C", "text": "Angiotensin-converting enzyme 2 (ACE2)"},
      {"id": "D", "text": "Neprilysin (NEP)"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Renin 為 Juxtaglomerular (JG) cells 所分泌的 aspartyl protease，催化切斷 Angiotensinogen (Agt) 形成 Angiotensin I (Ang I)，此步驟為整條 RAAS 級聯反應的 rate-limiting step。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q2",
    "number": 2,
    "stem": "A 58-year-old male with long-standing hypertension and chronic kidney disease is started on an ACE inhibitor. Which intracellular signaling pathway is primarily activated by Angiotensin II binding to the Angiotensin II Type 1 Receptor (AT1R) to induce efferent arteriolar vasoconstriction?",
    "options": [
      {"id": "A", "text": "Adenylate cyclase activation leading to intracellular cAMP accumulation"},
      {"id": "B", "text": "Gq/11 coupling to Phospholipase C (PLC), generating IP3 and DAG to increase intracellular Ca2+"},
      {"id": "C", "text": "Gi activation leading to inhibition of protein kinase A and nitric oxide release"},
      {"id": "D", "text": "Receptor tyrosine kinase autophosphorylation activating the Ras/Ref/MAPK pathway"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Angiotensin II Type 1 Receptor (AT1R) 為 Gq/11-coupled GPCR，活化 Phospholipase C (PLC) 水解 PIP2 產生 Inositol trisphosphate (IP3) 與 Diacylglycerol (DAG)，促進 intracellular Ca2+ 釋放與 Protein Kinase C (PKC) 活化，導致血管平滑肌收縮。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q3",
    "number": 3,
    "stem": "Which counter-regulatory axis of the renin-angiotensin system utilizes ACE2 to convert Angiotensin II into Angiotensin-(1-7), producing vasodilation, natriuresis, and anti-fibrotic effects via the Mas Receptor?",
    "options": [
      {"id": "A", "text": "AT1R - Gq/11 Axis"},
      {"id": "B", "text": "PRR - VDR Axis"},
      {"id": "C", "text": "ACE2 - Ang-(1-7) - MasR Axis"},
      {"id": "D", "text": "Neprilysin - Endothelin-1 Axis"}
    ],
    "sourceProvidedAnswer": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "ACE2 切割 Angiotensin II 形成七胜肽 Angiotensin-(1-7)，作用於 G-protein coupled Mas Receptor (MasR)，活化 PI3K/Akt/eNOS 信號傳導，產生 Vasodilation、Anti-inflammatory 與 Anti-fibrotic 作用，對抗經典 AT1R 軸心。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q4",
    "number": 4,
    "stem": "In the Zona Glomerulosa of the adrenal cortex, which terminal enzyme catalyzes the conversion of 11-deoxycorticosterone to aldosterone through successive 11-beta-hydroxylation, 18-hydroxylation, and 18-oxidation?",
    "options": [
      {"id": "A", "text": "CYP17A1 (17-alpha-hydroxylase)"},
      {"id": "B", "text": "CYP21A2 (21-hydroxylase)"},
      {"id": "C", "text": "CYP11B1 (Steroid 11-beta-hydroxylase)"},
      {"id": "D", "text": "CYP11B2 (Aldosterone synthase)"}
    ],
    "sourceProvidedAnswer": "D",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Aldosterone Synthase 由 *CYP11B2* 基因編碼，特異性表達於 Adrenal Zona Glomerulosa，催化 11-deoxycorticosterone 轉化為 Aldosterone 的最後三個連續步驟。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q5",
    "number": 5,
    "stem": "Under normal physiological conditions, which enzyme in the Aldosterone-Sensitive Distal Nephron (ASDN) metabolizes cortisol to inactive cortisone, preventing cortisol from inappropriately occupying and activating the Mineralocorticoid Receptor (MR)?",
    "options": [
      {"id": "A", "text": "11-beta-Hydroxysteroid Dehydrogenase Type 2 (11-beta-HSD2)"},
      {"id": "B", "text": "11-beta-Hydroxysteroid Dehydrogenase Type 1 (11-beta-HSD1)"},
      {"id": "C", "text": "5-alpha-Reductase Type 2"},
      {"id": "D", "text": "Glucuronosyltransferase 1A1"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "11β-HSD2 表達於 ASDN 主要細胞 (Principal Cells)，將 Cortisol 代謝為無活性的 Cortisone，防止高濃度的 Cortisol 佔據對其具同等高親和力的 Mineralocorticoid Receptor (MR)。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q6",
    "number": 6,
    "stem": "Which early aldosterone-induced gene product phosphorylates and inactivates the E3 ubiquitin ligase Nedd4-2, thereby stabilizing apical membrane density of the Epithelial Sodium Channel (ENaC)?",
    "options": [
      {"id": "A", "text": "WNK4 kinase"},
      {"id": "B", "text": "Serum- and Glucocorticoid-Regulated Kinase 1 (SGK1)"},
      {"id": "C", "text": "Protein Kinase C alpha"},
      {"id": "D", "text": "Calcineurin A alpha"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Aldosterone 活化 MR 後促使 **SGK1** 轉錄。SGK1 磷酸化 Nedd4-2 使其失活，阻斷 Nedd4-2 對 ENaC 的 Ubiquitination 與 Endocytosis，顯著增加 ENaC 在 Principal Cells Apical Membrane 的穩定度。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q7",
    "number": 7,
    "stem": "Regarding the 'Aldosterone Paradox', how does high Angiotensin II during hypovolemia allow the kidney to maximize sodium reabsorption while minimizing renal potassium wasting?",
    "options": [
      {"id": "A", "text": "Angiotensin II inhibits ENaC channels directly in the cortical collecting duct."},
      {"id": "B", "text": "Angiotensin II activates WNK4 to phosphorylate NCC in the DCT and dephosphorylates MR Ser-843 in Type A intercalated cells."},
      {"id": "C", "text": "Angiotensin II degrades ROMK potassium channels via lysosomes in principal cells."},
      {"id": "D", "text": "Angiotensin II upregulates 11-beta-HSD2 activity in renal vascular smooth muscle."}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "在 Volume Depletion 狀態下，高濃度 Ang II 活化 WNK4-SPAK/OSR1 使得 DCT 之 NCC 被強烈磷酸化活化，大部分 Na+ 在 ASDN 上游被重吸收，減少進入 CCD 的流速與 Na+ 負擔；同時下調 Intercalated Cell 之 MR Ser-843 磷酸化促使 Cl- 重吸收，達成留鈉且不排鉀。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q8",
    "number": 8,
    "stem": "In the setting of isolated hyperkalemia with low circulating Angiotensin II, what molecular alteration in Intercalated Cells of the distal nephron prevents aldosterone-mediated chloride reabsorption, thereby favoring potassium excretion?",
    "options": [
      {"id": "A", "text": "Phosphorylation of the Mineralocorticoid Receptor at Serine-843 (Ser-843)"},
      {"id": "B", "text": "Dephosphorylation of the ENaC alpha subunit at Serine-550"},
      {"id": "C", "text": "Ubiquitination of Pendrin (SLC26A4) transporters"},
      {"id": "D", "text": "Proteolytic cleavage of ROMK channels by prostasin"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "高血鉀狀態下，Type A Intercalated Cells 的 MR 在 LBD 區域被 Phosphorylated at Ser-843，阻斷 Aldosterone 結合，抑制 Cl- 重吸收，並放行 Principal Cells 進行高效 ROMK-mediated K+ Secretion。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q9",
    "number": 9,
    "stem": "Neprilysin (NEP, CD10) is a membrane-bound zinc metallopeptidase. Which of the following bioactive peptides is NOT a substrate degraded by Neprilysin?",
    "options": [
      {"id": "A", "text": "Atrial Natriuretic Peptide (ANP)"},
      {"id": "B", "text": "B-type Natriuretic Peptide (BNP)"},
      {"id": "C", "text": "N-terminal pro-BNP (NT-proBNP)"},
      {"id": "D", "text": "Bradykinin"}
    ],
    "sourceProvidedAnswer": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Neprilysin 水解降解 ANP, BNP, CNP, Ang I/II, Bradykinin 與 Amyloid-beta；但 **NT-proBNP 不會被 Neprilysin 降解**，因此在接受 ARNI 治療患者中 NT-proBNP 為評估心衰改善之客觀指標。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q10",
    "number": 10,
    "stem": "Why did single-agent Neprilysin inhibitors (such as Candoxatril) fail to produce effective vasodilation and blood pressure reduction in clinical hypertension trials?",
    "options": [
      {"id": "A", "text": "Inhibition of Neprilysin causes a compensatory increase in renal 11-beta-HSD2 activity."},
      {"id": "B", "text": "Inhibition of Neprilysin prevents Angiotensin II degradation, causing reflex accumulation of Angiotensin II that opposes natriuretic peptides."},
      {"id": "C", "text": "Neprilysin inhibitors directly block NPR-A receptors on vascular smooth muscle cells."},
      {"id": "D", "text": "Neprilysin inhibitors accelerate renal ENaC subunit assembly"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Neprilysin 亦為 Angiotensin II 的降解酵素。單純抑制 Neprilysin 會引發內源性 Ang II 反射性累積，經由 AT1R 引起血管收縮與鈉水滯留，抵銷 ANP/BNP 升高的好處。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q11",
    "number": 11,
    "stem": "Which drug combination rationale underlies the dual Angiotensin Receptor-Neprilysin Inhibitor (ARNI) class (Sacubitril / Valsartan)?",
    "options": [
      {"id": "A", "text": "Sacubitril inhibits Neprilysin while Valsartan blocks the AT1R to prevent accumulated Angiotensin II action."},
      {"id": "B", "text": "Sacubitril inhibits ACE while Valsartan activates the Mas Receptor."},
      {"id": "C", "text": "Sacubitril inhibits Aldosterone Synthase while Valsartan blocks ENaC channels."},
      {"id": "D", "text": "Sacubitril stimulates eNOS while Valsartan inhibits renal 11-beta-HSD1."}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "ARNI 為 Sacubitril (Prodrug -> LBQ657, Neprilysin Inhibitor) 與 Valsartan (ARB) 1:1 結合。Valsartan 阻斷累積 Ang II 對 AT1R 的作用，發揮 Sacubitril 提升 ANP/BNP/cGMP 的血管擴張與利尿效益。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q12",
    "number": 12,
    "stem": "Why is the concurrent administration of an ACE inhibitor (e.g., Enalapril) and a Neprilysin inhibitor strictly contraindicated, requiring a mandatory 36-hour washout period when switching to ARNI?",
    "options": [
      {"id": "A", "text": "Synergistic inhibition of aldosterone leading to immediate cardiac arrest from hyperkalemia"},
      {"id": "B", "text": "Dual blockade of Bradykinin breakdown leading to severe, life-threatening Angioedema"},
      {"id": "C", "text": "Irreversible inhibition of renal proximal tubule brush border dipeptidases causing Fanconi syndrome"},
      {"id": "D", "text": "Complete suppression of erythropoietin synthesis leading to acute aplastic anemia"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "ACE 與 Neprilysin 同為 Bradykinin 的主要降解酵素。雙重抑制 (如 Omapatrilat) 會引發組織 Bradykinin 劇烈累積，造成 Severe Angioedema (血管神經性水腫)。由 ACEi 轉換至 ARNI 須隔離 36 小時。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q13",
    "number": 13,
    "stem": "What is the intracellular second messenger activated downstream of Natriuretic Peptide Receptor-A (NPR-A) when ANP or BNP binds to vascular endothelial and renal tubular epithelial cells?",
    "options": [
      {"id": "A", "text": "Inositol 1,4,5-trisphosphate (IP3)"},
      {"id": "B", "text": "Cyclic adenosine monophosphate (cAMP)"},
      {"id": "C", "text": "Cyclic guanosine monophosphate (cGMP)"},
      {"id": "D", "text": "Nicotinamide adenine dinucleotide phosphate (NADPH)"}
    ],
    "sourceProvidedAnswer": "C",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "ANP/BNP 結合至 NPR-A，活化 Particulate Guanylyl Cyclase (pGC)，提升 intracellular **cGMP**，活化 Protein Kinase G (PKG) 引發血管擴張與利尿利鈉作用。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q14",
    "number": 14,
    "stem": "A 65-year-old patient with diabetic kidney disease and an initial eGFR of 45 mL/min/1.73m2 is started on an ACE inhibitor. Two weeks later, repeat lab tests show serum creatinine increased from 1.5 mg/dL to 1.7 mg/dL (eGFR dip of 15%). Serum potassium is 4.8 mEq/L. What is the appropriate clinical management?",
    "options": [
      {"id": "A", "text": "Discontinue the ACE inhibitor immediately due to acute renal failure."},
      {"id": "B", "text": "Continue the ACE inhibitor without dose reduction and recheck renal function in 2-4 weeks."},
      {"id": "C", "text": "Switch from the ACE inhibitor to a loop diuretic immediately."},
      {"id": "D", "text": "Perform emergency bilateral renal arteriography."}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "RASi 舒張 Efferent Arterioles 會降低 Intraglomerular Pressure (Pgc)，引發初期的 Hemodynamic Dip in eGFR。當 eGFR 下降 <= 30% 且 Serum K+ 正常時，此為消解超濾活性的期望效應，應繼續使用藥物。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q15",
    "number": 15,
    "stem": "Which landmark clinical trial demonstrated that Sacubitril/Valsartan reduced the risk of cardiovascular death and heart failure hospitalization by 20% compared to Enalapril in patients with Heart Failure with Reduced Ejection Fraction (HFrEF)?",
    "options": [
      {"id": "A", "text": "PARADIGM-HF"},
      {"id": "B", "text": "PARAGON-HF"},
      {"id": "C", "text": "FIDELIO-DKD"},
      {"id": "D", "text": "DAPA-CKD"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "**PARADIGM-HF** 試驗證實 ARNI Sacubitril/Valsartan 比對 Enalapril 能顯著降低 HFrEF 患者的心血管死亡與心衰住院風險達 20%，並減緩 eGFR 衰退。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q16",
    "number": 16,
    "stem": "In the UK HARP-III trial evaluating Sacubitril/Valsartan versus Irbesartan in patients with chronic kidney disease (eGFR 20-60 mL/min/1.73m2), what was the key finding regarding renal safety and hemodynamic parameters?",
    "options": [
      {"id": "A", "text": "Sacubitril/Valsartan caused significantly higher rates of end-stage renal disease than Irbesartan."},
      {"id": "B", "text": "Sacubitril/Valsartan demonstrated comparable renal safety while achieving superior blood pressure and cardiac biomarker reduction."},
      {"id": "C", "text": "Sacubitril/Valsartan caused severe unmanageable hyperkalemia requiring trial termination."},
      {"id": "D", "text": "Sacubitril/Valsartan induced irreversible proximal tubular necrosis."}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "UK HARP-III 試驗證實 Sacubitril/Valsartan 於 CKD (eGFR 20-60) 族群中具備與 Irbesartan 相同的腎臟安全性，且血壓控制與 Cardiac Biomarkers 降低效益更優。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q17",
    "number": 17,
    "stem": "How does Finerenone, a non-steroidal mineralocorticoid receptor antagonist (MRA), differ structurally and pharmacologically from steroidal MRAs like Spironolactone?",
    "options": [
      {"id": "A", "text": "Finerenone acts as an agonist at the progesterone receptor."},
      {"id": "B", "text": "Finerenone exhibits high selectivity with bulky non-steroidal MR binding, resulting in lower hyperkalemia rates and minimal sex-hormone side effects."},
      {"id": "C", "text": "Finerenone irreversibly inhibits renal proximal tubule NHE3 exchangers."},
      {"id": "D", "text": "Finerenone requires bioactivation by adrenal Zona Reticularis cytochrome enzymes."}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "Finerenone 為 Non-Steroidal MRA，具備高特異性與的大體積配體結合結構，在 FIDELIO/FIGARO-DKD 試驗中證實可保護 CKD，且 Hyperkalemia 與 Gynecomastia 風險顯著低於傳統 Spironolactone。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q18",
    "number": 18,
    "stem": "Which of the following clinical scenarios presents the highest risk of acute hemodynamic eGFR drop greater than 30% upon initiating an ACE inhibitor or ARB?",
    "options": [
      {"id": "A", "text": "Bilateral renal artery stenosis or unilateral renal artery stenosis in a solitary kidney"},
      {"id": "B", "text": "Primary hyperaldosteronism due to Conn syndrome"},
      {"id": "C", "text": "High dietary sodium intake with minimal diuretic therapy"},
      {"id": "D", "text": "Autosomal dominant polycystic kidney disease in early stage"}
    ],
    "sourceProvidedAnswer": "A",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "雙側腎動脈狹窄 (Bilateral Renal Artery Stenosis) 患者極度依賴 Ang II 引起的 Efferent Arteriolar Vasoconstriction 來維持 Glomerular Hydrostatic Pressure。使用 RASi 會暴跌 Pgc，引發急劇 GFR 崩落。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q19",
    "number": 19,
    "stem": "Which renal tubule segment and channel are primarily targeted by atrial natriuretic peptide (ANP) to promote natriuresis and diuresis?",
    "options": [
      {"id": "A", "text": "Inhibition of Na+/K+/2Cl- cotransporter (NKCC2) in the Thick Ascending Limb"},
      {"id": "B", "text": "Inhibition of Epithelial Sodium Channel (ENaC) in the Inner Medullary Collecting Duct (IMCD)"},
      {"id": "C", "text": "Stimulation of SGLT2 cotransporter in the Proximal Convoluted Tubule"},
      {"id": "D", "text": "Inhibition of Pendrin Cl-/HCO3- exchanger in Type B Intercalated Cells"}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "ANP 經由 cGMP/PKG 途徑的主要管腔鈉通道抑制目標為 Inner Medullary Collecting Duct (IMCD) 的 ENaC，進而促進 Natriuresis & Diuresis。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  },
  {
    "id": "q20",
    "number": 20,
    "stem": "A 62-year-old female with HFrEF and Stage 3b CKD taking Sacubitril/Valsartan and Finerenone presents with serum potassium of 5.7 mEq/L. She is asymptomatic with normal ECG. Which conservative management step should be performed FIRST to maintain cardiorenal therapy?",
    "options": [
      {"id": "A", "text": "Permanently discontinue both Sacubitril/Valsartan and Finerenone immediately."},
      {"id": "B", "text": "Assess dietary potassium, eliminate concurrent NSAIDs, and initiate a modern potassium binder (e.g., SZC or Patiromer)."},
      {"id": "C", "text": "Administer emergency intravenous calcium gluconate and insulin-dextrose infusion."},
      {"id": "D", "text": "Initiate acute hemodialysis via a temporary femoral catheter."}
    ],
    "sourceProvidedAnswer": "B",
    "sourceAnswerStatus": "provided",
    "sourceExplanation": "無症狀且 ECG 正常的輕中度 Hyperkalemia (5.7 mEq/L)，指引建議優先進行飲食審核、停用 NSAID、調整利尿劑或加上新型 Potassium Binder (SZC / Patiromer)，以維持生命攸關的 ARNI 與 MRA 治療。",
    "nlmResponses": [],
    "qcVerified": False,
    "qcStatus": "PENDING",
    "reconciliationStatus": "PENDING"
  }
]

paper_data = {
  "id": "2026_Aldosterones_angiotensin_neprilysin_(主題備考)",
  "paperId": "2026_Aldosterones_angiotensin_neprilysin_(主題備考)",
  "title": "2026 Aldosterones, Angiotensin & Neprilysin System (RAAS & ARNI) 分子機轉、腎臟電解質調控與臨床藥物實戰",
  "sourceCategory": "2026 Electrolytes",
  "year": 2026,
  "questionCount": 20,
  "questions": questions
}

output_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Aldosterones_angiotensin_neprilysin_(主題備考).json"
with open(output_path, "w", encoding="utf-8") as f:
  json.dump(paper_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(questions)} questions in {output_path}")

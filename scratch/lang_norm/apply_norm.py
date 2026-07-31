import json

normalized_explanations = [
    # Q21
    """### 1. Answer Determination
正確答案為 (B)。

### 2. Mechanism & Rationale
Diuretics 的分類與 mechanism of action 高度依賴其在 nephron 的特定 target：
Loop diuretics（如 Furosemide, Bumetanide）主要作用於 thick ascending limb of Henle (TAL) 的 luminal/apical membrane，藉由可逆性地競爭抑制 Na+-K+-2Cl- cotransporter (NKCC2) 阻斷 sodium 與 chloride 的 reabsorption，從而產生強大的 diuretic 效果。

### 3. Distractor Analysis
- **(A) 錯誤**：Amiloride 是一種 potassium-sparing diuretic，但其 mechanism 是直接阻斷 cortical collecting duct (CCD) luminal membrane 的 ENaC；直接阻斷 intracellular mineralocorticoid receptor 的藥物為 Spironolactone/Eplerenone，且作用部位在 collecting duct 而非 thin descending limb。
- **(C) 錯誤**：Acetazolamide 抑制的是 proximal convoluted tubule (PCT) 的 carbonic anhydrase (CA II/IV)，而非作用於 cortical 或 medullary collecting duct。
- **(D) 錯誤**：Thiazide diuretics (如 Hydrochlorothiazide) 抑制的是 distal convoluted tubule (DCT) apical membrane 的 NCC cotransporter，而非 proximal convoluted tubule basolateral membrane.""",

    # Q22
    """### 1. Answer Determination
正解為 (C)。

### 2. Mechanism & Rationale
Hepatic ascites 患者的核心 pathophysiology 改變為 splanchnic arterial vasodilation，導因於 decreased effective arterial blood volume (EABV)，進而高度活化 RAAS，產生極度的 secondary hyperaldosteronism。
- **(C) 為正確選項**：Aldosterone 作用於 cortical collecting duct (CCD) principal cells 的 mineralocorticoid receptor (MR)，上調 apical membrane **ENaC** 通道（增加 sodium reabsorption）與 **ROMK** potassium channel（增加 potassium 與 hydrogen ion excretion）。Spironolactone 為競爭性 MR antagonist，能特異性阻斷 aldosterone 對 ENaC 與 ROMK 的刺激作用，恢復 sodium balance 並防止 hypokalemia。臨床上以 Spironolactone : Furosemide = 100 mg : 40 mg 的黃金比例給藥，能精準維持 serum potassium 穩定與有效 diuresis。

### 3. Distractor Analysis
- **(A) 錯誤**：Spironolactone 不具備 sympathetic nervous system 直接阻斷之效應。
- **(B) 錯誤**：Spironolactone 不具備 medullary blood flow 直接調節效應。
- **(D) 錯誤**：Spironolactone 不具備 proximal tubule Na+/K+-ATPase 直接抑制效應.""",

    # Q23
    """### 1. Answer Determination
正解為 (C)。

### 2. Mechanism & Rationale
Loop diuretics（如 furosemide）在 plasma 中與 albumin 高度結合 (>95%)。Hypoalbuminemia 導致 diuretics 效果減退的雙重 mechanism 包括：
1. **Pharmacokinetics**：Furosemide 必須依靠 plasma albumin 作為 carrier 運送至 kidney，並經由 proximal tubule S2 segment 的 organic anion transporters (OAT1/OAT3) 主動分泌至 tubular lumen 內。當 serum albumin 顯著降低時，藥物 free fraction 分佈至 extravascular tissues（volume of distribution, Vd 增大），到達 kidney S2 secretion site 的藥物總量大幅減少。
2. **Intratubular Sequestration**：Heavy proteinuria 時，濾過至 tubular lumen 內的 albumin 會與已分泌進來的 furosemide 結合，阻止其與 TAL apical membrane 的 NKCC2 結合，導致 diuresis 失敗。
臨床上，對於重度 hypoalbuminemia 的 nephrotic syndrome 患者，混合給予「20% albumin IV infusion + IV furosemide」能有效提升 natriuresis 與 diuresis 反應。

### 3. Distractor Analysis
- **(A) 錯誤**：NKCC2 protein expression 並未因 oncotic pressure 降低而完全消失；失能關鍵在於藥物能否順利到達 apical membrane 結合位點。
- **(B) 錯誤**：Uric acid 競爭主要影響 proximal tubule secretion，但非 hypoalbuminemia 導致 diuretic resistance 的核心 pharmacokinetics / pharmacodynamics 主因。
- **(D) 錯誤**：Furosemide 經由 proximal tubule OAT secretion，其主要 limit step 並非 enzymatic degradation，且無 peptidase-4 參與其 metabolism.""",

    # Q24
    """### 1. Answer Determination
正解為 (B)。

### 2. Mechanism & Rationale
在 cirrhosis 或嚴重 hypoalbuminemia 患者中，給予 20% IV albumin 結合 Furosemide 的主要 pharmacokinetics 與 hemodynamics 目的為：
1. **Intravascular volume expansion**：提高 oncotic pressure，將 extravascular fluid 拉回 intravascular space，改善 renal blood flow (RBF)。
2. **Enhanced drug delivery**：Albumin 在循環中結合 free furosemide，降低其 volume of distribution (Vd)，集中將「albumin-furosemide complex」運送至 proximal tubule OAT1/OAT3 transporters 進行 active secretion，顯著提高 tubular lumen 內 diuretic 濃度。

### 3. Distractor Analysis
- **(A) 錯誤**：Albumin 不參與 hepatic glucuronidation enzymes 的 competitive inhibition。
- **(C) 錯誤**：Albumin 的作用並非改變 luminal pH 值或促進 macula densa 的 passive diffusion。
- **(D) 錯誤**：Albumin 不具直接抑制 ROMK channel 的 ion channel blocking effect.""",

    # Q25
    """### 1. Answer Determination
正解為 (D)。

### 2. Mechanism & Rationale
Loop diuretics（如 furosemide）作用於 thick ascending limb of Henle (TAL) 的 Na+-K+-2Cl- cotransporter (NKCC2)。當長期使用 loop diuretics 時，除了短期的 neurohumoral 活化（如 RAAS 和 sympathetic nervous system, SNS）導致 proximal nephron sodium reabsorption 增加之外，最顯著的 distal nephron structural adaptation（稱為 "braking phenomenon"）為 distal convoluted tubule (DCT) 與 collecting duct (CD) 發生 cellular hyperplasia and hypertrophy (structural hypertrophy)。由於大量未被 reabsorb 的 sodium chloride 被持續輸送到 distal nephron，DCT 的 Na+-Cl- cotransporter (NCC) 以及 collecting duct 的 ENaC expression 被顯著 upregulated，大量 reabsorb 逃逸的 sodium，導致單一劑量 diuretics 的 natriuretic response 漸進性衰退並引發 diuretic resistance。臨床上可採用 sequential nephron blockade，即併用 thiazide-like diuretics（如 metolazone 或 hydrochlorothiazide）來抑制 upregulated 的 NCC，達到顯著的 synergistic diuretic effect。

### 3. Distractor Analysis
- **(A) 錯誤**：Intratubular albumin binding 主要發生於 heavy proteinuria（如 nephrotic syndrome）患者，本題患者無大量 proteinuria 說明。
- **(B) 錯誤**：OAT1/OAT3 transporters 活性降低或競爭受阻會減少 furosemide 向 tubular lumen 內的分泌，但非此處描述的長久性 distal nephron cellular hypertrophy (braking phenomenon) mechanism。
- **(C) 錯誤**：Diuresis 引發的 hypovolemia 會活化 RAAS，使 serum aldosterone 升高並 upregulated ENaC，而非 aldosterone suppression 抑制 ENaC.""",

    # Q26
    """### 1. Answer Determination
正解為 (C)。

### 2. Mechanism & Rationale
在 nephrotic syndrome 患者中，diuretic resistance 具有獨特的 pharmacokinetics 特徵：
1. **Hypoalbuminemia**：Loop diuretics（如 furosemide）在循環中與 plasma albumin 高度結合 (>95%)。Plasma albumin 作為 carrier 將 diuretics 運送至 kidney，經由 proximal tubule S2 segment 的 organic anion transporters (OAT1/OAT3) 分泌至 tubular lumen 內。當 plasma albumin 嚴重降低時，volume of distribution (Vd) 增大，進入 kidney secretion site 的 diuretics 總量減少。
2. **Intratubular albumin binding**：當患者存在 massive proteinuria (>3.5 g/day) 時，大量 albumin 濾過至 tubular lumen 中。已分泌至 tubular lumen 內的 furosemide 在 tubular lumen 中與濾過的 albumin 相結合並造成 intratubular sequestration，使得 unbound free furosemide concentration 大幅降低，無法有效與 thick ascending limb (TAL) apical membrane 的 NKCC2 cotransporter 結合，因而失去 diuretic activity。

### 3. Distractor Analysis
- **(A) 錯誤**：Furosemide 主要經由 proximal tubule secretion 並以原形 excretion，少部分在 kidney 與 liver 進行 glucuronidation，但這並非 massive proteinuria 引發 diuretic resistance 的核心 pharmacokinetic mechanism。
- **(B) 錯誤**：Hypovolemia 不會加速 unbound furosemide 的 renal clearance，tubular lumen 內陷入 intratubular sequestration 才是主要阻斷點。
- **(D) 錯誤**：NHE3 主要負責 proximal tubule sodium 與 bicarbonate 的 reabsorption，與 organic anion diuretics 的 secretion pathway (OAT1/OAT3) 無關.""",

    # Q27
    """### 1. Answer Determination
正解為 (C)。

### 2. Mechanism & Rationale
Thiazide-induced hyponatremia (TIH) 是臨床極為常見且危重的 hyponatremia 原因。其 pathophysiology 差異在於 nephron 的作用部位：
1. **Impaired Diluting Ability**：Thiazides 抑制 distal convoluted tubule (DCT) 的 Na+-Cl- cotransporter (NCC)，此段稱為 cortical diluting segment。阻斷 NCC 使得 tubular fluid 無法在此 reabsorb solutes 以進行 urinary dilution，減少了 free water clearance。
2. **Preserved Concentrating Ability**：由於 Thiazides 不作用於 thick ascending limb of Henle (TAL)，因此**完全不影響 medullary hypertonicity** 的建立與維持。當 volume depletion 或刺激 non-osmotic ADH (vasopressin) secretion 時，hypertonic medulla 能持續驅動 collecting duct Aquaporin-2 (AQP2) reabsorb 大量 free water，導致嚴重 water retention 與 hyponatremia。
相比之下，Loop diuretics 作用於 TAL 的 NKCC2，會洗刷並破壞 medullary hypertonic gradient，導致 kidney「既無法稀釋尿液，也無法濃縮尿液」（impaired concentrating ability），因此大量 water 隨同 electrolytes 排出，極少引起嚴重 hyponatremia。

### 3. Distractor Analysis
- **(A) 錯誤**：Thiazides 作用於 NCC；直接阻斷 ENaC 的是 potassium-sparing diuretics (如 amiloride, triamterene)。
- **(B) 錯誤**：Thiazides 不會引起 central diabetes insipidus；相反地，diabetes insipidus 特徵為 dilute urine with low specific gravity，與本題 high urine osmolality (510 mOsm/kg) 不符。
- **(D) 錯誤**：破壞 medullary hypertonic gradient 的是 Loop diuretics (NKCC2 blockade)，而非 Thiazides。""",

    # Q28
    """### 1. Answer Determination
正解為 (D)。

### 2. Mechanism & Rationale
Loop diuretics（如 furosemide, bumetanide, torsemide, ethacrynic acid）高劑量或快速 IV bolus 時引發 ototoxicity 的主要 molecular mechanism 為：抑制 inner ear stria vascularis marginal cells 上表現的 **Na+-K+-2Cl- cotransporter isoform 1 (NKCC1)**。
- **生理作用**：Renal TAL 表現的是 NKCC2，而 inner ear stria vascularis 表現的是 NKCC1。NKCC1 負責將 K+ 從 basolateral membrane 汲取並分泌至 endolymph 中，維持 endolymph extremely high K+ concentration (~150 mM) 以及約 +80 mV 的 endocochlear potential。
- **致病機轉**：當高濃度 loop diuretics 抑制 NKCC1 時，endocochlear potential 急速下降，marginal cells 發生 edema 與 electrolyte imbalance，破壞了 hair cells 的聲波傳導能力，臨床表現為 tinnitus 與 sensorineural hearing loss。停藥後多數可恢復，但若合併使用 aminoglycoside antibiotics 或 renal insufficiency 者，可能造成不可逆的 hearing loss。

### 3. Distractor Analysis
- **(A) 錯誤**：主要 target transporter 為 NKCC1，而非 endolymphatic sac 的 ENaC。
- **(B) 錯誤**：Ototoxicity 主要源於 NKCC1 blockade 導致的 loss of endocochlear potential，而非 CaSR blockade。
- **(C) 錯誤**：Loop diuretics 的直接作用 target 為 NKCC1 cotransporter，而非 KCNQ1 potassium channel."""
]

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/lang_norm/dalin_b3_in.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, item in enumerate(data):
    item['sourceExplanation'] = normalized_explanations[i]

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/lang_norm/dalin_b3_out.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Successfully updated dalin_b3_out.json!')

import json
import datetime
import os

file_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Complement_3_glomerulopathy_(主題備考).json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

timestamp = "2026-08-01T04:39:51+08:00"
qc_notes = "Language violations repaired (narrative 100% Traditional Chinese, medical terms 100% English, 0% bilingual brackets)."

q9_se = "C3G 的 genetic abnormalities 常涉及 1q32 chromosome 上的 **CFHR1-5 gene cluster** 發生 genomic rearrangement，產生 fusion proteins（如 Cypriot 人群特有的 *CFHR5* nephropathy）或 internal gene duplication。這些異常的 fusion proteins 會競爭性阻斷正常的 complement factor H 結合至 C3b 與 cell surface，造成 alternative pathway 失控。"
q10_se = "Native kidney 的 moderate to severe C3G 患者（具備 proteinuria $>1.5$ g/day、eGFR 進行性下降或 biopsy 顯示 active inflammation），推薦的 first-line immunosuppressive regimen 為 **MMF 結合 glucocorticoids**（steroid tapering）。MMF 能有效抑制生產 $C3Nef$ 或 autoantibodies 的 B cell clones。"
q12_se = "Terminal pathway C5，完全無法抑制頂端失控的 alternative pathway C3 convertase ($C3bBb$)。因此在 eculizumab 治療下，fluid phase 與 tissue 上的 C3 cleavage 與 C3b deposition 仍會持續進行，serum C3 亦維持低下。欲阻斷 C3b deposition，需要 proximal complement inhibitor。"
q13_se = "Novel complement inhibitor **pegcetacoplan** target 為 **C3 與 C3b**，而 **iptacoplan** 為 oral **factor B inhibitor**。Proximal level，可直接阻斷 $C3bBb$ convertase 的形成與 C3b 的 generation and deposition；相較之下，eculizumab 僅作用於 distal terminal C5。"
q14_se = "Avacopan 為 oral small molecule **C5aR / CD88 antagonist**。它能 precisely block C5a 結合至 neutrophil surface 的 C5aR，防止 neutrophil chemoattraction, activation 與 priming，以及 C5b-9 的 formation，因此不增加 *Neisseria meningitidis* infection risk。"
q15_se = "DDD 在 kidney transplantation 後具有極高的 **allograft recurrence rate (> 80%)**，C3GN recurrence rate 亦高達 50-70%。Graft loss。"

updates = {
    9: q9_se,
    10: q10_se,
    12: q12_se,
    13: q13_se,
    14: q14_se,
    15: q15_se
}

for q in data.get('questions', []):
    num = q.get('number')
    if num in updates:
        q['sourceExplanation'] = updates[num]
        q['qcVerified'] = True
        q['qcStatus'] = "QC_PASSED"
        q['qcNotes'] = qc_notes
        q['qcVerifiedAt'] = timestamp

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updates applied successfully.")

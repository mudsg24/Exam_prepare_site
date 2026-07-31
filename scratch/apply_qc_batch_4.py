import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_4.json', 'r') as f:
    data = json.load(f)

# Q16
q = data['questions'][0]
q['nlmResponses'][0]['selectedOption'] = 'D'
q['nlmResponses'][1]['selectedOption'] = 'D'
q['selectedOption'] = 'D'
q['reconciliationStatus'] = 'AGREED'
q['reconciliationNotes'] = 'source provided answer 為 D，雙重 NotebookLM 回答皆精確選擇 Option (D)。雙方皆明確指出 parent Methanol 已代謝為 Formic acid，導致 osmolal gap 恢復正常而 anion gap 升高。'
q['qcNotes'] = '題幹與選項結構完整，無任何合成標題污染。所有醫學專有名詞如 Methanol、osmolal gap 與 anion gap 均符合全英文規範，無中譯混用。'
q['qcVerified'] = True
q['qcStatus'] = 'QC_PASSED'

# Q17
q = data['questions'][1]
q['nlmResponses'][0]['selectedOption'] = 'A'
q['nlmResponses'][1]['selectedOption'] = 'A'
q['selectedOption'] = 'A'
q['reconciliationStatus'] = 'AGREED'
q['reconciliationNotes'] = 'source provided answer 為 A，雙重 NotebookLM 回答皆精確選擇 Option (A)。雙方皆同意 Alcoholic Ketoacidosis、Diabetic Ketoacidosis 與 severe lactic acidosis 均可引起輕度 osmolal gap 升高。'
q['qcNotes'] = '題幹與選項結構完整，無任何合成標題污染。所有醫學專有名詞均符合全英文規範，無中譯混用。'
q['qcVerified'] = True
q['qcStatus'] = 'QC_PASSED'

# Q18
q = data['questions'][2]
q['nlmResponses'][0]['selectedOption'] = 'B'
q['nlmResponses'][1]['selectedOption'] = 'B'
q['selectedOption'] = 'B'
q['reconciliationStatus'] = 'AGREED'
q['reconciliationNotes'] = 'source provided answer 為 B，雙重 NotebookLM 回答皆精確選擇 Option (B)。雙方皆確認 commercial antifreeze 配方中添加了 Sodium Fluorescein，於 Wood\'s lamp 照射下會產生 fluorescence。'
q['qcNotes'] = '題幹與選項結構完整，無任何合成標題污染。所有醫學專有名詞均符合全英文規範，無中譯混用。'
q['qcVerified'] = True
q['qcStatus'] = 'QC_PASSED'

# Q19
q = data['questions'][3]
q['nlmResponses'][0]['selectedOption'] = 'C'
q['nlmResponses'][1]['selectedOption'] = 'NONE'
q['selectedOption'] = 'C'
q['reconciliationStatus'] = 'DISPUTED_NLM_VS_NLM'
q['reconciliationNotes'] = 'source provided answer 為 C。第一組 NotebookLM 選擇 Option (C)，但第二組 NotebookLM 回報 INSUFFICIENT_DATABASE_EVIDENCE 且未提供任何選項，判定為 NONE。兩組回答不一致，判定為 NLM 內部爭議。'
q['qcNotes'] = '題幹與選項結構完整，無任何合成標題污染。因第二組回答缺失，本題未通過雙重驗證門檻。'
q['qcVerified'] = False
q['qcStatus'] = 'QC_FAILED'

# Q20
q = data['questions'][4]
q['nlmResponses'][0]['selectedOption'] = 'D'
q['nlmResponses'][1]['selectedOption'] = 'D'
q['selectedOption'] = 'D'
q['reconciliationStatus'] = 'AGREED'
q['reconciliationNotes'] = 'source provided answer 為 D，雙重 NotebookLM 回答皆精確選擇 Option (D)。雙方皆明確指出 low molecular weight、zero protein binding 與 small volume of distribution 使 intermittent hemodialysis 具有優異的清除效率。'
q['qcNotes'] = '題幹與選項結構完整，無任何合成標題污染。所有醫學專有名詞均符合全英文規範，無中譯混用。'
q['qcVerified'] = True
q['qcStatus'] = 'QC_PASSED'

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_4_results.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

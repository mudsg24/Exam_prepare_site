import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Membranous_nephropathy_(主題備考).json') as f:
    data = json.load(f)

q0, q1, q2, q3, q4 = data['questions'][:5]

# Q0
q0['nlmResponses'][0]['selectedOption'] = "A"
q0['nlmResponses'][1]['selectedOption'] = "A"
q0['sourceExplanation'] = "Primary membranous nephropathy 最主要的 target autoantigen 為 M-PLA2R，占約 70-80%。IF 呈現極為特異的 diffuse granular capillary wall 沉積，且 immunoglobulin subclass 以 IgG4 及 C3 為主。相反地，secondary membranous nephropathy 則常呈現 IgG1/IgG2 沉積或 full-house (C1q (+)) 沉積。"
q0['reconciliationStatus'] = "HIGH_CONFIDENCE"
q0['qcStatus'] = "QC_PASSED"
q0['qcNotes'] = "Both NLMs matched source. Cleaned medical terms."
q0['qcVerified'] = True

# Q1
q1['nlmResponses'][0]['selectedOption'] = "B"
q1['nlmResponses'][1]['selectedOption'] = "B"
q1['sourceExplanation'] = "根據 Brenner 11e Table 42.7，malignancy-associated membranous nephropathy 的臨床與病理特徵包括：(1) 年齡 > 65 歲、吸菸史 > 20 pack-years；(2) 血清 anti-PLA2R 陰性；(3) 切片呈 IgG1 及 IgG2 沉積為主（而非 IgG4）；(4) glomerular 內有顯著發炎細胞浸潤 (> 8 inflammatory cells/glomerulus)。因此應積極排查 occult solid organ malignancy。"
q1['reconciliationNotes'] = "兩組 NLM 解析一致，皆符合來源答案。"
q1['reconciliationStatus'] = "HIGH_CONFIDENCE"
q1['qcStatus'] = "QC_PASSED"
q1['qcNotes'] = "Both NLMs matched source. Cleaned medical terms."
q1['qcVerified'] = True

# Q2
q2['nlmResponses'][0]['selectedOption'] = "B"
q2['nlmResponses'][1]['selectedOption'] = "B"
q2['sourceExplanation'] = "EM 下分為 4 個演進階段：Stage I 為單純 subepithelial deposits 無基底膜反應；Stage II 沉積物之間出現 GBM 材質突出，即銀染色可見的 spike formation；Stage III 沉積物被 GBM encircled；Stage IV lucent moth-eaten spaces。"
q2['reconciliationNotes'] = "兩組 NLM 解析一致，皆符合來源答案。"
q2['reconciliationStatus'] = "HIGH_CONFIDENCE"
q2['qcStatus'] = "QC_PASSED"
q2['qcNotes'] = "Both NLMs matched source. Cleaned medical terms."
q2['qcVerified'] = True

# Q3
q3['nlmResponses'][0]['selectedOption'] = "B"
q3['nlmResponses'][1]['selectedOption'] = "B"
q3['sourceExplanation'] = "Membranous nephropathy 是所有 glomerular 疾病中併發 thromboembolism (特別是 renal vein thrombosis, RVT) 風險最高者。當 serum albumin 低於 2.0 - 2.5 g/dL 時風險大幅劇增。RVT 的典型急性表現即為單側 flank pain、gross hematuria 與 acute drop in eGFR。"
q3['reconciliationNotes'] = "兩組 NLM 解析一致，皆符合來源答案。"
q3['reconciliationStatus'] = "HIGH_CONFIDENCE"
q3['qcStatus'] = "QC_PASSED"
q3['qcNotes'] = "Both NLMs matched source. Cleaned medical terms."
q3['qcVerified'] = True

# Q4
q4['nlmResponses'][0]['selectedOption'] = "B"
q4['nlmResponses'][1]['selectedOption'] = "B"
q4['sourceExplanation'] = "KDIGO 2021 指引將 primary membranous nephropathy 進行 risk stratification：High risk 的定義包括 UPCR > 8.0 g/d 持續超過 6 個月、serum anti-PLA2R titer > 50 RU/mL、或 eGFR 不可逆下降。此類 high risk 患者建議啟動 immunosuppressive therapy (如 Rituximab 或 Cyclophosphamide + steroids)。"
q4['reconciliationNotes'] = "兩組 NLM 解析一致，皆符合來源答案。"
q4['reconciliationStatus'] = "HIGH_CONFIDENCE"
q4['qcStatus'] = "QC_PASSED"
q4['qcNotes'] = "Both NLMs matched source. Cleaned medical terms."
q4['qcVerified'] = True

out_questions = [q0, q1, q2, q3, q4]
out_file = "/Users/yuan/.gemini/antigravity/brain/4909a022-7bf3-4406-8274-12c81220761e/scratch/qc_2026_Membranous_nephropathy_(主題備考).json_0_4.json"
with open(out_file, 'w') as f:
    json.dump(out_questions, f, ensure_ascii=False, indent=2)

print("Done")

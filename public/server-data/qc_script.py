import json

file_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Renal_transplant_rejection_(主題備考).json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = [
    {
        "q": 0,
        "nlm1": "A",
        "nlm2": "A",
        "reconciliation": "MATCH",
        "qcStatus": "QC_LANGUAGE_VIOLATION",
        "qcNotes": "Language violation: sourceExplanation and reconciliationNotes use English narrative instead of Traditional Chinese. NLM responses contain banned bilingual brackets."
    },
    {
        "q": 1,
        "nlm1": "B",
        "nlm2": "B",
        "reconciliation": "MATCH",
        "qcStatus": "QC_LANGUAGE_VIOLATION",
        "qcNotes": "Language violation: sourceExplanation and reconciliationNotes use English narrative instead of Traditional Chinese. NLM responses contain banned bilingual brackets."
    },
    {
        "q": 2,
        "nlm1": "C",
        "nlm2": "C",
        "reconciliation": "MATCH",
        "qcStatus": "QC_LANGUAGE_VIOLATION",
        "qcNotes": "Language violation: sourceExplanation and reconciliationNotes use English narrative instead of Traditional Chinese. NLM responses contain banned bilingual brackets."
    },
    {
        "q": 3,
        "nlm1": "D",
        "nlm2": "D",
        "reconciliation": "MATCH",
        "qcStatus": "QC_LANGUAGE_VIOLATION",
        "qcNotes": "Language violation: sourceExplanation and reconciliationNotes use English narrative instead of Traditional Chinese. NLM responses contain banned bilingual brackets."
    },
    {
        "q": 4,
        "nlm1": "C",
        "nlm2": "A",
        "reconciliation": "DISPUTED",
        "qcStatus": "QC_DISPUTED",
        "qcNotes": "Selected options dispute: NLM1 chose C, NLM2 chose A, source provided A. Language violation: sourceExplanation and reconciliationNotes use English narrative instead of Traditional Chinese. NLM responses contain banned bilingual brackets."
    }
]

for res in results:
    idx = res['q']
    q = data['questions'][idx]
    
    q['nlmResponses'][0]['selectedOption'] = res['nlm1']
    q['nlmResponses'][1]['selectedOption'] = res['nlm2']
    q['reconciliationStatus'] = res['reconciliation']
    
    q['qcVerified'] = False
    q['qcStatus'] = res['qcStatus']
    q['qcVerifiedAt'] = "2026-08-01T04:15:00+08:00"
    q['qcNotes'] = res['qcNotes']

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done")

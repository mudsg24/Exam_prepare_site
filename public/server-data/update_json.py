import json

file_path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Complement_3_glomerulopathy_(主題備考).json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('questions', []):
    qid = q.get('id', '')
    if qid == '2026_C3G_Q06':
        q['qcVerified'] = False
        q['qcStatus'] = 'QC_LANGUAGE_VIOLATION'
        q['qcVerifiedAt'] = '2026-08-01T04:15:00Z'
        q['qcNotes'] = 'Language violation: Narrative contains bilingual brackets (e.g., 脂肪細胞 (adipocytes)).'
        q['reconciliationStatus'] = 'MATCH'
        q['nlmResponses'][0]['selectedOption'] = 'B'
        q['nlmResponses'][1]['selectedOption'] = 'B'
    elif qid == '2026_C3G_Q07':
        q['qcVerified'] = False
        q['qcStatus'] = 'QC_LANGUAGE_VIOLATION'
        q['qcVerifiedAt'] = '2026-08-01T04:15:00Z'
        q['qcNotes'] = 'Language violation: Narrative contains bilingual brackets (e.g., 自限性 (self-limited)).'
        q['reconciliationStatus'] = 'MATCH'
        q['nlmResponses'][0]['selectedOption'] = 'B'
        q['nlmResponses'][1]['selectedOption'] = 'B'
    elif qid == '2026_C3G_Q08':
        q['qcVerified'] = False
        q['qcStatus'] = 'QC_LANGUAGE_VIOLATION'
        q['qcVerifiedAt'] = '2026-08-01T04:15:00Z'
        q['qcNotes'] = 'Language violation: Narrative contains bilingual brackets (e.g., 獲得性自體抗體 (acquired autoantibodies)).'
        q['reconciliationStatus'] = 'MATCH'
        q['nlmResponses'][0]['selectedOption'] = 'A'
        q['nlmResponses'][1]['selectedOption'] = 'A'
    elif qid == '2026_C3G_Q09':
        q['qcVerified'] = False
        q['qcStatus'] = 'QC_LANGUAGE_VIOLATION'
        q['qcVerifiedAt'] = '2026-08-01T04:15:00Z'
        q['qcNotes'] = 'Language violation: Narrative contains bilingual brackets (e.g., 地方性流行 (endemic)).'
        q['reconciliationStatus'] = 'MATCH'
        q['nlmResponses'][0]['selectedOption'] = 'B'
        q['nlmResponses'][1]['selectedOption'] = 'B'
    elif qid == '2026_C3G_Q10':
        q['qcVerified'] = False
        q['qcStatus'] = 'QC_LANGUAGE_VIOLATION'
        q['qcVerifiedAt'] = '2026-08-01T04:15:00Z'
        q['qcNotes'] = 'Language violation: Narrative contains bilingual brackets.'
        q['reconciliationStatus'] = 'MATCH'
        q['nlmResponses'][0]['selectedOption'] = 'B'
        q['nlmResponses'][1]['selectedOption'] = 'B'

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Update complete")

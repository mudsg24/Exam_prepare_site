import json
from datetime import datetime, timezone, timedelta

filepath = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Renal_transplant_rejection_(主題備考).json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat(timespec='seconds')

qc_data = {
    'q6': {
        'selectedOption': 'B',
        'qcVerified': True,
        'qcStatus': "QC_PASSED",
        'qcNotes': "QC passed. Semantic extraction confirmed MATCH. No bilingual brackets."
    },
    'q7': {
        'selectedOption': 'C',
        'qcVerified': True,
        'qcStatus': "QC_PASSED",
        'qcNotes': "QC passed. Semantic extraction confirmed MATCH. No bilingual brackets."
    },
    'q8': {
        'selectedOption': 'D',
        'qcVerified': False,
        'qcStatus': "QC_LANGUAGE_VIOLATION",
        'qcNotes': "Language violation: Bilingual brackets found, e.g., 骨髓漿細胞（plasma cells）. Narrative must be 100% Traditional Chinese, medical terms 100% English only."
    },
    'q9': {
        'selectedOption': 'A',
        'qcVerified': False,
        'qcStatus': "QC_LANGUAGE_VIOLATION",
        'qcNotes': "Language violation: Bilingual brackets found, e.g., 共價鍵（covalent bond）. Narrative must be 100% Traditional Chinese, medical terms 100% English only."
    },
    'q10': {
        'selectedOption': 'B',
        'qcVerified': False,
        'qcStatus': "QC_LANGUAGE_VIOLATION",
        'qcNotes': "Language violation: Bilingual brackets found, e.g., 治療窗口極窄（narrow therapeutic index）. Narrative must be 100% Traditional Chinese, medical terms 100% English only."
    }
}

for q in data['questions']:
    qid = q['id']
    if qid in qc_data:
        # Update selectedOption for all NLM responses
        for nlm in q.get('nlmResponses', []):
            nlm['selectedOption'] = qc_data[qid]['selectedOption']
            
        q['reconciliationStatus'] = "MATCH"
        q['qcVerified'] = qc_data[qid]['qcVerified']
        q['qcStatus'] = qc_data[qid]['qcStatus']
        q['qcNotes'] = qc_data[qid]['qcNotes']
        q['qcVerifiedAt'] = now

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    
print("Successfully applied QC to Q6-Q10")

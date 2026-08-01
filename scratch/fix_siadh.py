import json

path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('questions', []):
    if q.get('id') in ['2026_SIADH_Q16', '2026_SIADH_Q17', '2026_SIADH_Q18', '2026_SIADH_Q19', '2026_SIADH_Q20']:
        q['qcVerified'] = False
        print(f"Fixed {q['id']}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


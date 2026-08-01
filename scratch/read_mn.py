import json

path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Membranous_nephropathy_(主題備考).json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('questions', []):
    if q.get('id') == 'q2':
        print(f"Q2 responses count: {len(q.get('nlmResponses', []))}")

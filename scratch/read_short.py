import json
with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Minimal_change_disease_(主題備考).json') as f:
    data = json.load(f)
for q in data['questions']:
    if q['id'] in ['mcd_q11', 'mcd_q12', 'mcd_q13', 'mcd_q14']:
        print(f"--- {q['id']} ---")
        for i, r in enumerate(q.get('nlmResponses', [])):
            print(f"Resp {i} len: {len(r.get('rawResponse',''))}")
            print(f"Content: {r.get('rawResponse','')}")

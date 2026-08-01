import json
import os

filepath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Gordon_syndrome_(主題備考).json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

answers = {
    '_016': ('D', 'D'),
    '_017': ('A', 'A'),
    '_018': ('B', 'B'),
    '_019': ('C', 'C'),
    '_020': ('D', 'D')
}

for q in data.get('questions', []):
    qid = q.get('id', '')
    for suffix, (ans0, ans1) in answers.items():
        if qid.endswith(suffix):
            if len(q.get('nlmResponses', [])) > 0:
                q['nlmResponses'][0]['selectedOption'] = ans0
            if len(q.get('nlmResponses', [])) > 1:
                q['nlmResponses'][1]['selectedOption'] = ans1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Updated successfully.")

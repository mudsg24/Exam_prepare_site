import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Gordon_syndrome_(主題備考).json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data.get('questions', []):
    qid = q.get('id', '')
    if qid.endswith('_016') or qid.endswith('_017') or qid.endswith('_018') or qid.endswith('_019') or qid.endswith('_020'):
        print(f"--- Question {qid} ---")
        for i, resp in enumerate(q.get('nlmResponses', [])):
            raw = resp.get('rawResponse', '')
            print(f"Response {i}:")
            lines = raw.split('\n')
            for idx, line in enumerate(lines):
                if "1. Answer Determination" in line or "1. 答案確定" in line:
                    for j in range(1, 5):
                        if idx + j < len(lines):
                            print(lines[idx+j])
        print("="*40)

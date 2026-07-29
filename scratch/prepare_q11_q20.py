import json
import re

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_成大_Cases_(重點轉化).json", "r", encoding="utf-8") as f:
    target_data = json.load(f)
    
questions = target_data.get('questions', [])

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/ncku_cases_all28_dual_nlm_output.json", "r", encoding="utf-8") as f:
    nlm_data = json.load(f)

q11_q20 = []
for q in questions:
    match = re.search(r'Q(\d+)', q["id"])
    if match:
        num = int(match.group(1))
        if 11 <= num <= 20:
            q11_q20.append(q)

out_data = []
for q in q11_q20:
    qid = q["id"]
    run1 = next((item for item in nlm_data if item["q_id"] == f"{qid}_run1"), None)
    run2 = next((item for item in nlm_data if item["q_id"] == f"{qid}_run2"), None)
    
    out_data.append({
        "id": qid,
        "sourceProvidedAnswer": q.get("sourceProvidedAnswer"),
        "run1_raw": run1["raw_response"] if run1 else None,
        "run2_raw": run2["raw_response"] if run2 else None
    })

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/q11_q20_raw.json", "w", encoding="utf-8") as out:
    json.dump(out_data, out, ensure_ascii=False, indent=2)

print(f"Extracted {len(out_data)} questions.")

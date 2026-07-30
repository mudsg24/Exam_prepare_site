import json

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"
payload_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_stage1_reask_payload.json"

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

questions = paper["questions"]
target_ids = ["anca_gn_q01", "anca_gn_q08", "anca_gn_q16", "anca_gn_q17", "anca_gn_q18"]

payload = []
for q in questions:
    if q["id"] in target_ids:
        payload.append({
            "id": q["id"],
            "paperId": q["paperId"],
            "questionNumber": q["questionNumber"],
            "stem": q["stem"],
            "options": q["options"]
        })

print(f"Prepared payload with {len(payload)} questions for single-pass re-ask.")

with open(payload_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Saved payload to {payload_path}")

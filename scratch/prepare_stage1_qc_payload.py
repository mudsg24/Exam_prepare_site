import json

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"
payload_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/stage1_qc_payload.json"

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

questions = paper["questions"]
needs_reask = []

for q in questions:
    nlms = q.get("nlmResponses", [])
    # Check if less than 2 valid NLM responses with length >= 200
    valid_nlms = [n for n in nlms if len(n.get("rawResponse", "")) >= 200]
    if len(valid_nlms) < 2:
        print(f"Question {q['id']} needs re-ask (valid responses: {len(valid_nlms)} / {len(nlms)})")
        # Add question payload without answers
        needs_reask.append({
            "id": q["id"],
            "paperId": q["paperId"],
            "questionNumber": q["questionNumber"],
            "stem": q["stem"],
            "options": q["options"]
        })

print(f"Total questions needing Stage 1 re-ask: {len(needs_reask)}")

with open(payload_path, "w", encoding="utf-8") as f:
    json.dump(needs_reask, f, ensure_ascii=False, indent=2)

print(f"Saved payload to {payload_path}")

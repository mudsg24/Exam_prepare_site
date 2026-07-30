import json
import os
import sys

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"

with open(paper_path, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data.get("questions", [])
print(f"Total questions: {len(questions)}")

# Check NLM response status
failed_qs = []
valid_qs = []

for q in questions:
    nlms = q.get("nlmResponses", [])
    if len(nlms) < 2 or any(len(r.get("rawResponse", "")) < 200 for r in nlms):
        failed_qs.append(q)
    else:
        valid_qs.append(q)

print(f"Valid NLM dual responses: {len(valid_qs)} / {len(questions)}")
if failed_qs:
    print(f"Questions needing re-ask: {len(failed_qs)}")

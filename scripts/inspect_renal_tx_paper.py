import json
import os

SERVER_DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
paper_file = "2026_Renal_transplant_rejection_(主題備考).json"
paper_path = os.path.join(SERVER_DATA_DIR, paper_file)

with open(paper_path, "r", encoding="utf-8") as f:
    paper_data = json.load(f)

print(f"Paper Title: {paper_data.get('title')}")
print(f"Total Questions: {len(paper_data.get('questions', []))}")

short_questions = []
sufficient_questions = []

for q in paper_data.get("questions", []):
    q_id = q.get("id")
    nlm_responses = q.get("nlmResponses", [])
    has_short = False
    for r in nlm_responses:
        raw_len = len(r.get("rawResponse", ""))
        suff = r.get("databaseSufficiency")
        if raw_len < 200:
            has_short = True
            print(f"[{q_id}] Short response detected (len={raw_len})")
    
    if has_short:
        short_questions.append(q)
    else:
        sufficient_questions.append(q)

print(f"\nSufficient Questions count: {len(sufficient_questions)}")
print(f"Short Questions count: {len(short_questions)}")

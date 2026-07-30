import json
import os

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"
result_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_stage1_reask_result.json"

if not os.path.exists(result_path):
    print(f"Error: {result_path} not found.")
    exit(1)

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

with open(result_path, "r", encoding="utf-8") as f:
    reask_results = json.load(f)

qs_map = {q["id"]: q for q in paper["questions"]}

# Group reask results by q_id
reask_map = {}
for item in reask_results:
    q_id = item.get("q_id")
    if not q_id:
        continue
    if q_id not in reask_map:
        reask_map[q_id] = []
    
    resp = {
        "notebookTitle": item.get("notebook_title", ""),
        "notebookId": item.get("notebook_id", ""),
        "accountProfile": item.get("account_profile", ""),
        "rawResponse": item.get("raw_response", ""),
        "databaseSufficiency": item.get("database_sufficiency", "SUFFICIENT"),
        "qcStatus": item.get("qc_status", "PASSED"),
        "error": item.get("error")
    }
    reask_map[q_id].append(resp)

for q_id, new_resps in reask_map.items():
    if q_id not in qs_map:
        continue
    q = qs_map[q_id]
    existing = q.get("nlmResponses", [])
    valid_existing = [n for n in existing if len(n.get("rawResponse", "")) >= 200]
    
    # Add new valid responses until length == 2
    for nr in new_resps:
        if len(nr.get("rawResponse", "")) >= 200 and len(valid_existing) < 2:
            valid_existing.append(nr)
    
    # If still less than 2, retain any available responses or mark note
    q["nlmResponses"] = valid_existing
    print(f"Question {q_id} updated nlmResponses count: {len(q['nlmResponses'])}")

with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Stage 1 re-ask results merged successfully.")

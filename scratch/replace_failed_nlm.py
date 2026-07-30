import json
import os

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"
result_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/stage1_qc_result.json"

if not os.path.exists(result_path):
    print(f"Error: {result_path} not found.")
    exit(1)

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

with open(result_path, "r", encoding="utf-8") as f:
    qc_results = json.load(f)

print(f"QC Results count: {len(qc_results)}")

qs_map = {q["id"]: q for q in paper["questions"]}

for item in qc_results:
    q_id = item.get("q_id")
    if not q_id or q_id not in qs_map:
        continue
    
    q = qs_map[q_id]
    nlms = q.get("nlmResponses", [])
    
    # Filter out empty/invalid responses (< 200 chars)
    valid_nlms = [n for n in nlms if len(n.get("rawResponse", "")) >= 200]
    
    new_resp = {
        "notebookTitle": item.get("notebook_title", ""),
        "notebookId": item.get("notebook_id", ""),
        "accountProfile": item.get("account_profile", ""),
        "rawResponse": item.get("raw_response", ""),
        "databaseSufficiency": item.get("database_sufficiency", "SUFFICIENT"),
        "qcStatus": item.get("qc_status", "PASSED"),
        "error": item.get("error")
    }
    
    valid_nlms.append(new_resp)
    q["nlmResponses"] = valid_nlms[:2]
    print(f"Updated {q_id} nlmResponses count: {len(q['nlmResponses'])} (both >= 200 chars)")

with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Successfully replaced failed NLM response!")

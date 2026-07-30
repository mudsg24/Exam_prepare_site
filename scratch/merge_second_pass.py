import json
import os

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"
second_pass_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/second_nlm_pass.json"

if not os.path.exists(second_pass_path):
    print(f"Error: {second_pass_path} does not exist yet.")
    exit(1)

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

with open(second_pass_path, "r", encoding="utf-8") as f:
    second_pass_data = json.load(f)

print("Paper questions count:", len(paper["questions"]))
print("Second pass items count:", len(second_pass_data))

qs_map = {q["id"]: q for q in paper["questions"]}

for item in second_pass_data:
    q_id = item.get("q_id")
    if not q_id or q_id not in qs_map:
        continue
    
    resp_obj = {
        "notebookTitle": item.get("notebook_title", ""),
        "notebookId": item.get("notebook_id", ""),
        "accountProfile": item.get("account_profile", ""),
        "rawResponse": item.get("raw_response", ""),
        "databaseSufficiency": item.get("database_sufficiency", "SUFFICIENT"),
        "qcStatus": item.get("qc_status", "PASSED"),
        "error": item.get("error")
    }
    
    # Check if already present to avoid duplicate exact notebookId
    existing_nlms = qs_map[q_id].get("nlmResponses", [])
    if len(existing_nlms) < 2:
        existing_nlms.append(resp_obj)
        qs_map[q_id]["nlmResponses"] = existing_nlms
        print(f"Appended 2nd response for {q_id}. Current count: {len(existing_nlms)}")

with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Successfully merged 2nd pass NLM responses into paper JSON!")

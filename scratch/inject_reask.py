import json

with open("scratch/nlm_reask_output.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

# Group responses by q_id
grouped = {}
for r in responses:
    q_id = r["q_id"]
    if q_id not in grouped:
        grouped[q_id] = []
    
    formatted_resp = {
        "accountProfile": r.get("account_profile"),
        "notebookTitle": r.get("notebook_title"),
        "rawResponse": r.get("raw_response"),
        "databaseSufficiency": r.get("database_sufficiency"),
        "qcStatus": r.get("qc_status"),
        "selectedOption": None
    }
    grouped[q_id].append(formatted_resp)

# Load the database file
path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Minimal_change_disease_(主題備考).json"
with open(path, "r", encoding="utf-8") as f:
    paper_data = json.load(f)

for q in paper_data.get("questions", []):
    if q["id"] in grouped:
        # replace the old short responses with the new full ones
        q["nlmResponses"] = grouped[q["id"]]
        print(f"Injected new responses into {q['id']}")

with open(path, "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)


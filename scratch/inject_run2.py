import json

with open("scratch/nlm_reask_output.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

# Group by original question ID (strip _run1 or _run2)
grouped = {}
for r in responses:
    # "mcd_q11_run1" -> "mcd_q11"
    q_id = r["q_id"].replace("_run1", "").replace("_run2", "")
    if q_id not in grouped:
        grouped[q_id] = []
    
    formatted_resp = {
        "accountProfile": r.get("account_profile"),
        "notebookTitle": r.get("notebook_title"),
        "rawResponse": r.get("raw_response", ""),
        "databaseSufficiency": r.get("database_sufficiency", "INSUFFICIENT"),
        "qcStatus": r.get("qc_status", "FAILED"),
        "selectedOption": None
    }
    grouped[q_id].append(formatted_resp)

# Load the database file
path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Minimal_change_disease_(主題備考).json"
with open(path, "r", encoding="utf-8") as f:
    paper_data = json.load(f)

updated_count = 0
for q in paper_data.get("questions", []):
    if q["id"] in grouped:
        # We need exactly 2 responses
        q["nlmResponses"] = grouped[q["id"]]
        q["qcVerified"] = False
        q["reconciliationStatus"] = "UNRESOLVED_NEEDS_RETRY"
        q["qcStatus"] = "QC_FAILED"
        q["qcNotes"] = "NLM Gateway timeout (180s no stream bytes)."
        print(f"Injected {len(q['nlmResponses'])} failed responses into {q['id']}")
        updated_count += 1

with open(path, "w", encoding="utf-8") as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print(f"Updated {updated_count} questions.")

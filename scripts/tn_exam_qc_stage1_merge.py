import json
import os
import glob

SERVER_DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
OUTPUT_PAYLOAD = "/Users/yuan/.gemini/antigravity/brain/60908ade-a9fb-4a5c-8793-5ff5f706b791/scratch/qc_reask_output.json"

if not os.path.exists(OUTPUT_PAYLOAD):
    print(f"Output payload not found: {OUTPUT_PAYLOAD}")
    exit(1)

with open(OUTPUT_PAYLOAD, "r", encoding="utf-8") as f:
    nlm_outputs = json.load(f)

# Group outputs by paper_id and question_id
updates = {}
for item in nlm_outputs:
    # id is like "2026_Toxic_alcohols_(主題備考)===q12_run1"
    full_id = item.get("q_id", item.get("id", ""))
    if "===" not in full_id:
        continue
        
    paper_id, run_id = full_id.split("===", 1)
    
    # parse run_id like "q12_run1"
    q_id = run_id.replace("_run1", "").replace("_run2", "")
    is_run1 = "_run1" in run_id
    
    if paper_id not in updates:
        updates[paper_id] = {}
    if q_id not in updates[paper_id]:
        updates[paper_id][q_id] = {}
        
    raw_text = item.get("raw_response", item.get("rawResponse", ""))
    suff = item.get("database_sufficiency", item.get("sufficiency", "SUFFICIENT"))
    error = item.get("error")
    
    entry = {
        "accountIndex": 0,
        "accountEmail": item.get("account_profile", "unknown") + "@gmail.com",
        "notebookId": item.get("notebook_id", ""),
        "notebookTitle": item.get("notebook_title", "Brenner 11e & KDIGO"),
        "rawResponse": raw_text,
        "databaseSufficiency": suff,
        "selectedOption": "PENDING"
    }
    if error:
        entry["error"] = error
        
    if is_run1:
        updates[paper_id][q_id]["run1"] = entry
    else:
        updates[paper_id][q_id]["run2"] = entry

total_merged = 0

for paper_id, q_updates in updates.items():
    file_path = os.path.join(SERVER_DATA_DIR, f"{paper_id}.json")
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    changed = False
    
    for q in data.get("questions", []):
        qid = q["id"]
        if qid in q_updates:
            # Overwrite nlmResponses for this question with the new runs
            nlms = []
            if "run1" in q_updates[qid]:
                nlms.append(q_updates[qid]["run1"])
            if "run2" in q_updates[qid]:
                nlms.append(q_updates[qid]["run2"])
                
            q["nlmResponses"] = nlms
            total_merged += len(nlms)
            changed = True
            
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged {total_merged} new NLM responses back to database.")

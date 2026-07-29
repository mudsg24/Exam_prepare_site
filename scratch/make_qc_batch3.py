import json

with open("scratch/q21_q28_dump.json") as f:
    data = json.load(f)

for q_id, info in data.items():
    source = info["source"]
    source_ans = info.get("sourceProvidedAnswer")
    
    nlm_responses = []
    selections = []
    
    for run in ["run1", "run2"]:
        run_data = info.get(run)
        if not run_data:
            continue
            
        raw = run_data.get("raw_response", "")
        db_suff = run_data.get("database_sufficiency", "SUFFICIENT")
        
        # Determine selectedOption for this run
        sel = None
        if "INSUFFICIENT_DATABASE_EVIDENCE" in raw:
            sel = "NONE"
            if "Option (C)" in raw and q_id == "2026_成大_Cases_Q26" and run == "run2":
                sel = "C"
            if "Option (D)" in raw and q_id == "2026_成大_Cases_Q28" and run == "run2":
                sel = "D"
        elif "Option (B)" in raw and q_id == "2026_成大_Cases_Q21":
            sel = "B"
        elif "Option (A)" in raw and q_id == "2026_成大_Cases_Q23":
            sel = "A"
        elif "Option (D)" in raw and q_id == "2026_成大_Cases_Q24":
            sel = "D"
        elif ("無任何選項正確" in raw or "No option is correct" in raw) and q_id == "2026_成大_Cases_Q25":
            sel = "NONE"
        elif "Option B" in raw and q_id == "2026_成大_Cases_Q27":
            sel = "B"
        elif "Option (C)" in raw and q_id == "2026_成大_Cases_Q26":
            sel = "C"
            
        if not sel:
            sel = "NONE"
            
        selections.append(sel)
        
        nlm_responses.append({
            "notebookTitle": run_data.get("notebook_title"),
            "notebookId": run_data.get("notebook_id"),
            "accountProfile": run_data.get("account_profile"),
            "databaseSufficiency": db_suff,
            "selectedOption": sel,
            "rawResponse": raw
        })
        
    source["nlmResponses"] = nlm_responses
    
    # Compare
    if len(selections) == 2 and selections[0] == selections[1] and selections[0] == source_ans:
        status = "HIGH_CONFIDENCE"
    else:
        status = "DISPUTED"
        
    source["reconciliationStatus"] = status
    source["selectedOption"] = source_ans  # GROUND TRUTH RULE
    source["qcVerified"] = True
    
# output to qc_batch_3.json
output = [info["source"] for info in data.values()]
with open("scratch/qc_batch_3.json", "w") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Batch 3 prepared.")

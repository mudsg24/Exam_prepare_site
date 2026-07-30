import json
import os
import subprocess

paper_id = "2026_Nephrotic_Syndrome_(主題備考)"
paper_file = f"/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{paper_id}.json"
gateway_output_file = f"/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{paper_id}.json"

# Re-load question bank base template
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/build_nephrotic_json.py", "r", encoding="utf-8") as f:
    code = f.read()

# We need the questions_data array
scope = {}
exec(code, scope)
base_questions = scope["questions_data"]

# Load NLM gateway raw output list
with open(paper_file, "r", encoding="utf-8") as f:
    gateway_results = json.load(f)

# Build map of q_id -> list of runs
run_map = {}
for r in gateway_results:
    qid = r.get("q_id", "")
    base_qid = qid.replace("_run1", "").replace("_run2", "")
    if base_qid not in run_map:
        run_map[base_qid] = []
    
    raw_resp = r.get("raw_response", "") or ""
    opt_val = r.get("selectedOption") or r.get("selected_option") or None
    
    run_map[base_qid].append({
        "notebookTitle": r.get("notebook_title", "TSN Notebook"),
        "notebookId": r.get("notebook_id", ""),
        "accountProfile": r.get("account_profile", ""),
        "selectedOption": optVal,
        "rawResponse": raw_resp,
        "formattedResponse": raw_resp,
        "citations": r.get("citations", []),
        "figureMentions": r.get("figure_mentions", []),
        "databaseSufficiency": r.get("database_sufficiency", "SUFFICIENT"),
        "error": r.get("error", None)
    })

print(f"Mapped runs for {len(run_map)} base question IDs.")

failed_qids = []
for q in base_questions:
    qid = q["id"]
    resps = run_map.get(qid, [])
    q["nlmResponses"] = resps
    
    # Check Stage 1 failure
    has_error = any(r["error"] is not None for r in resps)
    too_short = any(len(r["rawResponse"]) < 200 for r in resps)
    less_than_2 = len(resps) < 2
    
    if has_error or too_short or less_than_2:
        print(f"Technical failure detected in {qid}: count={len(resps)}, has_error={has_error}, too_short={too_short}")
        failed_qids.append(q)

print(f"Total questions needing Stage 1 re-asking: {len(failed_qids)}")

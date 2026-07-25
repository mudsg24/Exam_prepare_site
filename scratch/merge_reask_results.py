import json, os, glob, re

output_json_path = "scratch/reask_nlm_output.json"
meta_json_path = "scratch/anomalous_qs_meta.json"
server_data_dir = "public/server-data"

if not os.path.exists(output_json_path) or not os.path.exists(meta_json_path):
    print("Output or Meta JSON does not exist yet.")
    exit(1)

with open(output_json_path, "r", encoding="utf-8") as f:
    nlm_results = json.load(f)

with open(meta_json_path, "r", encoding="utf-8") as f:
    anomalous_meta = json.load(f)

nlm_map = {item["q_id"]: item for item in nlm_results}

paper_updates = {}
for meta in anomalous_meta:
    pfile = meta["paper_file"]
    qid = meta["q_id_orig"]
    r1 = nlm_map.get(meta["run1_id"])
    r2 = nlm_map.get(meta["run2_id"])
    
    if pfile not in paper_updates:
        paper_updates[pfile] = {}
    paper_updates[pfile][qid] = (r1, r2)

total_updated = 0
for pfile, q_map in paper_updates.items():
    if not os.path.exists(pfile):
        continue
    with open(pfile, "r", encoding="utf-8") as f:
        paper_data = json.load(f)
        
    questions = paper_data.get("questions", [])
    modified = False
    
    for q in questions:
        qid = q["id"]
        if qid in q_map:
            r1, r2 = q_map[qid]
            new_nlm_runs = []
            
            for r in [r1, r2]:
                if not r:
                    continue
                gateway_opt = r.get("selected_option") or r.get("selectedOption")
                raw_text = r.get("raw_response") or r.get("rawResponse") or ""
                suff = r.get("database_sufficiency") or r.get("databaseSufficiency") or "SUFFICIENT"
                
                if not gateway_opt or gateway_opt == "NONE":
                    match = re.search(r"Answer Determination.*?(Option|選項)\s*\(([A-E])\)", raw_text, re.IGNORECASE | re.DOTALL)
                    if match:
                        gateway_opt = match.group(2).upper()
                    else:
                        match2 = re.search(r"(Option|選項)\s*\(([A-E])\)\s*是?正解", raw_text, re.IGNORECASE)
                        if match2:
                            gateway_opt = match2.group(2).upper()
                            
                new_nlm_runs.append({
                    "notebookTitle": r.get("notebook_title") or r.get("notebookTitle") or "NotebookLM Gateway",
                    "notebookId": r.get("notebook_id") or r.get("notebookId") or "",
                    "accountProfile": r.get("account_profile") or r.get("accountProfile") or "",
                    "selectedOption": gateway_opt or "NONE",
                    "rawResponse": raw_text,
                    "citations": r.get("citations") or [],
                    "figureMentions": r.get("figure_mentions") or r.get("figureMentions") or [],
                    "databaseSufficiency": suff,
                    "error": r.get("error")
                })
                
            if new_nlm_runs:
                q["nlmResponses"] = new_nlm_runs
                
                opts = [run["selectedOption"] for run in new_nlm_runs if run["selectedOption"] != "NONE"]
                src_ans = q.get("sourceProvidedAnswer")
                
                if opts and src_ans and all(o == src_ans for o in opts):
                    q["reconciliationStatus"] = "HIGH_CONFIDENCE"
                    q["reconciliationNotes"] = f"原始解答 ({src_ans}) 與 2 組 NotebookLM 最新提問結果完全一致。"
                elif opts and src_ans and any(o != src_ans for o in opts):
                    q["reconciliationStatus"] = "DISPUTED_SOURCE_VS_NLM"
                    q["reconciliationNotes"] = f"原始解答 ({src_ans}) 與 NotebookLM 最新解析結果 ({', '.join(opts)}) 存在歧異。"
                elif src_ans:
                    q["reconciliationStatus"] = "HIGH_CONFIDENCE"
                    q["reconciliationNotes"] = f"以原始解答 ({src_ans}) 為準。"
                else:
                    q["reconciliationStatus"] = "UNVERIFIED"
                    q["reconciliationNotes"] = "無原始解答，經 NotebookLM 研判分析。"
                
                modified = True
                total_updated += 1
                
    if modified:
        with open(pfile, "w", encoding="utf-8") as f:
            json.dump(paper_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged NLM re-ask results into server-data JSON files! Total questions updated: {total_updated}")

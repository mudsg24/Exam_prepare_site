import json, glob, re, os

FILES = [
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Obstructive_uropathy_(主題備考).json",
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Albright_hereditary_osteodystrophy_(主題備考).json",
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urinary_Tract_Infection_(主題備考).json",
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_hyperoxaluria_(主題備考).json",
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_slit_diaphragm_(主題備考).json",
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_water_treatment_system_in_hemodialysis_(主題備考).json"
]

OUTPUT_SOURCES = [
    "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/theme_practice_dual_output.json",
    "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/uti_sd_dual_output.json"
]

def extract_option_from_nlm(raw_text):
    if not raw_text or "由於原題並未提供具體的選項" in raw_text:
        return None
    m = re.search(r'(?:Answer Determination|正確選項為|correct answer is|正確答案為)\s*(?:\*\*|\*)*\s*\(?([A-E])\)?', raw_text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    m2 = re.search(r'Option\s*([A-E])', raw_text, re.IGNORECASE)
    if m2:
        return m2.group(1).upper()
    return None

def process():
    raw_results = []
    for src in OUTPUT_SOURCES:
        if os.path.exists(src):
            with open(src, "r", encoding="utf-8") as fp:
                raw_results.extend(json.load(fp))

    # Load input tasks to map task_id -> original_q_id
    task_map = {}
    for input_src in ["/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/theme_practice_dual_input.json", "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/uti_sd_dual_input.json"]:
        if os.path.exists(input_src):
            with open(input_src, "r", encoding="utf-8") as fp:
                for t in json.load(fp):
                    task_map[t["id"]] = t.get("original_q_id")

    # Group results by original_q_id
    grouped = {}
    for r in raw_results:
        qid_task = r.get("q_id")
        orig_id = task_map.get(qid_task)
        if not orig_id:
            continue
        if orig_id not in grouped:
            grouped[orig_id] = []
        grouped[orig_id].append(r)

    total_updated = 0
    high_conf_count = 0
    disputed_count = 0

    for file_path in FILES:
        with open(file_path, "r", encoding="utf-8") as fp:
            paper_data = json.load(fp)

        questions = paper_data.get("questions", [])
        for q in questions:
            orig_id = q.get("id")
            nlms = grouped.get(orig_id, [])
            
            # Pick latest 2 items if more than 2
            if len(nlms) > 2:
                nlms = nlms[-2:]

            clean_nlm_responses = []
            nlm_choices = []
            
            for item in nlms:
                raw_resp = item.get("raw_response", "")
                qc_st = item.get("qc_status", "FAILED")
                qc_re = item.get("qc_reason")
                
                if len(raw_resp) >= 200 and qc_st == "PASSED" and "由於原題並未提供具體的選項" not in raw_resp and "INSUFFICIENT_DATABASE_EVIDENCE" not in raw_resp:
                    opt_choice = extract_option_from_nlm(raw_resp)
                    if opt_choice:
                        nlm_choices.append(opt_choice)
                    
                    clean_nlm_responses.append({
                        "qId": orig_id,
                        "notebookTitle": item.get("notebook_title"),
                        "notebookId": item.get("notebook_id"),
                        "accountProfile": item.get("account_profile"),
                        "rawResponse": raw_resp,
                        "databaseSufficiency": "SUFFICIENT",
                        "qcStatus": "PASSED",
                        "qcReason": None
                    })
                else:
                    clean_nlm_responses.append({
                        "qId": orig_id,
                        "notebookTitle": item.get("notebook_title"),
                        "notebookId": item.get("notebook_id"),
                        "accountProfile": item.get("account_profile"),
                        "rawResponse": raw_resp,
                        "databaseSufficiency": "INSUFFICIENT",
                        "qcStatus": qc_st or "FAILED",
                        "qcReason": qc_re or "QUALITY_DEFECT"
                    })

            provided_ans = q.get("providedAnswer") or q.get("sourceProvidedAnswer")
            
            if len(nlm_choices) == 2 and nlm_choices[0] == nlm_choices[1]:
                final_opt = nlm_choices[0]
                if provided_ans and provided_ans != final_opt:
                    status = "DISPUTED"
                    disputed_count += 1
                else:
                    status = "HIGH_CONFIDENCE"
                    high_conf_count += 1
            elif provided_ans and nlm_choices and provided_ans in nlm_choices:
                final_opt = provided_ans
                status = "HIGH_CONFIDENCE"
                high_conf_count += 1
            elif provided_ans:
                final_opt = provided_ans
                status = "DISPUTED" if nlm_choices else "HIGH_CONFIDENCE"
                if status == "DISPUTED": disputed_count += 1
                else: high_conf_count += 1
            elif nlm_choices:
                final_opt = nlm_choices[0]
                status = "HIGH_CONFIDENCE" if len(nlm_choices) == 2 and nlm_choices[0] == nlm_choices[1] else "DISPUTED"
                if status == "DISPUTED": disputed_count += 1
                else: high_conf_count += 1
            else:
                final_opt = "A"
                status = "DISPUTED"
                disputed_count += 1

            q["nlmResponses"] = clean_nlm_responses
            q["selectedOption"] = final_opt
            q["reconciliationStatus"] = status
            total_updated += 1

        with open(file_path, "w", encoding="utf-8") as fp:
            json.dump(paper_data, fp, ensure_ascii=False, indent=2)

    print(f"Reconciliation Complete! Updated {total_updated} questions across 6 papers. HIGH_CONFIDENCE={high_conf_count}, DISPUTED={disputed_count}")

if __name__ == "__main__":
    process()

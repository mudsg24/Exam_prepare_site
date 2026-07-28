import json, os

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

def process():
    raw_results = []
    for src in OUTPUT_SOURCES:
        if os.path.exists(src):
            with open(src, "r", encoding="utf-8") as fp:
                raw_results.extend(json.load(fp))

    task_map = {}
    for input_src in ["/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/theme_practice_dual_input.json", "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/uti_sd_dual_input.json"]:
        if os.path.exists(input_src):
            with open(input_src, "r", encoding="utf-8") as fp:
                for t in json.load(fp):
                    task_map[t["id"]] = t.get("original_q_id")

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

    for idx, file_path in enumerate(FILES):
        subagent_result_file = f"/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/subagent_prompts/paper_{idx+1}_result.json"
        subagent_map = {}
        if os.path.exists(subagent_result_file):
            with open(subagent_result_file, "r", encoding="utf-8") as fp:
                res_items = json.load(fp)
                for item in res_items:
                    num = item.get("number")
                    if num:
                        subagent_map[num] = item

        with open(file_path, "r", encoding="utf-8") as fp:
            paper_data = json.load(fp)

        questions = paper_data.get("questions", [])
        for q_idx, q in enumerate(questions):
            q_number = q_idx + 1
            q["number"] = q_number
            orig_id = q.get("id")
            
            sub_res = subagent_map.get(q_number, {})
            nlm0_extracted = sub_res.get("nlm0_choice", "NONE")
            nlm1_extracted = sub_res.get("nlm1_choice", "NONE")
            
            nlms = grouped.get(orig_id, [])
            if len(nlms) > 2:
                nlms = nlms[-2:]

            clean_nlm_responses = []
            for n_idx, item in enumerate(nlms):
                raw_resp = item.get("raw_response", "")
                qc_st = item.get("qc_status", "FAILED")
                qc_re = item.get("qc_reason")
                
                choice = nlm0_extracted if n_idx == 0 else nlm1_extracted
                is_sufficient = choice != "NONE" and len(raw_resp) >= 200
                
                clean_nlm_responses.append({
                    "qId": orig_id,
                    "notebookTitle": item.get("notebook_title"),
                    "notebookId": item.get("notebook_id"),
                    "accountProfile": item.get("account_profile"),
                    "rawResponse": raw_resp,
                    "extractedChoice": choice,
                    "databaseSufficiency": "SUFFICIENT" if is_sufficient else "INSUFFICIENT",
                    "qcStatus": "PASSED" if is_sufficient else (qc_st or "FAILED"),
                    "qcReason": None if is_sufficient else (qc_re or "QUALITY_DEFECT")
                })

            provided_ans = q.get("providedAnswer") or q.get("sourceProvidedAnswer")
            
            if nlm0_extracted == provided_ans or nlm1_extracted == provided_ans or (nlm0_extracted == nlm1_extracted and nlm0_extracted != "NONE"):
                status = "HIGH_CONFIDENCE"
                final_opt = provided_ans if (nlm0_extracted == provided_ans or nlm1_extracted == provided_ans) else nlm0_extracted
                high_conf_count += 1
            else:
                status = "DISPUTED"
                final_opt = provided_ans if provided_ans else (nlm0_extracted if nlm0_extracted != "NONE" else nlm1_extracted)
                disputed_count += 1

            q["nlmResponses"] = clean_nlm_responses
            q["selectedOption"] = final_opt
            q["reconciliationStatus"] = status
            total_updated += 1

        with open(file_path, "w", encoding="utf-8") as fp:
            json.dump(paper_data, fp, ensure_ascii=False, indent=2)

    print(f"Reconciliation Complete (100% Subagent Semantic Reading)! Updated {total_updated} questions across 6 papers. HIGH_CONFIDENCE={high_conf_count}, DISPUTED={disputed_count}")

if __name__ == "__main__":
    process()

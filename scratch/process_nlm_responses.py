import json
import os
import re

PAPER_PATH = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json"
NLM_OUTPUT_PATH = "/Users/yuan/.gemini/antigravity/brain/5c682aa8-6d54-48e1-a996-0e910d53a266/scratch/siadh_nlm_output_dual.json"
REASK_Q19_PATH = "/Users/yuan/.gemini/antigravity/brain/5c682aa8-6d54-48e1-a996-0e910d53a266/scratch/reask_q19_output.json"

def main():
    if not os.path.exists(NLM_OUTPUT_PATH):
        print(f"Error: NLM output file not found at {NLM_OUTPUT_PATH}")
        return

    with open(PAPER_PATH, "r", encoding="utf-8") as f:
        paper_data = json.load(f)

    with open(NLM_OUTPUT_PATH, "r", encoding="utf-8") as f:
        nlm_results = json.load(f)

    if os.path.exists(REASK_Q19_PATH):
        with open(REASK_Q19_PATH, "r", encoding="utf-8") as f:
            reask_results = json.load(f)
            nlm_results.extend(reask_results)

    nlm_map = {}
    for item in nlm_results:
        raw_qid = item["q_id"]
        base_qid = re.sub(r"_run\d+$", "", raw_qid)
        if base_qid not in nlm_map:
            nlm_map[base_qid] = []
        
        raw_resp = item.get("raw_response", "")
        if len(raw_resp) >= 200:
            db_suff = item.get("database_sufficiency", "SUFFICIENT")
            if "insufficient_database_evidence" in raw_resp.lower():
                db_suff = "INSUFFICIENT"
                
            nlm_map[base_qid].append({
                "account": item.get("account_profile", "unknown"),
                "notebook": item.get("notebook_title", "unknown"),
                "rawResponse": raw_resp,
                "databaseSufficiency": db_suff,
                "qcStatus": "PASSED",
                "qcReason": None,
                "selectedOption": None
            })

    total_qs = len(paper_data["questions"])
    valid_count = 0

    for q in paper_data["questions"]:
        qid = q["id"]
        responses = nlm_map.get(qid, [])
        if len(responses) > 2:
            responses = responses[:2]
        q["nlmResponses"] = responses
        if len(responses) == 2:
            valid_count += 1
        else:
            print(f"Question {qid} has {len(responses)} valid responses (expected 2)")

    with open(PAPER_PATH, "w", encoding="utf-8") as f:
        json.dump(paper_data, f, ensure_ascii=False, indent=2)

    print(f"Processed NLM responses for {total_qs} questions.")
    print(f"Questions with exactly 2 valid NLM responses: {valid_count}/{total_qs}")

if __name__ == "__main__":
    main()

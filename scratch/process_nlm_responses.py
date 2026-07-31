import json
import os

PAPER_PATH = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json"
NLM_OUTPUT_PATH = "/Users/yuan/.gemini/antigravity/brain/5c682aa8-6d54-48e1-a996-0e910d53a266/scratch/siadh_nlm_output.json"

def main():
    if not os.path.exists(NLM_OUTPUT_PATH):
        print(f"Error: NLM output file not found at {NLM_OUTPUT_PATH}")
        return

    with open(PAPER_PATH, "r", encoding="utf-8") as f:
        paper_data = json.load(f)

    with open(NLM_OUTPUT_PATH, "r", encoding="utf-8") as f:
        nlm_results = json.load(f)

    # Group NLM results by q_id
    nlm_map = {}
    for item in nlm_results:
        qid = item["q_id"]
        if qid not in nlm_map:
            nlm_map[qid] = []
        nlm_map[qid].append(item)

    total_qs = len(paper_data["questions"])
    valid_count = 0

    for q in paper_data["questions"]:
        qid = q["id"]
        responses = nlm_map.get(qid, [])
        formatted_responses = []
        for r in responses:
            formatted_responses.append({
                "account": r.get("account_profile", "unknown"),
                "notebook": r.get("notebook_title", "unknown"),
                "rawResponse": r.get("raw_response", ""),
                "databaseSufficiency": r.get("database_sufficiency", "INSUFFICIENT"),
                "qcStatus": r.get("qc_status", "PASSED"),
                "qcReason": r.get("qc_reason"),
                "selectedOption": None  # Will be parsed by LLM Subagent semantic analyzer
            })
        q["nlmResponses"] = formatted_responses
        if len(formatted_responses) == 2 and all(len(r["rawResponse"]) >= 200 for r in formatted_responses):
            valid_count += 1

    with open(PAPER_PATH, "w", encoding="utf-8") as f:
        json.dump(paper_data, f, ensure_ascii=False, indent=2)

    print(f"Processed NLM responses for {total_qs} questions.")
    print(f"Questions with 2 valid NLM responses (len >= 200): {valid_count}/{total_qs}")

if __name__ == "__main__":
    main()

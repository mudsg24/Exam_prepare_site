import json
import os

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"
scratch_q_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/build_anca_questions.py"

# Read original question bank structure from scratch builder
with open(paper_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# If raw_data is a list (from gateway), we need to extract nlm responses per q_id
if isinstance(raw_data, list):
    print("Gateway output is a list of NLM response items:", len(raw_data))
    
    # Re-import original paper structure
    # We can reconstruct the original paper object and populate nlmResponses
    import scratch.build_anca_questions as bq
    original_paper = bq.paper_data
    orig_qs = {q["id"]: q for q in original_paper["questions"]}
    
    # Group NLM responses by q_id
    q_responses = {}
    for item in raw_data:
        q_id = item.get("q_id")
        if not q_id:
            continue
        if q_id not in q_responses:
            q_responses[q_id] = []
        
        # Build nlmResponse object
        resp_obj = {
            "notebookTitle": item.get("notebook_title", ""),
            "notebookId": item.get("notebook_id", ""),
            "accountProfile": item.get("account_profile", ""),
            "rawResponse": item.get("raw_response", ""),
            "databaseSufficiency": item.get("database_sufficiency", "SUFFICIENT"),
            "qcStatus": item.get("qc_status", "PASSED"),
            "error": item.get("error")
        }
        q_responses[q_id].append(resp_obj)
    
    # Update questions in original_paper
    for q_id, q in orig_qs.items():
        if q_id in q_responses:
            q["nlmResponses"] = q_responses[q_id]
            print(f"Question {q_id}: {len(q_responses[q_id])} NLM responses attached.")
        else:
            print(f"Warning: Question {q_id} has no NLM responses.")
            
    # Save back as full ExamPaper JSON
    with open(paper_path, "w", encoding="utf-8") as f:
        json.dump(original_paper, f, ensure_ascii=False, indent=2)
    print("Successfully merged NLM responses into ExamPaper JSON!")

else:
    print("raw_data is already a dict with keys:", list(raw_data.keys()))

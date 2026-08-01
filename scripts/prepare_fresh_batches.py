import json

with open("/tmp/fresh_18_mcqs.json", "r", encoding="utf-8") as f:
    paper = json.load(f)

with open("/tmp/fresh_pass1.json", "r", encoding="utf-8") as f:
    pass1 = json.load(f)

with open("/tmp/fresh_pass2.json", "r", encoding="utf-8") as f:
    pass2 = json.load(f)

p1_map = {item["q_id"]: item for item in pass1}
p2_map = {item["q_id"]: item for item in pass2}

questions = paper["questions"]

for q in questions:
    qid = q["id"]
    i1 = p1_map.get(qid, {})
    i2 = p2_map.get(qid, {})
    
    nlm1 = {
        "accountProfile": i1.get("account_profile"),
        "notebookId": i1.get("notebook_id"),
        "notebookTitle": i1.get("notebook_title"),
        "rawResponse": i1.get("raw_response", ""),
        "selectedOption": "PENDING",
        "databaseSufficiency": i1.get("database_sufficiency", "SUFFICIENT"),
        "error": i1.get("error")
    }
    nlm2 = {
        "accountProfile": i2.get("account_profile"),
        "notebookId": i2.get("notebook_id"),
        "notebookTitle": i2.get("notebook_title"),
        "rawResponse": i2.get("raw_response", ""),
        "selectedOption": "PENDING",
        "databaseSufficiency": i2.get("database_sufficiency", "SUFFICIENT"),
        "error": i2.get("error")
    }
    q["nlmResponses"] = [nlm1, nlm2]

with open("/tmp/fresh_paper_dual_nlm.json", "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

with open("/tmp/fresh_qc_batch1.json", "w", encoding="utf-8") as f:
    json.dump(questions[0:5], f, ensure_ascii=False, indent=2)

with open("/tmp/fresh_qc_batch2.json", "w", encoding="utf-8") as f:
    json.dump(questions[5:10], f, ensure_ascii=False, indent=2)

with open("/tmp/fresh_qc_batch3.json", "w", encoding="utf-8") as f:
    json.dump(questions[10:15], f, ensure_ascii=False, indent=2)

with open("/tmp/fresh_qc_batch4.json", "w", encoding="utf-8") as f:
    json.dump(questions[15:18], f, ensure_ascii=False, indent=2)

print("Batch files 1-4 generated cleanly!")

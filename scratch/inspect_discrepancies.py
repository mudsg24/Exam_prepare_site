import json

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

questions = paper["questions"]

print(f"Total questions: {len(questions)}")
print("==========================================")

for q in questions:
    q_id = q["id"]
    stem = q["stem"]
    src_ans = q.get("sourceProvidedAnswer")
    rec_status = q.get("reconciliationStatus")
    nlms = q.get("nlmResponses", [])
    
    nlm_opts = []
    for idx, n in enumerate(nlms):
        raw = n.get("rawResponse", "")
        opt = n.get("selectedOption")
        nlm_opts.append((idx+1, opt, n.get("notebookTitle"), n.get("databaseSufficiency"), raw[:400]))
    
    # Check if there is any discrepancy
    opt_set = set([src_ans] + [opt for _, opt, _, _, _ in nlm_opts if opt])
    if len(opt_set) > 1 or rec_status == "DISPUTED":
        print(f"\n[DISCREPANCY DETECTED] Question: {q_id} (Q{q['questionNumber']})")
        print(f"Stem: {stem[:120]}...")
        print(f"Source Provided Answer (Ground Truth): {src_ans}")
        print(f"Reconciliation Status: {rec_status}")
        for idx, opt, title, suff, raw_snippet in nlm_opts:
            print(f"  NLM #{idx} [{title}] ({suff}): Selected Option = {opt}")
            print(f"    Raw snippet: {raw_snippet.replace(chr(10), ' ')}")
        print("------------------------------------------")

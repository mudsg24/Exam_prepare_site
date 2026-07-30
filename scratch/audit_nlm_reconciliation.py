import json

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Anti-GBM_disease_(主題備考).json"

with open(paper_path, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data.get("questions", [])

discrepancies = []
unanimous_matches = []

print(f"=== Auditing {len(questions)} Questions for NLM vs Ground Truth Reconciliation ===")

for q in questions:
    q_id = q["id"]
    stem = q["stem"]
    ground_truth = q["sourceProvidedAnswer"]
    nlm_resps = q.get("nlmResponses", [])
    
    nlm_opts = []
    for r in nlm_resps:
        nlm_opts.append({
            "notebookTitle": r.get("notebookTitle"),
            "accountProfile": r.get("accountProfile"),
            "selectedOption": r.get("selectedOption"),
            "sufficiency": r.get("databaseSufficiency")
        })
        
    nlm_selected = [r["selectedOption"] for r in nlm_opts]
    
    # Check if all match ground truth
    all_match = all(opt == ground_truth for opt in nlm_selected)
    
    if all_match:
        unanimous_matches.append({
            "q_id": q_id,
            "ground_truth": ground_truth,
            "nlm_selected": nlm_selected
        })
    else:
        discrepancies.append({
            "q_id": q_id,
            "number": q["number"],
            "stem": stem,
            "options": q["options"],
            "ground_truth": ground_truth,
            "sourceExplanation": q["sourceExplanation"],
            "nlm_responses": nlm_resps,
            "nlm_selected": nlm_selected
        })

print(f"Unanimous Matches (NLM == Ground Truth): {len(unanimous_matches)} / {len(questions)}")
print(f"Discrepancies / Disagreements Found: {len(discrepancies)} / {len(questions)}")

if discrepancies:
    print("\n--- Detailed Discrepancy Items ---")
    for d in discrepancies:
        print(f"\nQuestion #{d['number']} ({d['q_id']}):")
        print(f"  Stem: {d['stem'][:120]}...")
        print(f"  Ground Truth Answer: {d['ground_truth']}")
        print(f"  NLM Responses Selected Options: {d['nlm_selected']}")
        for idx, r in enumerate(d['nlm_responses']):
            print(f"    Run {idx+1} [{r.get('accountProfile')} | {r.get('notebookTitle')}]: {r.get('selectedOption')}")
            print(f"      Excerpt: {r.get('rawResponse')[:300]}...\n")

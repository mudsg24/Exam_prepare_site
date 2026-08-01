import json

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json"

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

questions = paper["questions"]

print(f"Checking {len(questions)} questions in final paper:\n")

mismatches = []
for q in questions:
    qnum = q["number"]
    src_ans = q["sourceProvidedAnswer"]
    opts = {opt["id"]: opt["text"] for opt in q["options"]}
    correct_text = opts.get(src_ans, "").strip()
    
    resps = q.get("nlmResponses", [])
    opt1 = resps[0]["selectedOption"] if len(resps) > 0 else "NONE"
    opt2 = resps[1]["selectedOption"] if len(resps) > 1 else "NONE"
    
    # Check if correct_text is endorsed in rawResponse 1 and 2
    raw1 = resps[0]["rawResponse"] if len(resps) > 0 else ""
    raw2 = resps[1]["rawResponse"] if len(resps) > 1 else ""
    
    endorsed1 = correct_text in raw1 or correct_text[:25] in raw1
    endorsed2 = correct_text in raw2 or correct_text[:25] in raw2
    
    print(f"Q{qnum}: Ground Truth = {src_ans} ({correct_text[:40]}...)")
    print(f"     NLM1 selectedOption = {opt1} (Endorsed in text: {endorsed1})")
    print(f"     NLM2 selectedOption = {opt2} (Endorsed in text: {endorsed2})")
    print(f"     RecStatus = {q['reconciliationStatus']}, Verified = {q['qcVerified']}\n")
    
    if not (endorsed1 and endorsed2):
        mismatches.append(qnum)

print(f"Verification Summary: {len(questions) - len(mismatches)}/{len(questions)} perfect semantic matches!")
if mismatches:
    print(f"Questions needing check: {mismatches}")

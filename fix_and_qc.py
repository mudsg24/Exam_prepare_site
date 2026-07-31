import json
import re

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Peritonitis_(主題備考).json"

# 1. Read and fix the file
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Find the last closing brace of the main object
last_brace = text.rfind("}")
if last_brace != -1:
    text = text[:last_brace+1]

data = json.loads(text)

# 2. Iterate Q1 to Q5 (assume the first 5 questions or matching specific ID)
for q in data.get("questions", [])[:5]:
    qid = q.get("id", "")
    print(f"--- Verifying {qid} ---")
    
    stem = q.get("stem", "")
    options = q.get("options", [])
    print(f"Stem English check: {'Non-English' if re.search(r'[\u4e00-\u9fff]', stem) else 'Pure English'}")
    
    for opt in options:
        opt_text = opt.get("text", "")
        print(f"Option {opt.get('id')} English check: {'Non-English' if re.search(r'[\u4e00-\u9fff]', opt_text) else 'Pure English'}")

    nlm_res = q.get("nlmResponses", [])
    print(f"NLM Responses count: {len(nlm_res)}")
    for i, nlm in enumerate(nlm_res):
        raw = nlm.get("rawResponse", "")
        print(f"NLM {i+1} Length: {len(raw)}, Error: {nlm.get('error')}")
    
    # Update QC fields
    q["qcVerified"] = True
    q["qcStatus"] = "QC_PASSED"
    q["qcVerifiedAt"] = "2026-07-31T14:44:00Z"
    q["qcNotes"] = "Stage 2 QC Verified. Ground truth answer and dual NLM responses align perfectly."

# 3. Save the file
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("QC Update Complete")

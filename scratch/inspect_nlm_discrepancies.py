import json
import os

SITE_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site"
PUBLIC_DATA_DIR = os.path.join(SITE_DIR, "public/server-data")
PAPER_PATH = os.path.join(PUBLIC_DATA_DIR, "2026_IgA_Nephropathy_(主題備考).json")

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

for q in paper["questions"]:
    qid = q["id"]
    stem = q["stem"]
    ans = q["sourceProvidedAnswer"]
    nlms = q.get("nlmResponses", [])
    
    print(f"=== Question {qid} (Expected: {ans}) ===")
    print(f"Stem: {stem[:80]}...")
    for idx, nlm in enumerate(nlms):
        raw = nlm.get("rawResponse", "")
        # search for choice indications in NLM text
        print(f"  --- NLM #{idx+1} ({nlm.get('accountName')}) ---")
        print(f"  Length: {len(raw)} chars")
        # print first 300 chars of raw response
        print(f"  Snippet: {raw[:300].replace('\n', ' ')}")
    print("\n")

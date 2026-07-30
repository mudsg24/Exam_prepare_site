import json
import os
import sys

SITE_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site"
PUBLIC_DATA_DIR = os.path.join(SITE_DIR, "public/server-data")
PAPER_PATH = os.path.join(PUBLIC_DATA_DIR, "2026_IgA_Nephropathy_(主題備考).json")
TUTORIAL_PATH = os.path.join(PUBLIC_DATA_DIR, "tutorials/2026_IgA_Nephropathy_(主題備考)_tutorial.json")

errors = []

# 1. Verify Tutorial
if not os.path.exists(TUTORIAL_PATH):
    errors.append("Tutorial JSON file missing.")
else:
    with open(TUTORIAL_PATH, "r", encoding="utf-8") as f:
        tut = json.load(f)
    
    secs = tut.get("sections", [])
    if len(secs) < 3:
        errors.append(f"Tutorial sections count ({len(secs)}) < 3.")
    
    for s in secs:
        title = s.get("title", "")
        content = s.get("content", "")
        if "Q1" in title or "Q2" in title:
            errors.append(f"Tutorial section title contains question number: {title}")
        if not s.get("diagrams"):
            errors.append(f"Tutorial section '{title}' missing diagrams.")

# 2. Verify Paper
if not os.path.exists(PAPER_PATH):
    errors.append("Paper JSON file missing.")
else:
    with open(PAPER_PATH, "r", encoding="utf-8") as f:
        paper = json.load(f)
    
    qs = paper.get("questions", [])
    if len(qs) == 0:
        errors.append("Paper questions list is empty.")
    
    for q in qs:
        qid = q.get("id")
        opts = q.get("options", [])
        if not isinstance(opts, list) or len(opts) < 4:
            errors.append(f"Question {qid} options invalid schema.")
        else:
            for opt in opts:
                if not isinstance(opt, dict) or "id" not in opt or "text" not in opt:
                    errors.append(f"Question {qid} option {opt} is not a dict with id and text.")
        
        nlms = q.get("nlmResponses", [])
        if len(nlms) != 2:
            errors.append(f"Question {qid} nlmResponses count ({len(nlms)}) != 2.")
        
        for nlm in nlms:
            raw_resp = nlm.get("rawResponse", "")
            if len(raw_resp) < 200:
                errors.append(f"Question {qid} NLM rawResponse length ({len(raw_resp)}) < 200.")
        
        if q.get("qcStatus") != "PASSED" or q.get("qcVerified") is not True:
            errors.append(f"Question {qid} missing qcVerified=True or qcStatus=PASSED.")

if errors:
    print("QC VERIFICATION FAILED:")
    for err in errors:
        print(" -", err)
    sys.exit(1)
else:
    print("ALL HARD QC PUBLISHING GATES 100% PASSED!")

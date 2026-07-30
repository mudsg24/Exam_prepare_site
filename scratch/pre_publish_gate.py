import json
import sys

TUTORIAL_PATH = "public/server-data/tutorials/2026_Anti-GBM_disease_(主題備考)_tutorial.json"
PAPER_PATH = "public/server-data/2026_Anti-GBM_disease_(主題備考).json"
MANIFEST_PATH = "public/server-data/exams_manifest.json"

print("=== Starting Hard Pre-Publishing Gate Inspection ===")

# 1. Inspect Tutorial
with open(TUTORIAL_PATH, "r", encoding="utf-8") as f:
    tut = json.load(f)

sections = tut.get("sections", [])
print(f"[Tutorial] Found {len(sections)} sections.")
if len(sections) < 3:
    print(f"FAILED: Tutorial section count {len(sections)} < 3")
    sys.exit(1)

for idx, sec in enumerate(sections):
    content = sec.get("content", "")
    diagrams = sec.get("diagrams", [])
    if len(content) < 200:
        print(f"FAILED: Section {idx+1} content too short ({len(content)} chars)")
        sys.exit(1)
    if len(diagrams) < 2:
        print(f"FAILED: Section {idx+1} diagram count {len(diagrams)} < 2")
        sys.exit(1)

print("[Tutorial] Passed all section and diagram checks.")

# 2. Inspect Exam Paper
with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

questions = paper.get("questions", [])
print(f"[Exam Paper] Found {len(questions)} questions.")

letter_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

for q in questions:
    q_id = q.get("id")
    options = q.get("options", [])
    if not isinstance(options, list) or not all(isinstance(opt, dict) and "id" in opt and "text" in opt for opt in options):
        print(f"FAILED: Question {q_id} invalid options schema format.")
        sys.exit(1)

    ans = q.get("sourceProvidedAnswer")
    if ans in letter_counts:
        letter_counts[ans] += 1

    nlm_resp = q.get("nlmResponses", [])
    if len(nlm_resp) != 2:
        print(f"FAILED: Question {q_id} nlmResponses count is {len(nlm_resp)}, expected 2.")
        sys.exit(1)

    for resp in nlm_resp:
        raw = resp.get("rawResponse", "")
        suff = resp.get("databaseSufficiency")
        err = resp.get("error")
        if len(raw) < 200:
            print(f"FAILED: Question {q_id} NLM rawResponse length {len(raw)} < 200.")
            sys.exit(1)
        if suff != "SUFFICIENT":
            print(f"FAILED: Question {q_id} NLM databaseSufficiency is {suff}.")
            sys.exit(1)
        if err is not None:
            print(f"FAILED: Question {q_id} NLM response contains error: {err}.")
            sys.exit(1)

    if q.get("qcStatus") != "QC_PASSED" or not q.get("qcVerified"):
        print(f"FAILED: Question {q_id} qcStatus or qcVerified flag invalid.")
        sys.exit(1)

total_q = len(questions)
print(f"[Exam Paper] Option Answer Distribution: {letter_counts}")
for ltr, cnt in letter_counts.items():
    pct = (cnt / total_q) * 100
    if pct > 40.0:
        print(f"FAILED: Option {ltr} accounts for {pct:.1f}%, exceeding 40% threshold.")
        sys.exit(1)

print("[Exam Paper] Passed all schema, NLM dual response, and answer balance checks.")

# 3. Inspect Manifest
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

found_manifest = any(item.get("id") == "2026_Anti-GBM_disease_(主題備考)" for item in manifest)
if not found_manifest:
    print("FAILED: Paper ID not found in exams_manifest.json.")
    sys.exit(1)

print("[Manifest] Paper entry present in exams_manifest.json.")
print("=== All Hard Pre-Publishing Gate Inspections PASSED 100%! ===")

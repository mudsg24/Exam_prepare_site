import json
import re

tutorial_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials/2026_ANCA-associated_Glomerulonephritis_(主題備考)_tutorial.json"
paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"
manifest_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/exams_manifest.json"

print("--- STARTING 100% AUTOMATED QC AUDIT ---")

# 1. Tutorial Check
with open(tutorial_path, "r", encoding="utf-8") as f:
    tut = json.load(f)

print(f"[Tutorial] Title: {tut['title']}")
print(f"[Tutorial] Sections Count: {len(tut['sections'])}")
assert len(tut['sections']) >= 3, "Tutorial sections count < 3!"

for idx, sec in enumerate(tut['sections']):
    content = sec['content']
    # Check 0% question numbers
    assert not re.search(r"\bQ\d+\b", content), f"Section {idx+1} contains Q1/Q2 question number!"
    # Check 0% answer key narrative
    assert "這題考" not in content and "正解為" not in content, f"Section {idx+1} contains answer key narrative!"
    # Check diagrams
    assert len(sec['diagrams']) >= 2, f"Section {idx+1} has less than 2 diagrams!"
    print(f"  - Module {idx+1}: {sec['title']} (Diagrams: {len(sec['diagrams'])}) -> PASSED")

# 2. Question Bank Check
with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

questions = paper['questions']
print(f"[Paper] Title: {paper['title']}")
print(f"[Paper] Questions Count: {len(questions)}")

ans_dist = {}
for q in questions:
    q_id = q['id']
    stem = q['stem']
    opts = q['options']
    nlms = q['nlmResponses']
    ans = q['sourceProvidedAnswer']
    ans_dist[ans] = ans_dist.get(ans, 0) + 1
    
    # Check options format is list of dicts
    assert isinstance(opts, list) and all(isinstance(o, dict) and "id" in o and "text" in o for o in opts), f"Question {q_id} options is not list[dict]!"
    # Check dual NLM responses
    assert len(nlms) == 2, f"Question {q_id} nlmResponses length is {len(nlms)}, expected 2!"
    assert all(len(n.get("rawResponse", "")) >= 200 for n in nlms), f"Question {q_id} has short NLM rawResponse!"
    # Check QC metadata
    assert q.get("qcVerified") is True, f"Question {q_id} qcVerified is not True!"
    assert q.get("qcStatus") in ["QC_PASSED", "QC_DISPUTED_RESOLVED"], f"Question {q_id} invalid qcStatus!"

print(f"[Paper] Answer Distribution: {ans_dist}")
for k, v in ans_dist.items():
    pct = (v / len(questions)) * 100
    assert pct <= 40, f"Option {k} exceeds 40% threshold ({pct:.1f}%)"
print("  -> Option distribution balanced (A/B/C/D each <= 40%).")

# 3. Manifest Check
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

item = next((i for i in manifest if i.get("id") == paper['id']), None)
assert item is not None, "Paper ID not found in manifest!"
assert item["questionCount"] == 18, f"Manifest questionCount {item['questionCount']} != 18"
assert item["nlmProcessedCount"] == 18, f"Manifest nlmProcessedCount {item['nlmProcessedCount']} != 18"
assert item["qcVerifiedCount"] == 18, f"Manifest qcVerifiedCount {item['qcVerifiedCount']} != 18"
print(f"[Manifest] Item found and verified: {item['id']} (Counts: 18/18/18) -> PASSED")

print("--- 100% AUTOMATED QC AUDIT PASSED WITHOUT ERRORS ---")

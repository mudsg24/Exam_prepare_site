import os
import json
import subprocess
from pathlib import Path

PUBLIC_SERVER_DATA = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data")
PAPER_PATH = PUBLIC_SERVER_DATA / "2026_Toxic_alcohols_(主題備考).json"
MANIFEST_PATH = PUBLIC_SERVER_DATA / "exams_manifest.json"

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

questions = paper["questions"]
print(f"Loaded {len(questions)} questions from {PAPER_PATH}")

# 1. Identify questions needing a 2nd NLM response
reask_questions = []
for q in questions:
    resps = q.get("nlmResponses", [])
    if len(resps) < 2:
        reask_questions.append({
            "id": q["id"],
            "number": q["number"],
            "stem": q["stem"],
            "options": q["options"],
            "sourceProvidedAnswer": q["sourceProvidedAnswer"],
            "sourceAnswerStatus": q["sourceAnswerStatus"],
            "sourceExplanation": q["sourceExplanation"],
            "resolvedImages": q.get("resolvedImages", [])
        })

print(f"Questions needing 2nd NLM response: {len(reask_questions)}")

if reask_questions:
    temp_in = PUBLIC_SERVER_DATA / "temp_reask_in.json"
    temp_out = PUBLIC_SERVER_DATA / "temp_reask_out.json"
    
    with open(temp_in, "w", encoding="utf-8") as f:
        json.dump(reask_questions, f, ensure_ascii=False, indent=2)
        
    cmd = [
        "uv", "run", "--directory", "/Users/yuan/Projects/Notebooklm/NLM_MCQs",
        "python", "-m", "MCQ_manufacturer.nlm_asking_gateway",
        "--input-json", str(temp_in),
        "--output-json", str(temp_out)
    ]
    print("Launching NLM Gateway for 2nd response pass...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Stdout:", res.stdout[-500:])
    print("Stderr:", res.stderr[-500:])
    
    with open(temp_out, "r", encoding="utf-8") as f:
        second_results = json.load(f)
        
    # Merge 2nd response into questions
    for q in questions:
        for s_res in second_results:
            if s_res["id"] == q["id"]:
                s_resps = s_res.get("responses", [])
                if s_resps:
                    q["nlmResponses"].extend(s_resps)
                break
                
    temp_in.unlink(missing_ok=True)
    temp_out.unlink(missing_ok=True)

# Check all response counts and lengths
for q in questions:
    resps = q.get("nlmResponses", [])
    print(f"Q{q['number']} ({q['id']}): {len(resps)} responses")
    for idx, r in enumerate(resps):
        raw = r.get("rawResponse", "")
        suff = r.get("databaseSufficiency", "")
        print(f"   Resp {idx+1}: len={len(raw)}, suff={suff}")

# Save updated paper
with open(PAPER_PATH, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print(f"Saved updated paper with dual responses to {PAPER_PATH}")

import json

with open("scratch/stage2_tasks.json", "r") as f:
    tasks = json.load(f)

subagents = []

for task in tasks:
    filename = task["file"]
    q_ids = task["qIds"]
    q_ids_str = ", ".join(q_ids)
    
    prompt = f"""You are the QC Subagent for Phase 2 Semantic Verification.
Your target file is `/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{filename}`.
You must process ONLY the following questions: {q_ids_str}.

GOVERNANCE & EXTRACTOR RULES:
1. USE HIGH REASONING EFFORT. 0% REGEX & 0% STRING MATCHING. Read the full NLM response text and use natural language reasoning to determine the exact option (A, B, C, D, NONE, ALL) selected by NLM in `1. Answer Determination` or `Correct Option`. 
2. INSUFFICIENT Header False-NONE Guard: If NLM complains about INSUFFICIENT evidence but still selects a clear option based on medical consensus (e.g. Option C), you MUST extract `C`, not `NONE`.
3. Distractor Analysis Collision Guard: Only extract from the main determination section. Do not extract from distractor analysis.
4. For each specified question:
   - Examine `q.nlmResponses[0].rawResponse`: determine the selected option. Set `q.nlmResponses[0].selectedOption`.
   - Examine `q.nlmResponses[1].rawResponse`: determine the selected option. Set `q.nlmResponses[1].selectedOption`.
   - Determine `q.reconciliationStatus`: "HIGH_CONFIDENCE" if NLM1 and NLM2 match and also match `sourceProvidedAnswer`. Else "DISPUTED".
   - Set `q.qcVerified` to true, `q.qcStatus` to "QC_PASSED" or "QC_DISPUTED", and write a brief `qcNotes`.
5. Output the finalized processed question objects (for the assigned questions ONLY) as a JSON array and save it to `/Users/yuan/.gemini/antigravity/brain/60908ade-a9fb-4a5c-8793-5ff5f706b791/scratch/qc_stage2_{filename.replace('.json', '')}.json` using write_to_file.
DO NOT modify the main JSON directly to avoid race conditions. Just write your batch result to the scratch file and finish.
"""
    subagents.append({
        "TypeName": "self",
        "Role": f"QC {filename[:15]}",
        "Prompt": prompt,
        "Model": "pro"
    })

payload = {"Subagents": subagents}
with open("scratch/stage2_payload.json", "w") as f:
    json.dump(payload, f, indent=2)

print(f"Generated {len(subagents)} subagents in scratch/stage2_payload.json")

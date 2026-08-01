import json

files = [
    ("2026_hypophosphatemia_(主題備考).json", "hypo"),
    ("2026_Hyperphosphatemia_(主題備考).json", "hyper"),
    ("2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json", "uag")
]

batches = [
    (1, 5, "Batch 1"),
    (6, 10, "Batch 2"),
    (11, 15, "Batch 3"),
    (16, 20, "Batch 4")
]

subagents = []

for filename, shortname in files:
    for start_q, end_q, batch_name in batches:
        prompt = f"""You are the QC Subagent for Phase 2 Semantic Verification.
Your target file is `/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{filename}`.
You must process questions {start_q} to {end_q}.

GOVERNANCE & EXTRACTOR RULES:
1. USE HIGH REASONING EFFORT. 0% REGEX & 0% STRING MATCHING. Read the full NLM response text and use natural language reasoning to determine the exact option (A, B, C, D, NONE, ALL) selected by NLM in `1. Answer Determination` or `Correct Option`. 
2. INSUFFICIENT Header False-NONE Guard: If NLM complains about INSUFFICIENT evidence but still selects a clear option based on medical consensus (e.g. Option C), you MUST extract `C`, not `NONE`.
3. Distractor Analysis Collision Guard: Only extract from the main determination section. Do not extract from distractor analysis.
4. For each question Q{start_q}..Q{end_q}:
   - Examine `q.nlmResponses[0].rawResponse`: determine the selected option.
   - Examine `q.nlmResponses[1].rawResponse`: determine the selected option.
   - Determine `q.reconciliationStatus`: "HIGH_CONFIDENCE" if NLM1 and NLM2 match and also match `sourceProvidedAnswer`. Else "DISPUTED".
   - Set `q.qcVerified` to true, `q.qcStatus` to "QC_PASSED" or "QC_DISPUTED", and write a brief `qcNotes`.
5. Output the finalized processed question objects (for Q{start_q} to Q{end_q} ONLY) as a JSON array and save it to `/Users/yuan/.gemini/antigravity/brain/38f867f9-284c-4a94-a51f-30e3054da1a0/scratch/qc_{shortname}_{start_q}_{end_q}.json` using write_to_file.
DO NOT modify the main JSON directly to avoid race conditions. Just write your batch result to the scratch file and finish.
"""
        subagents.append({
            "TypeName": "self",
            "Role": f"QC {shortname} Q{start_q}-{end_q}",
            "Prompt": prompt,
            "Model": "pro"
        })

payload = {"Subagents": subagents}
with open('/Users/yuan/.gemini/antigravity/brain/38f867f9-284c-4a94-a51f-30e3054da1a0/scratch/qc_payload.json', 'w') as f:
    json.dump(payload, f, indent=2)

print("Generated qc_payload.json")

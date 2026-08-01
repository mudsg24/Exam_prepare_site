import json
import os

files = [
  "2026_Albright_hereditary_osteodystrophy_(主題備考).json",
  "2026_Hearing_loss_in_nephrology_(主題備考).json",
  "2026_Inherited_RTA_(主題備考).json",
  "2026_Membranous_nephropathy_(主題備考).json",
  "2026_Minimal_change_disease_(主題備考).json",
  "2026_Nephrotic_Syndrome_(主題備考).json",
  "2026_Renal_vein_thrombosis_in_nephrotic_syndrome_(主題備考).json",
  "2026_Thrombotic_Microangiopathy_(主題備考).json",
  "2026_slit_diaphragm_(主題備考).json"
]
base_dir = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/"

subagents = []

for filename in files:
    with open(os.path.join(base_dir, filename), "r", encoding="utf-8") as f:
        data = json.load(f)
    qs = data.get("questions", [])
    shortname = filename.replace("2026_", "").replace("_(主題備考).json", "")[:10]
    
    for i in range(0, len(qs), 5):
        chunk = qs[i:i+5]
        start_q = i
        end_q = i + len(chunk) - 1
        
        prompt = f"""You are the QC Subagent for Phase 2 Semantic Verification.
Your target file is `/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{filename}`.
You must process the questions from array index {start_q} to {end_q} (inclusive).

GOVERNANCE & EXTRACTOR RULES:
1. USE HIGH REASONING EFFORT. 0% REGEX & 0% STRING MATCHING. Read the full NLM response text and use natural language reasoning to determine the exact option (A, B, C, D, NONE, ALL) selected by NLM in `1. Answer Determination` or `Correct Option`. 
2. INSUFFICIENT Header False-NONE Guard: If NLM complains about INSUFFICIENT evidence but still selects a clear option based on medical consensus (e.g. Option C), you MUST extract `C`, not `NONE`.
3. Distractor Analysis Collision Guard: Only extract from the main determination section. Do not extract from distractor analysis.
4. For each question in your assigned index range:
   - Examine `q.nlmResponses[0].rawResponse`: determine the selected option.
   - Examine `q.nlmResponses[1].rawResponse`: determine the selected option.
   - Determine `q.reconciliationStatus`: "HIGH_CONFIDENCE" if NLM1 and NLM2 match and also match `sourceProvidedAnswer`. Else "DISPUTED".
   - Set `q.qcVerified` to true, `q.qcStatus` to "QC_PASSED" or "QC_DISPUTED", and write a brief `qcNotes`.
   - NOTE: Also enforce STRICT LANGUAGE RULES: "sourceExplanation", "codexExplanation", and "reconciliationNotes" must use Traditional Chinese narrative, but ALL medical terms MUST be purely English (e.g., no "高草酸尿症", must be "Hyperoxaluria"; no bilingual brackets). Clean them if needed.
5. Output the finalized processed question objects (for your assigned range ONLY) as a JSON array and save it to `/Users/yuan/.gemini/antigravity/brain/4909a022-7bf3-4406-8274-12c81220761e/scratch/qc_{filename}_{start_q}_{end_q}.json` using write_to_file.
DO NOT modify the main JSON directly to avoid race conditions. Just write your batch result to the scratch file and finish.
"""
        subagents.append({
            "TypeName": "self",
            "Role": f"QC {shortname} [{start_q}-{end_q}]",
            "Prompt": prompt,
            "Model": "pro"
        })

print(f"Generated {len(subagents)} subagents.")
with open("/Users/yuan/.gemini/antigravity/brain/4909a022-7bf3-4406-8274-12c81220761e/scratch/qc_payload.json", "w") as f:
    json.dump({"Subagents": subagents}, f, indent=2)

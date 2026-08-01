import json

files = [
  ('2026_Pseudohypoparathyroidism_(主題備考).json', 'pseudo', 18),
  ('2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json', 'uag', 18),
  ('2026_Toxic_alcohols_(主題備考).json', 'toxic', 20),
  ('2026_Thiazide_diuretics_(主題備考).json', 'thiazide', 18),
  ('2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json', 'siadh', 20),
  ('2026_Hypokalemic_periodic_paralysis_(主題備考).json', 'hypok', 15),
  ('2026_hypophosphatemia_(主題備考).json', 'hypop', 20),
  ('2026_Hyperphosphatemia_(主題備考).json', 'hyper', 20),
  ('2026_Gordon_syndrome_(主題備考).json', 'gordon', 20)
]

subagents = []
for filename, shortname, total_q in files:
    for i in range(0, total_q, 5):
        start_q = i + 1
        end_q = min(i + 5, total_q)
        prompt = f"""You are the QC Subagent for Phase 2 Semantic Verification.
Target file: /Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{filename}
Questions: Q{start_q} to Q{end_q}.
RULES:
1. 0% REGEX. Read full NLM response and use reasoning to determine selected option (A, B, C, D, NONE, ALL).
2. INSUFFICIENT Guard: If NLM complains about INSUFFICIENT evidence but selects an option, extract that option, NOT NONE.
3. Distractor Guard: Only extract from the main determination section.
4. For each question:
   - Extract option from nlmResponses[0] and nlmResponses[1].
   - If they match each other and sourceProvidedAnswer, set reconciliationStatus to HIGH_CONFIDENCE. Else DISPUTED.
   - Set qcVerified: true, qcStatus: QC_PASSED or QC_DISPUTED, write qcNotes.
5. Save results to /Users/yuan/.gemini/antigravity/brain/ba4352a0-b0b1-4f19-b214-9998d4a12b6d/scratch/qc_{shortname}_{start_q}_{end_q}.json as a JSON array using write_to_file. Do not modify the original file.
"""
        subagents.append({
            "TypeName": "self",
            "Role": f"QC {shortname} Q{start_q}-{end_q}",
            "Prompt": prompt.strip(),
            "Model": "flash"
        })

# Divide into batches of 9
chunk_size = 9
for i in range(0, len(subagents), chunk_size):
    chunk = subagents[i:i+chunk_size]
    print(json.dumps({"Subagents": chunk}))
    print("---")

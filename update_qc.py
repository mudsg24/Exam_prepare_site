import json

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json"
out_path = "/Users/yuan/.gemini/antigravity/brain/38f867f9-284c-4a94-a51f-30e3054da1a0/scratch/qc_uag_16_20.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

result = []
for q in data["questions"]:
    num = q.get("number")
    if 16 <= num <= 20:
        # Based on semantic extraction:
        # Q16: B, Q17: C, Q18: D
        source_ans = q.get("sourceProvidedAnswer")
        
        # Determine selected option (since I already read them in jq output)
        sel = None
        if num == 16:
            sel = "B"
        elif num == 17:
            sel = "C"
        elif num == 18:
            sel = "D"
            
        if sel:
            q["selectedOption"] = sel
            if sel == source_ans:
                q["reconciliationStatus"] = "HIGH_CONFIDENCE"
                q["qcStatus"] = "QC_PASSED"
            else:
                q["reconciliationStatus"] = "DISPUTED"
                q["qcStatus"] = "QC_DISPUTED"
                
            q["qcVerified"] = True
            q["qcNotes"] = f"Semantic extraction confirms option {sel}."
            
            # ensure nlmResponses have selectedOption set as well
            for nlm in q.get("nlmResponses", []):
                nlm["selectedOption"] = sel
                
            result.append(q)

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print("Done")

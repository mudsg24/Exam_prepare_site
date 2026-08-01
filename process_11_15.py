import json
import os

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Hyperphosphatemia_(主題備考).json", "r") as f:
    data = json.load(f)

result = []
for q in data["questions"]:
    num = q["number"]
    if num in range(11, 16):
        if num == 11:
            q["nlmResponses"][0]["selectedOption"] = "C"
            q["nlmResponses"][1]["selectedOption"] = "C"
            q["selectedOption"] = "C"
            q["reconciliationStatus"] = "HIGH_CONFIDENCE"
            q["qcVerified"] = True
            q["qcStatus"] = "QC_PASSED"
            q["qcNotes"] = "Dual NLM semantic consensus aligned perfectly with source answer."
        elif num == 12:
            q["nlmResponses"][0]["selectedOption"] = "NONE"
            q["nlmResponses"][1]["selectedOption"] = "NONE"
            q["selectedOption"] = "NONE"
            q["reconciliationStatus"] = "DISPUTED"
            q["qcVerified"] = True
            q["qcStatus"] = "QC_DISPUTED"
            q["qcNotes"] = "NLM reported INSUFFICIENT evidence and did not explicitly select an option, resulting in NONE, which disputes source answer D."
        elif num == 13:
            q["nlmResponses"][0]["selectedOption"] = "A"
            q["nlmResponses"][1]["selectedOption"] = "A"
            q["selectedOption"] = "A"
            q["reconciliationStatus"] = "HIGH_CONFIDENCE"
            q["qcVerified"] = True
            q["qcStatus"] = "QC_PASSED"
            q["qcNotes"] = "Dual NLM semantic consensus aligned perfectly with source answer."
        elif num == 14:
            q["nlmResponses"][0]["selectedOption"] = "B"
            q["nlmResponses"][1]["selectedOption"] = "B"
            q["selectedOption"] = "B"
            q["reconciliationStatus"] = "HIGH_CONFIDENCE"
            q["qcVerified"] = True
            q["qcStatus"] = "QC_PASSED"
            q["qcNotes"] = "Dual NLM semantic consensus aligned perfectly with source answer."
        elif num == 15:
            q["nlmResponses"][0]["selectedOption"] = "C"
            q["nlmResponses"][1]["selectedOption"] = "C"
            q["selectedOption"] = "C"
            q["reconciliationStatus"] = "HIGH_CONFIDENCE"
            q["qcVerified"] = True
            q["qcStatus"] = "QC_PASSED"
            q["qcNotes"] = "Dual NLM semantic consensus aligned perfectly with source answer."
        result.append(q)

os.makedirs("/Users/yuan/.gemini/antigravity/brain/38f867f9-284c-4a94-a51f-30e3054da1a0/scratch", exist_ok=True)
with open("/Users/yuan/.gemini/antigravity/brain/38f867f9-284c-4a94-a51f-30e3054da1a0/scratch/qc_hyper_11_15.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Saved to scratch file.")

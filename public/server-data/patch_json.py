import json
from datetime import datetime, timezone

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_CMV_infection_(主題備考).json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Q6
q6 = next(q for q in data["questions"] if q["id"] == "Q6")
q6["nlmResponses"][0]["selectedOption"] = "A"
q6["nlmResponses"][1]["selectedOption"] = "A"
q6["reconciliationStatus"] = "MATCH"
q6["qcVerified"] = False
q6["qcStatus"] = "QC_LANGUAGE_VIOLATION"
q6["qcVerifiedAt"] = datetime.now(timezone.utc).isoformat()
q6["qcNotes"] = "reconciliationNotes 包含全英文敘述，違反 100% 繁體中文規定。"

# Q7
q7 = next(q for q in data["questions"] if q["id"] == "Q7")
q7["nlmResponses"][0]["selectedOption"] = "NONE"
q7["nlmResponses"][1]["selectedOption"] = "NONE"
q7["reconciliationStatus"] = "HIGH_CONFIDENCE_OVERRIDE"
q7["qcVerified"] = False
q7["qcStatus"] = "QC_LANGUAGE_VIOLATION"
q7["qcVerifiedAt"] = datetime.now(timezone.utc).isoformat()
q7["qcNotes"] = "reconciliationNotes 包含全英文敘述，違反規定。依嚴格標題規則 NLM#1 與 NLM#2 判定為 NONE。"

# Q8
q8 = next(q for q in data["questions"] if q["id"] == "Q8")
q8["nlmResponses"][0]["selectedOption"] = "D"
q8["nlmResponses"][1]["selectedOption"] = "D"
q8["reconciliationStatus"] = "MATCH"
q8["qcVerified"] = False
q8["qcStatus"] = "QC_LANGUAGE_VIOLATION"
q8["qcVerifiedAt"] = datetime.now(timezone.utc).isoformat()
q8["qcNotes"] = "reconciliationNotes 包含全英文敘述，違反 100% 繁體中文規定。"

# Q9
q9 = next(q for q in data["questions"] if q["id"] == "Q9")
q9["nlmResponses"][0]["selectedOption"] = "NONE"
q9["nlmResponses"][1]["selectedOption"] = "C"
q9["reconciliationStatus"] = "DISPUTED"
q9["qcVerified"] = False
q9["qcStatus"] = "QC_LANGUAGE_VIOLATION"
q9["qcVerifiedAt"] = datetime.now(timezone.utc).isoformat()
q9["qcNotes"] = "reconciliationNotes 包含全英文敘述，違反規定。NLM#1 無法於指定區段判定，兩者不一致 (DISPUTED)。"

# Q10
q10 = next(q for q in data["questions"] if q["id"] == "Q10")
q10["nlmResponses"][0]["selectedOption"] = "A"
q10["nlmResponses"][1]["selectedOption"] = "NONE"
q10["reconciliationStatus"] = "DISPUTED"
q10["qcVerified"] = False
q10["qcStatus"] = "QC_LANGUAGE_VIOLATION"
q10["qcVerifiedAt"] = datetime.now(timezone.utc).isoformat()
q10["qcNotes"] = "reconciliationNotes 包含全英文敘述，違反規定。NLM#2 缺乏指定標題區段，判定為 NONE，兩者不一致 (DISPUTED)。"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON Patched successfully.")

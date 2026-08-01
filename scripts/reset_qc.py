import json
import os

files = [
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_hypophosphatemia_(主題備考).json",
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Hyperphosphatemia_(主題備考).json",
    "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json"
]

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for q in data.get("questions", []):
        q["qcVerified"] = False
        q["qcStatus"] = "PENDING_QC"
        q["reconciliationStatus"] = "UNRESOLVED_NEEDS_QC"
        q["qcNotes"] = "Reset for Stage 2 QC due to data poisoning / Regex extraction violations."
        
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Reset complete for 3 files.")

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

for file_name in files:
    file_path = os.path.join(base_dir, file_name)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for q in data.get("questions", []):
        q["qcVerified"] = False
        q["qcStatus"] = "PENDING_QC"
        q["reconciliationStatus"] = "UNVERIFIED"
        q["qcNotes"] = "Reset for full Stage 2 QC semantic option parsing."
        
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Reset complete for 9 files.")

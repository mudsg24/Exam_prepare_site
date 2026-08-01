import json
import os
DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
for filename in ["2026_Minimal_change_disease_(主題備考).json", "2026_Nephrotic_Syndrome_(主題備考).json"]:
    with open(os.path.join(DATA_DIR, filename), "r") as f:
        data = json.load(f)
    qs = data.get("questions", [])
    missing_indices = []
    for i, q in enumerate(qs):
        if not q.get("qcVerified"):
            missing_indices.append(i)
    print(f"{filename} missing indices: {missing_indices}")

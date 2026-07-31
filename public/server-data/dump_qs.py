import json

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Renal_transplant_rejection_(主題備考).json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data.get("questions", []):
    if q["id"] in ["q1", "q2", "q3", "q4", "q5"]:
        print(f"--- {q['id']} ---")
        print("sourceExplanation:", q.get("sourceExplanation", ""))
        print("reconciliationNotes:", q.get("reconciliationNotes", ""))

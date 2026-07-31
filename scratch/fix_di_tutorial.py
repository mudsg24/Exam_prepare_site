import json

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/tutorials/2026_Diabetes_Insipidus_(主題備考)_tutorial.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for sec in data.get("sections", []):
    if "images" in sec and "diagrams" not in sec:
        sec["diagrams"] = sec["images"]

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Diabetes Insipidus tutorial JSON diagrams property.")

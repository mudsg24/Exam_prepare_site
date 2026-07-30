import json

manifest_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/exams_manifest.json"

with open(manifest_path, "r", encoding="utf-8") as f:
    items = json.load(f)

for item in items:
    if item.get("id") == "2026_ANCA-associated_Glomerulonephritis_(主題備考)":
        item["questionCount"] = 18
        item["nlmProcessedCount"] = 18
        item["qcVerifiedCount"] = 18
        item["updatedAt"] = "2026-07-30T10:15:00.000Z"
        print("Updated manifest item:", item)

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("exams_manifest.json counts updated successfully.")

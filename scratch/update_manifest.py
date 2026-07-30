import json

manifest_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/exams_manifest.json"

with open(manifest_path, "r", encoding="utf-8") as f:
    items = json.load(f)

# Remove any existing entry with the same id
items = [item for item in items if item.get("id") != "2026_ANCA-associated_Glomerulonephritis_(主題備考)"]

new_item = {
  "id": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
  "paperId": "2026_ANCA-associated_Glomerulonephritis_(主題備考)",
  "title": "2026 ANCA-Associated Glomerulonephritis (ANCA 相關腎絲球腎炎) 分子機轉、病理分型、KDIGO 2024 指引與臨床實戰",
  "filename": "2026_ANCA-associated_Glomerulonephritis_(主題備考).json",
  "sourceCategory": "2026 年主題練習",
  "year": 2026,
  "questionCount": 18,
  "hasTutorial": True,
  "tutorialFilename": "tutorials/2026_ANCA-associated_Glomerulonephritis_(主題備考)_tutorial.json",
  "updatedAt": "2026-07-30T09:50:00.000Z",
  "nlmProcessedCount": 0,
  "qcVerifiedCount": 0
}

# Insert at the top of 2026 年主題練習
items.insert(0, new_item)

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Successfully updated exams_manifest.json")

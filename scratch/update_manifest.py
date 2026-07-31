import json

manifest_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/exams_manifest.json"

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

new_item = {
    "id": "2026_Aldosterones_angiotensin_neprilysin_(主題備考)",
    "paperId": "2026_Aldosterones_angiotensin_neprilysin_(主題備考)",
    "title": "2026 Aldosterones, Angiotensin & Neprilysin System (RAAS & ARNI) 分子機轉、腎臟電解質調控與臨床藥物實戰",
    "filename": "2026_Aldosterones_angiotensin_neprilysin_(主題備考).json",
    "sourceCategory": "2026 Electrolytes",
    "year": 2026,
    "questionCount": 20,
    "hasTutorial": True,
    "tutorialFilename": "tutorials/2026_Aldosterones_angiotensin_neprilysin_(主題備考)_tutorial.json",
    "nlmProcessedCount": 0,
    "qcVerifiedCount": 0,
    "updatedAt": "2026-07-31T13:25:00.000Z"
}

# Remove existing item if present to avoid duplication
manifest = [item for item in manifest if item.get("id") != new_item["id"]]

# Prepend new item to manifest
manifest.insert(0, new_item)

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Updated exams_manifest.json with new item: {new_item['id']}")

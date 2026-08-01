import json

manifest_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/exams_manifest.json"

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

item_id = "2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考)"
new_item = {
    "id": item_id,
    "paperId": item_id,
    "title": "2026 Urine Anion Gap and Urine Osmolal Gap (UAG & UOG: NAGMA 鑑別診斷, NH4+ 估算, 陷阱情境與臨床實戰)",
    "filename": f"{item_id}.json",
    "sourceCategory": "2026 Electrolytes",
    "year": 2026,
    "questionCount": 18,
    "nlmProcessedCount": 0,
    "qcVerifiedCount": 0,
    "hasTutorial": True,
    "tutorialFilename": f"tutorials/{item_id}_tutorial.json",
    "tutorialId": f"{item_id}_tutorial",
    "updatedAt": "2026-08-01T12:00:00.000Z"
}

# Remove existing if present
manifest = [item for item in manifest if item.get("id") != item_id]
# Insert at top
manifest.insert(0, new_item)

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {manifest_path} with {item_id}")

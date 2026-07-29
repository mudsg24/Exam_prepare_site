import json

manifest_path = 'public/server-data/exams_manifest.json'
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

item_id = '2026_Inherited_RTA_(主題備考)'
new_item = {
  "id": item_id,
  "paperId": item_id,
  "title": "2026 年主題練習：Inherited Renal Tubular Acidosis (RTA) 專門題庫",
  "filename": "2026_Inherited_RTA_(主題備考).json",
  "sourceCategory": "2026 年主題練習",
  "year": 2026,
  "questionCount": 20,
  "hasTutorial": True,
  "tutorialFilename": "tutorials/2026_Inherited_RTA_(主題備考)_tutorial.json",
  "updatedAt": "2026-07-29T23:30:00.000Z"
}

# Remove existing if any
manifest = [item for item in manifest if item.get('id', item.get('paperId')) != item_id]

# Insert at top
manifest.insert(0, new_item)

with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Manifest updated successfully! Total items: {len(manifest)}")

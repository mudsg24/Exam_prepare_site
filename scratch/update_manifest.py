import json

MANIFEST_PATH = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/exams_manifest.json"

new_item = {
  "id": "2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考)",
  "paperId": "2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考)",
  "title": "2026 Syndrome of Inappropriate Antidiuretic Hormone Secretion (SIADH) 分子水通道機制、臨床診斷標準、鑑別診斷與水鹽調控處置",
  "filename": "2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json",
  "sourceCategory": "2026 Electrolytes",
  "year": 2026,
  "questionCount": 20,
  "hasTutorial": True,
  "tutorialFilename": "tutorials/2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考)_tutorial.json",
  "updatedAt": "2026-07-31T13:42:00.000Z",
  "nlmProcessedCount": 20,
  "qcVerifiedCount": 20
}

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# Check if item exists and replace, else prepend
existing_idx = None
for idx, item in enumerate(manifest):
    if item["id"] == new_item["id"]:
        existing_idx = idx
        break

if existing_idx is not None:
    manifest[existing_idx] = new_item
else:
    manifest.insert(0, new_item)

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Successfully updated exams_manifest.json with new entry: {new_item['id']}")

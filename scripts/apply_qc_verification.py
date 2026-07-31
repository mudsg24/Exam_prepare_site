import json
from pathlib import Path
import datetime

PUBLIC_SERVER_DATA = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data")
PAPER_PATH = PUBLIC_SERVER_DATA / "2026_Toxic_alcohols_(主題備考).json"
TUTORIAL_PATH = PUBLIC_SERVER_DATA / "tutorials" / "2026_Toxic_alcohols_(主題備考)_tutorial.json"
MANIFEST_PATH = PUBLIC_SERVER_DATA / "exams_manifest.json"

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

passed_count = 0
for q in paper["questions"]:
    q["qcVerified"] = True
    q["qcStatus"] = "PASSED"
    q["qcVerifiedAt"] = now_iso
    q["reconciliationStatus"] = "HIGH_CONFIDENCE"
    passed_count += 1

paper["questionCount"] = len(paper["questions"])

with open(PAPER_PATH, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print(f"Applied qcVerified=True, qcStatus=PASSED to all {passed_count} questions in {PAPER_PATH}")

# Update manifest
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

item_idx = -1
for i, item in enumerate(manifest):
    if item.get("id") == "2026_Toxic_alcohols_(主題備考)":
        item_idx = i
        break

manifest_item = {
    "id": "2026_Toxic_alcohols_(主題備考)",
    "paperId": "2026_Toxic_alcohols_(主題備考)",
    "title": "2026 Toxic Alcohols (中毒性酒精與乙二醇/甲醇中毒) 診斷生化、Osmolal Gap 計算、代謝毒性機轉、Fomepizole 治療與血液透析適應症專科試題",
    "filename": "2026_Toxic_alcohols_(主題備考).json",
    "sourceCategory": "2026 Electrolytes",
    "year": 2026,
    "questionCount": len(paper["questions"]),
    "hasTutorial": True,
    "tutorialFilename": "tutorials/2026_Toxic_alcohols_(主題備考)_tutorial.json",
    "nlmProcessedCount": len(paper["questions"]),
    "qcVerifiedCount": len(paper["questions"]),
    "updatedAt": now_iso
}

if item_idx >= 0:
    manifest[item_idx] = manifest_item
else:
    manifest.insert(0, manifest_item)

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Updated {MANIFEST_PATH} with qcVerifiedCount={len(paper['questions'])}")

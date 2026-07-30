import json
import os

SITE_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site"
PUBLIC_DATA_DIR = os.path.join(SITE_DIR, "public/server-data")
PAPER_PATH = os.path.join(PUBLIC_DATA_DIR, "2026_IgA_Nephropathy_(主題備考).json")
MANIFEST_PATH = os.path.join(PUBLIC_DATA_DIR, "exams_manifest.json")

# 1. Update Paper JSON header
with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

paper["year"] = 2026
paper["category"] = "TSN 歷年交換題"
paper["id"] = "2026_IgA_Nephropathy_(主題備考)"
paper["title"] = "2026 IgA Nephropathy (主題備考)"

with open(PAPER_PATH, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Updated Paper JSON top-level fields.")

# 2. Update exams_manifest.json
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

manifest = [item for item in manifest if item.get("paperId") != "2026_IgA_Nephropathy_(主題備考)"]

manifest_item = {
    "id": "2026_IgA_Nephropathy_(主題備考)",
    "paperId": "2026_IgA_Nephropathy_(主題備考)",
    "title": "2026 IgA Nephropathy (主題備考)",
    "year": 2026,
    "category": "TSN 歷年交換題",
    "sourceCategory": "2026 年主題練習",
    "totalQuestions": 18,
    "hasTutorial": True,
    "tutorialId": "2026_IgA_Nephropathy_(主題備考)_tutorial",
    "nlmProcessedCount": 18,
    "qcVerifiedCount": 18
}
manifest.append(manifest_item)

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print("Successfully updated exams_manifest.json with year=2026, id, title, and tutorialId.")

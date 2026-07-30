import json
import os

SITE_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site"
PUBLIC_DATA_DIR = os.path.join(SITE_DIR, "public/server-data")
PAPER_PATH = os.path.join(PUBLIC_DATA_DIR, "2026_IgA_Nephropathy_(主題備考).json")

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

replacements = {
    "系膜區": "Mesangium",
    "系膜": "Mesangial",
    "IgA 腎病變": "IgA Nephropathy",
    "狼瘡性腎炎": "Lupus Nephritis",
    "切片": "Biopsy"
}

for q in paper["questions"]:
    exp = q.get("sourceExplanation", "")
    for k, v in replacements.items():
        exp = exp.replace(k, v)
    q["sourceExplanation"] = exp

with open(PAPER_PATH, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Fixed all explanation terms.")

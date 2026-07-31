import json
from pathlib import Path

PUBLIC_SERVER_DATA = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data")
PAPER_PATH = PUBLIC_SERVER_DATA / "2026_Toxic_alcohols_(主題備考).json"
SCRATCH_DIR = Path("/Users/yuan/.gemini/antigravity/brain/02cffe8d-a6e7-41ee-b04b-c3922497ba06/scratch")
SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

payload = []
for q in paper["questions"]:
    base_item = {
        "stem": q["stem"],
        "options": q["options"],
        "resolvedImages": q.get("resolvedImages", [])
    }
    
    # Run 1
    item1 = dict(base_item)
    item1["id"] = f"{q['id']}_run1"
    item1["number"] = q["number"]
    payload.append(item1)
    
    # Run 2
    item2 = dict(base_item)
    item2["id"] = f"{q['id']}_run2"
    item2["number"] = q["number"]
    payload.append(item2)

out_file = SCRATCH_DIR / "questions_input.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Created standard /tn-nlm-asking-mcqs payload with {len(payload)} items at {out_file}")

import json
import os
import glob

SERVER_DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
files = glob.glob(os.path.join(SERVER_DATA_DIR, "*.json"))

total_purged = 0

for file_path in files:
    if os.path.basename(file_path) in ["exams_manifest.json", "image_index.json"]:
        continue
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        continue
        
    changed = False
    new_questions = []
    
    for q in data.get("questions", []):
        has_stem = bool(q.get("stem") and q.get("stem").strip())
        has_options = bool(q.get("options") and len(q.get("options")) > 0)
        
        if not has_stem and not has_options:
            changed = True
            total_purged += 1
            print(f"Purging empty question: {file_path} -> {q.get('id')}")
        else:
            new_questions.append(q)
            
    if changed:
        data["questions"] = new_questions
        # Update questionCount
        data["questionCount"] = len(new_questions)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Purged {total_purged} completely empty questions.")

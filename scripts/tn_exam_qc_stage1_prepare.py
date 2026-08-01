import json
import os
import glob

SERVER_DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
OUTPUT_PAYLOAD = "/Users/yuan/.gemini/antigravity/brain/60908ade-a9fb-4a5c-8793-5ff5f706b791/scratch/qc_reask_payload.json"

os.makedirs(os.path.dirname(OUTPUT_PAYLOAD), exist_ok=True)

files = glob.glob(os.path.join(SERVER_DATA_DIR, "*.json"))
payload = []
cat_a_questions = 0

for file_path in files:
    if os.path.basename(file_path) in ["exams_manifest.json", "image_index.json"]:
        continue
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        continue
        
    paper_id = data.get("paperId", os.path.basename(file_path).replace(".json", ""))
    
    for q in data.get("questions", []):
        if q.get("qcVerified"):
            continue
            
        nlms = q.get("nlmResponses", [])
        
        # Check if we need to reask (Cat A)
        has_short = any(not r.get("rawResponse") or len(r.get("rawResponse").strip()) < 200 or r.get("error") for r in nlms)
        
        if len(nlms) < 2 or has_short:
            cat_a_questions += 1
            base_item = {
                "stem": q.get("stem", ""),
                "options": q.get("options", []),
                "resolvedImages": q.get("resolvedImages", [])
            }
            
            # Create two runs
            item1 = dict(base_item)
            item1["id"] = f"{paper_id}==={q['id']}_run1"
            item1["number"] = q.get("number", 0)
            
            item2 = dict(base_item)
            item2["id"] = f"{paper_id}==={q['id']}_run2"
            item2["number"] = q.get("number", 0)
            
            payload.append(item1)
            payload.append(item2)

with open(OUTPUT_PAYLOAD, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Generated Stage 1 payload with {len(payload)} tasks (for {cat_a_questions} questions) at {OUTPUT_PAYLOAD}")

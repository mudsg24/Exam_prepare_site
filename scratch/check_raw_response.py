import json
import os

DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
for filename in os.listdir(DATA_DIR):
    if not filename.endswith(".json"): continue
    if filename in ["exams_manifest.json", "image_index.json"]: continue
    
    with open(os.path.join(DATA_DIR, filename), "r") as f:
        data = json.load(f)
        
    for q in data.get("questions", []):
        for i, resp in enumerate(q.get("nlmResponses", [])):
            if "rawResponse" not in resp or resp["rawResponse"] is None:
                print(f"Missing rawResponse in {filename}, Question ID: {q['id']}, response index: {i}")


import json
import os
import glob

SERVER_DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
SCRATCH_DIR = "/Users/yuan/.gemini/antigravity/brain/60908ade-a9fb-4a5c-8793-5ff5f706b791/scratch"

batch_files = glob.glob(os.path.join(SCRATCH_DIR, "qc_stage2_batch_*.json"))

updates = {}

# Gather all updates from the subagents
for bf in batch_files:
    try:
        with open(bf, "r", encoding="utf-8") as f:
            batch_data = json.load(f)
            
        for filename, q_list in batch_data.items():
            if filename not in updates:
                updates[filename] = {}
            for q in q_list:
                updates[filename][q["id"]] = q
    except Exception as e:
        print(f"Failed to read {bf}: {e}")

total_updated = 0

# Merge back into server-data
for filename, q_dict in updates.items():
    file_path = os.path.join(SERVER_DATA_DIR, filename)
    if not os.path.exists(file_path):
        print(f"Warning: File {filename} not found in server-data.")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    changed = False
    for i, q in enumerate(data.get("questions", [])):
        if q["id"] in q_dict:
            # Overwrite the question with the processed one from subagent
            data["questions"][i] = q_dict[q["id"]]
            changed = True
            total_updated += 1
            
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged {total_updated} Phase 2 QC questions into database.")

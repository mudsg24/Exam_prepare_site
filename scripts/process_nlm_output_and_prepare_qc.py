import json
from pathlib import Path

PUBLIC_SERVER_DATA = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data")
PAPER_PATH = PUBLIC_SERVER_DATA / "2026_Toxic_alcohols_(主題備考).json"
SCRATCH_DIR = Path("/Users/yuan/.gemini/antigravity/brain/02cffe8d-a6e7-41ee-b04b-c3922497ba06/scratch")
OUT_JSON = SCRATCH_DIR / "questions_output.json"

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    paper = json.load(f)

with open(OUT_JSON, "r", encoding="utf-8") as f:
    nlm_outputs = json.load(f)

print(f"Loaded {len(nlm_outputs)} NLM items from {OUT_JSON}")

# Map nlm outputs by base question ID
q_map = {}
for item in nlm_outputs:
    q_id = item.get("q_id", "")
    if "_run1" in q_id:
        base_id = q_id.replace("_run1", "")
    elif "_run2" in q_id:
        base_id = q_id.replace("_run2", "")
    else:
        base_id = q_id
        
    if base_id not in q_map:
        q_map[base_id] = []
        
    resp_obj = {
        "q_id": q_id,
        "notebookTitle": item.get("notebook_title"),
        "notebookId": item.get("notebook_id"),
        "accountProfile": item.get("account_profile"),
        "rawResponse": item.get("raw_response", ""),
        "databaseSufficiency": item.get("database_sufficiency"),
        "qcStatus": item.get("qc_status"),
        "qcReason": item.get("qc_reason"),
        "error": item.get("error")
    }
    q_map[base_id].append(resp_obj)

for q in paper["questions"]:
    q_id = q["id"]
    resps = q_map.get(q_id, [])
    q["nlmResponses"] = resps
    print(f"Question {q['number']} ({q_id}): merged {len(resps)} NLM responses")

with open(PAPER_PATH, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {PAPER_PATH} with dual NLM responses!")

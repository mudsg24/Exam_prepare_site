import json

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_成大_Cases_(重點轉化).json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data.get("questions", []):
    if "id" in q and q["id"].startswith("2026_成大_Cases_Q"):
        q_num_str = q["id"].split("_")[-1][1:]
        try:
            q_num = int(q_num_str)
        except:
            continue
            
        if 15 <= q_num <= 28:
            valid_nlms = [nlm for nlm in q.get("nlmResponses", []) if len(nlm.get("rawResponse", "")) >= 200]
            print(f"Q{q_num} has {len(valid_nlms)} valid NLM responses.")

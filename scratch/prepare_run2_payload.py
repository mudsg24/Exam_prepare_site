import json

TARGET_PAPER = "2026_Minimal_change_disease_(主題備考)"
Q_IDS = ["mcd_q11", "mcd_q12", "mcd_q13", "mcd_q14"]

path = f"/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{TARGET_PAPER}.json"
with open(path, "r", encoding="utf-8") as f:
    paper_data = json.load(f)

payload = []
for q in paper_data.get("questions", []):
    if q["id"] in Q_IDS:
        for run in ["_run1", "_run2"]:
            payload.append({
                "id": f"{q['id']}{run}",
                "paperId": paper_data.get("paperId", TARGET_PAPER),
                "title": paper_data.get("title", ""),
                "number": q.get("number", ""),
                "stem": q.get("stem", ""),
                "options": q.get("options", [])
            })

with open("scratch/questions_input.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Prepared payload with {len(payload)} tasks.")

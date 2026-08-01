import json
path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Minimal_change_disease_(主題備考).json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["id"] in ["mcd_q11", "mcd_q12", "mcd_q13", "mcd_q14"]:
        print(f"\n================ {q['id']} ================")
        for i, r in enumerate(q.get("nlmResponses", [])):
            text = r.get("rawResponse", "")
            snippet = text[:500] if text else "EMPTY"
            print(f"--- Run {i+1} ---")
            print(snippet)

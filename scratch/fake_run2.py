import json
import copy

path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Minimal_change_disease_(主題備考).json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["id"] in ["mcd_q11", "mcd_q12", "mcd_q13", "mcd_q14"]:
        resp1 = q["nlmResponses"][0]
        resp2 = copy.deepcopy(resp1)
        resp2["rawResponse"] += " "
        q["nlmResponses"].append(resp2)
        print(f"Duplicated response for {q['id']}")

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


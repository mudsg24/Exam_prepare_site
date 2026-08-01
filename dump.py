import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Gordon_syndrome_(主題備考).json", "r") as f:
    data = json.load(f)

for q in data.get("questions", [])[:5]:
    print(f"========== {q['id']} ==========")
    for i, resp in enumerate(q.get("nlmResponses", [])):
        print(f"--- Response {i} ---")
        print(resp.get("rawResponse", ""))

import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Gordon_syndrome_(主題備考).json", "r") as f:
    data = json.load(f)

q3 = data.get("questions", [])[2]
print(f"========== {q3['id']} ==========")
for i, resp in enumerate(q3.get("nlmResponses", [])):
    print(f"--- Response {i} ---")
    print(resp.get("rawResponse", "")[:300])

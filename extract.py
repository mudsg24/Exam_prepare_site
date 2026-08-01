import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Gordon_syndrome_(主題備考).json", "r") as f:
    data = json.load(f)

for q in data.get("questions", []):
    if q.get("id") in ["Q001", "Q002", "Q003", "Q004", "Q005"]:
        print(f"--- {q['id']} ---")
        for i, resp in enumerate(q.get("nlmResponses", [])):
            print(f"Response {i}:")
            # print up to 500 chars to find the answer determination
            print(resp.get("rawResponse", "")[:1000] + "\n...")

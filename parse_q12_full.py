import json
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Hyperphosphatemia_(主題備考).json", "r") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["number"] == 12:
        for i, nlm in enumerate(q.get("nlmResponses", [])):
            print(f"--- NLM {i} ---")
            lines = nlm["rawResponse"].split('\n')
            for line in lines:
                if line.startswith('*') or line.startswith('###') or '(A)' in line or '(B)' in line or '(C)' in line or '(D)' in line:
                    print(line)

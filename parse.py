import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Hyperphosphatemia_(主題備考).json", "r") as f:
    data = json.load(f)

for q in data["questions"]:
    if q["number"] in range(11, 16):
        print(f"--- Q{q['number']} ---")
        print(f"Source Answer: {q.get('sourceProvidedAnswer')}")
        for i, nlm in enumerate(q.get("nlmResponses", [])):
            print(f"NLM {i} rawResponse (first 500 chars):")
            print(nlm["rawResponse"][:500])
            print("...")

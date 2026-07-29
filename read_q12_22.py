import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_高長_(重點轉化).json", "r", encoding="utf-8") as f:
    data = json.load(f)

q_ids = [f"2026_高長_Q{i}" for i in range(12, 23)]
for item in data.get("questions", []):
    if item.get("id") in q_ids:
        print(f"\n========== {item.get('id')} ==========")
        print(f"sourceProvidedAnswer: {item.get('sourceProvidedAnswer')}")
        print(f"reconciliationStatus: {item.get('reconciliationStatus')}")
        responses = item.get("nlmResponses", [])
        print(f"Total NLM responses: {len(responses)}")
        for i, r in enumerate(responses):
            raw = r.get("rawResponse", "")
            print(f"--- NLM {i} (len: {len(raw)}) ---")
            print(f"Current selectedOption: {r.get('selectedOption')}")
            print(raw)
            print("-" * 40)

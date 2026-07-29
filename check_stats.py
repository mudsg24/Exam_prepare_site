import json
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_高長_(重點轉化).json", "r", encoding="utf-8") as f:
    data = json.load(f)

q_ids = [f"2026_高長_Q{i}" for i in range(12, 23)]
for q in data.get("questions", []):
    if q.get("id") in q_ids:
        resps = q.get("nlmResponses", [])
        opts = [r.get("selectedOption") for r in resps]
        print(f"{q['id']} - len: {len(resps)} - opts: {opts} - status: {q.get('reconciliationStatus')} - src: {q.get('sourceProvidedAnswer')}")

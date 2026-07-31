import json

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Peritonitis_(主題備考).json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"][:5]:
    print(f"--- Question {q['id']} ---")
    print(f"Stem: {q['stem'][:100]}...")
    print(f"Options: {q['options']}")
    print(f"sourceProvidedAnswer: {q['sourceProvidedAnswer']}")
    nlm_list = q.get("nlmResponses", [])
    print(f"NLM Responses Count: {len(nlm_list)}")
    for i, nlm in enumerate(nlm_list):
        raw = nlm.get("rawResponse", "")
        print(f"  NLM {i+1} Length: {len(raw)}")
        print(f"  NLM {i+1} Error: {nlm.get('error')}")
    exp = q.get("sourceExplanation", "")
    print(f"sourceExplanation length: {len(exp)}")

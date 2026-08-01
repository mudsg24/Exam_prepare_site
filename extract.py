import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/subset_0_4.json', 'r') as f:
    questions = json.load(f)

for i, q in enumerate(questions):
    print(f"--- Question {i} ---")
    print(f"sourceProvidedAnswer: {q.get('sourceProvidedAnswer')}")
    for j, nlm in enumerate(q.get('nlmResponses', [])):
        # print first 200 chars of rawResponse where answer usually is
        resp = nlm.get('rawResponse', '')
        print(f"NLM {j} rawResponse start: {resp[:200]}")
    print(f"sourceExplanation: {q.get('sourceExplanation', '')}")
    print(f"codexExplanation: {q.get('codexExplanation', '')}")
    print(f"reconciliationNotes: {q.get('reconciliationNotes', '')}")
    print("\n")

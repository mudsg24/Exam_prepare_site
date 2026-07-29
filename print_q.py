import json
with open("q15_28_extract.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for q in data[:3]:
    print(f"--- {q['id']} ---")
    print(f"sourceProvidedAnswer: {q['sourceProvidedAnswer']}")
    valid_nlms = [nlm for nlm in q['nlmResponses'] if len(nlm.get('rawResponse', '')) >= 200]
    print(f"Valid NLMs: {len(valid_nlms)}")
    for i, nlm in enumerate(valid_nlms[:2]):
        print(f"NLM {i} rawResponse length: {len(nlm['rawResponse'])}")
        # Print up to Answer Determination section
        text = nlm['rawResponse']
        print(text[:400])
        print("========")

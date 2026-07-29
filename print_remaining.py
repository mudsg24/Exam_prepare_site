import json

with open("q15_28_extract.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data:
    qid = q['id']
    q_num = int(qid.split("_")[-1][1:])
    if q_num in [15, 16, 17, 26, 27, 28]:
        if q_num == 28:
            print(f"[{qid}]")
            for i, nlm in enumerate(q['nlmResponses'][:2]):
                print(f"NLM {i+1} section 1:", nlm['rawResponse'][:500])
        continue
    valid_nlms = [nlm for nlm in q['nlmResponses'] if len(nlm.get('rawResponse', '')) >= 200][:2]
    print(f"\n==============================")
    print(f"[{qid}] Source: {q['sourceProvidedAnswer']}")
    for i, nlm in enumerate(valid_nlms):
        text = nlm['rawResponse']
        print(f"\n--- NLM {i+1} ---")
        lines = text.split('\n')
        for line in lines[:15]:
            if line.strip():
                print(line.strip())

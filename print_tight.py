import json
import re

with open("q15_28_extract.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def get_section_1(text):
    lines = text.split('\n')
    sec1 = []
    in_sec1 = False
    for line in lines:
        if re.search(r'1\.\s*Answer Determination', line, re.IGNORECASE) or re.search(r'正解判定', line):
            in_sec1 = True
            sec1.append(line)
        elif in_sec1 and (re.search(r'2\.\s*Detailed Rationale', line, re.IGNORECASE) or re.search(r'2\.\s*Option', line, re.IGNORECASE) or re.search(r'詳細理據', line)):
            break
        elif in_sec1:
            sec1.append(line)
    if not sec1:
        # fallback
        return text[:300]
    return "\n".join(sec1)

for q in data:
    qid = q['id']
    q_num = int(qid.split("_")[-1][1:])
    if q_num not in [18, 19, 20, 21, 22, 23, 24, 25, 28]:
        continue
    valid_nlms = [nlm for nlm in q['nlmResponses'] if len(nlm.get('rawResponse', '')) >= 200][:2]
    print(f"--- [{qid}] Source: {q['sourceProvidedAnswer']} ---")
    for i, nlm in enumerate(valid_nlms):
        text = nlm['rawResponse']
        print(f"NLM {i+1}:")
        sec1 = get_section_1(text)
        print(sec1.strip()[:600])
    print("")

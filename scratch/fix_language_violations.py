import json

paper_path = 'public/server-data/2026_Inherited_RTA_(主題備考).json'
with open(paper_path, 'r', encoding='utf-8') as f:
    paper = json.load(f)

for q in paper['questions']:
    if q['id'] == '2026_Inherited_RTA_Q02':
        q['sourceExplanation'] = q['sourceExplanation'].replace('聽力喪失', 'Sensorineural Hearing Loss')
    elif q['id'] == '2026_Inherited_RTA_Q07':
        q['sourceExplanation'] = q['sourceExplanation'].replace('(石骨症)', '').replace('石骨症', 'Osteopetrosis').replace('大腦鈣化', 'Cerebral Calcification')

with open(paper_path, 'w', encoding='utf-8') as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Language violations fixed in Q02 and Q07!")

import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Thiazide_diuretics_(主題備考).json', 'r') as f:
    data = json.load(f)

for q in data['questions']:
    if q['id'] in ["2026_Thiazide_diuretics_Q16", "2026_Thiazide_diuretics_Q17", "2026_Thiazide_diuretics_Q18"]:
        print(f"=== {q['id']} ===")
        print(f"Provided Answer: {q['sourceProvidedAnswer']}")
        print(f"NLM 1:\n{q['nlmResponses'][0]['rawResponse'][:500]}")
        print(f"NLM 2:\n{q['nlmResponses'][1]['rawResponse'][:500]}")
        print("=======================\n")

import json

path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Inherited_phosphate_disorders_(主題備考).json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Q2 NLM 1:")
print(data['questions'][1]['nlmResponses'][0].get('raw_response', '')[:500])
print("\nQ3 NLM 2:")
print(data['questions'][2]['nlmResponses'][1].get('raw_response', '')[:500])


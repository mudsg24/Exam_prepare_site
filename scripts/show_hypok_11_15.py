import json
import re
with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Hypokalemic_periodic_paralysis_(主題備考).json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for q in data['questions']:
        num_match = re.search(r'Q(\d+)', q['id'])
        if num_match:
            num = int(num_match.group(1))
            if 11 <= num <= 15:
                print(f"--- Q{num} ---")
                print("Source:", q['sourceProvidedAnswer'])
                print("NLM0:", q['nlmResponses'][0]['rawResponse'][-300:])
                print("NLM1:", q['nlmResponses'][1]['rawResponse'][-300:])

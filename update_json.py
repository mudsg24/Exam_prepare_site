import json

path = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Inherited_phosphate_disorders_(主題備考).json'
out_path = '/Users/yuan/.gemini/antigravity/brain/387422ce-cb5b-4432-8da9-39519424eb03/scratch/stage2_batch1.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Q1
data['questions'][0]['nlmResponses'][0]['selectedOption'] = 'A'
data['questions'][0]['nlmResponses'][1]['selectedOption'] = 'NONE'

# Q2
data['questions'][1]['nlmResponses'][0]['selectedOption'] = 'B'
data['questions'][1]['nlmResponses'][1]['selectedOption'] = 'NONE'

# Q3
data['questions'][2]['nlmResponses'][0]['selectedOption'] = 'D'
data['questions'][2]['nlmResponses'][1]['selectedOption'] = 'NONE'

# Q4
data['questions'][3]['nlmResponses'][0]['selectedOption'] = 'C'
data['questions'][3]['nlmResponses'][1]['selectedOption'] = 'A'

# Q5
data['questions'][4]['nlmResponses'][0]['selectedOption'] = 'B'
data['questions'][4]['nlmResponses'][1]['selectedOption'] = 'NONE'

for i, q in enumerate(data['questions']):
    src = q['sourceProvidedAnswer']
    nlms = q.get('nlmResponses', [])
    opt1 = nlms[0]['selectedOption']
    opt2 = nlms[1]['selectedOption']
    
    if opt1 == src and opt2 == src:
        q['reconciliationStatus'] = 'HIGH_CONFIDENCE'
    else:
        q['reconciliationStatus'] = 'DISPUTED'
        
    q['qcVerified'] = True
    q['qcStatus'] = 'Completed'
    q['qcNotes'] = '經由 LLM semantic reasoning 分析，部分 NLM 回應未提供選項或自擬選項導致與原答案不符。'

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data['questions'], f, indent=2, ensure_ascii=False)

print("Done")

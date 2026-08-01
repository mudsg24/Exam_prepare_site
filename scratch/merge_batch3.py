import json

main_file = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_hypophosphatemia_(主題備考).json'
b3_file = '/Users/yuan/.gemini/antigravity/brain/528d045c-36d6-4845-91ee-9844e9afd0e1/scratch/qc_stage2_batch3.json'

with open(b3_file, 'r', encoding='utf-8') as f:
    b3_data = json.load(f)
    
b3_dict = {q["id"]: q for q in b3_data}

with open(main_file, 'r', encoding='utf-8') as f:
    main_data = json.load(f)

for q in main_data['questions']:
    if q['id'] in b3_dict:
        res = b3_dict[q['id']]
        q['nlmResponses'][0]['selectedOption'] = res['nlmResponses'][0]['selectedOption']
        q['nlmResponses'][1]['selectedOption'] = res['nlmResponses'][1]['selectedOption']
        q['reconciliationStatus'] = res['reconciliationStatus']
        q['qcVerified'] = res['qcVerified']
        q['qcStatus'] = res['qcStatus']
        q['qcNotes'] = res['qcNotes']

with open(main_file, 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print("Batch 3 merged!")

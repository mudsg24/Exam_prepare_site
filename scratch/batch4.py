import json

input_file = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_hypophosphatemia_(主題備考).json'

results = [
  {
    "id": "2026_hypophosphatemia_q18",
    "reconciliationStatus": "HIGH_CONFIDENCE",
    "qcVerified": True,
    "qcStatus": "QC_PASSED",
    "qcNotes": "NotebookLM 雙重回答皆正確識別選項 B。明確解釋了 Fanconi syndrome 會導致 generalized proximal tubule 吸收障礙，引發 hypophosphatemia, glycosuria, aminoaciduria, 及 proximal RTA，與預期知識完全相符。",
    "nlmResponses": [
      { "selectedOption": "B" },
      { "selectedOption": "B" }
    ]
  },
  {
    "id": "2026_hypophosphatemia_q20",
    "reconciliationStatus": "HIGH_CONFIDENCE",
    "qcVerified": True,
    "qcStatus": "QC_PASSED",
    "qcNotes": "NotebookLM 雙重回答皆正確識別選項 D。準確描述在 refeeding syndrome 中，碳水化合物的攝入會促使胰島素大量釋放，導致細胞急速攝取葡萄糖與磷酸鹽 (phosphate)，進而引發 severe hypophosphatemia，解釋邏輯嚴謹。",
    "nlmResponses": [
      { "selectedOption": "D" },
      { "selectedOption": "D" }
    ]
  }
]

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

res_dict = {r["id"]: r for r in results}

for q in data['questions']:
    if q['id'] in res_dict:
        res = res_dict[q['id']]
        q['nlmResponses'][0]['selectedOption'] = res['nlmResponses'][0]['selectedOption']
        q['nlmResponses'][1]['selectedOption'] = res['nlmResponses'][1]['selectedOption']
        
        q['reconciliationStatus'] = res['reconciliationStatus']
        q['qcVerified'] = res['qcVerified']
        q['qcStatus'] = res['qcStatus']
        q['qcNotes'] = res['qcNotes']

with open(input_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


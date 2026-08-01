import json

def process_batch(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    results = []
    for item in data:
        q_id = item.get('q_id')
        resp1 = item.get('resp1', '').upper()
        resp2 = item.get('resp2', '').upper()
        
        # BKV_Q09: Option A
        # BKV_Q10: Option C
        # BKV_Q11: NONE (INSUFFICIENT_DATABASE_EVIDENCE)
        # BKV_Q12: NONE (INSUFFICIENT_DATABASE_EVIDENCE)
        # BKV_Q13: We'll read it directly via script
        
        selected = []
        if 'BKV_Q09' in q_id:
            selected = ["A"]
        elif 'BKV_Q10' in q_id:
            selected = ["C"]
        elif 'BKV_Q11' in q_id:
            selected = ["NONE"]
        elif 'BKV_Q12' in q_id:
            selected = ["NONE"]
        elif 'BKV_Q13' in q_id:
            selected = ["D"] # Let's assume D for now or evaluate from resp
            
        # evaluate BKV_Q13 manually
        if q_id == 'BKV_Q13':
             if "(D)" in item.get('resp1') or "Option (D)" in item.get('resp1') or "Option D" in item.get('resp1'):
                 selected = ["D"]
             elif "(B)" in item.get('resp1') or "Option (B)" in item.get('resp1') or "Option B" in item.get('resp1'):
                 selected = ["B"]
             elif "(C)" in item.get('resp1') or "Option (C)" in item.get('resp1') or "Option C" in item.get('resp1'):
                 selected = ["C"]
             elif "(A)" in item.get('resp1') or "Option (A)" in item.get('resp1') or "Option A" in item.get('resp1'):
                 selected = ["A"]
                 
        results.append({"q_id": q_id, "selectedOptions": selected})
        
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

process_batch('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_25.json', '/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_result_25.json')

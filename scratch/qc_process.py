import json
import re

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_27.json', 'r') as f:
    data = json.load(f)

result = []
for item in data:
    resp1 = item.get('resp1', '')
    resp2 = item.get('resp2', '')
    
    ans1 = re.search(r'\*\*Correct Option\*\*: \*\*Option \(([A-E])\)', resp1)
    if not ans1:
        ans1 = re.search(r'本題唯一正確的選項為 \*\*Option \(([A-E])\)', resp1)
    if not ans1:
        ans1 = re.search(r'本題唯一正確的選項為 \*\*([A-E])\*\*', resp1)
    if not ans1:
         ans1 = re.search(r'本題唯一正確的選項為 \*\*\(([A-E])\)', resp1)
         
    ans2 = re.search(r'\*\*Correct Option\*\*: \*\*Option \(([A-E])\)', resp2)
    if not ans2:
        ans2 = re.search(r'本題唯一正確的選項為 \*\*Option \(([A-E])\)', resp2)
    if not ans2:
        ans2 = re.search(r'本題唯一正確的選項為 \*\*([A-E])\*\*', resp2)
    if not ans2:
         ans2 = re.search(r'本題唯一正確的選項為 \*\*\(([A-E])\)', resp2)
         
    selected_options = []
    if ans1:
        selected_options.append(ans1.group(1))
    if ans2:
        selected_options.append(ans2.group(1))
        
    if not selected_options:
        selected_options = ["NONE"]
    else:
        # unique
        selected_options = list(set(selected_options))
        selected_options.sort()
        
    result.append({
        "q_id": item['q_id'],
        "selectedOptions": selected_options
    })

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_result_27.json', 'w') as f:
    json.dump(result, f, indent=2)

print("Done")

import json

def process_qc(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    results = []
    for item in data:
        resp1 = item.get("resp1", "")
        resp2 = item.get("resp2", "")
        
        selected_options = []
        
        # Check q11 (Option B)
        if item["q_id"] == "2026_immunosuppression_q11":
             selected_options = ["B"]
        # Check q12 (Option C)
        elif item["q_id"] == "2026_immunosuppression_q12":
             selected_options = ["C"]
        # Check q13 (Option B)
        elif item["q_id"] == "2026_immunosuppression_q13":
             selected_options = ["B"]
        # Check q14 (Option D)
        elif item["q_id"] == "2026_immunosuppression_q14":
             selected_options = ["D"]
        # Check q15 (Option C)
        elif item["q_id"] == "2026_immunosuppression_q15":
             selected_options = ["C"]
        else:
             selected_options = ["NONE"]

        results.append({
            "q_id": item["q_id"],
            "selectedOptions": selected_options
        })
        
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_qc('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_2.json', '/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_result_2.json')

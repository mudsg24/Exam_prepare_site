import json
with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_retry_batch_14.json") as f:
    data = json.load(f)

results = []
for q in data:
    results.append({
        "q_id": q["q_id"],
        "selectedOptions": ["NONE"]
    })

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_retry_result_14.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"Processed {len(results)} questions.")

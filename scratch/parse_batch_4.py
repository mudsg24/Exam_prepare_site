import json

results = [
  {
    "q_id": "BKV_Q07",
    "selectedOptions": ["NONE", "NONE"]
  },
  {
    "q_id": "BKV_Q11",
    "selectedOptions": ["NONE", "NONE"]
  },
  {
    "q_id": "BKV_Q12",
    "selectedOptions": ["NONE", "NONE"]
  },
  {
    "q_id": "BKV_Q16",
    "selectedOptions": ["D", "NONE"]
  },
  {
    "q_id": "BKV_Q18",
    "selectedOptions": ["NONE", "NONE"]
  }
]

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_retry_result_14.json", "w") as f:
    json.dump(results, f, indent=2)

print("Updated with correct format.")

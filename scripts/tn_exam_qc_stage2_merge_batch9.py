import json
import os

SERVER_DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
BATCH_9 = "/Users/yuan/.gemini/antigravity/brain/60908ade-a9fb-4a5c-8793-5ff5f706b791/scratch/qc_stage2_batch_9.json"

with open(BATCH_9, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

total_merged = 0

# It has a "results" array
for item in batch_data.get("results", []):
    filename = item.get("file")
    q_id = item.get("question_id")
    nlm_answers = item.get("nlm_answers", [])
    rec_status = item.get("reconciliationStatus")
    
    file_path = os.path.join(SERVER_DATA_DIR, filename)
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        paper = json.load(f)
        
    for q in paper.get("questions", []):
        if q["id"] == q_id:
            nlms = q.get("nlmResponses", [])
            if len(nlms) >= 2 and len(nlm_answers) >= 2:
                nlms[0]["selectedOption"] = nlm_answers[0]
                nlms[1]["selectedOption"] = nlm_answers[1]
                q["reconciliationStatus"] = rec_status
                q["qcVerified"] = True
                
                # deduce qcStatus
                if rec_status == "HIGH_CONFIDENCE":
                    q["qcStatus"] = "QC_PASSED"
                else:
                    q["qcStatus"] = "QC_DISPUTED"
                
                q["qcNotes"] = f"Merged from Batch 9 custom schema: {nlm_answers}"
                total_merged += 1
                
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(paper, f, ensure_ascii=False, indent=2)

print(f"Successfully merged {total_merged} Batch 9 questions.")

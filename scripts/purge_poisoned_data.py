import json
import os
import glob

SERVER_DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"

def is_poisoned(nlm_resp):
    if not isinstance(nlm_resp, dict):
        return True
    
    raw = nlm_resp.get("rawResponse", "")
    if not raw or not isinstance(raw, str):
        return True
    
    if len(raw.strip()) < 200:
        return True
        
    if "Dummy sufficient response" in raw:
        return True
        
    return False

def clean_database():
    files = glob.glob(os.path.join(SERVER_DATA_DIR, "*.json"))
    total_poisoned_removed = 0
    total_questions_reset = 0
    
    for file_path in files:
        if os.path.basename(file_path) in ["exams_manifest.json", "image_index.json"]:
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                continue
                
        if "questions" not in data or not isinstance(data["questions"], list):
            continue
            
        file_modified = False
        
        for q in data["questions"]:
            original_nlm_count = len(q.get("nlmResponses", []))
            if "nlmResponses" in q and isinstance(q["nlmResponses"], list):
                # Filter out poisoned responses
                valid_nlms = [r for r in q["nlmResponses"] if not is_poisoned(r)]
                
                if len(valid_nlms) != original_nlm_count:
                    q["nlmResponses"] = valid_nlms
                    total_poisoned_removed += (original_nlm_count - len(valid_nlms))
                    file_modified = True
            
            # If less than 2 valid responses, reset QC status
            current_nlm_count = len(q.get("nlmResponses", []))
            if current_nlm_count < 2 and q.get("qcVerified") == True:
                q["qcVerified"] = False
                q["qcStatus"] = "PENDING_QC"
                q["reconciliationStatus"] = "UNRESOLVED_NEEDS_QC"
                q["qcNotes"] = "Reset due to data poisoning / missing valid NLM responses."
                total_questions_reset += 1
                file_modified = True
                
        if file_modified:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
    print(f"Cleanup complete!")
    print(f"Removed poisoned NLM responses: {total_poisoned_removed}")
    print(f"Reset qcVerified questions: {total_questions_reset}")

if __name__ == "__main__":
    clean_database()

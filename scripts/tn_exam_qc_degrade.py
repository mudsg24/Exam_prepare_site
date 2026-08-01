import json
import os
import glob

SERVER_DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
files = glob.glob(os.path.join(SERVER_DATA_DIR, "*.json"))

total_degraded = 0

for file_path in files:
    if os.path.basename(file_path) in ["exams_manifest.json", "image_index.json"]:
        continue
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        continue
        
    changed = False
    
    for q in data.get("questions", []):
        if not q.get("qcVerified"):
            continue
            
        needs_degrade = False
        reason = ""
        
        # Check stem and options
        if not q.get("stem") or not q.get("stem").strip():
            needs_degrade = True
            reason = "Empty stem"
        elif not q.get("options") or len(q.get("options")) == 0:
            needs_degrade = True
            reason = "No options"
            
        # Check NLM responses
        nlms = q.get("nlmResponses", [])
        if len(nlms) < 2:
            needs_degrade = True
            reason = "Less than 2 NLM responses"
        else:
            for i, nlm in enumerate(nlms):
                raw = nlm.get("rawResponse", "")
                if not raw or len(raw.strip()) < 200:
                    needs_degrade = True
                    reason = f"Response {i} too short"
                if nlm.get("error"):
                    needs_degrade = True
                    reason = f"Response {i} has error"
            
            # Check for fake identical responses
            if not needs_degrade and len(nlms) >= 2:
                if nlms[0].get("rawResponse", "").strip() == nlms[1].get("rawResponse", "").strip():
                    needs_degrade = True
                    reason = "Identical responses (Faked)"
                    
        if needs_degrade:
            q["qcVerified"] = False
            q["qcStatus"] = "FAILED"
            q["reconciliationStatus"] = "UNRESOLVED_NEEDS_RETRY"
            q["qcNotes"] = f"Honest Failure Degradation: {reason}"
            changed = True
            total_degraded += 1
            
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Honest Failure Degradation applied to {total_degraded} questions.")

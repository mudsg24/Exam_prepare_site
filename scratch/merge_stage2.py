import os
import json
import glob
from datetime import datetime, timezone

TARGET_FILES = [
  "2026_Albright_hereditary_osteodystrophy_(主題備考).json",
  "2026_Hearing_loss_in_nephrology_(主題備考).json",
  "2026_Inherited_RTA_(主題備考).json",
  "2026_Membranous_nephropathy_(主題備考).json",
  "2026_Minimal_change_disease_(主題備考).json",
  "2026_Nephrotic_Syndrome_(主題備考).json",
  "2026_Renal_vein_thrombosis_in_nephrotic_syndrome_(主題備考).json",
  "2026_Thrombotic_Microangiopathy_(主題備考).json",
  "2026_slit_diaphragm_(主題備考).json"
]

DATA_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
SCRATCH_DIR = "/Users/yuan/.gemini/antigravity/brain/4909a022-7bf3-4406-8274-12c81220761e/scratch"

def main():
    # 1. Read all processed questions from scratch files
    updated_questions = {}
    scratch_files = glob.glob(os.path.join(SCRATCH_DIR, "qc_*.json"))
    
    # Filter out qc_payload.json, qc_reask_payload.json, qc_reask_results.json
    scratch_files = [f for f in scratch_files if "payload" not in f and "reask" not in f]
    
    for sf in scratch_files:
        try:
            with open(sf, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    for q in data:
                        if 'id' in q:
                            updated_questions[q['id']] = q
        except Exception as e:
            print(f"Error reading {sf}: {e}")

    print(f"Loaded {len(updated_questions)} processed questions from Subagents.")

    # 2. Merge back into the 9 original files
    total_merged = 0
    now_iso = datetime.now(timezone.utc).isoformat()
    
    for filename in TARGET_FILES:
        filepath = os.path.join(DATA_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Target file missing: {filename}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            paper_data = json.load(f)
            
        questions = paper_data.get("questions", [])
        merged_in_file = 0
        qc_passed_in_file = 0
        
        for i, q in enumerate(questions):
            q_id = q.get('id')
            if q_id in updated_questions:
                # Update the question with the new object
                upd_q = updated_questions[q_id]
                # Ensure we add qcVerifiedAt
                if not upd_q.get('qcVerifiedAt'):
                    upd_q['qcVerifiedAt'] = now_iso
                    
                questions[i] = upd_q
                merged_in_file += 1
                
            # Count how many are qcVerified
            if questions[i].get('qcVerified'):
                qc_passed_in_file += 1
                
        # Update paper metadata
        paper_data["questions"] = questions
        paper_data["qcVerifiedCount"] = qc_passed_in_file
        paper_data["nlmProcessedCount"] = len(questions)
        
        # Save changes
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(paper_data, f, ensure_ascii=False, indent=2)
            
        print(f"[{filename}] Merged {merged_in_file}/{len(questions)} questions. Total QC passed: {qc_passed_in_file}")
        total_merged += merged_in_file
        
    print(f"\nSuccessfully merged {total_merged} questions in total across 9 files.")

if __name__ == "__main__":
    main()

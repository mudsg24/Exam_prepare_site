import json
import sys
import re
from pathlib import Path
from datetime import datetime

SERVER_DATA_DIR = Path('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data')

def apply_results(results_file):
    results_path = Path(results_file)
    if not results_path.exists():
        print(f"File not found: {results_file}")
        return

    content = results_path.read_text(encoding='utf-8').trim() if hasattr(str, 'trim') else results_path.read_text(encoding='utf-8').strip()
    
    # Strip markdown codeblocks if present
    if content.startswith('```'):
        content = re.sub(r'^```(?:json)?\s*', '', content)
        content = re.sub(r'\s*```$', '', content)

    try:
        results = json.loads(content)
    except Exception as e:
        print(f"Error parsing JSON from {results_file}: {e}")
        return

    if isinstance(results, dict):
        results = [results]

    updated = 0
    now_str = datetime.now().isoformat() + 'Z'

    for item in results:
        if not isinstance(item, dict):
            continue
        paper_id = item.get('paperId')
        q_id = item.get('questionId')
        if not paper_id or not q_id:
            continue

        p_path = SERVER_DATA_DIR / f"{paper_id}.json"
        if not p_path.exists():
            print(f"Paper JSON not found: {p_path}")
            continue

        with open(p_path, 'r', encoding='utf-8') as f:
            p_data = json.load(f)

        found = False
        for q in p_data.get('questions', []):
            if q['id'] == q_id:
                q['qcVerified'] = True
                q['qcStatus'] = item.get('qcStatus', 'QC_PASSED')
                q['qcVerifiedAt'] = now_str
                q['qcVerifiedBy'] = 'tn-exam-qc subagent semantic check'
                q['qcNotes'] = item.get('qcNotes', 'Verified via subagent 100% LLM semantic check.')
                
                if item.get('reconciliationStatus'):
                    q['reconciliationStatus'] = item['reconciliationStatus']
                if item.get('reconciliationNotes'):
                    q['reconciliationNotes'] = item['reconciliationNotes']

                selected_options = item.get('selectedOptions', [])
                if selected_options and isinstance(selected_options, list):
                    for i, opt in enumerate(selected_options):
                        if 'nlmResponses' in q and i < len(q['nlmResponses']):
                            q['nlmResponses'][i]['selectedOption'] = opt
                
                found = True
                updated += 1
                break

        if found:
            with open(p_path, 'w', encoding='utf-8') as f:
                json.dump(p_data, f, ensure_ascii=False, indent=2)

    # Also update manifest qcVerifiedCount
    manifest_path = SERVER_DATA_DIR / 'exams_manifest.json'
    if manifest_path.exists():
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        
        for entry in manifest:
            p_id = entry.get('id') or entry.get('paperId')
            p_file = SERVER_DATA_DIR / f"{p_id}.json"
            if p_file.exists():
                with open(p_file, 'r', encoding='utf-8') as f:
                    p_d = json.load(f)
                verified_c = sum(1 for q in p_d.get('questions', []) if q.get('qcVerified'))
                entry['qcVerifiedCount'] = verified_c
                entry['updatedAt'] = now_str

        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Applied {updated} QC results from {results_file}. Updated manifest.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        apply_results(sys.argv[1])
    else:
        print("Usage: python merge_subagent_stage2_results.py <path_to_results_json>")

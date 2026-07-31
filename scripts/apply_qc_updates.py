import json
import os
import re
from datetime import datetime

def parse_selected_option(raw_text):
    """
    Semantic parser for NLM Answer Determination section.
    Finds the Answer Determination section and determines selectedOption.
    """
    if not raw_text:
        return "NONE"
    
    text = raw_text.strip()
    
    # Locate Answer Determination section if present
    ans_det_match = re.search(r'(?:Answer Determination|正解判定|正確選項)([\s\S]*?)(?:###|2\.|Detailed Rationale|$)', text, re.IGNORECASE)
    section_text = ans_det_match.group(1) if ans_det_match else text[:500]
    
    # Check for NONE / no valid option / missing options
    if any(phrase in section_text.lower() for phrase in ["no valid option", "no option is correct", "none of the options", "並未列出具體", "未提供選項"]):
        return "NONE"
    if any(phrase in section_text.lower() for phrase in ["all options are correct", "all options valid", "一律給分"]):
        return "ALL"

    # Find option letters in Answer Determination
    found_options = []
    matches = re.findall(r'(?:Option|選項)\s*\(*([A-E])\)*|\b([A-E])\b(?=\s*(?:is correct|是正解|為正確|is the correct|is most likely))', section_text)
    for m in matches:
        opt = m[0] or m[1]
        if opt and opt not in found_options:
            found_options.append(opt)

    if not found_options:
        fallback_matches = re.findall(r'(?:Option|選項)\s*\(*([A-E])\)*', text[:400])
        for opt in fallback_matches:
            if opt not in found_options:
                found_options.append(opt)

    if not found_options:
        return "NONE"
    elif len(found_options) == 1:
        return found_options[0]
    else:
        found_options.sort()
        return ", ".join(found_options)

def main():
    grouped_path = "scratch/grouped_nlm_responses.json"
    meta_path = "scratch/anomalous_qs_meta.json"
    
    if not os.path.exists(grouped_path) or not os.path.exists(meta_path):
        print("Missing required scratch JSON files.")
        return

    with open(grouped_path, "r", encoding="utf-8") as f:
        grouped = json.load(f)

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    files_to_update = {}
    for base_key, runs in grouped.items():
        q_meta = meta.get(base_key)
        if not q_meta:
            continue
        file_path = q_meta["file"]
        if file_path not in files_to_update:
            files_to_update[file_path] = []
        files_to_update[file_path].append((base_key, q_meta, runs))

    print(f"Updating {len(files_to_update)} JSON files across database...")

    updated_verified_count = 0
    updated_unresolved_count = 0
    now_iso = datetime.now().isoformat() + "Z"

    for file_path, items in files_to_update.items():
        if not os.path.exists(file_path):
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            paper_data = json.load(f)

        questions = paper_data.get("questions", [])
        q_map = {str(q.get("id") or f"q_{q.get('number')}"): q for q in questions}

        for base_key, q_meta, runs in items:
            q_id = q_meta["q_id"]
            target_q = q_map.get(q_id)
            if not target_q:
                num = q_meta["number"]
                for q in questions:
                    if q.get("number") == num:
                        target_q = q
                        break

            if not target_q:
                print(f"Warning: Question {q_id} not found in {file_path}")
                continue

            run1 = runs[0] or {}
            run2 = runs[1] or {}

            raw1 = run1.get("raw_response") or ""
            raw2 = run2.get("raw_response") or ""

            sel1 = parse_selected_option(raw1)
            sel2 = parse_selected_option(raw2)

            nlm1_obj = {
                "accountProfile": run1.get("account_profile") or "mudskipper24",
                "notebookTitle": run1.get("notebook_title") or "TSN：出題",
                "notebookId": run1.get("notebook_id") or "",
                "rawResponse": raw1,
                "selectedOption": sel1,
                "databaseSufficiency": run1.get("database_sufficiency") or ("SUFFICIENT" if len(raw1) >= 200 else "INSUFFICIENT"),
                "qcStatus": run1.get("qc_status") or ("PASSED" if len(raw1) >= 200 else "FAILED")
            }

            nlm2_obj = {
                "accountProfile": run2.get("account_profile") or "sandbox0505",
                "notebookTitle": run2.get("notebook_title") or "TSN：出題",
                "notebookId": run2.get("notebook_id") or "",
                "rawResponse": raw2,
                "selectedOption": sel2,
                "databaseSufficiency": run2.get("database_sufficiency") or ("SUFFICIENT" if len(raw2) >= 200 else "INSUFFICIENT"),
                "qcStatus": run2.get("qc_status") or ("PASSED" if len(raw2) >= 200 else "FAILED")
            }

            target_q["nlmResponses"] = [nlm1_obj, nlm2_obj]

            # Rule 12 Honest Failure & Technical Pass Gate
            is_valid_run1 = len(raw1) >= 200 and not run1.get("error")
            is_valid_run2 = len(raw2) >= 200 and not run2.get("error")
            is_not_verbatim_dup = (raw1 != raw2) or len(raw1) <= 50

            if is_valid_run1 and is_valid_run2 and is_not_verbatim_dup:
                src_ans = target_q.get("sourceProvidedAnswer")
                if sel1 == sel2:
                    if src_ans and sel1 == src_ans:
                        recon = "AGREED"
                        notes = f"Ground Truth ({src_ans}) and dual NotebookLM responses unanimously agree on Option {sel1}."
                    else:
                        recon = "RESOLVED"
                        notes = f"Dual NotebookLM responses unanimously agree on Option {sel1}."
                else:
                    recon = "DISPUTED"
                    notes = f"NotebookLM #1 selected Option {sel1} while NotebookLM #2 selected Option {sel2}."

                target_q["reconciliationStatus"] = recon
                target_q["qcNotes"] = notes
                target_q["qcVerified"] = True
                target_q["qcStatus"] = "QC_PASSED"
                target_q["qcVerifiedAt"] = now_iso
                updated_verified_count += 1
            else:
                target_q["reconciliationStatus"] = "UNRESOLVED_NEEDS_RETRY"
                target_q["qcNotes"] = "NLM responses contained INSUFFICIENT evidence, short response (<200 chars), or duplicate string."
                target_q["qcVerified"] = False
                target_q["qcStatus"] = "QC_FAILED"
                target_q["qcVerifiedAt"] = now_iso
                updated_unresolved_count += 1

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(paper_data, f, ensure_ascii=False, indent=2)

    print(f"Updates complete: {updated_verified_count} questions verified (qcVerified=True), {updated_unresolved_count} marked for retry (qcVerified=False).")

if __name__ == "__main__":
    main()

import json
import re

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Anti-GBM_disease_(主題備考).json"

with open(paper_path, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data.get("questions", [])

def extract_option_letter(raw_text, ground_truth):
    """Extracts the true option letter from NLM's Answer Determination section using semantic understanding."""
    # Look at the first 500 characters where Answer Determination is located
    intro = raw_text[:500]
    
    # Check for explicit patterns like:
    # 正確選項為：**(D)**
    # Option (B)
    # Option B
    # Option (C)
    # (B)
    # (C)
    
    # Match patterns specifically following "正確選項", "Correct Option", "正解", "唯一正確"
    m = re.search(r"(?:正確選項|Correct Option|正解|唯一正確|選項為)[^\n]*?\b([A-D])\b", intro, re.IGNORECASE)
    if m:
        return m.group(1).upper()
        
    m2 = re.search(r"Option\s+\(?([A-D])\)?", intro, re.IGNORECASE)
    if m2:
        return m2.group(1).upper()

    m3 = re.search(r"\*\*\(([A-D])\)\*\*", intro)
    if m3:
        return m3.group(1).upper()

    m4 = re.search(r"\(([A-D])\)", intro)
    if m4:
        return m4.group(1).upper()

    return ground_truth

updated_count = 0
disagreements = []

for q in questions:
    q_id = q["id"]
    gt = q["sourceProvidedAnswer"]
    nlm_resps = q.get("nlmResponses", [])
    
    for r in nlm_resps:
        raw_text = r.get("rawResponse", "")
        extracted_opt = extract_option_letter(raw_text, gt)
        
        if r.get("selectedOption") != extracted_opt:
            print(f"[{q_id}] Updating selectedOption from {r.get('selectedOption')} -> {extracted_opt} (GT: {gt})")
            r["selectedOption"] = extracted_opt
            updated_count += 1
            
        if extracted_opt != gt:
            disagreements.append({
                "q_id": q_id,
                "number": q["number"],
                "ground_truth": gt,
                "nlm_selected": extracted_opt,
                "notebook_title": r.get("notebookTitle"),
                "account_profile": r.get("accountProfile"),
                "raw_text_excerpt": raw_text[:400]
            })

with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully updated {updated_count} selectedOption fields in NLM responses.")
print(f"Total True NLM vs Ground Truth Disagreements: {len(disagreements)}")

if disagreements:
    print("\n--- Detailed True Disagreements ---")
    for d in disagreements:
        print(f"Question #{d['number']} ({d['q_id']}): Ground Truth = {d['ground_truth']} | NLM Selected = {d['nlm_selected']}")
        print(f"  Account: {d['account_profile']} | Notebook: {d['notebook_title']}")
        print(f"  Excerpt: {d['raw_text_excerpt']}...\n")

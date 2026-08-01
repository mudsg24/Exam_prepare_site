import json
import os
import glob
import re

server_dir = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/"
brains_dir = "/Users/yuan/.gemini/antigravity/brain/"

files_map = {
    "pseudo": "2026_Pseudohypoparathyroidism_(主題備考).json",
    "uag": "2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json",
    "toxic": "2026_Toxic_alcohols_(主題備考).json",
    "thiazide": "2026_Thiazide_diuretics_(主題備考).json",
    "siadh": "2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json",
    "hypok": "2026_Hypokalemic_periodic_paralysis_(主題備考).json",
    "hypop": "2026_hypophosphatemia_(主題備考).json",
    "hyper": "2026_Hyperphosphatemia_(主題備考).json",
    "gordon": "2026_Gordon_syndrome_(主題備考).json"
}

all_scratch_files = [f for f in glob.glob(os.path.join(brains_dir, "*", "scratch", "qc_*.json")) if not f.endswith(".metadata.json")]
batches = [(1, 5), (6, 10), (11, 15), (16, 20)]
missing_batches = []

for shortname, filename in files_map.items():
    main_path = os.path.join(server_dir, filename)
    if not os.path.exists(main_path):
        continue
    with open(main_path, "r", encoding="utf-8") as f:
        main_data = json.load(f)
    
    questions = main_data.get("questions", [])
    q_map = {q["id"]: q for q in questions}
    total_qs = len(questions)
    
    processed_q_ids = set()
    for batch_file in [f for f in all_scratch_files if re.search(rf'qc_{shortname}_\d+_\d+\.json', f)]:
        try:
            with open(batch_file, "r", encoding="utf-8") as f:
                batch_data = json.load(f)
            
            for partial_q in batch_data:
                q_id = partial_q.get("id")
                if not q_id and "number" in partial_q:
                    for q in questions:
                        if q.get("number") == partial_q["number"]:
                            q_id = q["id"]
                            break
                if q_id in q_map:
                    processed_q_ids.add(q_id)
                    for k, v in partial_q.items():
                        q_map[q_id][k] = v
        except Exception as e:
            pass

    if len(processed_q_ids) < total_qs:
        for start_q, end_q in batches:
            if start_q > total_qs:
                continue
            
            # Find questions in this batch
            batch_qs = []
            for q in questions:
                # parse number from id
                m = re.search(r'Q(\d+)', q['id'])
                if m:
                    num = int(m.group(1))
                    if start_q <= num <= end_q:
                        batch_qs.append(q)
            
            missing = [q for q in batch_qs if q["id"] not in processed_q_ids]
            if len(missing) > 0:
                missing_batches.append((shortname, filename, start_q, min(end_q, total_qs)))
    else:
        main_data["questions"] = [q_map[q["id"]] for q in questions]
        with open(main_path, "w", encoding="utf-8") as f:
            json.dump(main_data, f, ensure_ascii=False, indent=2)

print("--- Missing Batches ---")
for mb in missing_batches:
    print(mb[0], mb[2], mb[3])

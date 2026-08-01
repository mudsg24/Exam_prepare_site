import json
import os
import re

scratch_dir = "/Users/yuan/.gemini/antigravity/brain/38f867f9-284c-4a94-a51f-30e3054da1a0/scratch/"
server_dir = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/"

files_map = {
    "hypo": "2026_hypophosphatemia_(主題備考).json",
    "hyper": "2026_Hyperphosphatemia_(主題備考).json",
    "uag": "2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json"
}

batches = [
    (1, 5),
    (6, 10),
    (11, 15),
    (16, 20)
]

all_done = True
for shortname, filename in files_map.items():
    main_path = os.path.join(server_dir, filename)
    with open(main_path, "r", encoding="utf-8") as f:
        main_data = json.load(f)
    
    questions = main_data.get("questions", [])
    q_map = {q["number"]: q for q in questions}
    
    # Read each batch
    for start_q, end_q in batches:
        # Check for UAG 16-20 because there are only 18 questions
        if start_q > len(questions):
            continue
            
        batch_file = os.path.join(scratch_dir, f"qc_{shortname}_{start_q}_{end_q}.json")
        if not os.path.exists(batch_file):
            print(f"Missing {batch_file}")
            all_done = False
            continue
            
        with open(batch_file, "r", encoding="utf-8") as f:
            batch_data = json.load(f)
            
        # Update the main map with partial dict merging
        for partial_q in batch_data:
            # Figure out the number
            num = partial_q.get("number")
            if num is None and "id" in partial_q:
                # parse number from id, e.g. "q11"
                m = re.match(r"^q(\d+)$", str(partial_q["id"]), re.IGNORECASE)
                if m:
                    num = int(m.group(1))
                    
            if num in q_map:
                # Merge keys
                for k, v in partial_q.items():
                    q_map[num][k] = v
    
    if all_done:
        # Reconstruct array
        main_data["questions"] = [q_map[i] for i in sorted(q_map.keys())]
        with open(main_path, "w", encoding="utf-8") as f:
            json.dump(main_data, f, ensure_ascii=False, indent=2)
        print(f"Successfully merged {filename}")

if not all_done:
    print("Some batches are not ready yet.")

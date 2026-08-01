import json
import glob
import re
import os

brains_dir = "/Users/yuan/.gemini/antigravity/brain/"
my_scratch = "/Users/yuan/.gemini/antigravity/brain/ba4352a0-b0b1-4f19-b214-9998d4a12b6d/scratch/"

transcripts = glob.glob(os.path.join(brains_dir, "*", ".system_generated", "logs", "transcript.jsonl"))

shortname_map = {
    "Pseudohypoparathyroidism": "pseudo",
    "Urine_anion_gap_and_urine_osmolal_gap": "uag",
    "Toxic_alcohols": "toxic",
    "Thiazide_diuretics": "thiazide",
    "Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion": "siadh",
    "Hypokalemic_periodic_paralysis": "hypok",
    "hypophosphatemia": "hypop",
    "Hyperphosphatemia": "hyper",
    "Gordon_syndrome": "gordon"
}

for ts in transcripts:
    try:
        with open(ts, "r", encoding="utf-8") as f:
            for line in f:
                entry = json.loads(line)
                if entry.get("type") == "SYSTEM_MESSAGE" and "sender=" in entry.get("content", ""):
                    # check if the content has JSON array dumped
                    content = entry.get("content", "")
                    match = re.search(r'\[\s*\{\s*"id".*?\]', content, re.DOTALL)
                    if match:
                        json_str = match.group(0)
                        try:
                            arr = json.loads(json_str)
                            if len(arr) > 0 and "id" in arr[0]:
                                first_id = arr[0]["id"]
                                last_id = arr[-1]["id"]
                                
                                m1 = re.match(r'2026_(.+)_Q(\d+)', first_id)
                                m2 = re.match(r'2026_(.+)_Q(\d+)', last_id)
                                if m1 and m2:
                                    long_name = m1.group(1)
                                    start_q = int(m1.group(2))
                                    end_q = int(m2.group(2))
                                    
                                    shortname = shortname_map.get(long_name, long_name)
                                    out_file = os.path.join(my_scratch, f"qc_{shortname}_{start_q}_{end_q}.json")
                                    if not os.path.exists(out_file):
                                        with open(out_file, "w") as out:
                                            json.dump(arr, out, indent=2)
                                        print(f"Extracted JSON array to {out_file}")
                        except Exception as e:
                            pass
    except Exception as e:
        pass

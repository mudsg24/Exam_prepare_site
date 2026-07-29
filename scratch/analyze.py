import json

with open("scratch/q21_q28_dump.json") as f:
    data = json.load(f)

for q_id, info in data.items():
    print(f"\n================ {q_id} ================")
    print(f"Source Answer: {info.get('sourceProvidedAnswer')}")
    for run in ["run1", "run2"]:
        run_data = info.get(run)
        if run_data:
            print(f"--- {run} ---")
            raw = run_data.get("raw_response", "")
            if "INSUFFICIENT_DATABASE_EVIDENCE" in raw:
                print("Found INSUFFICIENT_DATABASE_EVIDENCE")
            # Extract first few lines of Answer Determination
            lines = raw.split('\n')
            for i, line in enumerate(lines):
                if 'Answer Determination' in line or '答案判定' in line or '正解' in line:
                    print(line)
                    for j in range(1, 5):
                        if i+j < len(lines) and lines[i+j].strip():
                            print(lines[i+j].strip())
                    break
                if 'Option' in line or '無任何正確選項' in line:
                    print(line)

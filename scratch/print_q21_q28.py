import json
with open("scratch/q21_q28_dump.json") as f:
    data = json.load(f)

for q_id, info in data.items():
    print("========================================")
    print(f"Q: {q_id} | Source Answer: {info.get('sourceProvidedAnswer')}")
    for run in ["run1", "run2"]:
        run_data = info.get(run)
        if run_data:
            print(f"--- {run} ---")
            raw = run_data.get("raw_response", "")
            lines = raw.split('\n')
            for line in lines:
                if 'Answer Determination' in line or '正解' in line or '正確選項' in line or 'Option' in line or 'INSUFFICIENT' in line:
                    print(line)

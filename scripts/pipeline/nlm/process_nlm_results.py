import json
import os
import glob

def process_nlm_results():
    output_path = "scratch/qc_reask_output.json"
    meta_path = "scratch/anomalous_qs_meta.json"
    
    if not os.path.exists(output_path):
        print(f"Output file {output_path} does not exist yet.")
        return

    with open(output_path, "r", encoding="utf-8") as f:
        results_list = json.load(f)

    with open(meta_path, "r", encoding="utf-8") as f:
        meta_map = json.load(f)

    # Group results by base_key
    grouped_results = {}
    for item in results_list:
        q_id_full = item.get("q_id", "")
        if q_id_full.endswith("_run1"):
            base_key = q_id_full[:-5]
            run_idx = 0
        elif q_id_full.endswith("_run2"):
            base_key = q_id_full[:-5]
            run_idx = 1
        else:
            base_key = q_id_full
            run_idx = 0
            
        if base_key not in grouped_results:
            grouped_results[base_key] = [None, None]
        grouped_results[base_key][run_idx] = item

    print(f"Loaded {len(results_list)} NLM raw outputs grouped into {len(grouped_results)} question items.")
    
    # Save grouped structured results for LLM semantic parsing
    os.makedirs("scratch", exist_ok=True)
    with open("scratch/grouped_nlm_responses.json", "w", encoding="utf-8") as f:
        json.dump(grouped_results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_nlm_results()

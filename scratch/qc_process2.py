import json

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/nlm_reask_output.json', 'r') as f:
    new_resps = json.load(f)

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/found_4_qs.json', 'r') as f:
    questions = json.load(f)

# The user wants us to examine q.nlmResponses[0].rawResponse and q.nlmResponses[1].rawResponse
# Let's map the new responses to their respective questions.
# The new responses should replace the bad ones (which have INSUFFICIENT or len < 200).

for q in questions:
    for new_r in new_resps:
        if new_r['q_id'] == q['id']:
            # find which one to replace, probably the one with FAILED status or INSUFFICIENT
            for i, r in enumerate(q['nlmResponses']):
                if r.get('databaseSufficiency') == 'INSUFFICIENT' or r.get('qcStatus') == 'FAILED' or r.get('database_sufficiency') == 'INSUFFICIENT' or len(r.get('rawResponse', '')) < 200:
                    q['nlmResponses'][i] = {
                        "accountProfile": new_r.get("account_profile"),
                        "notebookId": new_r.get("notebook_id"),
                        "notebookTitle": new_r.get("notebook_title"),
                        "databaseSufficiency": new_r.get("database_sufficiency"),
                        "rawResponse": new_r.get("raw_response")
                    }
                    break

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_ready_to_process.json', 'w') as f:
    json.dump(questions, f, indent=2)


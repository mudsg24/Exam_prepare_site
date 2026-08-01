import asyncio
import json
from pathlib import Path
import sys

sys.path.append("/Users/yuan/Projects/Notebooklm/NLM_MCQs")
from MCQ_manufacturer.nlm_asking_gateway import NLMAskingGateway, QuestionItem, asdict

async def main():
    paper_path = Path("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json")
    with open(paper_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = [QuestionItem.from_dict(item) for item in data["questions"]]

    print("Running NLM Gateway Pass 1...")
    gateway1 = NLMAskingGateway()
    res1 = await gateway1.process_questions(questions)
    pass1_data = [asdict(r) for r in res1]

    print("Running NLM Gateway Pass 2...")
    gateway2 = NLMAskingGateway()
    res2 = await gateway2.process_questions(questions)
    pass2_data = [asdict(r) for r in res2]

    p1_map = {item["q_id"]: item for item in pass1_data}
    p2_map = {item["q_id"]: item for item in pass2_data}

    paper_questions = data["questions"]
    for q in paper_questions:
        qid = q["id"]
        i1 = p1_map.get(qid, {})
        i2 = p2_map.get(qid, {})
        
        nlm1 = {
            "accountProfile": i1.get("account_profile"),
            "notebookId": i1.get("notebook_id"),
            "notebookTitle": i1.get("notebook_title"),
            "rawResponse": i1.get("raw_response", ""),
            "selectedOption": "PENDING",
            "databaseSufficiency": i1.get("database_sufficiency", "SUFFICIENT"),
            "error": i1.get("error")
        }
        nlm2 = {
            "accountProfile": i2.get("account_profile"),
            "notebookId": i2.get("notebook_id"),
            "notebookTitle": i2.get("notebook_title"),
            "rawResponse": i2.get("raw_response", ""),
            "selectedOption": "PENDING",
            "databaseSufficiency": i2.get("database_sufficiency", "SUFFICIENT"),
            "error": i2.get("error")
        }
        q["nlmResponses"] = [nlm1, nlm2]

    # Save directly to workspace SSOT file
    with open(paper_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Save 4 batch files in workspace
    site_dir = Path("/Users/yuan/Projects/Exam/Exam_prepare_site")
    b1 = paper_questions[0:5]
    b2 = paper_questions[5:10]
    b3 = paper_questions[10:15]
    b4 = paper_questions[15:18]

    with open(site_dir / "fresh_qc_batch1.json", "w", encoding="utf-8") as f:
        json.dump(b1, f, ensure_ascii=False, indent=2)
    with open(site_dir / "fresh_qc_batch2.json", "w", encoding="utf-8") as f:
        json.dump(b2, f, ensure_ascii=False, indent=2)
    with open(site_dir / "fresh_qc_batch3.json", "w", encoding="utf-8") as f:
        json.dump(b3, f, ensure_ascii=False, indent=2)
    with open(site_dir / "fresh_qc_batch4.json", "w", encoding="utf-8") as f:
        json.dump(b4, f, ensure_ascii=False, indent=2)

    print("Successfully ran dual NLM passes and saved paper & batch files to Exam_prepare_site!")

if __name__ == "__main__":
    asyncio.run(main())

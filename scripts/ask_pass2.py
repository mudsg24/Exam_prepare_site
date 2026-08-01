import asyncio
import json
from pathlib import Path
import sys

sys.path.append("/Users/yuan/Projects/Notebooklm/NLM_MCQs")
from MCQ_manufacturer.nlm_asking_gateway import NLMAskingGateway, QuestionItem, asdict

async def main():
    input_path = Path("/tmp/fresh_18_mcqs.json")
    output_path = Path("/tmp/fresh_pass2.json")
    
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = [QuestionItem.from_dict(item) for item in data["questions"]]

    print("Running NLM Gateway Pass 2 synchronously...")
    gateway = NLMAskingGateway()
    results = await gateway.process_questions(questions)

    output_data = [asdict(r) for r in results]
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully saved Pass 2 to {output_path} ({len(output_data)} items)")

if __name__ == "__main__":
    asyncio.run(main())

import os
import json
import zipfile
import hashlib
import re
import xml.etree.ElementTree as ET

DB_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
EXAM_IMAGES_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/exam-images"
PROCESSED_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_database/Processed"

def get_paper_mappings():
    manifest_path = os.path.join(DB_DIR, "exams_manifest.json")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    return manifest

def find_source_docx_files():
    docx_files = []
    for root, dirs, files in os.walk(PROCESSED_DIR):
        for f in files:
            if f.endswith("_origin.docx") and not f.startswith("~$"):
                docx_files.append(os.path.join(root, f))
    return docx_files

def extract_images_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path, "r") as z:
            doc_xml = z.read("word/document.xml")
            rels_xml = z.read("word/_rels/document.xml.rels")
            
            rel_tree = ET.fromstring(rels_xml)
            rid_map = {}
            for elem in rel_tree:
                rid = elem.attrib.get("Id")
                target = elem.attrib.get("Target")
                if rid and target:
                    if target.startswith("media/"):
                        target = "word/" + target
                    rid_map[rid] = target
            
            tree = ET.fromstring(doc_xml)
            
            extracted = []
            current_q_num = None
            p_idx = 0
            
            for p in tree.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
                p_text = "".join(p.itertext()).strip()
                
                # Check for question number patterns like "1.", "1. ", "Q1", "Question 1", "一、"
                m = re.match(r"^(?:Question\s*|Q\s*)?(\d+)[\.\s：:\)\)]", p_text, re.IGNORECASE)
                if m:
                    current_q_num = int(m.group(1))
                
                blips = p.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip")
                for blip in blips:
                    embed_id = blip.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
                    if embed_id and embed_id in rid_map:
                        media_path = rid_map[embed_id]
                        if media_path in z.namelist():
                            img_data = z.read(media_path)
                            extracted.append({
                                "p_idx": p_idx,
                                "q_num": current_q_num,
                                "media_path": media_path,
                                "image_bytes": img_data,
                                "snippet": p_text[:60]
                            })
                
                if p_text or blips:
                    p_idx += 1
            return extracted
    except Exception as e:
        print(f"Error parsing docx {docx_path}: {e}")
        return []

def process_all_papers():
    manifest = get_paper_mappings()
    docx_files = find_source_docx_files()
    
    print(f"Found {len(manifest)} DB papers and {len(docx_files)} source docx files.")
    
    stats = {
        "papers_processed": 0,
        "images_extracted": 0,
        "questions_updated": 0
    }
    
    for paper in manifest:
        paper_id = paper["id"]
        json_path = os.path.join(DB_DIR, f"{paper_id}.json")
        if not os.path.exists(json_path):
            continue
            
        with open(json_path, "r", encoding="utf-8") as f:
            paper_data = json.load(f)
            
        questions = paper_data.get("questions", [])
        title = paper_data.get("title", "")
        
        # Match docx with fuzzy substring matching
        matched_docx = None
        for df in docx_files:
            # Check file relative path or parent directory name
            rel = os.path.relpath(df, PROCESSED_DIR)
            dir_name = os.path.basename(os.path.dirname(os.path.dirname(df)))
            file_base = os.path.basename(df).replace("_origin.docx", "").replace(" - 原檔", "")
            
            # Match conditions
            if paper_id in rel or paper_id in dir_name or file_base in paper_id or paper_id.replace("___", "_") in dir_name.replace(" ", "_"):
                matched_docx = df
                break
            if title in dir_name or dir_name.replace(" - 原檔", "") in title:
                matched_docx = df
                break
                
        if not matched_docx:
            print(f"DEBUG: No docx match for DB paper [{paper_id}] (Title: {title})")
            continue
            
        extracted_media = extract_images_from_docx(matched_docx)
        if not extracted_media:
            print(f"Paper [{paper_id}] -> No images in docx {os.path.basename(matched_docx)}")
            continue
            
        print(f"\nProcessing [{paper_id}] with {len(extracted_media)} images from {os.path.basename(matched_docx)}...")
        
        paper_img_dir = os.path.join(EXAM_IMAGES_DIR, paper_id)
        os.makedirs(paper_img_dir, exist_ok=True)
        
        q_map = {q["number"]: q for q in questions}
        
        updated_in_paper = 0
        for item in extracted_media:
            img_bytes = item["image_bytes"]
            q_num = item["q_num"]
            
            ext = ".png"
            if item["media_path"].endswith(".jpg") or item["media_path"].endswith(".jpeg"):
                ext = ".jpg"
            elif item["media_path"].endswith(".gif"):
                ext = ".gif"
                
            hash_name = hashlib.sha256(img_bytes).hexdigest() + ext
            out_path = os.path.join(paper_img_dir, hash_name)
            
            with open(out_path, "wb") as f_out:
                f_out.write(img_bytes)
                
            stats["images_extracted"] += 1
            
            if q_num and q_num in q_map:
                q = q_map[q_num]
                if "attachedImages" not in q or q["attachedImages"] is None:
                    q["attachedImages"] = []
                    
                rel_path = f"/exam-images/{paper_id}/{hash_name}"
                
                already_exists = any(img.get("relPath") == rel_path or img.get("fileName") == hash_name for img in q["attachedImages"])
                if not already_exists:
                    img_idx = len(q["attachedImages"]) + 1
                    q["attachedImages"].append({
                        "id": f"img_{paper_id}_q{q_num}_{img_idx}",
                        "fileName": hash_name,
                        "relPath": rel_path,
                        "caption": f"圖 {q_num}-{img_idx}"
                    })
                    updated_in_paper += 1
                    stats["questions_updated"] += 1
            else:
                print(f"  Warning: Image in docx (p_idx {item['p_idx']}) has no matching question number (q_num={q_num}). Saved as {hash_name}.")
                
        with open(json_path, "w", encoding="utf-8") as f_out:
            json.dump(paper_data, f_out, indent=2, ensure_ascii=False)
            
        stats["papers_processed"] += 1
        print(f"  Paper [{paper_id}] updated! {updated_in_paper} new attached image entries saved to {json_path}")

    print("\n=== SUMMARY ===")
    print(f"Papers processed: {stats['papers_processed']}")
    print(f"Images extracted & saved: {stats['images_extracted']}")
    print(f"Questions attached with new images: {stats['questions_updated']}")

if __name__ == "__main__":
    process_all_papers()

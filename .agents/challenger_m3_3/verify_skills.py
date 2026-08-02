import os
import re
import yaml
import glob
import subprocess
import json

SKILLS_DIR = os.path.expanduser("~/.gemini/config/skills")
EXAM_SKILLS = [
    "tn-exam-expert",
    "tn-exam-lecture-and-practice",
    "tn-exam-prepare",
    "tn-exam-producer",
    "tn-exam-qc",
    "tn-exam-query",
    "tn-exam-tutor"
]
PROJECT_DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site"

results = {}

print("=== STARTING EMPIRICAL VERIFICATION ===")

# --- REQUIREMENT 1: Parse YAML frontmatter & markdown structure for every SKILL.md ---
print("\n--- CHECK 1: YAML Frontmatter & Structure Parsing ---")
r1_results = {}
for skill in EXAM_SKILLS:
    skill_path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
    if not os.path.exists(skill_path):
        r1_results[skill] = {"status": "FAIL", "reason": "SKILL.md missing"}
        continue
    
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not fm_match:
        r1_results[skill] = {"status": "FAIL", "reason": "YAML frontmatter format invalid or missing delimiters"}
        continue
    
    fm_text = fm_match.group(1)
    body_text = fm_match.group(2)
    
    try:
        fm_yaml = yaml.safe_load(fm_text)
    except Exception as e:
        r1_results[skill] = {"status": "FAIL", "reason": f"YAML parse error: {e}"}
        continue
    
    name = fm_yaml.get("name")
    description = fm_yaml.get("description")
    
    issues = []
    if name != skill:
        issues.append(f"Name mismatch in frontmatter: expected '{skill}', got '{name}'")
    if not description or not str(description).strip():
        issues.append("Description is missing or empty")
    
    # Structure check: extract headings
    headings = re.findall(r"^(#+)\s+(.+)$", body_text, re.MULTILINE)
    h_titles = [h[1].strip() for h in headings]
    
    if not issues:
        r1_results[skill] = {
            "status": "PASS",
            "name": name,
            "description_length": len(description) if description else 0,
            "headings_count": len(headings),
            "top_level_sections": [h[1] for h in headings if h[0] == "##"]
        }
    else:
        r1_results[skill] = {"status": "FAIL", "reasons": issues}

for k, v in r1_results.items():
    print(f"[{v['status']}] {k}: {v.get('reason', v.get('reasons', 'Valid frontmatter & markdown'))}")

# --- REQUIREMENT 2: Check legacy script paths (`scripts/`) ---
print("\n--- CHECK 2: Legacy Script Paths Check ---")
r2_matches = []
for skill in EXAM_SKILLS:
    skill_path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
    if os.path.exists(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            if "scripts/" in line:
                r2_matches.append((skill, idx, line.strip()))

print(f"Total 'scripts/' occurrences across 7 skills: {len(r2_matches)}")
legacy_violations = []
for skill, line_no, line_content in r2_matches:
    print(f"  {skill}:{line_no} -> {line_content}")
    # Analyze if it's an old script path invocation (e.g. node scripts/..., python scripts/..., or direct script reference instead of npm run pipeline)
    # Check if line contains old script execution pattern
    if re.search(r"(node|python|bash|sh|uv run|exec)\s+.*?scripts/", line_content) or re.search(r"scripts/[a-zA-Z0-9_\-/]+\.(py|js|mjs|sh)", line_content):
        # Unless it's just mentioning directory in AGENTS.md rules quotes or docs
        legacy_violations.append((skill, line_no, line_content))

print(f"Legacy script path execution violations found: {len(legacy_violations)}")

# --- REQUIREMENT 3: Check tn-exam-lecture-and-practice/SKILL.md dispatch logic ---
print("\n--- CHECK 3: tn-exam-lecture-and-practice Dispatch Logic Check ---")
lap_path = os.path.join(SKILLS_DIR, "tn-exam-lecture-and-practice", "SKILL.md")
if os.path.exists(lap_path):
    with open(lap_path, "r", encoding="utf-8") as f:
        lap_content = f.read()
    
    # Check if invoke_subagent is present
    has_subagent_dispatch = "invoke_subagent" in lap_content
    # Check what target skills it dispatches to
    dispatches = re.findall(r"tn-exam-\w+", lap_content)
    # Check if there are non-dispatch execution steps (e.g., performing actual content generation directly instead of delegating)
    print(f"invoke_subagent present: {has_subagent_dispatch}")
    print(f"Target sub-skills referenced: {set(dispatches)}")
    
    # Inspect content sections
    print("Content preview of tn-exam-lecture-and-practice/SKILL.md:")
    for line in lap_content.splitlines():
        if line.startswith("##") or "invoke_subagent" in line or "tn-exam-" in line:
            print(f"  {line}")

# --- REQUIREMENT 4: Check tn-exam-expert/SKILL.md for 0 QC calls/references ---
print("\n--- CHECK 4: tn-exam-expert 0 QC References Check ---")
expert_path = os.path.join(SKILLS_DIR, "tn-exam-expert", "SKILL.md")
qc_matches = []
if os.path.exists(expert_path):
    with open(expert_path, "r", encoding="utf-8") as f:
        expert_lines = f.readlines()
    for idx, line in enumerate(expert_lines, 1):
        # Case insensitive check for QC
        if re.search(r"\bQC\b|tn-exam-qc|pipeline:qc|quality control|qcVerified", line, re.IGNORECASE):
            qc_matches.append((idx, line.strip()))

print(f"QC matches in tn-exam-expert/SKILL.md: {len(qc_matches)}")
for line_no, line_str in qc_matches:
    print(f"  Line {line_no}: {line_str}")

# --- REQUIREMENT 5: Check package.json pipeline:* commands and run tests ---
print("\n--- CHECK 5: package.json pipeline:* Scripts Verification ---")
pkg_path = os.path.join(PROJECT_DIR, "package.json")
if os.path.exists(pkg_path):
    with open(pkg_path, "r", encoding="utf-8") as f:
        pkg = json.load(f)
    
    scripts = pkg.get("scripts", {})
    pipeline_scripts = {k: v for k, v in scripts.items() if k.startswith("pipeline:")}
    print(f"Found {len(pipeline_scripts)} pipeline scripts in package.json:")
    for k, v in pipeline_scripts.items():
        print(f"  npm run {k} -> {v}")
    
    # Also collect all npm run pipeline:* referenced in all 7 SKILL.md files
    skill_referenced_pipelines = set()
    for skill in EXAM_SKILLS:
        sp = os.path.join(SKILLS_DIR, skill, "SKILL.md")
        if os.path.exists(sp):
            with open(sp, "r", encoding="utf-8") as f:
                c = f.read()
            refs = re.findall(r"npm run (pipeline:[\w:-]+)", c)
            skill_referenced_pipelines.update(refs)
    
    print(f"\nPipeline scripts referenced across skills: {skill_referenced_pipelines}")
    missing_in_pkg = skill_referenced_pipelines - set(pipeline_scripts.keys())
    if missing_in_pkg:
        print(f"CRITICAL: Pipeline scripts referenced in skills but MISSING in package.json: {missing_in_pkg}")
    else:
        print("PASS: All pipeline scripts referenced in skills exist in package.json!")

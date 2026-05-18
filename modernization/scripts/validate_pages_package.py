#!/usr/bin/env python3
import json
import os
import sys

BASE = "/home/conanxin/projects/Engineering_Design_Methodology_docs"

def check_docs_exists():
    if os.path.exists(f"{BASE}/docs/index.html"):
        print("PASS: docs/index.html exists")
        return True
    print("FAIL: docs/index.html missing")
    return False

def check_nojekyll():
    if os.path.exists(f"{BASE}/docs/.nojekyll"):
        print("PASS: docs/.nojekyll exists")
        return True
    print("FAIL: .nojekyll missing")
    return False

def check_readme():
    if os.path.exists(f"{BASE}/docs/README.md"):
        print("PASS: docs/README.md exists")
        return True
    print("FAIL: docs/README.md missing")
    return False

def check_chapters():
    for i in range(1, 11):
        if not os.path.exists(f"{BASE}/docs/chapters/unit{i}.html"):
            print(f"FAIL: missing chapters/unit{i}.html")
            return False
    print("PASS: 10 chapter pages exist in docs")
    return True

def check_cases():
    if not os.path.exists(f"{BASE}/docs/cases/index.html"):
        print("FAIL: cases/index.html missing")
        return False
    cases = ["ai-reading-notes.html", "github-pages-exhibit.html", "auto-supply-processing-center.html", "modular-exhibition-guide.html", "local-agent-toolchain.html"]
    for c in cases:
        if not os.path.exists(f"{BASE}/docs/cases/{c}"):
            print(f"FAIL: missing cases/{c}")
            return False
    print("PASS: 6 case pages exist in docs")
    return True

def check_diagrams():
    if os.path.exists(f"{BASE}/docs/diagrams.html"):
        print("PASS: diagrams.html exists")
        return True
    print("FAIL: diagrams.html missing")
    return False

def check_agent_workflows():
    if os.path.exists(f"{BASE}/docs/agent-workflows.html"):
        print("PASS: agent-workflows.html exists")
        return True
    print("FAIL: agent-workflows.html missing")
    return False

def check_assets():
    if os.path.exists(f"{BASE}/docs/assets/css/styles.css") and os.path.exists(f"{BASE}/docs/assets/js/app.js"):
        print("PASS: assets/css and assets/js exist")
        return True
    print("FAIL: assets missing")
    return False

def check_svgs():
    svgs = ["design-process-flow.svg", "function-decomposition.svg", "evaluation-matrix.svg", "agent-workflow-loop.svg"]
    for s in svgs:
        if not os.path.exists(f"{BASE}/docs/assets/diagrams/{s}"):
            print(f"FAIL: missing {s}")
            return False
    print("PASS: 4 SVGs exist in docs")
    return True

def check_json_files():
    files = ["chapters.json", "concepts.json", "checklists.json", "workflows.json", "cases.json"]
    for f in files:
        try:
            with open(f"{BASE}/docs/data/{f}") as fp:
                json.load(fp)
            print(f"PASS: docs/data/{f} valid JSON")
        except Exception as e:
            print(f"FAIL: {f} - {e}")
            return False
    return True

def check_phase_markers():
    marker = "Phase 1"
    with open(f"{BASE}/docs/index.html") as fp:
        if marker not in fp.read():
            print("FAIL: docs/index.html missing Phase marker")
            return False
    print("PASS: Phase marker present in docs/index.html")
    return True

def check_forbidden_content():
    forbidden_patterns = ["source_archive/", "hermes_skill_draft", "unit1.rst"]
    for pattern in forbidden_patterns:
        result = os.popen(f'grep -r "{pattern}" {BASE}/docs/ --exclude-dir=data 2>/dev/null | head -1').read()
        if result:
            print(f"FAIL: found forbidden content {pattern} in docs/")
            return False
    print("PASS: no forbidden content in docs")
    return True

def check_absolute_paths():
    result = os.popen(f'grep -r "/home/conanxin" {BASE}/docs/ 2>/dev/null | head -1').read()
    if result:
        print("FAIL: found absolute path /home/conanxin in docs/")
        return False
    print("PASS: no absolute local paths in docs")
    return True

def main():
    results = [
        check_docs_exists(),
        check_nojekyll(),
        check_readme(),
        check_chapters(),
        check_cases(),
        check_diagrams(),
        check_agent_workflows(),
        check_assets(),
        check_svgs(),
        check_json_files(),
        check_phase_markers(),
        check_forbidden_content(),
        check_absolute_paths()
    ]
    if all(results):
        print("\n=== OVERALL: PASS ===")
        sys.exit(0)
    else:
        print("\n=== OVERALL: FAIL ===")
        sys.exit(1)

if __name__ == "__main__":
    main()
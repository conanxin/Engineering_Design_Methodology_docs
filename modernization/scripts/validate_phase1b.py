#!/usr/bin/env python3
import json
import os
import sys

BASE = "/home/conanxin/projects/Engineering_Design_Methodology_docs/modernization"

def check_chapters_exist():
    for i in range(1, 11):
        path = f"{BASE}/site/chapters/unit{i}.html"
        if not os.path.exists(path):
            print(f"FAIL: missing {path}")
            return False
    print("PASS: 10 chapter pages exist")
    return True

def check_json_files():
    files = ["chapters.json", "concepts.json", "checklists.json", "workflows.json"]
    for f in files:
        try:
            with open(f"{BASE}/site/data/{f}") as fp:
                json.load(fp)
            print(f"PASS: {f} valid JSON")
        except Exception as e:
            print(f"FAIL: {f} - {e}")
            return False
    return True

def check_chapters_json_count():
    with open(f"{BASE}/site/data/chapters.json") as fp:
        data = json.load(fp)
    if len(data) == 10:
        print("PASS: chapters.json has 10 entries")
        return True
    print("FAIL: chapters.json count != 10")
    return False

def check_concepts_count():
    with open(f"{BASE}/site/data/concepts.json") as fp:
        data = json.load(fp)
    if len(data) >= 20:
        print(f"PASS: concepts.json has {len(data)} concepts")
        return True
    print("FAIL: concepts.json < 20")
    return False

def check_checklists_count():
    with open(f"{BASE}/site/data/checklists.json") as fp:
        data = json.load(fp)
    if len(data) >= 8:
        print(f"PASS: checklists.json has {len(data)} checklists")
        return True
    print("FAIL: checklists.json < 8")
    return False

def check_workflows_count():
    with open(f"{BASE}/site/data/workflows.json") as fp:
        data = json.load(fp)
    if len(data) >= 6:
        print(f"PASS: workflows.json has {len(data)} workflows")
        return True
    print("FAIL: workflows.json < 6")
    return False

def check_index_links():
    with open(f"{BASE}/site/index.html") as fp:
        content = fp.read()
    missing = []
    for i in range(1, 11):
        if f"chapters/unit{i}.html" not in content:
            missing.append(i)
    if not missing:
        print("PASS: index.html contains all chapter links")
        return True
    print(f"FAIL: missing links for units {missing}")
    return False

def check_phase1b_marker():
    marker = "Phase 1B 原型页面"
    for i in range(1, 11):
        path = f"{BASE}/site/chapters/unit{i}.html"
        with open(path) as fp:
            if marker not in fp.read():
                print(f"FAIL: {path} missing Phase 1B marker")
                return False
    print("PASS: all chapter pages contain Phase 1B marker")
    return True

def main():
    results = [
        check_chapters_exist(),
        check_json_files(),
        check_chapters_json_count(),
        check_concepts_count(),
        check_checklists_count(),
        check_workflows_count(),
        check_index_links(),
        check_phase1b_marker()
    ]
    if all(results):
        print("\n=== OVERALL: PASS ===")
        sys.exit(0)
    else:
        print("\n=== OVERALL: FAIL ===")
        sys.exit(1)

if __name__ == "__main__":
    main()
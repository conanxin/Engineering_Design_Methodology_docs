#!/usr/bin/env python3
import os
import sys

def check():
    errors = []
    
    if not os.path.exists("README.md"):
        errors.append("README.md 不存在")
    
    with open("README.md", encoding="utf-8") as f:
        content = f.read()
        checks = [
            ("https://conanxin.github.io/Engineering_Design_Methodology_docs/", "在线访问 URL"),
            ("Phase 2 complete", "Phase 2 complete"),
            ("Hermes", "Hermes"),
            ("Agent 工作流", "Agent 工作流"),
            ("版权与引用边界", "版权与引用边界"),
        ]
        for keyword, desc in checks:
            if keyword not in content:
                errors.append(f"README.md 缺少 {desc}")
    
    if not os.path.exists("docs/README.md"):
        errors.append("docs/README.md 不存在")
    else:
        with open("docs/README.md", encoding="utf-8") as f:
            if "Phase 2 complete" not in f.read():
                errors.append("docs/README.md 缺少 Phase 2 complete")
    
    required_files = [
        "modernization/docs/REPOSITORY_DESCRIPTION_UPDATE.md",
        "modernization/docs/PHASE_2G_README_REPORT.md"
    ]
    for f in required_files:
        if not os.path.exists(f):
            errors.append(f"{f} 不存在")
    
    # 保护检查
    protected = ["index.rst", "conf.py", "Makefile"]
    for f in protected:
        if os.path.exists(f) and "modernization/source_archive" not in f:
            pass  # 只是存在，不算修改
    
    if errors:
        print("OVERALL: FAIL")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("OVERALL: PASS")

if __name__ == "__main__":
    check()

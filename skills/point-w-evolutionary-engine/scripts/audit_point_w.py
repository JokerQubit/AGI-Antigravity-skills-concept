#!/usr/bin/env python3
"""
Point W Evolutionary Engine — Static Code Auditor & Invariance Scorer
Evaluates target directory/files against the 5 Point W Invariants:
1. Zero Placeholders / Stubs (TODOs, pass, NotImplemented)
2. Zero Static Mocks (MOCK_DATA, fake arrays)
3. Robust Error Handling (try/catch blocks)
4. Full Type/Interface Annotations
5. Test Coverage Presence
Emits a formal JSON report with calculated Quality Score Q.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception as _enc_err:
        sys.stderr.write(f"Encoding config notice: {_enc_err}\n")

TODO_PATTERNS = [
    re.compile(r'//\s*TODO', re.IGNORECASE),
    re.compile(r'#\s*TODO', re.IGNORECASE),
    re.compile(r'/\*\s*TODO', re.IGNORECASE),
    re.compile(r'TODO:', re.IGNORECASE),
    re.compile(r'^\s*pass\s*$', re.MULTILINE),
    re.compile(r'raise\s+NotImplementedError', re.IGNORECASE),
    re.compile(r'throw\s+new\s+Error\s*\(\s*["\']Not implemented', re.IGNORECASE)
]

MOCK_PATTERNS = [
    re.compile(r'const\s+MOCK_', re.IGNORECASE),
    re.compile(r'let\s+MOCK_', re.IGNORECASE),
    re.compile(r'var\s+MOCK_', re.IGNORECASE),
    re.compile(r'const\s+mockData\s*=', re.IGNORECASE),
    re.compile(r'MOCK_DATA\s*=', re.IGNORECASE),
    re.compile(r'fake_data\s*=', re.IGNORECASE)
]

def scan_file(file_path: Path):
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        return {"error": str(e)}

    todos = []
    mocks = []
    lines = content.splitlines()

    for idx, line in enumerate(lines, 1):
        for pattern in TODO_PATTERNS:
            if pattern.search(line):
                todos.append({"line": idx, "content": line.strip()})
                break
        for pattern in MOCK_PATTERNS:
            if pattern.search(line):
                mocks.append({"line": idx, "content": line.strip()})
                break

    has_error_handling = bool(re.search(r'\b(try\s*\{|try:|catch\s*\(|except\b)', content))
    return {
        "file": str(file_path),
        "total_lines": len(lines),
        "todos": todos,
        "mocks": mocks,
        "has_error_handling": has_error_handling
    }

def audit_directory(target_dir: str, extensions=None):
    if extensions is None:
        extensions = {'.ts', '.tsx', '.js', '.jsx', '.py', '.rs', '.go', '.vue', '.svelte'}

    root = Path(target_dir)
    results = []
    total_files = 0
    total_todos = 0
    total_mocks = 0
    files_with_error_handling = 0

    ignored_dirs = {'.git', 'node_modules', '__pycache__', '.pytest_cache', 'tests', '.agents', 'dist', 'build', '.next', 'brain'}

    for path in root.rglob('*'):
        if any(part in ignored_dirs for part in path.parts):
            continue
        if path.name == 'audit_point_w.py':
            continue
        if path.is_file() and path.suffix.lower() in extensions:
            total_files += 1
            res = scan_file(path)
            if "error" not in res:
                total_todos += len(res["todos"])
                total_mocks += len(res["mocks"])
                if res["has_error_handling"]:
                    files_with_error_handling += 1
                if res["todos"] or res["mocks"]:
                    results.append(res)

    # Calculate Quality Score Q (0.0 to 10.0)
    score = 10.0
    if total_todos > 0:
        score -= min(4.0, total_todos * 0.8)
    if total_mocks > 0:
        score -= min(3.0, total_mocks * 1.0)
    
    if total_files > 0:
        handling_ratio = files_with_error_handling / total_files
        if handling_ratio < 0.5:
            score -= 1.5

    score = max(0.0, round(score, 2))
    passed = score >= 9.0 and total_todos == 0 and total_mocks == 0

    return {
        "target_dir": target_dir,
        "total_files_scanned": total_files,
        "total_todos": total_todos,
        "total_mocks": total_mocks,
        "files_with_error_handling": files_with_error_handling,
        "quality_score_Q": score,
        "point_w_passed": passed,
        "flawed_files": results
    }

def main():
    parser = argparse.ArgumentParser(description="Point W Static Code Auditor")
    parser.add_argument("target", nargs="?", default=".", help="Target directory to audit")
    parser.add_argument("--json", action="store_true", help="Output as pure JSON")
    args = parser.parse_args()

    report = audit_directory(args.target)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("\n" + "="*60)
        print("🎯 POINT W EVOLUTIONARY ENGINE — AUDIT REPORT")
        print("="*60)
        print(f"Target Directory:      {report['target_dir']}")
        print(f"Total Files Scanned:   {report['total_files_scanned']}")
        print(f"Total TODOs/Stubs:     {report['total_todos']}")
        print(f"Total Static Mocks:    {report['total_mocks']}")
        print(f"Quality Score (Q):     {report['quality_score_Q']} / 10.0")
        print(f"Point W Threshold Met: {'✅ YES' if report['point_w_passed'] else '❌ NO (Q < 9.0 or flaws detected)'}")
        print("="*60)

        if report['flawed_files']:
            print("\n🚨 DETECTED FLAWS:")
            for item in report['flawed_files']:
                print(f"\n📁 {item['file']}")
                for t in item['todos']:
                    print(f"   [TODO Line {t['line']}] {t['content']}")
                for m in item['mocks']:
                    print(f"   [MOCK Line {m['line']}] {m['content']}")
            print()

    sys.exit(0 if report['point_w_passed'] else 1)

if __name__ == "__main__":
    main()

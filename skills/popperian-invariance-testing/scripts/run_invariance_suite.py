#!/usr/bin/env python3
"""
Popperian Invariance Testing — Metamorphic Invariance Runner
Executes metamorphic transformations across Scale, Temporal, Regime, and Boundary dimensions.
Emits Popperian Falsification Verdict (VERDICT::NOT_FALSIFIED / STRONGLY_FALSIFIED / FATALLY_FALSIFIED).
"""

import sys
import json
import argparse
import subprocess
from typing import List, Dict

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception as _enc_err:
        sys.stderr.write(f"Encoding config notice: {_enc_err}\n")

def run_test_command(command: str, timeout_sec: int = 30):
    try:
        res = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        return {
            "command": command,
            "exit_code": res.returncode,
            "stdout": res.stdout[:500],
            "stderr": res.stderr[:500],
            "success": res.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            "command": command,
            "exit_code": -1,
            "stdout": "",
            "stderr": f"Timeout after {timeout_sec}s",
            "success": False
        }
    except Exception as e:
        return {
            "command": command,
            "exit_code": -2,
            "stdout": "",
            "stderr": str(e),
            "success": False
        }

def run_invariance_suite(suite_config: Dict):
    tests = suite_config.get("tests", [])
    results = []
    failed_tests = []

    for test in tests:
        name = test.get("name", "Unnamed Invariance Test")
        cmd = test.get("command")
        if not cmd:
            continue
        
        exec_res = run_test_command(cmd)
        exec_res["name"] = name
        exec_res["invariant_type"] = test.get("type", "General")
        results.append(exec_res)

        if not exec_res["success"]:
            failed_tests.append(exec_res)

    all_passed = len(failed_tests) == 0
    verdict = "VERDICT::NOT_FALSIFIED" if all_passed else "VERDICT::STRONGLY_FALSIFIED"

    return {
        "verdict": verdict,
        "total_tests": len(results),
        "passed_tests": len(results) - len(failed_tests),
        "failed_tests_count": len(failed_tests),
        "results": results
    }

def main():
    parser = argparse.ArgumentParser(description="Popperian Invariance Testing Runner")
    parser.add_argument("--config", help="JSON config file defining invariance test commands")
    parser.add_argument("--test-cmd", help="Single test runner command to execute")
    args = parser.parse_args()

    if args.test_cmd:
        res = run_test_command(args.test_cmd)
        print(json.dumps(res, indent=2))
        sys.exit(0 if res["success"] else 1)

    if args.config:
        with open(args.config, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        report = run_invariance_suite(cfg)
        print(json.dumps(report, indent=2))
        sys.exit(0 if report["verdict"] == "VERDICT::NOT_FALSIFIED" else 1)

    print("Popperian Invariance Suite Runner ready. Specify --config or --test-cmd.")
    sys.exit(0)

if __name__ == "__main__":
    main()

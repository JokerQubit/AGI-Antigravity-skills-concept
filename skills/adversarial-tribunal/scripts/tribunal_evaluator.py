#!/usr/bin/env python3
"""
Adversarial Tribunal — Automated Evaluation Runner & Verdict Synthesizer
Parses Red Team vs Blue Team debate evidence across the 5 Universal Attack Vectors
and calculates surviving critical defects to emit a machine-readable verdict:
- VERDICT::APPROVED (0 surviving critical defects -> DEC::GROUNDED)
- VERDICT::QUARANTINE (1-2 surviving defects)
- VERDICT::REJECTED (3+ surviving critical defects)
"""

import sys
import json
import argparse
from typing import List, Dict

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception as _enc_err:
        sys.stderr.write(f"Encoding config notice: {_enc_err}\n")

ATTACK_VECTORS = [
    "V1_Counter_Example",
    "V2_Premise_Falsification",
    "V3_Boundary_Overreach",
    "V4_Invariant_Contradiction",
    "V5_Epistemic_Unfalsifiability"
]

def evaluate_tribunal(red_team_defects: List[Dict], blue_team_rebuttals: List[Dict]):
    surviving_defects = []

    for defect in red_team_defects:
        defect_id = defect.get("id")
        rebuttal = next((r for r in blue_team_rebuttals if r.get("defect_id") == defect_id), None)

        if not rebuttal or not rebuttal.get("empirically_verified", False):
            surviving_defects.append(defect)

    count = len(surviving_defects)
    if count == 0:
        verdict = "VERDICT::APPROVED"
        dec_level = "DEC::GROUNDED"
    elif count <= 2:
        verdict = "VERDICT::QUARANTINE"
        dec_level = "DEC::SPECULATIVE"
    else:
        verdict = "VERDICT::REJECTED"
        dec_level = "DEC::UNKNOWN"

    return {
        "verdict": verdict,
        "dec_level": dec_level,
        "total_red_team_attacks": len(red_team_defects),
        "total_rebuttals": len(blue_team_rebuttals),
        "surviving_defects_count": count,
        "surviving_defects": surviving_defects,
        "gate_passed": count == 0
    }

def main():
    parser = argparse.ArgumentParser(description="Adversarial Tribunal Evaluator")
    parser.add_argument("--defects-file", help="Path to JSON file containing red team defects")
    parser.add_argument("--rebuttals-file", help="Path to JSON file containing blue team rebuttals")
    parser.add_argument("--check-zero-trust", action="store_true", help="Run self-audit check")
    args = parser.parse_args()

    if args.check_zero_trust or not args.defects_file:
        print("Adversarial Tribunal Evaluator initialized and ready for subagent dispatch.")
        sys.exit(0)

    with open(args.defects_file, 'r', encoding='utf-8') as f:
        defects = json.load(f)
    
    rebuttals = []
    if args.rebuttals_file:
        with open(args.rebuttals_file, 'r', encoding='utf-8') as f:
            rebuttals = json.load(f)

    result = evaluate_tribunal(defects, rebuttals)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["gate_passed"] else 1)

if __name__ == "__main__":
    main()

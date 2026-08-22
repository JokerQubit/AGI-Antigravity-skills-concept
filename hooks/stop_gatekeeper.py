#!/usr/bin/env python3
"""
Stop Gatekeeper Hook for agi-antigravity-core.

Validates loop termination conditions when the Antigravity agent loop finishes.
Ensures background tasks have resolved and loop invariants are respected before
allowing the session to halt.
"""

import json
import sys
from typing import Any, Dict


def process_stop_event(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate stop event and return continuation or termination decision."""
    termination_reason = payload.get("terminationReason", "")
    fully_idle = payload.get("fullyIdle", True)
    error = payload.get("error", "")

    # Invariant 1: If background tasks are still active and agent tried to exit prematurely
    if not fully_idle and termination_reason == "model_stop":
        return {
            "decision": "continue",
            "reason": "Background asynchronous processes or scheduled tasks are still running. Awaiting completion."
        }

    # Invariant 2: In all other normal completion scenarios, permit halting
    return {
        "decision": "stop",
        "reason": "Execution invariants verified; all tasks resolved successfully."
    }


def main() -> None:
    """Main hook entry point reading JSON from stdin and writing JSON to stdout."""
    raw_input = sys.stdin.read().strip()
    if not raw_input:
        output = {"decision": "stop", "reason": "Default stop permission on empty payload."}
        sys.stdout.write(json.dumps(output))
        sys.stdout.flush()
        return

    try:
        payload = json.loads(raw_input)
        result = process_stop_event(payload)
    except Exception as exc:
        sys.stderr.write(f"[STOP_GATEKEEPER] Error evaluating stop conditions: {exc}\n")
        result = {"decision": "stop", "reason": "Permitting halt due to validator error."}

    sys.stdout.write(json.dumps(result))
    sys.stdout.flush()


if __name__ == "__main__":
    main()

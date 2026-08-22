#!/usr/bin/env python3
"""
Master Plugin Verification Test Runner for agi-antigravity-core.
Executes all 7 static & dynamic verification test suites, outputs color-coded diagnostics,
and strictly enforces exit code 0 for 100% pass rate (or exit code 1 on any failure).

Usage:
    python test_plugin.py
    python test_plugin.py --fail-fast
    python test_plugin.py --suite manifest
    python test_plugin.py --help
"""

import argparse
import os
import sys
import time
import unittest
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Ensure plugin root and tests dir are in sys.path
PLUGIN_ROOT = Path(__file__).resolve().parent
TESTS_DIR = PLUGIN_ROOT / "tests"

if str(PLUGIN_ROOT) not in sys.path:
    sys.path.insert(0, str(PLUGIN_ROOT))
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

# ANSI Color codes for beautiful terminal reporting
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


def colorize(text: str, color: str) -> str:
    # Check if stdout supports ANSI colors (or on Windows 10+)
    if sys.platform == "win32":
        # Enable ANSI virtual terminal processing on Windows if possible
        os.system("")
    return f"{color}{text}{Colors.RESET}"


# Suite metadata registry
SUITES_REGISTRY = [
    {
        "id": "manifest",
        "name": "1. Manifests, MCP & Hooks Schemas",
        "module": "test_manifest",
        "class": "TestManifestsAndSchemas",
        "tier": "Tier 1: Manifests & Configs",
    },
    {
        "id": "skills",
        "name": "2. Skills Frontmatter & Schemas",
        "module": "test_skills_frontmatter",
        "class": "TestSkillsFrontmatter",
        "tier": "Tier 2: Skills Frontmatter",
    },
    {
        "id": "links",
        "name": "3. Markdown Link Resolution",
        "module": "test_markdown_links",
        "class": "TestMarkdownLinks",
        "tier": "Tier 3: Markdown & Hygiene",
    },
    {
        "id": "placeholders",
        "name": "4. Zero Placeholders & Stubs",
        "module": "test_zero_placeholders",
        "class": "TestZeroPlaceholders",
        "tier": "Tier 3: Markdown & Hygiene",
    },
    {
        "id": "tools",
        "name": "5. Anti-Hallucination Tool Registry",
        "module": "test_tool_bindings",
        "class": "TestToolBindings",
        "tier": "Tier 4: Tool Bindings & Hooks",
    },
    {
        "id": "hooks",
        "name": "6. Lifecycle Hooks Contract",
        "module": "test_hooks_contract",
        "class": "TestHooksContract",
        "tier": "Tier 4: Tool Bindings & Hooks",
    },
    {
        "id": "dry_run",
        "name": "7. 5-Phase Autonomous Dry Run",
        "module": "test_autonomous_dry_run",
        "class": "TestAutonomousDryRun",
        "tier": "Tier 5: Autonomous Cycle",
    },
]


def print_banner():
    banner = f"""
{Colors.BOLD}{Colors.CYAN}================================================================================
          AGI-ANTIGRAVITY-CORE :: MASTER PLUGIN VERIFICATION HARNESS
================================================================================{Colors.RESET}
Plugin Path: {PLUGIN_ROOT}
Python:      {sys.version.split()[0]} ({sys.executable})
Date:        {time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())}
--------------------------------------------------------------------------------
"""
    print(banner)


def run_suite(suite_info: dict, failfast: bool = False, verbose: bool = False) -> Tuple[unittest.TestResult, float]:
    """Imports and executes a single test suite, returning TestResult and duration in seconds."""
    loader = unittest.TestLoader()
    try:
        mod = __import__(suite_info["module"])
        test_class = getattr(mod, suite_info["class"])
        suite = loader.loadTestsFromTestCase(test_class)
    except Exception as e:
        # Create synthetic failure result for import error
        class ImportErrorTestCase(unittest.TestCase):
            def test_import_suite(self):
                self.fail(f"Failed to import suite '{suite_info['module']}': {e}")

        suite = loader.loadTestsFromTestCase(ImportErrorTestCase)

    runner = unittest.TextTestRunner(
        verbosity=2 if verbose else 0,
        failfast=failfast,
        stream=open(os.devnull, "w") if not verbose else sys.stdout,
    )

    start_time = time.time()
    result = runner.run(suite)
    duration = time.time() - start_time
    return result, duration


def main():
    parser = argparse.ArgumentParser(
        description="Standalone Automated Verification Runner for agi-antigravity-core"
    )
    parser.add_argument(
        "--fail-fast",
        "-f",
        action="store_true",
        help="Halt execution immediately on first test failure",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Print verbose test execution output",
    )
    parser.add_argument(
        "--suite",
        "-s",
        type=str,
        choices=[s["id"] for s in SUITES_REGISTRY],
        help="Run only a specific test suite by ID",
    )
    args = parser.parse_args()

    print_banner()

    suites_to_run = SUITES_REGISTRY
    if args.suite:
        suites_to_run = [s for s in SUITES_REGISTRY if s["id"] == args.suite]

    suite_results: List[Dict] = []
    all_passed = True
    total_tests_run = 0
    total_failures = 0
    total_errors = 0
    total_skipped = 0
    start_total_time = time.time()

    for idx, s in enumerate(suites_to_run, start=1):
        print(f"[{idx}/{len(suites_to_run)}] Running {s['name']} ({s['tier']})...", end="", flush=True)

        res, duration = run_suite(s, failfast=args.fail_fast, verbose=args.verbose)

        passed = res.wasSuccessful()
        total_tests_run += res.testsRun
        total_failures += len(res.failures)
        total_errors += len(res.errors)
        total_skipped += len(res.skipped)

        if not passed:
            all_passed = False

        status_str = (
            colorize("[PASS]", Colors.GREEN + Colors.BOLD)
            if passed
            else colorize("[FAIL]", Colors.RED + Colors.BOLD)
        )
        print(f" {status_str} ({res.testsRun} tests in {duration:.2f}s)")

        suite_results.append(
            {
                "info": s,
                "result": res,
                "duration": duration,
                "passed": passed,
            }
        )

        if args.fail_fast and not passed:
            print(colorize("\n[!] Execution stopped early due to --fail-fast", Colors.YELLOW))
            break

    total_duration = time.time() - start_total_time

    # Print Summary Table
    print(f"\n{Colors.BOLD}============================== VERIFICATION SUMMARY =============================={Colors.RESET}")
    print(f"+-----------------------------------------+-------+------+------+-------+----------+")
    print(f"| {Colors.BOLD}Suite Name{Colors.RESET}                              | {Colors.BOLD}Total{Colors.RESET} | {Colors.BOLD}Pass{Colors.RESET} | {Colors.BOLD}Fail{Colors.RESET} | {Colors.BOLD}Error{Colors.RESET} | {Colors.BOLD}Status{Colors.RESET}   |")
    print(f"+-----------------------------------------+-------+------+------+-------+----------+")

    for sr in suite_results:
        s = sr["info"]
        res = sr["result"]
        passed = sr["passed"]
        name_padded = s["name"][:39].ljust(39)
        total_str = str(res.testsRun).rjust(5)
        pass_count = res.testsRun - len(res.failures) - len(res.errors) - len(res.skipped)
        pass_str = str(pass_count).rjust(4)
        fail_str = str(len(res.failures)).rjust(4)
        err_str = str(len(res.errors)).rjust(5)
        stat = colorize("PASS", Colors.GREEN) if passed else colorize("FAIL", Colors.RED)

        print(f"| {name_padded} | {total_str} | {pass_str} | {fail_str} | {err_str} |   {stat}   |")

    print(f"+-----------------------------------------+-------+------+------+-------+----------+")
    print(
        f"Total Tests: {total_tests_run} | Passed: {total_tests_run - total_failures - total_errors - total_skipped} | Failed: {total_failures} | Errors: {total_errors} | Skipped: {total_skipped}"
    )
    print(f"Elapsed Time: {total_duration:.2f}s\n")

    # Print detailed failure reports if any failures or errors occurred
    if not all_passed:
        print(f"{Colors.BOLD}{Colors.RED}============================== FAILURE DIAGNOSTICS =============================={Colors.RESET}")
        for sr in suite_results:
            res = sr["result"]
            s = sr["info"]
            if res.failures:
                print(f"\n{Colors.BOLD}{Colors.RED}--- Failures in {s['name']} ---{Colors.RESET}")
                for test_case, trace in res.failures:
                    print(f"\n{Colors.YELLOW}[TEST]{Colors.RESET} {test_case}")
                    print(trace.strip())

            if res.errors:
                print(f"\n{Colors.BOLD}{Colors.RED}--- Errors in {s['name']} ---{Colors.RESET}")
                for test_case, trace in res.errors:
                    print(f"\n{Colors.YELLOW}[TEST]{Colors.RESET} {test_case}")
                    print(trace.strip())

        print(f"\n{Colors.BOLD}{Colors.RED}================================================================================{Colors.RESET}")
        print(colorize("[FAIL] VERIFICATION GATE FAILED (Exit Code 1)", Colors.RED + Colors.BOLD))
        sys.exit(1)
    else:
        print(f"{Colors.BOLD}{Colors.GREEN}================================================================================{Colors.RESET}")
        print(colorize("[SUCCESS] ALL VERIFICATION GATES PASSED (Exit Code 0)", Colors.GREEN + Colors.BOLD))
        sys.exit(0)


if __name__ == "__main__":
    main()

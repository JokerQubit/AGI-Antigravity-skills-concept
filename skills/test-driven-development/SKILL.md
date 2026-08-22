---
name: test-driven-development
description: Enforces strict Test-Driven Development (TDD) workflows using the Red-Green-Refactor cycle. Guides agents to write failing unit or integration tests before production code, implement minimal passing logic, and refactor cleanly with zero regressions.
---

# Test-Driven Development (TDD) Engine

> *"If a test has not been observed to fail deterministically before production logic is written, it cannot be trusted to prevent regressions."*

---

## 1. Overview & Core Philosophy

Test-Driven Development (TDD) is an uncompromising engineering discipline that inverts traditional development. In Test-Driven Development, tests are not an afterthought or verification post-mortem; they are the executable specification that drives software architecture.

This skill establishes the **Red-Green-Refactor** execution contract across all code authoring, bug fixing, and progressive disclosure skill creation within the Antigravity ecosystem.

For specialized test harnesses, mock isolation patterns, and assertion strategies, see the [TDD Patterns Reference](./references/tdd-patterns.md).

---

## 2. The 3-Phase Execution Contract

```
┌─────────────────────────────────────────────────────────────┐
│ 1. RED PHASE: Deterministic Failure Proof                   │
│    - Author unit/integration test capturing requirement     │
│    - Execute test runner -> Verify failure with exit != 0   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. GREEN PHASE: Minimal Functional Implementation           │
│    - Write simplest compliant code to satisfy the test      │
│    - Execute test runner -> Verify pass with exit == 0      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. REFACTOR PHASE: Quality & Architectural Hardening        │
│    - Eliminate duplication, enforce typing & docstrings     │
│    - Execute test runner -> Verify 100% pass, 0 regressions │
└─────────────────────────────────────────────────────────────┘
```

### Phase 1: Red (Deterministic Failure)
1. **Identify the Atomic Unit of Behavior:** Determine the smallest testable assertion required for the feature or bugfix.
2. **Author the Test First:** Create the test in the appropriate test suite (e.g., `tests/test_<module>.py`).
3. **Execute and Observe Failure:** Run the project test command (e.g. `run_command(CommandLine="python -m unittest tests/test_<module>.py", Cwd="...")`).
4. **Failure Assertion Rule:** The test must fail for the *expected reason* (e.g. `AssertionError` or `AttributeError` indicating missing functionality), not due to syntax errors or harness misconfiguration.

### Phase 2: Green (Minimal Implementation)
1. **Author the Minimal Code:** Write only the code required to make the failing test pass. Do not speculate on future features.
2. **Execute the Test Runner:** Run the test command again.
3. **Verify Green Status:** Ensure the test passes deterministically with exit code 0.

### Phase 3: Refactor (Cleanliness & Zero Regressions)
1. **Structural Improvement:** Clean variable names, extract duplicate logic, enforce type annotations, and ensure asymptotic performance bounds.
2. **Preserve External Behavior:** Do not alter the public API contract without updating corresponding interface tests.
3. **Re-Run Full Test Suite:** Execute the complete test suite to confirm zero regressions across dependent modules.

---

## 3. Skill-Level Test-Driven Development

TDD applies equally to the creation and modification of Antigravity progressive disclosure skills:

1. **Trigger Contract Test (Red):** Prior to writing `SKILL.md`, define the canonical user prompt intents that must trigger the skill and counter-examples that must NOT trigger it.
2. **Frontmatter Implementation (Green):** Author YAML frontmatter with precise `name` and third-person trigger `description`.
3. **Harness Audit (Refactor):** Run `test_skills_frontmatter.py` and `test_markdown_links.py` to confirm schema validity, link resolution, and zero placeholder policy compliance.

---

## 4. Strict Anti-Patterns & Prohibitions

| Prohibited Anti-Pattern | Correct TDD Protocol |
|---|---|
| Writing production code before tests | Author the test first and verify deterministic failure |
| Modifying test assertions to mask code bugs | Fix the underlying code; tests represent the authoritative requirement |
| Tests that always pass (vacuous assertions) | Every test must assert specific invariant values or state changes |
| Testing private implementation details | Test observable public contracts, inputs, outputs, and side effects |
| Skipping the Refactor phase | Always perform a refactoring pass once the test turns green |
| Hardcoding test return values | Implement real state and computational logic |

---

## 5. Concrete Polyglot Examples

### Example A: Python Standard Library Unit Test
```python
import unittest

class TestTokenBucketRateLimiter(unittest.TestCase):
    def test_consume_within_capacity_returns_true(self):
        limiter = TokenBucketRateLimiter(capacity=10, fill_rate_per_sec=1.0)
        self.assertTrue(limiter.consume(5))
        self.assertEqual(limiter.available_tokens, 5)

    def test_consume_exceeding_capacity_returns_false(self):
        limiter = TokenBucketRateLimiter(capacity=5, fill_rate_per_sec=1.0)
        self.assertFalse(limiter.consume(10))
        self.assertEqual(limiter.available_tokens, 5)

if __name__ == "__main__":
    unittest.main()
```

### Example B: Verification Flow
```
1. Run test: python -m unittest tests/test_rate_limiter.py -> [FAIL: NameError 'TokenBucketRateLimiter']
2. Implement class TokenBucketRateLimiter in rate_limiter.py
3. Run test: python -m unittest tests/test_rate_limiter.py -> [PASS: 2 tests in 0.002s]
4. Refactor: Add docstrings and type hints -> Re-run full test suite.
```

---

## 6. Diagnostic & Verification Checklist

Before completing any implementation task:
- [ ] Was every test observed in a failing state prior to code authoring?
- [ ] Does the implementation contain only minimal, clean, production logic without stubs?
- [ ] Have all unit and integration tests passed with exit code 0?
- [ ] Have all relative links in documentation been verified against disk?

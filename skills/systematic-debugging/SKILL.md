---
name: systematic-debugging
description: Executes a rigorous 4-phase root-cause debugging protocol (Reproduce, Isolate, Diagnose, Verify) for complex defects. Eliminates trial-and-error edits, enforces zero-guesswork instrumentation, and triggers escalation upon 3 consecutive failures.
---

# Systematic Root-Cause Debugging Protocol

> *"Trial-and-error code edits without empirical root-cause isolation create new bugs while failing to resolve existing defects."*

---

## 1. Overview & The Zero-Guessing Mandate

Systematic Debugging is the disciplined practice of diagnosing and repairing software defects through evidence-based hypothesis testing. Modifying code on a hunch or applying shotgun edits without proving the root cause is strictly prohibited.

Every bug investigation must follow the **4-Phase Protocol**:
1. **Reproduce:** Construct a minimal, deterministic reproduction case.
2. **Isolate:** Trace backward from symptom to corrupted state to root cause.
3. **Diagnose:** Formulate a falsifiable hypothesis and verify with instrumentation.
4. **Verify:** Apply an atomic fix and verify full regression suite pass.

For deep causal tracing patterns and invariant verification tables, consult the [Root-Cause Playbook](./references/root-cause-playbook.md).

---

## 2. The 4-Phase Protocol

```
┌─────────────────────────────────────────────────────────────┐
│ 1. REPRODUCE: Minimal Deterministic Script                  │
│    - Isolate failing input vector                           │
│    - Create standalone test script reproducing failure      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. ISOLATE: Backward Data-Flow Tracing                      │
│    - Trace: Symptom -> Corrupted State -> Origin Node       │
│    - Inject observational logging (Zero-Guesswork)          │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. DIAGNOSE: Hypothesis Falsification                       │
│    - Formulate single causal hypothesis                     │
│    - Prove state invariant failure mathematically/empirically│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. VERIFY: Atomic Fix & Regression Defense                  │
│    - Apply minimal atomic fix                               │
│    - Verify reproduction test passes + 100% full test suite │
└─────────────────────────────────────────────────────────────┘
```

### Phase 1: Reproduce
- **Deterministic Replication:** Never attempt to fix an issue that cannot be deterministically triggered.
- **Minimal Reproduction Harness:** Create a standalone test case or script that triggers the failure in isolation from unrelated application logic.
- **Record Baseline:** Document the exact failure output, stack trace, exit code, and environment parameters.

### Phase 2: Isolate
- **Backward Data-Flow Analysis:** Follow the dependency tree in reverse:
  $$\text{Observed Symptom} \longrightarrow \text{Corrupted Variable} \longrightarrow \text{Executing Function} \longrightarrow \text{Root Fault}$$
- **Zero-Guesswork Instrumentation:** Never assume a variable's runtime value, type, or encoding. Print or log the runtime state at critical boundaries.

### Phase 3: Diagnose
- **Single Falsifiable Hypothesis:** Formulate a concise hypothesis: *"Function X produces invalid state Y when input satisfies condition Z because invariant W is violated."*
- **Empirical Falsification:** Test the hypothesis with targeted assertions before changing business logic.

### Phase 4: Verify
- **Atomic Modification:** Apply the smallest complete edit that corrects the root cause. Do not combine the fix with unrelated cleanup.
- **Dual Verification:**
  1. Verify that the reproduction test now passes cleanly.
  2. Execute the entire project test suite (e.g. `run_command(CommandLine="python test_plugin.py", Cwd="...")`) to ensure zero regressions.

---

## 3. The 3-Failure Escalation Rule

If three consecutive attempted fixes fail to resolve the defect:
1. **Halt Immediate Edits:** Stop modifying code. Further ad-hoc edits indicate that the initial diagnostic model is fundamentally incorrect.
2. **Re-evaluate Architectural Assumptions:** The failure is systemic or architectural rather than an isolated typo.
3. **Escalate to Review:** Document the full hypothesis log, failed attempts, and observations in a structured handoff report or escalate to an architectural tribunal.

---

## 4. Diagnostic Anti-Patterns

| Anti-Pattern | Root Risk | Corrective Action |
|---|---|---|
| Shotgun Editing | Introduces latent regressions | Make one atomic change at a time |
| Symptom Masking | Hides bug while corrupting state downstream | Fix the origin node where invalid state is born |
| Assumption-Based Reasoning | Misidentifies root cause | Log and verify exact runtime values |
| Premature Resolution | Bug recurs under edge cases | Run boundary and stress tests |
| Test Deletion | Weakens safety net | Tests are specifications; never delete failing tests |

---

## 5. Structured Debugging Log Template

When conducting complex investigations, maintain a structured log:

```markdown
### Bug Investigation: [Issue Identifier]
- **Reproduction Command:** `python -m unittest tests/test_defect.py`
- **Observed Behavior:** Null pointer dereference in payload parser on line 142.
- **Expected Invariant:** Payload dictionary must contain non-empty metadata key.
- **Backward Trace:** `parser.py:142` <- `router.py:88` <- `gateway.py:34`
- **Root Cause:** Gateway omitted default metadata header when processing SSE streams.
- **Atomic Fix:** Initialize default metadata dictionary in `gateway.py:34`.
- **Verification:** Reproduction test passes; full suite 100% green.
```

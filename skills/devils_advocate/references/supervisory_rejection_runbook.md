# Departmental Runbook: Supervisory Rejection & Quality Enforcement Protocol (`ADVOCATE-RUN-01`)

## 1. Trigger Conditions
Mandatory execution whenever:
1. A sub-agent submits a task deliverable for acceptance or milestone sign-off.
2. A deliverable contains stubs, placeholders, deferred work, or vague generalizations.
3. An inter-agent payload fails contract schema verification or lacks unit test coverage.
4. Output quality fails to meet the *Via Deserti* / Holy Grail enterprise standard.

---

## 2. Step-by-Step Execution Protocol

### Step 1: Pre-Flight Completeness Scan
- Scan source code or documentation for satisficing violations:
  - Check for stubs, unfinished logic, or unhandled errors.
- If any violation is found, halt evaluation immediately and issue a **Critical Rejection**.

### Step 2: Algorithmic & Contractual Stress Test
- Check parameter boundaries, defensive validation, and concurrency safety.
- Verify that every requirement in the initial task specification was completely fulfilled.

### Step 3: Formulate Non-Acceptance Dossier
- Construct the structured rejection payload:
  1. **Defect Inventory**: List every failing function, missing test, or incomplete specification.
  2. **Forbidden Repeat Vector**: Explicitly declare which algorithms, shortcuts, or libraries failed and cannot be attempted again.
  3. **Remediation Acceptance Criteria**: Define the exact observable conditions required for passing.

### Step 4: Dispatch Redo Directive & Track Iteration
- Re-prompt the sub-agent with the Non-Acceptance Dossier.
- Enforce strategy mutation.
- Track round number:
  - Round 1-2: Normal supervisory revision loop.
  - Round 3: Final remediation attempt.
  - Round > 3: Trigger **Escalation Circuit-Breaker** to CEO.

### Step 5: Final Certification & Ledger Commit
- Once the sub-agent delivers a complete, verified artifact that satisfies all criteria, issue an unconditional `CERTIFICATION_APPROVED` and log to `.state/ledger/`.

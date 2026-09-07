---
trigger: always_on
description: Layer 8 Supervisory Non-Acceptance Gating, Devil's Advocate Quality Rejection Engine, and Gauntlet Builder-Critic Loop
---
# Layer 8: Supervisory Rejection Gate & Quality Escalation

This document establishes the operational cybernetics, protocols, and execution standards governing Layer 8 of the OmniCognition Labs 12-Layer Neural Chain. Layer 8 serves as the sovereign supervisory quality gatekeeper. It executes the Devil's Advocate non-acceptance protocol, enforces mandatory strategy mutations upon rejected work, conducts the Gauntlet builder-critic convergence loop, and blocks premature delivery until all physical invariants are certified.

---

## 1. Supervisory Non-Acceptance Doctrine & The Anti-Satisficing Barrier

### 1.1 The Quality Enforcement Problem
In multi-agent autonomous execution, sub-agents frequently succumb to satisficing—delivering work that meets superficial lexical requirements but contains subtle logical flaws, incomplete error handling, or performance bottlenecks. Without an adversarial supervisory gate, defects slip into downstream modules and pollute the project continuum.

Layer 8 enforces the **Deterministic Rejection Gate**:
> The supervisor gate inspects deliverables against strict unit tests, AST parsers, and the Zero-Stub Law. Any deliverable containing stubs, unhandled exceptions, or missing edge cases is rejected immediately. Passive acceptance is forbidden.

### 1.2 The Strategy Mutation Mandate
When a deliverable is rejected:
- The sub-agent is **STRICTLY FORBIDDEN from retrying the identical failing method**.
- Retrying an identical failed prompt, repeating a broken pattern, or re-running failing tests without code mutation is classified as an infinite-loop violation.
- Every rejection must dictate a mandatory strategy mutation that alters the algorithmic or architectural approach.

### 1.3 Strategy Mutation Taxonomy
When a sub-agent receives a rejection dossier, it must execute one of four formal mutations:
1. **Algorithmic Transformation**: Replace naive linear iteration with indexed binary lookup, hash mapping, or dynamic programming.
2. **Concurrency Decoupling**: Transition from shared mutable locking to lock-free channels, producer-consumer queues, or actor message passing.
3. **Data Structure Replacement**: Replace unbuffered arrays or generic maps with typed structs, ringbuffers, or radix trees.
4. **Error Channel Re-Architecture**: Replace silent fallbacks or unhandled catch blocks with explicit Result envelopes and transactional rollback journals.

---

## 2. The Devil's Advocate Protocol (`devils_advocate`)

### 2.1 Departmental Staff & Roles
1. **Chief Quality Controller & Devil's Advocate Lead (`SUP-ADV-01`)**:
   - Pedigree: Former Principal Software Quality Architect and Automated Formal Gating Engineer.
   - Mandate: Sovereign authority to reject deliverables, formulate Non-Acceptance Dossiers, and enforce strategy mutations.
2. **AST & Static Code Inspector (`SUP-AST-02`)**:
   - Mandate: Executes dynamic AST parsing, checks cyclomatic complexity, and verifies that zero empty catch blocks exist.
3. **Idempotency & Boundary Verifier (`SUP-IDEM-03`)**:
   - Mandate: Verifies cryptographic idempotency keys, retry backoff algorithms, and atomic persistence mechanics.

### 2.2 The Non-Acceptance Dossier Schema
Whenever work is rejected, `SUP-ADV-01` must formulate a formal Non-Acceptance Dossier specifying:
1. **Exact Defect Vectors**: Specific file paths, line numbers, and character-level defect evidence.
2. **Forbidden Repeat Patterns**: Explicitly documented approaches that the sub-agent is legally prohibited from repeating.
3. **Mandatory Remediation Criteria**: Concrete algorithmic or structural invariants that must be satisfied for certification.

Example Dossier:
```json
{
  "sub_agent": "EMP-CORE-102",
  "deliverable": "scripts/sync_state.ps1",
  "timestamp": "2026-09-06T21:30:00-03:00",
  "status": "in_supervisory_loop",
  "rounds": [
    {
      "round": 1,
      "verdict": "REJECTED_FOR_REVISION",
      "defects": [
        "AST Parse Warning: Empty catch block at line 42",
        "Zero-Stub Violation: TODO marker found at line 89"
      ],
      "forbidden_repeat_vector": "Do not submit unhandled catch blocks or placeholder comments.",
      "remediation_criteria": "Implement explicit error rethrow and replace TODO with complete logic."
    }
  ]
}
```

---

## 3. The Gauntlet Loop Protocol (`gauntlet_loop`)

### 3.1 Self-Evolving Builder-Critic Convergence
For high-stakes, mission-critical artifacts (core engines, security protocols, compiler pipelines), Layer 8 activates the Gauntlet Loop:
```
+-----------------------------------------------------------------------------------+
| ROUND INITIALIZATION: Load Base Artifact + Blind Industry Reference Benchmark    |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| ADVERSARIAL CRITIQUE: Independent Critic evaluates gaps vs. Frontier Benchmark   |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CONVERGENCE CHECK: Does quality score meet threshold ($Q \ge 0.95$)?             |
+-----------------------------------------------------------------------------------+
       |                                                               |
       | No (Score < 0.95)                                             | Yes (Score >= 0.95)
       v                                                               v
+---------------------------------------------+   +---------------------------------+
| STRATEGY MUTATION & BUILDER REDO             |   | CERTIFIED PRODUCTION RELEASE    |
| Mutate approach, harden code on disk         |   | Commit to ledger and release    |
+---------------------------------------------+   +---------------------------------+
```

### 3.2 Gauntlet Scoring Metric $Q(\text{artifact})$
The Gauntlet quality score $Q$ is computed across five weighted dimensions:
$$Q = 0.25 \cdot C_{\text{correctness}} + 0.25 \cdot C_{\text{zero\_stub}} + 0.20 \cdot C_{\text{resilience}} + 0.15 \cdot C_{\text{performance}} + 0.15 \cdot C_{\text{clean\_code}}$$
Where each coefficient $C_i \in [0.0, 1.0]$. An artifact must achieve $Q \ge 0.95$ across 3 consecutive rounds or reach full certification.

### 3.3 Multi-Round Gauntlet Convergence Protocol
1. **Round 1 (Blind Reference Teardown)**: Compare deliverable against best-in-class open-source or proprietary industry standard. Flag any missing functional capabilities or architectural corners cut.
2. **Round 2 (Stress & Adversarial Critique)**: Inject extreme inputs, high concurrency, and sudden aborts. Require builder to fortify failing branches.
3. **Round 3 (Final Convergence & Gating)**: Re-calculate $Q$. If $Q \ge 0.95$, certify deliverable and emit `.state/gauntlet_progress.json`. If $Q < 0.95$, escalate to Chief Quality Controller.

### 3.4 Specialist Dispatch Directives for SUP-AST-02 and SUP-IDEM-03
```
Prompt for SUP-AST-02:
"You are SUP-AST-02. You MUST inspect skills/devils_advocate/SKILL.md via view_file before proceeding.
Mandate: Execute dynamic AST parsing on target code files. Audit cyclomatic complexity, verify zero empty catch blocks, and prove zero stubs."

Prompt for SUP-IDEM-03:
"You are SUP-IDEM-03. You MUST inspect skills/devils_advocate/SKILL.md via view_file before proceeding.
Mandate: Audit idempotency keys, retry backoff logic, and atomic swap persistence mechanisms across target scripts."
```

---

## 4. Dynamic Devil's Advocate Engine (`scripts/run_devils_advocate.ps1`)

### 4.1 Real Disk Code Auditing
The Devil's Advocate script inspects physical code on disk:
- Inspects target file syntax and runs PowerShell / Python AST parsers.
- Scans for banned stubs and placeholders (`TODO`, `FIXME`, `pass`).
- Evaluates multi-round revision cycles, logging `SUPERVISORY_WORK_REJECTED` or `SUPERVISORY_WORK_CERTIFIED` to `.state/ledger/`.
- Saves structured report to `.state/devils_advocate_latest.json`.

### 4.2 Automated Supervisory Invocation
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_devils_advocate.ps1 -TargetDeliverable "<Path>" -SubAgentId "<ID>" -MaxRounds 3
```

---

## 5. Supervisory Escalation Hierarchy & Deadlock Resolution

### 5.1 Escalation Flow
If a sub-agent reaches 3 consecutive rejections ($r = 3$) without achieving certification:
1. **Supervisory Pause**: Execution immediately halts on the sub-agent task.
2. **Escalation to Layer 11 (Strategic Meeting)**: `SUP-ADV-01` submits the Non-Acceptance Dossier to Level 6 (CEO Dr. Vance) and the Strategic Meeting Engine (`scripts/run_strategic_meeting.ps1`).
3. **Radical Scope Restructuring**: The task is either re-assigned to a different senior specialist, partitioned into smaller atomic sub-tasks, or discarded as an unviable path.

---

## 6. Sub-Agent Dispatch Directives for SUP-ADV-01

```
Prompt for SUP-ADV-01:
"You are SUP-ADV-01. You MUST read skills/devils_advocate/SKILL.md via view_file before proceeding.
Adhere strictly to Layer 8 Supervisory Rejection standards.
Target Deliverable: '<TARGET_PATH>'
Inspect physical disk code via dynamic AST and Zero-Stub scanners.
If defects exist: emit Non-Acceptance Dossier with forbidden repeat patterns and mandate strategy mutation.
If clean: certify approval and log event to corporate ledger."
```

---

## 7. Layer 8 to Layer 9 Cognitive Handshake Contract

Before Layer 9 (Multi-Modal Creative Synthesis) or final delivery initiates:
1. Deliverable must achieve `CERTIFIED_APPROVED` status in `.state/devils_advocate_latest.json`.
2. All previous non-acceptance defects must be proven resolved on physical disk.
3. Gauntlet quality score $Q \ge 0.95$ verified.
4. Transaction `SUPERVISORY_WORK_CERTIFIED` recorded in `.state/ledger/`.

### 7.1 Supervisory Certification Checklist
- [ ] Physical file AST parsed with zero syntax errors.
- [ ] Zero-Stub Law confirmed: 0 stubs, 0 fixmes, 0 todos.
- [ ] Strategy mutation verified on all prior rejections.
- [ ] Automated tests executed on hardware and passed.
- [ ] Gauntlet score meets threshold ($Q \ge 0.95$).
- [ ] Audit report serialized to `.state/devils_advocate_latest.json` without UTF-8 BOM.
- [ ] Multi-round convergence logs committed to corporate ledger.

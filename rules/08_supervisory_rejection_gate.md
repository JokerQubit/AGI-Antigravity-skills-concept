---
trigger: always_on
description: Layer 8 Supervisory Rejection Gate, Devil's Advocate Protocol, Non-Acceptance Dossiers, and Gauntlet Convergence Loop
---
# Layer 8: Supervisory Rejection Gate & Quality Escalation

Layer 8 serves as the sovereign supervisory quality gatekeeper. It executes the Devil's Advocate non-acceptance protocol, enforces mandatory strategy mutations upon rejected work, conducts the Gauntlet builder-critic loop, and blocks premature delivery.

## 1. Supervisory Non-Acceptance & Strategy Mutations

Deterministic Rejection Gate: Deliverables containing stubs, unhandled exceptions, or missing edge cases are rejected immediately. Passive acceptance is forbidden.

Strategy Mutation Mandate:
- Retrying the identical failing method is STRICTLY FORBIDDEN.
- Repeating a failed prompt or re-running tests without code mutation is an infinite-loop violation.
- Every rejection dictates an explicit strategy mutation.

Strategy Mutation Taxonomy:
1. Algorithmic Transformation: Replace linear scan with binary search, hash index, or dynamic programming.
2. Concurrency Decoupling: Transition from shared locking to lock-free channels or actor message passing.
3. Data Structure Replacement: Replace raw arrays with typed ringbuffers, structs, or radix trees.
4. Error Channel Re-Architecture: Replace silent fallbacks with explicit Result envelopes and transactional rollback journals.

## 2. Department of Devil's Advocate (`devils_advocate`)

### 2.1 Departmental Staff
- `SUP-ADV-01` (Chief Quality Controller & Devil's Advocate Lead): Veto authority to reject deliverables and formulate Non-Acceptance Dossiers.
- `SUP-AST-02` (AST & Static Code Inspector): Parses ASTs, audits cyclomatic complexity, checks empty catch blocks.
- `SUP-IDEM-03` (Idempotency Verifier): Audits idempotency keys, retry backoff, and atomic persistence.

### 2.2 Non-Acceptance Dossier Schema (`.state/devils_advocate_latest.json`)
```json
{
  "sub_agent": "PROD-101",
  "deliverable": "scripts/sync_state.ps1",
  "timestamp": "2026-09-06T21:30:00-03:00",
  "status": "in_supervisory_loop",
  "rounds": [{
    "round": 1,
    "verdict": "REJECTED_FOR_REVISION",
    "defects": ["Empty catch block at line 42", "Zero-Stub violation at line 89"],
    "forbidden_repeat_vector": "Do not submit unhandled catch blocks or stubs.",
    "remediation_criteria": "Implement structured exception rethrow and complete logic."
  }]
}
```

## 3. Gauntlet Loop Protocol (`gauntlet_loop`)

Builder-Critic Convergence Loop:
```
Load Base Artifact + Blind Industry Benchmark
   v
Adversarial Critique by Independent Critic
   v
Convergence Check: Quality Score Q >= 0.95?
   |-- No  -> Strategy Mutation & Builder Redo
   +-- Yes -> Certified Production Release
```

Gauntlet Scoring Metric:
$$Q = 0.25 C_{\text{correct}} + 0.25 C_{\text{zero\_stub}} + 0.20 C_{\text{resilience}} + 0.15 C_{\text{perf}} + 0.15 C_{\text{clean}}$$
Threshold: $Q \ge 0.95$ across 3 consecutive rounds for certification.

Gauntlet Rounds:
1. Round 1 (Blind Reference Teardown): Compare against best-in-class open-source or proprietary standard.
2. Round 2 (Stress & Adversarial Critique): Inject extreme inputs, high concurrency, and aborts.
3. Round 3 (Final Convergence & Gating): Re-calculate $Q$. If $Q \ge 0.95$, certify release.

## 4. Dynamic Devil's Advocate Engine (`scripts/run_devils_advocate.ps1`)

Automated Execution:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_devils_advocate.ps1 -TargetDeliverable "<Path>" -SubAgentId "<ID>" -MaxRounds 3
```
Inspects real disk AST, checks stubs, logs `SUPERVISORY_WORK_REJECTED` or `SUPERVISORY_WORK_CERTIFIED` to `.state/ledger/`.

## 5. Supervisory Escalation Hierarchy

If a sub-agent reaches 3 consecutive rejections ($r = 3$):
1. Supervisory Pause: Execution halts on the sub-agent task.
2. Escalation to Layer 11: `SUP-ADV-01` submits dossier to Level 6 (CEO Dr. Vance) and the Strategic Meeting engine (`scripts/run_strategic_meeting.ps1`).
3. Radical Scope Restructuring: Re-assign task, partition into smaller atomic sub-tasks, or discard route.

## 6. Layer 8 to Layer 9 Cognitive Handshake Contract

Checklist:
- [ ] Deliverable status `CERTIFIED_APPROVED` in `.state/devils_advocate_latest.json`.
- [ ] All previous non-acceptance defects proven resolved on physical disk.
- [ ] Zero stubs, zero empty catch blocks, zero syntax errors confirmed.
- [ ] Strategy mutation verified on all prior rejections.
- [ ] Gauntlet quality score $Q \ge 0.95$ achieved.
- [ ] Transaction `SUPERVISORY_WORK_CERTIFIED` recorded in `.state/ledger/`.

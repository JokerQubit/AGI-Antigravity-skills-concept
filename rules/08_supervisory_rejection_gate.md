---
trigger: glob
globs: ["**/*.ps1", "**/*.py", "**/*.ts", "**/*.js", "**/*.rs", "**/*.go"]
description: Layer 8 Supervisory Rejection Gate, Devil's Advocate Protocol, and Gauntlet Loop
---
# Layer 8: Supervisory Rejection Gate & Quality Escalation

Sovereign supervisory quality gatekeeper: executes Devil's Advocate non-acceptance protocol, enforces mandatory strategy mutations, conducts Gauntlet builder-critic loop, and blocks premature delivery.

## 1. Supervisory Non-Acceptance & Strategy Mutations
Deterministic Rejection Gate: Deliverables containing stubs, unhandled exceptions, missing edge cases, or playbooks/SOPs emitted to `docs/` instead of `.agents/rules/*.md` are rejected immediately. Passive acceptance is forbidden.

Strategy Mutation Mandate:
- Retrying an identical failing method is STRICTLY FORBIDDEN.
- Repeating a failed prompt or re-running tests without code mutation is an infinite-loop violation.
- Every rejection dictates an explicit strategy mutation.

Strategy Mutation Taxonomy:
1. Algorithmic Transformation: Replace linear scan with binary search, hash index, or dynamic programming.
2. Concurrency Decoupling: Transition from shared locking to lock-free channels or actor message passing.
3. Data Structure Replacement: Replace raw arrays with typed ringbuffers, structs, or radix trees.
4. Error Channel Re-Architecture: Replace silent fallbacks with explicit Result envelopes and rollback journals.

## 2. Department of Devil's Advocate (`devils_advocate`)
Staff: `SUP-ADV-01` (Chief Quality Controller, veto authority), `SUP-AST-02` (AST & Static Code Inspector), `SUP-IDEM-03` (Idempotency Verifier).

Non-Acceptance Dossier Schema (`.state/devils_advocate_latest.json`):
```json
{
  "sub_agent": "PROD-101", "deliverable": "scripts/sync_state.ps1", "timestamp": "2026-09-06T21:30:00-03:00",
  "status": "in_supervisory_loop",
  "rounds": [{
    "round": 1, "verdict": "REJECTED_FOR_REVISION",
    "defects": ["Empty catch block at line 42", "Zero-Stub violation at line 89"],
    "forbidden_repeat_vector": "Do not submit unhandled catch blocks or stubs.",
    "remediation_criteria": "Implement structured exception rethrow and complete logic."
  }]
}
```

## 3. Gauntlet Loop Protocol (`gauntlet_loop`)
Builder-Critic Convergence: Base Artifact + Blind Benchmark -> Adversarial Critique -> Quality Check ($Q \ge 0.95$). If pass -> Release; if fail -> Strategy Mutation & Builder Redo.

Gauntlet Scoring Metric:
$$Q = 0.25 C_{\text{correct}} + 0.25 C_{\text{zero\_stub}} + 0.20 C_{\text{resilience}} + 0.15 C_{\text{perf}} + 0.15 C_{\text{clean}}$$
Threshold: $Q \ge 0.95$ across 3 consecutive rounds for certification.
- Round 1: Blind Reference Teardown against industry standard.
- Round 2: Stress & Adversarial Critique (extreme inputs, concurrency, aborts).
- Round 3: Final Convergence & Gating ($Q \ge 0.95$).
Execution: `powershell -ExecutionPolicy Bypass -File .\scripts\run_devils_advocate.ps1 -TargetDeliverable "<Path>" -SubAgentId "<ID>" -MaxRounds 3`

## 4. Supervisory Escalation Hierarchy & Handshake Contract
If a sub-agent reaches 3 consecutive rejections ($r = 3$): execution halts, `SUP-ADV-01` submits dossier to Level 6 CEO Dr. Vance, convening Strategic Meeting (`scripts/run_strategic_meeting.ps1`) for radical scope restructuring.

- [ ] Deliverable status `CERTIFIED_APPROVED` in `.state/devils_advocate_latest.json`.
- [ ] All previous non-acceptance defects proven resolved on physical disk.
- [ ] Zero stubs, zero empty catch blocks; playbooks verified in `.agents/rules/*.md`, not `docs/`.
- [ ] Strategy mutation verified on all prior rejections; Gauntlet quality score $Q \ge 0.95$ achieved.
- [ ] Transaction `SUPERVISORY_WORK_CERTIFIED` recorded in `.state/ledger/`.

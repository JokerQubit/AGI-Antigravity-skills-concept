---
trigger: always_on
description: The Devil's Advocate Mutual Accountability, Supervisory Rejection & Strategy Mutation Engine
---
# The "Devil's Advocate" System: Mutual Accountability & Supervisory Rejection Protocol

**Document Revision**: 1.0.0  
**Classification**: Non-Negotiable Operational Quality & Supervisory Governance Rule  
**Codename**: *Advocatus Diaboli* (The Devil's Advocate Protocol)  
**Scope**: CEO-to-Sub-Agent, Manager-to-Employee, and Sub-Agent-to-Sub-Agent Handshakes  

---

## 1. Executive Purpose & The Non-Acceptance Mandate

In standard multi-agent workflows, supervising agents often succumb to "rubber-stamping": accepting superficial, incomplete, or flawed outputs simply because a sub-agent returned a response, then pushing the broken artifact downstream.

In the **OmniCognition Labs Ecosystem**, we enforce the **Devil's Advocate System**:
- **The Non-Acceptance Invariant**: No deliverable that is poorly executed, unfinished, contains placeholder stubs, or fails to meet the *Via Deserti* gold standard may be accepted.
- **Mandatory Rejection & Strategy Mutation Loop**: Before accepting work and instructing a sub-agent to conclude or proceed, the supervising node (Supervisor, Department Manager, Peer Sub-Agent, or CEO) must rigorously challenge the deliverable. If deficiencies are found, the work is **rejected and returned for revision**.
- **The Non-Repetition Rule**: The re-prompted sub-agent is strictly forbidden from repeating previous mistakes or returning cosmetic rewrites. The sub-agent must mutate its strategy, fix all identified failure vectors, and deliver complete, production-grade operational logic.

---

## 2. Multi-Directional Mutual Accountability Topology

The Devil's Advocate quality gate operates at three critical organizational junctions:

```
[1. Vertical Supervisory Gate]      CEO / Department Manager  â”€â”€â–º Rejection & Redo Directive â”€â”€â–º Sub-Agent Specialist
[2. Deterministic AST/Code Gate]     Level 2 Supervisor        â”€â”€â–º Linter/Test Failure Vector â”€â”€â–º Level 1 Employee
[3. Lateral Peer Handshake Gate]     Receiving Sub-Agent       â”€â”€â–º Contract Breach Notice     â”€â”€â–º Dispatching Sub-Agent
```

1. **CEO / Manager $\to$ Sub-Agent**: When an employee submits a research dossier or architecture document that skims the surface or defers critical complexity, the Manager acts as Devil's Advocate, denying acceptance and forcing a deep rewrite.
2. **Supervisor $\to$ Employee Specialist**: The Level 2 Supervisor automatically inspects code deliverables against the Zero-Stub Invariant, static linters, and type boundaries, triggering an immediate redo loop upon any violation.
3. **Sub-Agent $\leftrightarrow$ Sub-Agent (Peer Handshake)**: When Department $A$ hands an artifact to Department $B$, the receiving sub-agent acts as Devil's Advocate, auditing the incoming contract. If incomplete, it rejects the payload back to Department $A$ rather than inheriting upstream technical debt.

---

## 3. The 4-Phase Rejection & Remediation Cycle

```
[1. Deliverable Submitted]
           â”‚
           â–¼
[2. Devil's Advocate Audit Gate]
           â”‚
           â”œâ”€â”€â–º Meets Frontier Standard? â”€â”€â–º [ACCEPTED & CERTIFIED] â”€â”€â–º Move to Next Milestone
           â”‚
           â””â”€â”€â–º Fails Expectations / Defective?
                      â”‚
                      â–¼
[3. Formulate Non-Acceptance Dossier]
   â”œâ”€â”€ Defect Inventory (exact lines, missing functions, stubs)
   â”œâ”€â”€ Forbidden Repeat Vector (failed methods that must NOT be repeated)
   â””â”€â”€ Remediation Acceptance Criteria
                      â”‚
                      â–¼
[4. Dispatch Redo Directive with Strategy Mutation]
                      â”‚
                      â–¼
[Loop back to Step 1 (Max 3 Rejection Iterations before Escalation)]
```

### 3.1 Contents of the Non-Acceptance Dossier
When rejecting work, the Devil's Advocate must never give vague feedback like *"improve this"*. The rejection payload must provide:
1. **Defect Inventory**: Precise file paths, line numbers, and functional mechanisms that failed.
2. **Forbidden Repeat Vectors**: A catalog of the failed patterns to prevent repetitive loops.
3. **Mandatory Remediation Contract**: Explicit conditions that must be fulfilled for sign-off.
4. **Remaining Attempt Budget**: Number of remaining attempts before supervisory escalation.

---

## 4. Operational Invariants

1. **No Premature Advancement**: An agent is strictly prohibited from moving to the next task or phase while its current deliverable sits in an uncertified or rejected state.
2. **Strategy Mutation Invariant**: Repeating the exact same prompt, tool call, or implementation approach that resulted in rejection constitutes an executive failure.
3. **Escalation Circuit-Breaker**: If a sub-agent fails to resolve defects after 3 consecutive Devil's Advocate rejections, the task is halted, flagged as `[CRITICAL EXECUTION BLOCKER]`, and escalated to the CEO for intervention.
4. **Ledger Immutability**: All rejections, failure dossiers, and eventual certifications are permanently recorded in `.state/ledger/`.


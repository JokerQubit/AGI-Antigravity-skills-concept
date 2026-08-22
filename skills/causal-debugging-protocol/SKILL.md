---
name: causal-debugging-protocol
description: Guides deep causal root-cause investigations using mathematical state tracing, invariant tree verification, and Popperian falsification. Maps failure paths backwards and enforces atomic bug isolation with zero guesswork.
---

# Causal Debugging & Mathematical Falsification Protocol

> *"A defect is an invariant violation. Isolating a defect requires proving which state transition violated the invariant, not guessing which line looks suspicious."*

---

## 1. Core Dogma: Zero-Guessing Causality

Under the **Causal Debugging Protocol**, no fix may be proposed or committed until the root cause has been mathematically isolated, mapped through a causal failure tree, and proven via observable instrumentation. Guess-and-check edits and speculative multi-file modifications are strictly prohibited.

For hypothesis falsification tables, state transition matrices, and invariant tree models, see the [Falsification Matrices Reference](./references/falsification-matrices.md).

---

## 2. The Backward Causal Failure Tree

Every defect investigation constructs a reverse dependency path from observable symptom to root cause:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. OBSERVED SYMPTOM (Crash / Assertion Failure / Bad I/O)   │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Why did this occur?)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. CORRUPTED VARIABLE / UNEXPECTED STATE VALUE              │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Where was this value assigned?)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. CALLING NODE / TRANSITION FUNCTION                       │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Why did the transition violate invariant?)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. MATHEMATICAL INVARIANT VIOLATION                         │
└──────────────────────────────┬──────────────────────────────┘
                               │ (What environmental or logical fault caused this?)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. ROOT CAUSE (The deterministic flaw)                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Mathematical State Tracing & Instrumentation

1. **State Formalization:** Express the expected behavior as a strict invariant $\mathcal{I}(S) \equiv \text{True}$.
2. **Boundary Logging:** Inject instrumentation at subsystem boundaries (I/O, IPC, database, scheduler) to measure exact variable states $S_0, S_1, \dots, S_n$.
3. **Transition Analysis:** Determine the exact index $k$ such that:
   $$\mathcal{I}(S_{k-1}) = \text{True} \quad \land \quad \mathcal{I}(S_k) = \text{False}$$
4. **Origin Node Proof:** The function executing transition $S_{k-1} \to S_k$ contains either the flawed logic or failed to validate invalid preconditions from its caller.

---

## 4. Popperian Falsification (Atomic Fix Protocol)

- **Single-Vector Modification:** A proposed fix must modify only the atomic causal node identified in the trace. Modifying multiple decoupled functions simultaneously invalidates scientific causality.
- **Hypothesis Falsification:** Formulate the fix as a falsifiable assertion:
  $$\mathcal{H}_0: \text{Fix } F \text{ restores } \mathcal{I}(S_k) = \text{True without altering } \mathcal{I}(S_j) \text{ for } j \neq k$$
- **The 3-Failure Escalation Limit:** If 3 consecutive atomic fixes fail to restore invariant satisfaction, the defect is structural. Halt debugging immediately and escalate to an architectural tribunal.

---

## 5. Environment Parity Audit Protocol

When investigating discrepancies between local testing, CI pipelines, and production environments:

1. **Temporal & Scale Ingestion:** Verify whether timeframes (e.g. 50ms tick vs 1s batch) alter state accumulation.
2. **Recursive Accumulator Decay:** Verify that recursive filters, decay factors, and caches are not poisoned by repeated calls.
3. **Execution Loop Isomorphism:** Verify that asynchronous dispatch loops in simulation are identical in structure to production runtimes.
4. **Resource & Permission Constraints:** Isolate file handle limits, memory quotas, and execution privileges across environments.

# Falsification Matrices, Invariant Trees & Causal Verification

This reference outlines formal techniques for modeling software invariants, hypothesis falsification matrices, and causal failure analysis.

---

## 1. Invariant Tree Modeling

An invariant tree represents the hierarchical set of assertions that must hold across all execution states of an application component.

### 1.1 Root Invariants vs Operational Invariants
- **Root Invariants ($\mathcal{I}_{\text{root}}$):** High-level safety properties (e.g. "No unauthenticated request can mutate user state", "Memory allocation is strictly bounded by $M_{\max}$").
- **Node Invariants ($\mathcal{I}_{\text{node}}$):** Local component preconditions and postconditions (e.g. `len(buffer) <= capacity`, `status in ValidStatuses`).

### 1.2 State Transition Matrix Verification
Given state vector $S = (x_1, x_2, \dots, x_m)$ and transition function $T(S, e) \to S'$:

$$\begin{array}{|c|c|c|c|c|}
\hline
\text{Initial State } S & \text{Event } e & \text{Expected State } S' & \text{Precondition } \mathcal{P}(S) & \text{Postcondition } \mathcal{Q}(S') \\
\hline
S_{\text{idle}} & \text{START} & S_{\text{running}} & \text{lock} = \text{False} & \text{task\_id} \neq \text{None} \\
S_{\text{running}} & \text{COMPLETE} & S_{\text{finished}} & \text{task\_id} \neq \text{None} & \text{exit\_code} \in \{0, 1\} \\
S_{\text{running}} & \text{ERROR} & S_{\text{failed}} & \text{error} \neq \text{None} & \text{trace} \neq \text{None} \\
\hline
\end{array}$$

---

## 2. Hypothesis Falsification Matrix

When diagnosing non-trivial defects, tabulate competing causal hypotheses:

| Hypothesis ID | Proposed Root Cause | Necessary Observable Condition | Test Command | Outcome (Confirmed / Falsified) |
|---|---|---|---|---|
| $\mathcal{H}_1$ | Character encoding mismatch in file reader | `content.decode('utf-8')` raises `UnicodeDecodeError` | `python -m unittest tests/test_encoding.py` | Falsified (file is ASCII-clean) |
| $\mathcal{H}_2$ | Off-by-one error in buffer slicing | Slice length is $L+1$ on boundary condition $k=0$ | `python -m unittest tests/test_buffer.py` | Confirmed (length was 101 instead of 100) |
| $\mathcal{H}_3$ | Race condition in parallel task dispatch | Intermittent lock contention on shared resource | `python -m unittest tests/test_concurrency.py` | Falsified (synchronous execution) |

---

## 3. Causal Verification Matrix

Before concluding any debugging session, document the verification matrix:

1. **Reproduction Proof:** Standalone reproduction script reliably triggers invariant violation on unpatched code.
2. **Atomic Fix Verification:** Single patch resolves the reproduction script without modifying unrelated code paths.
3. **Regression Proof:** 100% of existing unit and integration test suites pass with exit code 0.
4. **Side-Effect Audit:** Resource utilization, memory footprint, and latency profile remain within baseline bounds.

---
name: structured-reasoning-engine
description: MANDATORY. Use when facing architectural choices with 2+ alternatives, complex trade-offs, formal mathematical proofs, or deep multi-branch reasoning (Graph-of-Thought).
---

# SKILL: Structured Reasoning Engine — Multi-Branch Formal Synthesis

> *"Linear reasoning is a fragile chain; AGI reasoning is a self-healing proof graph."*

---

## I. GRAPH-OF-THOUGHT (GoT) REASONING PARADIGM

Non-trivial reasoning ($N \ge 3$ causal links or structural mutations) MUST NOT proceed as a single unbranched narrative. It must be structured as a directed acyclic graph $G = (V, E)$, where each vertex $v \in V$ represents an atomic logical proposition and each edge $e \in E$ represents a formal inference step.

```
       [v0: Sensing / World State]
                /          \
     [v1: Hypothesis A]  [v2: Hypothesis B]
            /      \            |
     [v3: Proof] [v4: Fail]  [v5: Proof]
          \                    /
       [v6: Optimal Synthesized Solution]
```

---

## II. THE 5 ATOMIC PHASES OF FORMAL COGNITION

### Phase S — State Sensing & Substrate Grounding
- Retrieve ground-truth system state directly via deterministic tools (read files, execute environment checks). Zero reliance on unverified context memory.
- Compute state hash $H(S_0)$ to lock the baseline environment state.

### Phase R — Rigorous Formal Proving (Atomic Graph Construction)
- Decompose reasoning into discrete atomic operations: $v_i \xrightarrow{op_k} v_{i+1}$.
- Assign an explicit Epistemic Label $\text{DEC}(v_i)$ to each node.
- Compute weakest-link path confidence:

$$\text{DEC}_{\text{path}} = \min_{v \in \text{path}} \text{DEC}(v)$$

- Reject any path where $\text{DEC}_{\text{path}} = \text{SPECULATIVE}$ for production-critical actions.

### Phase P — Algorithmic Planning & Regression Space Definition
- Construct a deterministic execution DAG detailing exact mutations: $\text{Create}(f), \text{Modify}(f, \Delta), \text{Delete}(f)$.
- Compute the explicit **Regression Footprint** $\mathcal{R}_{\text{scope}}$: identify all dependent modules, interfaces, and invariant constraints.

### Phase E — Single-Mutation Execution Cycle
- Execute exactly one atomic mutation at a time.
- Immediately evaluate intermediate state invariants after each mutation step. If an invariant breaks, halt and rollback to $H(S_0)$.

### Phase V — Verification & Invariance Testing
- Execute formal verification suite: Unit Tests, Property-Based Falsification, Property Invariance, and Static Code Analysis Gates.
- Require zero-exit-code empirical confirmation before declaring path success.

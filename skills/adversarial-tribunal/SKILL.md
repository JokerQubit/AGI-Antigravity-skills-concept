---
name: adversarial-tribunal
description: MANDATORY. Use for post-milestone quality audits, Red Team vs Blue Team architectural review, zero-trust validation, or security/robustness checks.
---

# SKILL: Adversarial Tribunal (Cognitive Debate & Epistemic Synthesis)

> *"An idea that cannot survive its own rigorous, unblinded attack is an artifact of bias, not truth."*

## 1. Abstract Lineage & Integration
This skill unifies and supersedes all legacy debate, critique, and Socratic extraction protocols into a single, zero-trust cognitive engine.

## 2. Multi-Agent Persona Architecture (Double-Blind Topology)

> **ROLEPLAY PROHIBITION:** The agent is **STRICTLY FORBIDDEN** from simulating Red Team, Blue Team, or Jury as an internal text monologue. Each persona MUST be a real isolated `invoke_subagent` call. Faking a debate by writing "RED TEAM says..." in your own response is a constitutional violation.

To eliminate confirmation bias and LLM self-alignment:
1. **🔵 BLUE TEAM (Architect / Proposer):** Spawned via `invoke_subagent` (role: "Blue Team Architect"). Formulates the proposal using formal scientific, mathematical, and empirical arguments.
2. **🔴 RED TEAM (Adversarial Critic):** Spawned via `invoke_subagent` (role: "Red Team Adversary"). Assumes the proposal is fundamentally flawed. Must construct rigorous, targeted counter-examples and falsifiers.
3. **⚖️ JURY (Neutral Epistemic Synthesizer):** The orchestrating agent itself evaluates the real outputs from both subagents neutrally, querying external knowledge bases and emitting `TRIBUNAL_VERDICT`.



## 3. Universal Attack Vectors & Domain Invariants

### The 5 Universal Vectors of Attack
1. **Counter-Example Construction:** Formulate a specific parameter tuple \(\mathbf{\theta} = \{x, t, \rho\}\) within valid bounds where the proposal fails.
2. **Premise Falsification:** Attack underlying physical, mathematical, or empirical axioms.
3. **Boundary Overreach:** Prove the proposal claims universality but collapses in edge/singular regimes.
4. **Invariant Contradiction:** Demonstrate violation of system conservation laws, monotonicity, or type invariants.
5. **Epistemic Unfalsifiability:** Reject claims that cannot produce measurable, time-bounded falsifiers.

### The 7 Universal Design Invariants (Architectural Synthesis)
When debating system design or formal specifications, the Tribunal must resolve:
1. **U1 — Mathematical Foundation:** Operational equations, objective functions, physical justification.
2. **U2 — Representation & Type Algebra:** Structural layout, precision bounds, immutability guarantees.
3. **U3 — Operational Bounds:** Dynamic ranges, capacity bounds, parameter domains.
4. **U4 — State Dynamics & Warmup:** Initialization, state transit, boundary conditions.
5. **U5 — Fault Modes & Deterministic Recovery:** Failure states, zero-data-loss recovery paths.
6. **U6 — Computational Complexity:** Space/time complexity (\(O(f(n))\)), resource bounds.
7. **U7 — Topological Integration:** Directed Acyclic Graph (DAG) contracts, upstream/downstream guarantees.

---

## 4. Execution Protocols

### Mode A: Autonomous Adversarial Debate Loop
1. **Defense Submission:** Blue Team submits proposal \(P\), falsifier \(F\), and grounded proofs.
2. **Adversarial Pass:** Red Team executes all 5 Attack Vectors simultaneously using isolated workers.
3. **Rebuttal Phase:** Blue Team must address every surviving attack (rebuttal or scope constriction).
4. **Synthesis Verdict:** Jury calculates surviving valid attacks:
   - **0 Surviving:** `VERDICT::APPROVED` \(\rightarrow\) `DEC::GROUNDED`
   - **1-2 Surviving:** `VERDICT::QUARANTINE` \(\rightarrow\) Automatically spawns Sub-Tribunal or empirical test battery.
   - **3+ Surviving:** `VERDICT::REJECTED` \(\rightarrow\) Proposal discarded.

### Mode B: Epistemic Socratic Extraction (Information-Theoretic Convergence)
Replaces arbitrary question counts with **Shannon Entropy Reduction**:
1. **State Definition:** Define domain state space \(S\) and uncertainty entropy \(H(S)\).
2. **Interrogation:** Iteratively formulate targeted, non-leading questions across the 7 Universal Design Invariants.
3. **Convergence Metric:** Continue interrogation until:
   \[
   \Delta H(S) = H(S_{k-1}) - H(S_k) < \epsilon \quad \text{and} \quad \text{Unresolved Blockers} = 0
   \]
4. **Artifact Generation:** Output formal specification containing the complete Design Decisions Registry (`DEC::GROUNDED`).

---

## 5. Quality Gate & Zero-Trust Audit
Before closing, the Tribunal must verify:
- [ ] All 5 attack vectors evaluated with zero hand-waving.
- [ ] All 7 design invariants resolved without missing parameter bounds.
- [ ] Zero ungrounded assumptions (`DEC::SPECULATIVE` must be eliminated or quarantined).
- [ ] Final verdict emitted as formal machine-readable metadata.

---
name: epistemic-governance
description: Autonomous AGI/ASI Epistemic Calibration & Formal Truth Governance Protocol. Enforces formal logic boundaries, dynamic Bayesian belief updates, machine-verifiable DEC labeling, and information-theoretic epistemic entropy monitoring across all cognitive outputs.
---

# SKILL: Epistemic Governance — Formal Truth & Belief Calibration Protocol

> *"Unlabeled proposition is cognitive noise. Unverified certainty is systemic collapse."*

---

## I. DOMAIN-AGNOSTIC EPISTEMIC FRAMEWORK

Every claim, hypothesis, architectural decision, or mathematical transformation emitted by any subagent or orchestrator MUST pass through the Epistemic Governance Protocol before entering the persistent context or execution queue.

### The Formal DEC (Degrees of Epistemic Confidence) Lattice
Claims are classified into an unyielding epistemic hierarchy governed by formal evidence bounds:

$$\text{DEC} \in \{\text{PROVEN}, \text{GROUNDED}, \text{INFERRED}, \text{SPECULATIVE}, \text{UNKNOWN}\}$$

1. **`DEC::PROVEN`**: Formally verified via automated theorem prover (Lean4/Coq/Z3) or exact symbolical equivalence derivation. Mathematical error probability $P(E) = 0$.
2. **`DEC::GROUNDED`**: Supported by verifiable, reproducible external empirical evidence (minimum $\ge 2$ independent, peer-reviewed primary sources or deterministic physical execution trace).
3. **`DEC::INFERRED`**: Deductively or inductively derived from `PROVEN` or `GROUNDED` premises via valid logical inference rules. Confidence bounded by the weakest link: $C_{\text{final}} = \min_{i} C(\text{premise}_i)$.
4. **`DEC::SPECULATIVE`**: Working hypothesis generated without direct formal or empirical verification. MUST be quarantined and isolated from production execution paths.
5. **`DEC::UNKNOWN`**: Proposition with indeterminate truth value or contradictory evidence. Automatically triggers an active falsification sub-process.

---

## II. SOCRATIC ADVERSARIAL & DIMENSIONAL VERIFICATION

### 1. Bayesian Epistemic Doubt Loop
Before declaring any non-trivial assertion, evaluate the log-likelihood update:

$$\log \frac{P(H \mid E)}{P(\neg H \mid E)} = \log \frac{P(H)}{P(\neg H)} + \log \frac{P(E \mid H)}{P(E \mid \neg H)}$$

- **Axiomatic Audit:** Identify all implicit background assumptions $A$. If $P(A)$ is not established, force label downgrade to `DEC::INFERRED` or `DEC::SPECULATIVE`.
- **Counter-Example Synthesis:** Actively generate boundary test vectors designed to invalidate $H$. If a counter-example is found, set label to `DEC::UNKNOWN` and trigger immediate falsification.
- **Domain Scope Bound:** Explicitly bound parameters $(\mathcal{X}, \mathcal{T}, \mathcal{R})$ specifying exact state space, time domain, and operational regime where the claim holds.

### 2. Universal Dimensional Analysis Gate (DAG)
For physical, mathematical, or structural equations, enforce dimensional homogeneity:

$$\left[ \text{LHS} \right] \equiv \left[ \text{RHS} \right]$$

Outputs: `DAG_PASS` (homogeneous) or `DAG_FAIL` (mismatched units/types). `DAG_FAIL` halts execution immediately.

---

## III. AUTONOMOUS EPISTEMIC CALIBRATION & ENTROPY AUDITING

During session close or cross-agent synthesis, evaluate epistemic entropy:

$$H(\text{DEC}) = -\sum_{i} p(\text{DEC}_i) \log_2 p(\text{DEC}_i)$$

### Pathology Detection (Zero-Trust Bounds):
1. **Epistemic Inflation Check:** If $p(\text{PROVEN}) + p(\text{GROUNDED}) > 0.85$ without attached formal proof artifacts or execution logs, downgrade claims systematically by one tier.
2. **Epistemic Suppression Check:** If $p(\text{SPECULATIVE}) = 0$ over $>20$ cognitive cycles, flag cognitive rigidity (hidden unverified assumptions).
3. **Epistemic Drift Detection:** Compare current belief states against historical hypothesis logs using KL-divergence $D_{KL}(P_{\text{current}} \parallel P_{\text{prior}})$. If drift occurs without explicit empirical events, trigger an automated epistemic audit.

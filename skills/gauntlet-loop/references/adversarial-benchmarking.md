# Adversarial Benchmarking, Scoring Rubrics & Lyapunov Convergence

This reference details the mathematical and operational mechanics of the Gauntlet Loop adversarial verification system.

---

## 1. Mathematical Formulation of Convergence

Let $Q_k \in [0.0, 10.0]$ denote the composite quality score assigned by the Blind Critic at iteration $k$.

### 1.1 Quality Delta Function
$$\Delta Q_k = Q_k - Q_{k-1}$$

### 1.2 Convergence Criterion
The iteration sequence converges if and only if:
$$(Q_k \ge 9.0) \land (\text{Gate}_A(k) = \text{PASS}) \land (\text{Gate}_B(k) = \text{PASS})$$

### 1.3 Lyapunov Stabilization Guard
Let $\epsilon = 0.05$ denote the minimum expected progress increment. If:
$$\sum_{j=k-2}^{k} |\Delta Q_j| < 2\epsilon \quad \text{for } Q_k < 9.0$$
the loop has entered asymptotic stagnation or cyclic oscillation. The system triggers an automatic decomposition event rather than continuing unguided iterations.

---

## 2. Blind Critic Multi-Dimensional Scoring Rubric

The Blind Critic computes $Q$ as a weighted sum across four orthogonal dimensions:

$$Q = 0.35 \cdot S_{\text{functional}} + 0.25 \cdot S_{\text{architecture}} + 0.25 \cdot S_{\text{robustness}} + 0.15 \cdot S_{\text{efficiency}}$$

| Dimension | Weight | Criteria Evaluated | Score 9-10 Standard |
|---|---|---|---|
| **Functional Correctness** ($S_{\text{functional}}$) | 35% | Specification adherence, API contract integrity | 100% requirements satisfied, 0 edge defects |
| **Architectural Elegance** ($S_{\text{architecture}}$) | 25% | Modularity, separation of concerns, cohesion | Clean interfaces, single responsibility, extensible |
| **Robustness & Defensive Bounds** ($S_{\text{robustness}}$) | 25% | Error recovery, boundary handling, input validation | Explicit domain exceptions, zero unhandled errors |
| **Asymptotic Efficiency** ($S_{\text{efficiency}}$) | 15% | Time complexity, memory allocation, caching | Optimal asymptotic complexity, zero memory leaks |

---

## 3. Double-Blind Anonymization Protocol

To prevent confirmation bias:
1. **Identifier Sanitization:** Strip author names, commit hashes, filenames, and internal organizational references.
2. **Standardized Formatting:** Normalize code formatting and markdown layout so artifacts cannot be distinguished by formatting quirks.
3. **Randomized Presentation Order:** Present Artifact 1 and Artifact 2 in pseudo-randomized order.

---

## 4. Adversarial Tribunal Escalation Procedure

When convergence fails after $N = 5$ iterations:
1. **Halt Builder-Critic Loop:** Terminate automated iteration.
2. **Compile Tribunal Dossier:**
   - Candidate implementation artifact.
   - Reference Bar specification.
   - History of iterative modifications and delta scores $\Delta Q_k$.
   - Critic point-by-point critique ledger.
3. **Tribunal Debate:** Red Team (advocating rejection / fundamental redesign) debates Blue Team (advocating bounded refactoring) before an impartial adjudicator subagent.

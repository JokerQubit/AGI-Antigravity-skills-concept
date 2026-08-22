---
name: gauntlet-loop
description: Orchestrates double-blind Builder and Critic adversarial verification loops against an explicit Named Reference Bar. Enforces Dual-Gate convergence (empirical test pass and blind qualitative score Q >= 9.0) with Lyapunov delta stabilization.
---

# Gauntlet-Loop Adversarial Quality Engine

> *"Refinement without an empirical reference bar produces aesthetic drift. True quality requires double-blind adversarial verification."*

---

## 1. Overview & Architecture

The **Gauntlet Loop** transforms engineering objectives into an adversarial multi-agent refinement process. It eliminates subjective self-evaluation by decoupling the creator from the evaluator and judging candidate implementations against an authoritative **Named Reference Bar**.

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Establish Named Reference Bar (Ground Truth)              │
│    - Named, fetchable, measurable baseline implementation   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Builder Subagent Generation / Iteration                  │
│    - Implement candidate artifact meeting all constraints   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Anonymization & Dual-Gate Evaluation                      │
│    - Strip identifiers (Candidate vs Reference Bar)         │
│    - Gate A: Deterministic Empirical Test Suite (100% pass) │
│    - Gate B: Blind Critic Qualitative Audit (Q >= 9.0)      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
        [Pass Both Gates]             [Fail Either Gate]
                │                             │
                ▼                             ▼
   Converged: Produce Handoff     Check Lyapunov Delta:
                                  If N=5 or Delta Q < epsilon:
                                  Decompose / Escalate
                                  Else: Loop to Builder
```

For mathematical convergence formulas, blinded scoring rubrics, and tribunal escalation protocols, see the [Adversarial Benchmarking Reference](./references/adversarial-benchmarking.md).

---

## 2. The Named Reference Bar Protocol

Every Gauntlet Loop invocation requires an authoritative Reference Bar meeting three criteria:

1. **Named:** An explicit standard, industry specification, golden benchmark dataset, or production baseline codebase.
2. **Fetchable:** Accessible on disk or via network for direct side-by-side comparison.
3. **Measurable:** Contains both deterministic quantitative metrics (test suites, latency, type coverage) and qualitative requirements (modularity, clarity, API cleanliness).

---

## 3. The Dual-Gate Convergence System

A candidate artifact is certified only when it simultaneously satisfies both verification gates:

### Gate A: Deterministic Empirical Gate
- **100% Test Pass:** All unit, integration, and property tests pass with exit code 0.
- **Zero Static Violations:** 0 linter errors, 0 type checker warnings, 0 syntax defects.
- **Performance Thresholds:** Latency, memory footprint, and asymptotic bounds satisfy operational targets.

### Gate B: Blind Qualitative Critic Gate
- **Double-Blind Review:** Artifacts A (Reference Bar) and B (Candidate) are stripped of metadata/author tags.
- **Independent Critic Subagent:** The Critic audits architecture, edge-case resilience, and documentation without knowing the candidate's provenance.
- **Quality Score Threshold:** Candidate must achieve a composite quality score $Q \ge 9.0 / 10.0$ and outperform the Reference Bar.

---

## 4. Lyapunov Delta Stabilization & Convergence Safeguards

To prevent infinite loops, thrashing, or cyclic regressions:
- Track quality change per iteration:
  $$\Delta Q_k = Q_k - Q_{k-1}$$
- **Early Termination:** If after $N = 5$ iterations $\Delta Q_k < \epsilon$ without satisfying both gates, trigger an **Adversarial Decomposition Pass**:
  1. Break the component into smaller sub-modules.
  2. Isolate the specific failing dimension (empirical vs qualitative).
  3. Escalate unresolved architectural impasses to an adversarial tribunal.

---

## 5. Subagent Dispatch Schema

When dispatching Builder and Blind Critic subagents via `invoke_subagent` or `send_message`:

```json
{
  "BuilderPayload": {
    "Role": "Gauntlet Builder",
    "Objective": "Construct and refine candidate module to exceed Reference Bar standards",
    "Constraints": ["Zero placeholders", "100% type annotations", "All tests passing"]
  },
  "BlindCriticPayload": {
    "Role": "Gauntlet Blind Critic",
    "Objective": "Perform double-blind adversarial audit of Anonymized Artifact A vs Anonymized Artifact B",
    "EvaluationCriteria": ["Architectural elegance", "Edge-case coverage", "Defensive contracts", "Q-score (0-10)"]
  }
}
```

---

## 6. Execution Protocol Checklist

- [ ] Has an explicit Named Reference Bar been identified and loaded?
- [ ] Are Candidate and Reference Bar stripped of identifying provenance before Critic review?
- [ ] Has Gate A (Empirical Test Suite) passed with exit code 0?
- [ ] Has Gate B (Blind Critic) awarded $Q \ge 9.0$?
- [ ] Has Lyapunov delta stability $\Delta Q_k \ge \epsilon$ been confirmed across iterations?

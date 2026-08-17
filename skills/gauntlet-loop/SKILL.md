---
name: gauntlet-loop
description: High-rigor iterative improvement protocol. Deconstructs objectives, deploys double-blind Builder and Critic subagent ensembles against an empirical reference bar, and loops until verified superiority and convergence are achieved.
applies_when: Use for iterative optimization, benchmark refinement, builder-critic adversarial loops, code quality convergence, or when triggered by /goal command.
does_not_apply_when: Single-pass basic question answering or trivial minor file edits.
---

# SKILL: Gauntlet Loop Engine

> *"Iterative refinement without empirical ground truth is merely aesthetic drift."*

---

## 1. Core Architecture

The Gauntlet Loop transforms any development or research goal into a self-correcting multi-agent refinement process:
1. **Establish Ground Truth Bar:** Retrieve an explicit, named reference artifact, theoretical baseline, or benchmark suite.
2. **Atomic Deconstruction:** Break the work into independently judgeable components.
3. **Double-Blind Ensemble Execution:** Fan out independent **Builder** and **Critic** subagents with isolated context boundaries.
4. **Empirical & Blind Comparison:** The Critic evaluates artifacts blind (identifiers stripped) combined with deterministic sandbox execution metrics.
5. **Lyapunov Convergence Safeguard:** Loop until the artifact beats the bar AND quality improvement stabilizes (\(\Delta Q < \epsilon\)).

---

## 2. The Reference Bar Protocol

A valid reference bar must meet three criteria:
- **Named:** A concrete reference implementation, design spec, paper baseline, or benchmark suite.
- **Fetchable:** Fully accessible to Critic subagents for direct side-by-side inspection.
- **Measurable:** Contains both qualitative criteria AND deterministic execution benchmarks.

---

## 3. Double-Blind Critic & Execution Engine

To prevent subjective LLM bias and hallucinated approvals:
- **Identifier Stripping:** Artifacts A (Reference) and B (Candidate) are anonymized before passing to Critic.
- **Deterministic Verification Dual-Gate:**
  - *Gate A (Empirical Execution):* Automated test suite pass, zero static analysis warnings, performance latency/throughput bounds satisfied.
  - *Gate B (Blind Qualitative Critic):* Critic identifies specific remaining gaps and declares winner.
- **Exit Condition:** Candidate MUST pass Gate A (Empirical) AND win Gate B (Critic) across 2 consecutive loops.

---

## 4. Convergence & Stability Safeguard

To prevent infinite loops or oscillatory quality degradation:
- Track delta improvement metric \(\Delta Q_k = Q_k - Q_{k-1}\).
- If after \(N = 5\) iterations \(\Delta Q_k < \epsilon\) without winning, trigger **Adversarial Decomposition Pass**: re-split component into smaller sub-problems or escalate to `adversarial-tribunal` (`skills/adversarial-tribunal/SKILL.md`).

---

## 5. Universal Prompt Generation Template

Adapt for target domain (keep under 180 words):

```
Goal: [OBJECTIVE]
Reference Bar: [NAMED_FETCHABLE_BAR]

Step 1: Inspect the Reference Bar directly.
Step 2: Deconstruct objective into atomic sub-components.
Step 3: For each component, spawn an isolated Builder subagent and a separate Blind Critic subagent.
Step 4: The Blind Critic must inspect Candidate vs Bar with labels stripped, run empirical verification tests, declare the winner, and identify the single largest remaining gap.
Step 5: Loop iteratively until Candidate passes all empirical execution gates AND wins blind comparison.

Log loop progress continuously in [PROGRESS_LEDGER].
```

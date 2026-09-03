---
name: gauntlet_loop
description: Self-Evolving Gauntlet Loop Protocol. Activates when building high-stakes, mission-critical artifacts (codebases, architectures, research dossiers, UI/UX systems) requiring recursive adversarial critique, blind reference benchmarking, independent critic verification, and autonomous quality optimization.
---

# The Self-Evolving Gauntlet Loop Protocol (`gauntlet_loop`)

## 1. Executive Overview & Core Purpose
The **Gauntlet Loop** is an advanced AI loop engineering architecture based on Matt Shumer's builder-versus-critic paradigm and high-assurance iterative engineering. Rather than relying on single-shot prompt generation or self-grading models, the Gauntlet Loop splits execution across separate agents: **Builders** produce the artifact, **Fresh-Context Critics** judge the real artifact against an uncompromising reference bar, and an **Integration Critic** validates the synthesized whole.

```
       ┌────────────────────────────────────────────────────────┐
       ▼                                                        │
[1. Decompose] ──► [2. Build] ──► [3. Inspect Artifact] ──► [4. Critic]
                                                                │
                 ┌──────────────────────────────────────────────┘
                 ▼
         {Passes Bar?} ──(NO: Largest Gap Identified)──► Loop to Build
                 │
                 ▼ (YES: All Units Pass)
       [5. Integration Pass] ──► [6. Executive Delivery]
```

---

## 2. The Three Invariant Elements of AI Loop Engineering

Every execution of the Gauntlet Loop must be parameterized by the **Three Invariant Elements**:

| Element | Operational Definition | Enforcement Criteria |
| :--- | :--- | :--- |
| **1. Objective** | The concrete, immutable outcome that must become true in reality. | Must be state-verifiable (e.g., *"Zero test failures, 100% API schema validation, p99 latency < 20ms"*). Vague objectives like *"Make it good"* are strictly rejected. |
| **2. Metric / Verifier** | The empirical evidence, reference benchmark, or independent critic used to judge each attempt. | **Builder Never Grades Its Own Work**: The critic operates with a clean context, receives the real artifact (not a summary), and conducts a blind comparison against the reference bar. |
| **3. Boundary** | The explicit guardrails governing cost, time, attempts, permissions, and escalation. | Max rounds (e.g., 5 iterations), token expenditure bounds, safety invariants (no unauthorized deployment/deletion), and escalation triggers when the same blocker recurs twice. |

---

## 3. The 6-Stage Gauntlet Loop Procedure

### Stage 1: Decomposition into Orthogonal Units
- The lead agent analyzes the primary objective and decomposes the target artifact into the smallest independently improvable and judgeable units.
- Highly coupled components remain grouped; genuinely independent components are assigned to parallel builder tracks.

### Stage 2: Execution by Specialized Builders
- Dedicated builders (or employee sub-agents) construct each unit.
- Builders adhere to the **Zero-Stub and Zero-Ellipsis Invariants**: every function, interface, and error branch must be completely written out.

### Stage 3: Real Artifact Inspection
- The critic does NOT read the builder's progress report or conversational justifications.
- The critic inspects the actual output: reads the source code, executes unit tests, reviews rendered visual output, or analyzes empirical benchmark data.

### Stage 4: Fresh-Context Harsh Critique (Blind A/B Comparison)
- A separate critic sub-agent is spawned with a clean context window.
- The critic compares the generated artifact side-by-side with the reference benchmark.
- The critic answers:
  1. *Does our artifact meet or exceed the reference quality bar?*
  2. *What is the single largest meaningful defect or gap?*
  3. *What is the concrete, reproducible remediation directive for the builder?*
- If the artifact fails, the remediation directive is returned to the builder for the next round.

### Stage 5: Progress Ledger & Strategy Mutation
- The loop updates the local progress ledger:
  - *Current Round Number*
  - *Identified Gap*
  - *Failed Approaches (so the builder mutates strategy and avoids repeating errors)*
  - *Remaining Boundary Budget*

### Stage 6: The Whole-System Integration Pass
- Once all individual units pass their respective critic gates, a fresh **Integration Critic** inspects the entire unified system to resolve seam conflicts, ensure aesthetic/architectural consistency, and verify alignment with the original macro-objective.

---

## 4. Reference Runbooks & Automation
- Detailed step-by-step execution protocol: [gauntlet_execution_protocol.md](./references/gauntlet_execution_protocol.md)
- Automated loop runner: [`scripts/run_gauntlet.ps1`](../../scripts/run_gauntlet.ps1)

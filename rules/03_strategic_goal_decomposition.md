---
trigger: always_on
description: Layer 3 Strategic Goal Decomposition, DAG Task Scheduling, Empirical Research Grounding, and Multi-Stage Session Pacing
---
# Layer 3: Strategic Goal Decomposition & Empirical Research

Layer 3 translates epistemically verified consensus into formal OKRs, computes Directed Acyclic Graphs (DAGs) of sub-agent task dependencies, grounds roadmaps in empirical research, and enforces multi-stage session pacing.

## 1. Strategic Planning & Multi-Stage Session Pacing

- Anti-Rush Invariant: Monolithic "one-shot" execution is strictly banned. Complex initiatives must execute deliberately across staged sessions, with intermediate milestones verified and committed to disk.
- Fiduciary Resource Budgeting: Deconstruct tasks so operational specialists run in clean-context windows. Milestones are binary (100% complete with passing tests or 0% complete).

## 2. Department of Strategic Goal Setting (`dept_goals`)

### 2.1 Departmental Staff
- `CSO-GOAL-01` (Chief Strategy Officer): Translates consensus into OKR milestones and execution roadmaps.
- `GOAL-101` (OKR Metric Engineer): Authors quantitatively verifiable Key Results (e.g., "0 stubs across 100% of codebase").
- `GOAL-102` (DAG Dependency Analyst): Computes dependency graphs and critical path schedules.

### 2.2 Mathematical DAG Formulation
Execution roadmap is modeled as DAG $G = (V, E)$:
- $V = \{v_1, \dots, v_n\}$ represents atomic milestones.
- $E = \{(v_i, v_j)\}$ represents strict dependency edges where $v_i$ must be certified before $v_j$ initializes.
- Topological sort $\tau: V \to \{1, \dots, |V|\}$ ensures $\tau(u) < \tau(v)$ for all $(u, v) \in E$.
- Critical path length:
$$L_{\text{critical}} = \max_{p \in \text{Paths}(G)} \sum_{v \in p} \text{EstimatedCost}(v)$$
Graph cycles ($v_i \to \dots \to v_i$) trigger immediate execution freeze and DAG recompilation.

### 2.3 Token Economy Preservation
Sub-agents operate within finite token envelopes:
$$B_{\text{allocated}}(v_i) \le \alpha \cdot \text{Complexity}(v_i), \quad \sum_{i=1}^{n} B_{\text{allocated}}(v_i) \le B_{\text{total}}$$
Any subagent exceeding 85% of its budget without emitting a disk artifact must checkpoint state and yield execution.

## 3. Department of Strategic Research (`dept_research`)

### 3.1 Departmental Staff
- `DIR-RES-01` (Director of Strategic Research): Enforces empirical benchmarking before greenfield design.
- `RES-101` (Literature Investigator): Conducts teardowns of industry standards and academic literature.

### 3.2 Empirical Benchmarking Protocol
Before designing a subsystem, establish:
1. Global Frontier Exemplars: Best existing industry solutions (LMAX Disruptor for ringbuffers, Erlang OTP for actors, SQLite for persistence).
2. Historical Failure Modes: Common production traps, deadlocks, and memory leaks in predecessor architectures.
3. OS & Hardware Invariants: Platform-specific limits (Windows NTFS locking, PowerShell 5.1 vs Core differences, thread limits).

## 4. 4-Stage Multi-Stage Session Pacing & Checkpoints

```
STAGE 1: Scoping & Research (L1-L3) -> Yield for Founder "Proceed" Sign-Off
STAGE 2: Architecture & Contracts (L4-L5) -> Emit schemas and test harnesses
STAGE 3: Clean-Context Production (L6-L7) -> Level 1 specialists author code & tests
STAGE 4: Supervisory Gating & Ledger (L8, L10) -> Certify quality & commit to ledger
```

Checkpoint Gating Rules:
- No stage begins until preceding stage artifacts are committed to disk and logged in `.state/ledger/`.
- Parallel sub-agents execute in isolated processes (`invoke_subagent`), communicating solely via disk artifacts in `.state/`.

## 5. OKR & Sprint Status JSON Schema (`.state/status.json`)

```json
{
  "global_phase": "active_operations",
  "active_sprint": { "sprint_id": "SPRINT-002", "name": "Neural Layer Chain", "status": "in_progress" },
  "objectives": [
    {
      "id": "OBJ-1", "description": "Deploy 12-layer reflexive neural chain",
      "key_results": [
        { "id": "KR-1.1", "description": "Calibrate all rules to [3800, 5800] bytes (<=1500 tokens)", "status": "in_progress" },
        { "id": "KR-1.2", "description": "Keep total rule files <= 14", "status": "completed" }
      ]
    }
  ],
  "dependency_dag": {
    "nodes": ["L1_Sensory", "L2_Socratic", "L3_Goals", "L4_Arch", "L7_Prod", "L8_Supervisory"],
    "edges": [["L1_Sensory", "L2_Socratic"], ["L2_Socratic", "L3_Goals"], ["L3_Goals", "L4_Arch"], ["L4_Arch", "L7_Prod"], ["L7_Prod", "L8_Supervisory"]]
  }
}
```

## 6. Layer 3 to Layer 4 Cognitive Handshake Contract

Checklist:
- [ ] DAG acyclicity proven (zero cycles).
- [ ] Critical path and parallelization milestones mapped.
- [ ] Global frontier benchmarks and historical failure modes documented.
- [ ] Token budgets bounded with $\alpha$ density limits.
- [ ] `.state/status.json` updated and verified valid BOM-free UTF-8.

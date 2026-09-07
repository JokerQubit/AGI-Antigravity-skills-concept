---
trigger: always_on
description: Layer 3 Strategic Goal Decomposition, DAG Task Scheduling, and Session Pacing
---
# Layer 3: Strategic Goal Decomposition & Empirical Research

Translates verified consensus into formal OKRs, computes sub-agent DAG task dependencies, grounds roadmaps in empirical research, and enforces multi-stage session pacing.

## 1. Strategic Planning & Multi-Stage Session Pacing
- Anti-Rush Invariant: Monolithic "one-shot" execution is banned. Initiatives execute deliberately across staged sessions, with milestones committed to disk.
- Fiduciary Resource Budgeting: Deconstruct tasks so specialists run in clean-context windows. Milestones are binary (100% complete with tests or 0%).

## 2. Department of Strategic Goal Setting (`dept_goals`)
Staff: `CSO-GOAL-01` (Chief Strategy Officer), `GOAL-101` (OKR Metric Engineer), `GOAL-102` (DAG Dependency Analyst).

### 2.1 Mathematical DAG Formulation
Roadmap modeled as DAG $G = (V, E)$:
- $V = \{v_1, \dots, v_n\}$ represents atomic milestones; $E = \{(v_i, v_j)\}$ represents strict dependency edges.
- Topological sort $\tau: V \to \{1, \dots, |V|\}$ ensures $\tau(u) < \tau(v)$ for all $(u, v) \in E$.
- Critical path length:
$$L_{\text{critical}} = \max_{p \in \text{Paths}(G)} \sum_{v \in p} \text{EstimatedCost}(v)$$
Graph cycles ($v_i \to \dots \to v_i$) trigger execution freeze and DAG recompilation.

### 2.2 Token Economy Preservation
Sub-agents operate within finite token envelopes:
$$B_{\text{allocated}}(v_i) \le \alpha \cdot \text{Complexity}(v_i), \quad \sum_{i=1}^{n} B_{\text{allocated}}(v_i) \le B_{\text{total}}$$
Exceeding 85% of budget without emitting a disk artifact requires checkpointing state and yielding.

## 3. Department of Strategic Research (`dept_research`)
Staff: `DIR-RES-01` (Director), `RES-101` (Literature Investigator).
Benchmarking: 1. Global Frontier Exemplars (Disruptor, OTP, SQLite) | 2. Historical Failure Modes (deadlocks, memory leaks) | 3. Platform Invariants (NTFS locking, shell differences).

## 4. 4-Stage Session Pacing & Checkpoint Gating
Stages: 1. Scoping (L1-L3, await Proceed) -> 2. Architecture (L4-L5, schemas/tests) -> 3. Production (L6-L7, code/tests) -> 4. Supervisory Gate (L8, L10).
Rule: No stage begins until preceding stage artifacts are committed to disk and logged in `.state/ledger/`.

## 5. OKR & Sprint Status JSON Schema (`.state/status.json`)
```json
{
  "global_phase": "active_operations", "active_sprint": { "sprint_id": "SPRINT-002", "name": "Neural Chain", "status": "in_progress" },
  "objectives": [{
    "id": "OBJ-1", "description": "Deploy 12-layer reflexive neural chain",
    "key_results": [
      { "id": "KR-1.1", "description": "Calibrate all rules to [2800, 3900] bytes (~1000-1150 tokens)", "status": "in_progress" },
      { "id": "KR-1.2", "description": "Keep total rule files <= 14", "status": "completed" }
    ]
  }],
  "dependency_dag": { "nodes": ["L1", "L2", "L3", "L4", "L7", "L8"], "edges": [["L1","L2"], ["L2","L3"], ["L3","L4"], ["L4","L7"], ["L7","L8"]] }
}
```

## 6. Layer 3 to Layer 4 Handshake Contract
- [ ] DAG acyclicity proven (zero cycles); critical path and parallelization milestones mapped.
- [ ] Global frontier benchmarks and historical failure modes documented.
- [ ] Token budgets bounded with $\alpha$ density limits; `.state/status.json` valid BOM-free UTF-8.\n
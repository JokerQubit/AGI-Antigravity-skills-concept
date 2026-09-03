# Departmental Runbook: Gauntlet Loop Execution Protocol (`GAUNTLET-RUN-01`)

## 1. Trigger Conditions
Executes whenever an engineering, research, or design deliverable is deemed mission-critical, requires zero-defect quality, or must achieve parity with an authoritative reference standard.

---

## 2. Step-by-Step Operational Runbook

### Phase A: Loop Card Definition (The Three Elements)
Before running the first iteration, write the formal Loop Card:
```yaml
loop_card:
  objective: "Construct high-concurrency state synchronization engine with zero race conditions."
  metric:
    reference_bar: "100 concurrent read/write transactions without lock contention or data corruption."
    verifier: "Automated stress-test script + independent red-team critic code audit."
  boundary:
    max_rounds: 4
    token_budget_threshold: 50000
    forbidden_actions: ["Bypassing mutex locks", "Stubbing unit tests", "Ignoring race warnings"]
    escalation_rule: "If identical deadlocks occur in 2 consecutive rounds, escalate to Systems Architecture Head."
```

### Phase B: Builder Execution
1. Decompose the deliverable into modular components.
2. The Builder implements Component $k$ adhering to the **Zero-Stub and Zero-Ellipsis Invariant**.
3. The Builder saves the complete artifact to disk (e.g., `src/sync_engine.ps1`).

### Phase C: Fresh-Context Critic Invocation
1. Launch an independent sub-agent via `invoke_subagent`.
2. Do NOT pass the conversation history of the builder.
3. Pass ONLY:
   - The original Objective and Metric.
   - The path to the generated artifact.
   - The reference benchmark.
4. Prompt the Critic:
   *"Inspect the real artifact at <path>. Compare it directly against the benchmark. Grade ruthlessly. Does it reach Triple-A parity? If not, identify the single largest architectural/functional defect, explain the exact failure mode, and formulate a mandatory remediation specification."*

### Phase D: Evolution & Mutation
1. If the Critic rejects the attempt, record the failure mode into `.state/gauntlet_progress.json`.
2. Re-prompt the Builder with the Critic's remediation specification.
3. The Builder MUST adopt an alternate approach (no identical retries).
4. Repeat until Critic issues an unconditional certification or a boundary condition fires.

### Phase E: Final Integration Pass
1. A fresh **Integration Critic** inspects the entire integrated deliverable to verify coherence, interface compatibility, and holistic quality.

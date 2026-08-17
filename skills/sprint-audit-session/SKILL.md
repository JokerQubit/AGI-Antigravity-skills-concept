---
name: sprint-audit-session
description: Autonomous session management and state serialization protocol enforcing continuous multi-agent repository auditing and zero-loss context persistence.
---

# SKILL: Autonomous Continuous Session Protocol & State Serialization Engine

## 1. Purpose
The Autonomous Continuous Session Protocol guarantees zero-loss state persistence, continuous multi-agent progress, and deterministic recovery during repository auditing, independent of underlying execution environment restarts, API rate limits, or context window resets.

## 2. Session Architecture

```
                       ┌──────────────────────────────┐
                       │  Session State Deserializer  │
                       └──────────────┬───────────────┘
                                      │
                   ┌──────────────────┴──────────────────┐
                   ▼                                     ▼
      [Master Swarm Governor]             [Context Token Budget Guard]
                   │                                     │
       ┌───────────┴───────────┐                         │
       ▼                       ▼                         │
[Sub-Orchestrator A]   [Sub-Orchestrator B]               │
       │                       │                         │
  ┌────┴────┐             ┌────┴────┐                    │
  ▼         ▼             ▼         ▼                    │
[Worker] [Worker]       [Worker] [Worker]                │
  │         │             │         │                    │
  └─────────┴──────┬──────┴─────────┘                    │
                   ▼                                     ▼
        ┌──────────────────────────────────────────────────┐
        │   Continuous State Serialization & Handoff       │
        └──────────────────────────────────────────────────┘
```

## 3. Session Lifecycle Execution

### Phase 1: Session Initialization & State Recovery (T0 + 0m)
1. Read `session_state.md` and deserialization registers to restore complete system context.
2. Verify previous session audit ledgers and coverage maps.
3. Construct or update the dynamic subagent dispatch tree based on remaining un-audited AST clusters.

### Phase 2: Autonomous Parallel Execution
1. Dispatch parallel subagent swarms governed by token frequency boundaries (max 2 concurrent workers per sector).
2. Execute audit tasks strictly according to `audit-tier-classifier` depth levels.
3. Automatically stream intermediate worker outputs directly to persistent markdown artifacts in `docs/refactor/`.

### Phase 3: Continuous Checkpointing & Quota Management
1. Monitor context token usage and API rate thresholds dynamically.
2. Upon reaching context saturation or encountering environment suspension signals:
   - Execute synchronous atomic write to `session_state.md` and sector handoff ledgers.
   - Commit all audited artifacts to revision control (`git commit -m "audit: continuous checkpoint [sector] [coverage%]"`)
   - Generate an **Autonomous Recovery Payload** containing exact resumption offset pointers.

### Phase 4: Verification & Handoff Completion
1. Run automated `COVERAGE_GATE` verifying both quantitative file coverage AND AST semantic completeness.
2. Serialize state for the next session loop and present concise execution telemetry to system orchestrators.

## 4. Execution Falsification Criteria
This skill is falsified if any context state is lost across session boundaries, if a worker crash leaves uncommitted or orphaned audit files, or if coverage assertions pass without semantic AST validation.

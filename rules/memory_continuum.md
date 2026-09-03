---
trigger: always_on
description: Persistent State Continuum, Memory Ledger & Neural Map Protocol (.state/)
---
# Memory Continuum & Project Awareness Protocol

This rule governs how the primary AI (CEO) and all orchestrated sub-agents maintain continuous situational awareness, access project memory, and avoid operating in an amnesiac vacuum.

---

## 1. The Epistemic State Problem

By design, sub-agents run in isolated, clean contexts. While this prevents attention saturation and context drift, it creates a potential vulnerability: sub-agents may lack awareness of overall project progress, recent architectural decisions, or active corporate constraints.

To eliminate this vulnerability, the system enforces the **Memory Continuum Protocol**:

```
           [Append-Only Ledger: .state/ledger/]
                            â–²
                            â”‚ Atomic Transaction Log
[status.json & corporate_health.json] â—„â”€â”€â”€â–º [scripts/sync_state.ps1]
                            â”‚
                            â–¼
          [Context Hydration at Sub-Agent Launch]
```

---

## 2. The Three Memory Tiers

### 2.1 Tier 1: Ephemeral Working Memory (Context Window)
- Bounded strictly to the immediate task.
- Contains only the input data payload, targeted runbook, and tool interactions.
- Wiped upon sub-agent termination.

### 2.2 Tier 2: Real-Time Machine State (`.state/status.json` & `corporate_health.json`)
- Updated dynamically at every departmental state transition.
- Tracks active sprints, department statuses, open mandates, and real-time survival metrics.
- Injected automatically into the primary agent via `hooks.json` PreInvocation hook.

### 2.3 Tier 3: Immutable Append-Only Ledger (`.state/ledger/`)
- Permanent, chronological record of every executive decision, research conclusion, code commit, and audit verification.
- Every major deliverable commits an entry before being presented to the CEO.
- Allows any agent to inspect prior decisions and trace the lineage of any architectural component.

---

## 3. Operational Invariants for Agents

1. **Hydration Before Execution**: Before initiating a complex multi-step workflow, the agent must ensure it has hydrated its context with current state (either via PreInvocation telemetry or calling `sync_state.ps1`).
2. **Atomic State Commit**: No major work package is complete until its completion transaction is logged in `.state/ledger/`.
3. **No Phantom Progress**: Agents must never report a milestone as complete unless the corresponding verification artifact is written to the filesystem and recorded in the ledger.


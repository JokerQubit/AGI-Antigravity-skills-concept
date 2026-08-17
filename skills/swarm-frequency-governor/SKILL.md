---
name: swarm-frequency-governor
description: Use before dispatching any batch of parallel Workers to enforce the 2-concurrent-subagent limit, prevent 429 RESOURCE_EXHAUSTED errors, and sequence large swarms safely.
applies_when: Use prior to dispatching subagent swarms, parallel worker batches, or managing rate-limited API calls.
does_not_apply_when: Single-thread execution or single tool execution turns.
---

# SKILL: Adaptive Closed-Loop Frequency Governor & PID Concurrency Engine

## I. Hard Concurrency Cap & Closed-Loop Rate Governance
1. **Hard Concurrency Ceiling ($C_{\text{max}} = 2$):** At no point shall the Master Orchestrator dispatch more than **2 active worker subagents** running concurrently.
2. **Pre-Dispatch Active Count Check:** Before calling subagent dispatch tools (`invoke_subagent`), count currently running subagents. If Active Subagents >= 2, the Orchestrator MUST pause dispatching until a subagent completes and reports back.
3. **Dynamic Token-Bucket Telemetry:** If HTTP 429 `RESOURCE_EXHAUSTED` or rate-limit warnings occur, dynamically throttle concurrency to $C(t) = 1$ worker until rate windows clear.

## II. Dynamic Asynchronous Work-Stealing Queue
Replaces batch barrier synchronization with an asynchronous work-stealing task pool:
- Workers pull tasks continuously from the globally ordered DAG queue.
- As soon as any single Worker completes, its handoff is committed, state is verified, and the next eligible task is immediately dispatched without waiting for sibling nodes.

## III. Multi-Provider Sliding-Window Circuit Breaker
Statistical sliding window (last $N=50$ requests) monitoring:
- States: `HEALTHY`, `THROTTLED` (scale down $C(t)$ by 50%), `DRAINING` (route to fallback provider), `RECOVERY` (probe mode).
- Automatic vendor failover protocol across available API backends.

## IV. Zero-Polling & Reactive Wakeup Protocol
- **Strict Prohibition:** Polling loops calling `manage_task (Action: 'status')` or setting synthetic recurring timers to check if background commands or subagents finished is **STRICTLY FORBIDDEN**.
- **Execution Rule:** Dispatch the asynchronous task or subagent, perform any unrelated parallel preparation, and **stop calling tools to end the turn**. The Antigravity reactive message bus will wake up the orchestrator automatically with the exact result payload upon completion.


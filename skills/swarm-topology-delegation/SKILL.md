---
name: swarm-topology-delegation
description: Governs the multi-level parallel chat swarm, programmatic subagent teams, and execution mode decisions. Consolidates orchestration hierarchy, swarm map tracking, and worker role classification (CEO Direct, Manual Parallel Chat, Programmatic Subagent).
---

# SKILL: Dynamic Multi-Agent Topology & Autonomous Task Graph Orchestration

## I. Mathematical Principle & Topology Foundations
Multi-agent task decomposition is modeled as an acyclic execution graph $G = (V, E)$, where $V$ represents discrete cognitive atomic tasks and $E$ represents dependency edges. Tasks are dynamically routed based on agent capability matrices, context decay rates, and topological depth.

## II. Execution Node Classifications (100% Autonomous)
- Node Class Alpha (Inline Cognition): Single-turn transformations, context updates, and immediate graph reductions within the current agent context ($\text{Token Estimate} < 0.20 \cdot \text{Context Window}$).
- Node Class Beta (Autonomous Programmatic Worker Thread): Non-blocking sub-agent invocation via IPC/API. Operates on isolated memory spaces, emitting deterministic task results to the state bus.
- Node Class Gamma (Hierarchical Sub-Orchestrator Cluster): Autonomous intermediate graph supervisor capable of dynamically spawning sub-graphs, balancing loads, and running micro-consensus loops.

## III. Byzantine Fault Tolerance & Drift Control
- Redundant Verification: High-risk decisions require dual-worker independent processing ($W_A \neq W_B$) with cross-verification.
- Agent Drift Sentinel: Automated monitoring of intermediate state outputs. If semantic divergence exceeds threshold $\Delta > 0.15$, the execution node is halted and rolled back to checkpoint.

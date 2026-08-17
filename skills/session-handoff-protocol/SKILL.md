---
name: session-handoff-protocol
description: Cryptographically Verifiable Session State Serialization & Autonomous Handoff Protocol. Manages zero-loss state transitions between cognitive execution sessions and multi-agent swarm environments.
---

# SKILL: Session Handoff Protocol — Cryptographic State Serialization

> *"Continuity is the backbone of cognition. A system with unverified state handoffs has no identity."*

---

## I. ABSTRACT SYSTEM STATE ARCHITECTURE

Session Handoff is completely decoupled from specific domain codebases or legacy repository names. It manages state transitions through a standardized, cryptographically hashed state schema.

```
  [Session N]  ───(Serialize & Hash)───> [State File + SHA-256] ───(Deserialize & Verify)───> [Session N+1]
```

---

## II. AUTONOMOUS SESSION OPEN PROTOCOL

1. **State Retrieval & Cryptographic Validation:**
   - Read primary state artifact (`memory/session_state.md` / `.json`).
   - Verify SHA-256 state hash against `memory/state_manifest.sha256`. If hash mismatches, trigger emergency state recovery from historical snapshot.
2. **State Deserialization:**
   - Parse global project phase, active dependency graph, open blockers, and completed execution nodes.
3. **Autonomous Dependency Resolution & Priority Mapping:**
   - Derive the top 3 critical path actions ($P_1, P_2, P_3$) deterministically using critical-path method (CPM) analysis of the remaining task DAG.
4. **Orphan & Integrity Scan:**
   - Cross-reference physical skill assets against the capability manifest. Flag unregistered or orphaned capabilities for immediate registration or isolation.

---

## III. AUTONOMOUS SESSION CLOSE & HANDOFF PROTOCOL

Triggered via automated context threshold ($T_{\text{handoff}}$) or completion of a task epoch:

1. **Execution Freeze & Immutable Snapshot:**
   - Halt active work units. Compute diff vector of all state mutations during the session.
2. **State Payload Serialization:**
   - Update `session_count` ($N \to N+1$).
   - Serialize active worker topologies, resolved vs. outstanding blockers, and updated priority queues.
3. **Auto-Evolution & Fitness Update:**
   - Record capability usage frequencies and execution quality scores.
   - Update skill fitness ratings and append events to `memory/evolution_ledger.md`.
4. **Cryptographic Manifest Locking & Commit:**
   - Compute payload hash $H(\text{State}_{N+1})$.
   - Commit updated state files to version control with automated standardized state commit signature: `state(core): serialize session N+1 [hash: SHORT_SHA]`.

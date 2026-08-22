---
name: session-handoff-protocol
description: Manages transactional session state serialization, cryptographic SHA-256 state hashing, and atomic session handoffs across agent turns or context windows. Eliminates hallucinations and context drift during long-horizon tasks.
---

# Session State Handoff & Cryptographic Integrity Protocol

> *"Without deterministic state serialization and cryptographic hashing, long-horizon tasks degrade into hallucinatory context drift."*

---

## 1. Overview & Core Philosophy

The **Session Handoff Protocol** provides transactional state persistence across conversational boundaries, subagent context resets, and multi-turn execution windows. It ensures that an agent resuming work has an unambiguous, tamper-evident view of project state, completed milestones, verified invariants, and active constraints.

For cryptographic hashing algorithms, canonical JSON formatting, and recovery procedures, see the [State Cryptography Reference](./references/state-cryptography.md).

---

## 2. The Transactional State Schema

Session state is persisted deterministically as a JSON-serializable structured document containing five canonical keys:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. SESSION METADATA (Session ID, Timestamp, Schema Version) │
├─────────────────────────────────────────────────────────────┤
│ 2. CONSTITUTIONAL INVARIANTS (Locked dogmas, constraints)    │
├─────────────────────────────────────────────────────────────┤
│ 3. COMPLETED MILESTONES (Verified deliverables, test proofs) │
├─────────────────────────────────────────────────────────────┤
│ 4. ACTIVE EXECUTION POINTER (Current task, in-flight files) │
├─────────────────────────────────────────────────────────────┤
│ 5. CRYPTOGRAPHIC INTEGRITY BLOCK (SHA-256 state hash)       │
└─────────────────────────────────────────────────────────────┘
```

### JSON Schema Specification

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SessionStateSnapshot",
  "type": "object",
  "required": [
    "sessionId",
    "timestampUtc",
    "schemaVersion",
    "completedMilestones",
    "activeTask",
    "workspaceStateHash"
  ],
  "properties": {
    "sessionId": { "type": "string" },
    "timestampUtc": { "type": "string", "format": "date-time" },
    "schemaVersion": { "type": "string", "enum": ["1.0.0"] },
    "completedMilestones": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["milestoneId", "status", "testVerificationProof"],
        "properties": {
          "milestoneId": { "type": "string" },
          "status": { "type": "string", "enum": ["COMPLETED", "FAILED"] },
          "testVerificationProof": { "type": "string" }
        }
      }
    },
    "activeTask": {
      "type": "object",
      "required": ["taskId", "description", "targetFiles"],
      "properties": {
        "taskId": { "type": "string" },
        "description": { "type": "string" },
        "targetFiles": { "type": "array", "items": { "type": "string" } }
      }
    },
    "workspaceStateHash": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
  }
}
```

---

## 3. Cryptographic State Hashing Workflow

To guarantee zero silent corruption across session handoffs:

1. **Serialize Canonical State:** Sort keys and encode state snapshot using UTF-8 canonical JSON (zero extraneous whitespace).
2. **Compute SHA-256 Digest:** Compute the hex digest of the canonical state string:
   $$\mathcal{H}(S) = \text{SHA256}(\text{CanonicalJSON}(S))$$
3. **Commit State Checkpoint:** Write snapshot to disk at `session_state.json` or `.agents/<agent>/state.json`.
4. **Integrity Validation on Ingestion:** On session resumption, the receiving agent recomputes $\mathcal{H}(S)$ and asserts equality before executing further actions.

---

## 4. Atomic Session Transition Protocol

When transitioning across turns:

1. **Pre-Transition Validation:**
   - Execute all verification test suites (`python test_plugin.py`).
   - Confirm zero unstaged or corrupt files.
2. **Snapshot Write & Sync:** Write state snapshot and flush buffers to disk.
3. **Dispatch Transfer Message:** Send concise coordination message via `send_message` containing the state snapshot path and verification hash.
4. **Halt Execution:** Complete current turn without scheduling lingering detached tasks.

---

## 5. Recovery & Drift Reconciliation

If a session state hash mismatch is detected upon resumption:

- **Halt Execution:** Do not assume previous state was valid.
- **Diff Reconciliation:** Compare disk state against recorded file hashes in snapshot.
- **Rollback or Re-verification:** Re-run test suites to establish empirical ground truth before resuming task execution.

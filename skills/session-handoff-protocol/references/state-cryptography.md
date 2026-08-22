# State Cryptography, SHA-256 Hashing & Zero-Drift Verification

This reference details the cryptographic serialization and integrity verification algorithms used for session state persistence.

---

## 1. Canonical State Serialization Algorithm

To ensure cryptographic reproducibility across diverse JSON engines:

```python
import hashlib
import json
from typing import Any, Dict

def canonical_serialize(state: Dict[str, Any]) -> bytes:
    """
    Serializes a dictionary to deterministic UTF-8 bytes with sorted keys
    and normalized compact separators.
    """
    return json.dumps(
        state,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")

def compute_state_hash(state: Dict[str, Any]) -> str:
    """
    Computes a cryptographic SHA-256 digest of canonical state.
    """
    serialized = canonical_serialize(state)
    return hashlib.sha256(serialized).hexdigest()
```

---

## 2. Merkle Workspace State Trees

For large multi-file workspaces:

1. **Leaf Hashes:** Compute individual SHA-256 digests for every production file in the workspace:
   $$h_i = \text{SHA256}(\text{read\_bytes}(F_i))$$
2. **Directory Nodes:** Hash sorted pairs of child hashes recursively:
   $$h_{\text{dir}} = \text{SHA256}(h_1 \parallel h_2 \parallel \dots \parallel h_m)$$
3. **Root Tree Hash:** The root digest represents the complete cryptographic snapshot of the workspace filesystem.

---

## 3. Drift Detection & Crash Recovery State Machine

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Ingest session snapshot (session_state.json)             │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Compute candidate hash on disk                           │
└──────────────────────────────┬──────────────────────────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
       [Hashes Match Exactly]         [Hash Mismatch Detected]
                │                             │
                ▼                             ▼
       Resume Task Safely             Enter Drift Recovery:
                                      1. Compare file checksums
                                      2. Isolate mutated files
                                      3. Re-run verification suite
```

---

## 4. Operational Invariants for State Transitions

- **Atomic File Writing:** Write state to a temporary file (e.g. `session_state.tmp`) and atomically rename to `session_state.json` to prevent partial write corruption.
- **Strict Schema Enforcement:** Validate state dictionaries against schema before serializing and immediately after deserializing.
- **Append-Only Event Logs:** Record state transition history in an append-only audit log alongside the snapshot.

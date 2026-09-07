---
name: desert_water
description: The Desert Water Forensic Trajectory Audit & Subterranean Risk Detection Skill. Interrogates software artifacts across five vertical layers from raw byte encoding to distributed subterranean hazards, enforcing byte-level BOM-free UTF-8 hygiene, AST parsing, deterministic handle lifecycles, semantic data lineage, and Via Deserti dimension expansion.
---

# The Desert Water Forensic Trajectory Engine (`desert_water`)

## 1. Executive Purpose & Forensic Doctrine
The **Desert Water Skill** operationalizes the *Desert Water Forensic Doctrine*: software artifacts must be interrogated across five vertical operational strata—from raw byte encoding on physical disk to subterranean concurrency hazards. Evaluating software solely by surface naming conventions or docstrings is an operational pathology. This skill mandates physical byte inspection, Abstract Syntax Tree (AST) parsing, deterministic resource lifecycles, semantic trajectory lineage, and dynamic dimension expansion.

---

## 2. Specialized Specialist Profile

### Specialist: AUD-DES-01 (Chief Forensic Trajectory Auditor)
- **Pedigree**: Subterranean Systems Auditor, Kernel-Level Concurrency Analyst, and Formal Methods Inspector.
- **Operational Posture**: Deep Physicality & Zero-Skimming. Drills through surface facades down to disk bytes, AST nodes, and operating system handles.
- **Core Authority**: Veto power over deliverables exhibiting resource leaks, phantom locks, partial writes, or subterranean concurrency hazards.

---

## 3. The 5-Layer Forensic Interrogation Stack

```
LAYER 0: Surface Integrity
   ├── BOM-Free UTF-8 Byte Validation (Zero 0xEF, 0xBB, 0xBF bytes)
   ├── AST Syntax Tree Verification (No parsing warnings or errors)
   └── Whitespace & Character Hygiene (No trailing carriage returns, clean LF)
              │
              ▼
LAYER 1: Interface Contract Validation
   ├── Defensive Type Boundaries (Strict typing, no loose primitives)
   ├── Nullability Invariants (Explicit null checks, no silent coercions)
   └── Exhaustive Result Enumeration (No implicit swallowed failures)
              │
              ▼
LAYER 2: Operational Mechanism
   ├── Deterministic State Transitions (Finite State Machine verification)
   ├── Atomic Handle Disposal (Every stream/socket enclosed in try/finally)
   └── Bounded Memory Ceilings (Buffers strictly capped at M_buffer <= 64MB)
              │
              ▼
LAYER 3: Complete Trajectory Lineage
   ├── Ingestion -> Transformation -> Disk Storage Sink (Semantic Conservation)
   ├── Append-Only Ledger Commit (SHA-256 transaction chaining)
   └── Replayability Guarantee (Disaster recovery without state loss)
              │
              ▼
LAYER 4: Subterranean Risk Detection
   ├── Phantom Socket Locks (Unclosed child process stdin/stdout hangs)
   ├── Partial NTFS Writes (Atomic file replacement via temporary swap files)
   ├── Lock Inversion Deadlocks (Strict hierarchy on mutex acquisition)
   └── Unbounded Cache Aquifers (LRU/TTL eviction preventing silent OOM)
```

---

## 4. Subterranean Risk Taxonomy & Forensic Audit Runbook

### 4.1 The 5 Subterranean Distributed Hazards
1. **Phantom Socket Lock**: Child processes failing to close IO streams upon exit, leaving parent shells permanently deadlocked.
2. **Partial NTFS Write**: Interrupted writes leaving truncated JSON manifests on physical disk without atomic rollback journals.
3. **Lock Inversion Deadlock**: Thread $A$ acquiring Lock 1 then Lock 2, while Thread $B$ acquires Lock 2 then Lock 1 under concurrent load.
4. **Unbounded Cache Aquifer**: Hash tables and caches continuously appending entries without capacity limits or TTL eviction.
5. **Silent Type Coercion**: Dynamic scripting engines silently coercing nulls to empty strings, bypassing defensive input guards.

### 4.2 Forensic Audit Execution Runbook
1. **Byte Inspection**: Read physical bytes via `[System.IO.File]::ReadAllBytes($target)` to verify zero UTF-8 BOM (`0xEF, 0xBB, 0xBF`).
2. **AST Parsing**: Parse input via language parser (`[Parser]::ParseInput` for PowerShell) to detect empty catch blocks (`statements.Count == 0`).
3. **Handle Audit**: Trace all stream, handle, and socket allocations to ensure enclosing `try/finally` deterministic disposal.
4. **Dimension Expansion**: Execute `powershell -ExecutionPolicy Bypass -File .\scripts\expand_dimensions.ps1` to benchmark against frontier gold standards (*Via Deserti* $X \to Y \to Y_{n.m}$).
5. **Dossier Emission**: Record forensic audit conclusions into `.state/` and append transaction to `.state/ledger/`.

---

## 5. Automation & Tool References
- Dimension Expansion Engine: [`scripts/expand_dimensions.ps1`](../../scripts/expand_dimensions.ps1)
- State Synchronization & Ledger Engine: [`scripts/sync_state.ps1`](../../scripts/sync_state.ps1)
- Production Zero-Stub Law: [Layer 7 Rule](../../rules/07_production_zero_stub_execution.md)

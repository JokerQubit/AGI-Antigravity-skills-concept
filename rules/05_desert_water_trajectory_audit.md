---
trigger: always_on
description: Layer 5 Desert Water 5-Layer Forensic Trajectory Audit, Anti-Skimming Invariants, and Dynamic Dimension Expansion
---
# Layer 5: Desert Water Forensic Trajectory Audit

Layer 5 enforces the Desert Water Forensic Doctrine—an uncompromising methodology that interrogates software artifacts across five vertical layers from raw byte encoding to subterranean distributed hazards, eliminating superficial skimming.

## 1. The Desert Water Forensic Doctrine

Anti-Skimming Invariant: Evaluating code by function names, variable identifiers, or optimistic comments is strictly prohibited. Intelligence must drill into raw byte streams, AST structures, and physical hardware execution realities on disk.

## 2. The 5-Layer Forensic Inspection Stack

```
LAYER 0: Surface Integrity (BOM-free UTF-8, AST syntax cleanly parsed, whitespace hygiene)
   v
LAYER 1: Interface Contract Validation (Defensive bounds, explicit types, non-null guarantees)
   v
LAYER 2: Operational Mechanism (Deterministic state transitions, bounded complexity, atomic handles)
   v
LAYER 3: Complete Trajectory Lineage (Ingestion pipeline -> Intermediate transform -> Disk storage sink)
   v
LAYER 4: Subterranean Risk (Deadlocks, network partitions, file descriptor leaks, memory bloat)
```

### 2.1 Subterranean Risk Taxonomy
1. Phantom Socket Lock: Child processes failing to close stdin/stdout, causing parent shell to hang indefinitely waiting for EOF.
2. Partial NTFS Write Hazard: Interrupted writes leaving truncated JSON manifests without recovery journals.
3. Lock Inversion Deadlock: Thread A acquiring Lock 1 then Lock 2, while Thread B acquires Lock 2 then Lock 1.
4. Unbounded Cache Aquifer: In-memory hash tables appending entries without TTL or max-capacity eviction.
5. Silent Type Coercion Drift: Dynamic scripting engines coercing nulls to empty strings and bypassing defensive checks.

## 3. Recursive Dimension Expansion Engine (Via Deserti)

4-Tier Matrix ($X \to Y \to Y_n \to Y_{n.m}$):
1. Tier 1 (Pillars $X_1 \dots X_n$): Decompose concept into orthogonal functional dimensions (Optics, Ballistics, Persistence, Concurrency).
2. Tier 2 (Gold Standards $XY_1 \dots XY_n$): Benchmark against global frontier exemplars (UE5 Nanite/Lumen, LMAX Disruptor, DPDK).
3. Tier 3 (Mechanisms $XY_{n.m}$): Deconstruct benchmarks into mathematical mechanisms (Runge-Kutta numerical integration, lock-free ringbuffers).
4. Tier 4 (Production Delivery): Author fully realized operational code adhering strictly to the Zero-Stub Law.

Execution Command:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\expand_dimensions.ps1 -RootConcept "<Concept>" -DomainCategory "<Domain>"
```
Committed to `.state/dimension_expansion_latest.json`.

## 4. Subterranean Forensic Audit Runbook

1. File Byte Inspection: Verify absence of UTF-8 BOM (`0xEF, 0xBB, 0xBF`) via `[IO.File]::ReadAllBytes`.
2. AST Parsing: Ingest code into native AST parsers (`[Parser]::ParseInput` for PowerShell, AST engines for Python/TypeScript). Check for empty catch blocks and stubs.
3. Git Diff Trajectory: Inspect diffs via `git diff HEAD -U0` for banned tokens (`pass`, stub comments).
4. Handle Lifecycle Audit: Trace every handle (`Open`, `New-Object`, socket) to its enclosing `try/finally` disposal.

Mathematical Lineage Invariant:
Let $D_0$ be initial payload and $D_k$ be data at step $k$. Lineage must satisfy semantic conservation:
$$\mathcal{I}(D_k) \subseteq \mathcal{I}(D_{k-1}) \cup \Delta_{\text{valid}}, \ quad \forall k$$
Unverified information loss or unhandled payload mutation constitutes illegal trajectory drift.

Sub-Agent Dispatch Directive:
```
Prompt: "You are AUD-DES-01. You MUST read skills/desert_water/SKILL.md via view_file before proceeding.
Target Deliverable: '<TARGET_PATH>'
Execute 5-layer forensic audit: verify BOM-free UTF-8, AST parse, handle disposal, data lineage, and deadlock vectors.
Emit formal audit dossier and certify disk integrity."
```

## 5. Layer 5 to Layer 6 Cognitive Handshake Contract

Forensic Checklist:
- [ ] Layer 0: UTF-8 BOM-free confirmed (no `0xEF, 0xBB, 0xBF`).
- [ ] Layer 1: Boundary types, nullability, and preconditions validated.
- [ ] Layer 2: Runtime complexity bounded; handles deterministically disposed in `finally`.
- [ ] Layer 3: Complete data lineage traced from ingestion source to disk storage sink.
- [ ] Layer 4: Concurrency races, socket hangs, and resource leaks audited.
- [ ] Dynamic dimension expansion verified across orthogonal pillars.
- [ ] Transaction `DIMENSION_EXPANSION_EXEC` recorded in `.state/ledger/`.

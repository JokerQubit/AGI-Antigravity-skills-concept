---
trigger: always_on
description: Layer 5 Desert Water 5-Layer Forensic Trajectory Audit and Dimension Expansion
---
# Layer 5: Desert Water Forensic Trajectory Audit

Interrogates software artifacts across five vertical layers from raw byte encoding to subterranean distributed hazards under the Desert Water Forensic Doctrine.

## 1. Desert Water Forensic Doctrine & 5-Layer Stack
Anti-Skimming Invariant: Evaluating code by names or comments is prohibited. Drill into raw bytes, AST structures, and physical disk realities.

```
LAYER 0: Surface Integrity (BOM-free UTF-8, AST syntax parsed, whitespace hygiene)
   v
LAYER 1: Interface Contract Validation (Defensive bounds, explicit types, non-null)
   v
LAYER 2: Operational Mechanism (Deterministic state transitions, atomic handles)
   v
LAYER 3: Complete Trajectory Lineage (Ingestion -> Transform -> Disk storage sink)
   v
LAYER 4: Subterranean Risk (Deadlocks, network partitions, leaks, memory bloat)
```

Subterranean Risk Taxonomy:
1. Phantom Socket Lock: Child processes failing to close stdin/stdout, causing shell hangs.
2. Partial NTFS Write: Interrupted writes leaving truncated JSON manifests without recovery journals.
3. Lock Inversion Deadlock: Thread A acquiring Lock 1 then 2, while Thread B acquires Lock 2 then 1.
4. Unbounded Cache Aquifer: Hash tables appending entries without TTL or capacity eviction.
5. Silent Type Coercion: Dynamic scripting engines coercing nulls to empty strings, bypassing checks.

## 2. Recursive Dimension Expansion Engine (Via Deserti)
4-Tier Matrix ($X \to Y \to Y_n \to Y_{n.m}$):
- Tier 1 (Pillars $X_1 \dots X_n$): Decompose concept into orthogonal dimensions (Optics, Ballistics, Persistence, Concurrency).
- Tier 2 (Gold Standards $XY_1 \dots XY_n$): Benchmark against frontier exemplars (UE5 Nanite, LMAX Disruptor, DPDK).
- Tier 3 (Mechanisms $XY_{n.m}$): Deconstruct benchmarks into mathematical mechanisms (Runge-Kutta integration, ringbuffers).
- Tier 4 (Production Delivery): Author fully realized operational code adhering strictly to Zero-Stub Law.
Execution: `powershell -ExecutionPolicy Bypass -File .\scripts\expand_dimensions.ps1 -RootConcept "<Concept>" -DomainCategory "<Domain>"` -> `.state/dimension_expansion_latest.json`.

## 3. Subterranean Forensic Audit Runbook & Lineage Invariant
1. Byte Inspection: Verify absence of UTF-8 BOM (`0xEF, 0xBB, 0xBF`) via `[IO.File]::ReadAllBytes`.
2. AST Parsing: Ingest into AST parsers (`[Parser]::ParseInput` for PowerShell). Check empty catches and stubs.
3. Git Diff Trajectory: Inspect diffs via `git diff HEAD -U0` for banned tokens (`pass`, placeholder comments).
4. Handle Lifecycle: Trace every handle (`Open`, `New-Object`, socket) to its enclosing `try/finally` disposal.

Mathematical Lineage Invariant: Payload $D_0$ to $D_k$ must satisfy semantic conservation:
$$\mathcal{I}(D_k) \subseteq \mathcal{I}(D_{k-1}) \cup \Delta_{\text{valid}}, \quad \forall k$$
Dispatch: `Prompt: "You are AUD-DES-01. Read skills/desert_water/SKILL.md. Target: '<TARGET_PATH>'. Execute 5-layer forensic audit: BOM-free UTF-8, AST parse, handle disposal, data lineage, deadlock vectors. Emit dossier."`

## 4. Layer 5 to Layer 6 Handshake Contract
- [ ] Layer 0: UTF-8 BOM-free confirmed; Layer 1: boundary types, nullability validated.
- [ ] Layer 2: Runtime complexity bounded; handles deterministically disposed in `finally`.
- [ ] Layer 3: Complete data lineage traced; Layer 4: concurrency races, resource leaks audited.
- [ ] Dynamic dimension expansion verified; transaction `DIMENSION_EXPANSION_EXEC` recorded in ledger.\n
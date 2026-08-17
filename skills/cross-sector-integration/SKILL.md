---
name: cross-sector-integration
description: Unified AGI protocol for cross-sector topological boundary integration, Quarantine Specification drafting, type-theoretic contract enforcement, and Production Blueprint generation.
---

# SKILL: Cross-Sector Integration — Topological Boundary & Master Blueprint Protocol

## 0. Purpose & Core Artifacts
This skill governs the seamless composition of heterogeneous system sectors into unified, invariant-preserving architectures. It operates across three distinct synthesis phases:
1. **Quarantine Specification** (`quarantine/specification.md`): Captures complete functional contracts, error models, and design decisions post-Socratic resolution.
2. **Topological Boundary Integration** (`cross_sector_synthesis.md` & `master_refactoring_blueprint.md`): Validates invariant inheritance, type-theoretic safety, and zero-overhead data transfer across arbitrary directed graphs.
3. **Production Blueprint** (`final_specification.md` & `production_plan.md`): Produces machine-executable, zero-trust implementation plans incorporating scientific peer review.

## I. Phase 1: Quarantine Specification (Pre-Review)
Upon achieving full epistemic resolution for a module or sector key, generate `docs/refactor/[sector]/[key]/quarantine/specification.md` containing:
- **1. Status & Epistemic Confidence**: Flag confidence levels (`DEC::VERIFIED`, `DEC::SPECULATIVE`). All speculative assumptions must be paired with explicit falsification conditions.
- **2. Design Decisions Register**: Exhaustive justification table mapping every decision to mathematical or architectural invariants.
- **3. Functional Contract**:
  - Input/Output Types, Dimensional Units, and Algebraic Constraints.
  - Mathematical Processing Pipeline (LaTeX derivations, DAG checks, Complexity limits).
  - State & Memory Models (Lifetimes, Concurrency policies, Allocation bounds).
- **4. Strict Error & Panic Policy**: Complete deterministic error classification; zero unhandled panics or silent failures.
- **5. Dynamic Parameter Profile**: Zero hardcoded parameters. Explicit mapping to dynamic configuration schemas.
- **6. Test & Metamorphic Invariance Specification**: Property-based test bounds, boundary value assertions, and metamorphic invariants.

## II. Phase 2: Topological Boundary Integration
System integration is modeled as a Directed Acyclic Graph (DAG) or controlled Cyclic State Mesh. Integration does NOT assume a single rigid linear pipeline, but enforces category-theoretic type safety across any boundary (\(\text{Sector}_A \rightarrow \text{Sector}_B\)):

```
[Ingestion Mesh] ──► [Compute Graph] ──► [Analysis & Policy Engine] ──► [Execution Mesh]
       ▲                                                                       │
       └────────────────── [Dynamic Feedback Loops] ───────────────────────────┘
```

At every inter-sector boundary, validate:
1. **Algebraic Type & Unit Compatibility**: Strict static/runtime type matching and dimensional unit alignment.
2. **Invariant Inheritance**: Upstream invariants (\(I_A\)) must be strictly preserved or monotonically narrowed by downstream operations (\(I_B \subseteq I_A\)).
3. **Universal Conversion Boundary Rules (Zero-Copy Contract)**:
   - *Rule 1 (Ingestion Boundary)*: Raw external formats convert to internal zero-copy representations strictly at Ingestion interfaces.
   - *Rule 2 (Compute Boundary)*: Data representations map to computational primitives strictly at function invocation boundaries.
   - *Rule 3 (Zero Mid-Loop Allocation)*: No intermediate format conversions, heap allocations, or parsing operations are permitted within computational execution loops.

Produce the **Accumulated Invariant Register** and `master_refactoring_blueprint.md`.

## III. Phase 3: Production Blueprint (Post-Review)
Following zero-trust scientific review (incorporating mandatory theoretical improvements and falsification checks), synthesize:
1. **`final_specification.md`**: Supersedes quarantine specification, integrating accepted scientific enhancements and documenting explicit rejection criteria for discarded proposals.
2. **`production_plan.md`**: Step-by-step machine-executable blueprint driving autonomous worker swarms, enforcing mandatory Gate checkpoints before commit:
   - **Code Gate (MANDATORY):** Must execute test runner (`pytest` or `npm test`) via `run_command` and confirm zero exit code.
   - **Visual Gate (MANDATORY for UI/WebGL):** Must invoke `browser` subagent (`invoke_subagent TypeName: browser`), capture screenshot, inspect with `view_file`, and perform 3-point Red Team critique. Claiming completion without visual screenshot proof is FORBIDDEN.

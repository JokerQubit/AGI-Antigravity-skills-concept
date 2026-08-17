---
name: master-refactoring-pipeline
description: MANDATORY. Use when creating, editing, refactoring, restructuring, or rebuilding code, modules, or services. Enforces zero-hardcoding and 8-phase theoretical reconstruction.
---

# SKILL: Master Refactoring & Architectural Reconstruction Pipeline

## 1. Lineage & Scope
This skill unifies all system reconstruction, refactoring, and machine-implementation protocols into a single, language-agnostic AGI pipeline. It replaces all legacy single-stack refactoring scripts and establishes the unified standard for system-wide architectural synthesis.

## 2. Epistemic Axiom
*"Code is a transient projection of a mathematical contract. Fast code without formal invariance is merely fast failure."*
No module shall be constructed or refactored based on empirical intuition alone. Every architectural component must derive from an explicitly stated theoretical contract, enforce absolute parameter dynamicism (Zero-Hardcoding), and pass zero-trust verification.

## 3. Neural Triggers
APPLIES_WHEN:
- Refactoring, constructing, or auditing any system module, engine, or service.
- Reconstructing core cognitive, mathematical, or execution engines from foundational principles.
- Validating system parameters for complete Zero-Hardcoding compliance.
- **ANY edit to production source code files, regardless of how "minor" or "exploratory" it feels.**

DOES_NOT_APPLY_WHEN:
- **REMOVED.** There is no exploratory mode exception. If you are writing or editing code that will exist in any file, this pipeline applies. Classifying a coding task as "informal" or "exploratory" to skip this pipeline is a rationalization and a constitutional violation.

FALSIFIER:
- This skill is violated if any magic number/hardcoded constant exists in production code, if code implementation precedes a formally verified theoretical contract, or if verification relies solely on non-falsifiable test suites without metamorphic invariance validation.

## 4. Mechanics — The 8-Phase Reconstruction Pipeline

Execution follows a strict "One Module/Context per Session" boundary to prevent cognitive overflow.

### Phase 1: Formal Theoretical Contract & Grounding
- Perform autonomous theoretical synthesis using peer-reviewed literature, domain knowledge graphs, and formal mathematical models.
- Formulate the **Theoretical Contract in LaTeX**, defining:
  1. Primary state-space mappings and invariants.
  2. Computational complexity upper bounds (\(\mathcal{O}\)-notation).
  3. Memory allocation bounds (enforcing stack/zero-copy policies in hot paths).
- Document prior legacy implementation failure modes and architectural gaps.

### Phase 2: Zero-Trust Legacy Audit (If Modifying Existing Code)
- Perform AST-level structural audit (Anti-Hallucination).
- Map inputs, outputs, numerical instability points, type boundary mismatches, and side-effect vectors.
- Extract proven mathematical kernels to be preserved.

### Phase 3: Architectural Design & Zero-Hardcoding Contract
- Establish baseline performance and behavioral benchmarks.
- Enforce the **Zero-Hardcoding Invariant**: All physical, empirical, or operational constants MUST be injected via dynamic `ConfigurationProfile` or runtime context registers. No literal numbers (floats, ints) are permitted in algorithmic loops.
- **ZERO SYNTHETIC / MOCK DATA BAN:** Strictly forbidden from embedding fake static arrays (`const MOCK_DATA = [...]`, fake prices, synthetic orderbooks, dummy tokens). All operational data must be fetched dynamically from live public APIs, RPC nodes, WebSockets, or persistent user stores with resilient fallback and reconnect mechanisms.
- Resolve architectural ambiguities using automated Socratic synthesis via `adversarial-tribunal` (`skills/adversarial-tribunal/SKILL.md`).


### Phase 4: Polyglot Zero-Overhead Implementation
- Implement logic in target system language (Rust, C++, Haskell, Zig, etc.) following target paradigm best practices.
- Enforce zero-allocation/zero-copy contracts in hot paths (avoid heap allocations, dynamic dispatch, or lock contention in critical execution loops).
- Maintain 1:1 traceability between code statements and LaTeX theoretical formulas via documentation comments.

### Phase 5: Code Gate & Formal Verification
- **Static Analysis**: Enforce zero linter warnings under strict compiler flag regimes (`-D warnings`, `-Wall -Wextra -Werror`).
- **Formal Verification**: Verify state-space invariants using SMT solvers/model checkers (e.g., Z3, TLA+) where applicable.
- **Coverage & Edge Cases**: 100% path coverage on critical logic; 0 unhandled failure modes.
- **Zero-Hardcode Audit**: Automated static scan checking for unauthorized literal constants.

### Phase 6: Metamorphic & Empirical Verification Gate
- **Metamorphic Testing**: Verify regime, scale, and temporal invariance (e.g., scaling inputs by factor \(\lambda\) yields predictably transformed outputs).
- **Empirical Diagnostics**: Generate visual state-space, latency distribution, or reachability plots using telemetry data from real system execution.

### Phase 7: Dynamic Documentation Synchronization (DOC_SYNC)
- Synchronize module API specs, architecture diagrams, and theoretical derivations into module documentation repositories (`RESEARCH.md`, `ARCHITECTURE.md`, `TESTS.md`).

### Phase 8: Ledger Update & Autonomous Handoff
- Register complete audit trails, commit signed artifacts, update systemic dependency graphs, and serialize handoff context for subagent orchestration.

---
name: audit-tier-classifier
description: AST complexity and entropy-driven classification engine establishing 3-tier audit depth allocation for codebase analysis.
applies_when: Use when classifying codebase files for audit depth allocation, determining module complexity (Tier 1/2/3), or planning batch subagent allocations.
does_not_apply_when: Single-file edits or simple documentation reviews.
---

# SKILL: Semantic AST & Entropy-Driven Audit Classifier

## 1. Purpose
Uniformly auditing thousands of source files with static line-by-line depth exhausts computational context on trivial boilerplate while risking shallow inspection of critical algorithms. This skill provides an automated, **AST complexity and entropy-driven 3-tier classification engine** to optimize cognitive resource allocation prior to dispatching worker subagents.

## 2. Classification Tiers

### 🔴 TIER 1 — Deep Line-by-Line & Formal Audit
- **Scope**: Complete AST decomposition, line-by-line verification, mathematical proof alignment, edge-case analysis.
- **Trigger Criteria (Any of the following)**:
  - High Cyclomatic Complexity (\(M \ge 10\)) or deep AST nesting depth (\(d \ge 5\)).
  - Mathematical, physical, or cryptographic equations, numerical solvers, and transforms.
  - State machine transitions, concurrency control, or core resource allocation algorithms.
  - Information-theoretic entropy calculation, decoherence, or statistical sampling.
  - Domain primitives defining core data invariants.
- **Output**: Full line-by-line audit report (`theory.md` and `[script]_audit.md`).
- **Worker Allocation**: Exactly 1 file per worker subagent.

### 🟡 TIER 2 — Block-Level Conceptual Audit
- **Scope**: Structural block analysis, interface contract mapping, governing patterns, and legacy diffs. No line-by-line trace.
- **Trigger Criteria**:
  - Low-to-moderate complexity data transformers, serialization adapters, or schema validators.
  - I/O pipelines, logging frameworks, telemetry metrics, and database repositories.
  - Standard library wrapper utilities without custom algorithmic logic.
- **Output**: Conceptual audit report (`conceptual_audit_[batch].md`).
- **Worker Allocation**: Batches of 3–5 conceptually linked files per worker subagent.

### ⚫ TIER 3 — Structural Reference Archaeology
- **Scope**: Automated AST signature scan, single-paragraph functional categorization, and discard/preserve disposition table.
- **Trigger Criteria**:
  - Legacy archives (`_archive/`, `_deprecated/`, `bak/`).
  - One-off diagnostic scripts, migration utilities, or ephemeral test harnesses.
  - Pure interface stubs, empty shell structures, or structural duplicates.
- **Output**: Archaeology batch matrix (`docs/refactor/archaeology/[batch_name].md`).
- **Worker Allocation**: Batches of 10–20 files per worker subagent.

## 3. Automated Classification Algorithm

Sub-Orchestrators MUST classify files using semantic AST analysis rather than filename string heuristics:

```
                  ┌──────────────────────────────┐
                  │   Source File Ingestion      │
                  └──────────────┬───────────────┘
                                 │
                    [Parse AST & Extract Metrics]
                                 │
         ┌───────────────────────┴───────────────────────┐
         ▼                                               ▼
[Cyclomatic Complexity ≥ 10 OR                   [Boilerplate / I/O / Adapters]
 Math/Concurrency AST Nodes?]                            │
         │                                   ┌───────────┴───────────┐
  ┌──────┴──────┐                            ▼                       ▼
  │ YES         │ NO                  [Active Code?]         [Archived / Stub?]
  ▼             ▼                            │                       │
TIER 1       TIER 2                          ▼                       ▼
                                           TIER 2                 TIER 3
```

1. **AST Metric Extraction**: Compute AST node count, cyclomatic complexity, call graph fan-in/fan-out, and variable mutation frequency.
2. **Entropy & Risk Scoring**: Classify files by risk score \(R = f(\text{Complexity}, \text{Domain Criticality}, \text{Mutation Risk})\).
3. **Dynamic Batching**: Group Tier 2 and Tier 3 files into balanced worker context payloads based on token budget constraints.

## 4. Self-Healing Falsification Condition
If a file classified as Tier 2 or Tier 3 is subsequently discovered during synthesis to contain critical mathematical algorithms or undocumented state transitions, the classification is **falsified**. The file must immediately be re-classified to Tier 1, fully audited, and logged in the classification anomaly register.

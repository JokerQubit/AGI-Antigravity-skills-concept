---
name: swarm-legacy-archaeology
description: Consolidated skill for multi-level parallel swarm auditing of legacy repositories. Handles directory mapping, tier classification, batch planning, handoff generation, dashboard progress tracking, gap analysis, and the coverage gate.
---

# SKILL: Universal Corpus Archaeology & Semantic Dependency Mapper

## I. Platform-Agnostic Corpus Scanning Engine
Replaces OS-specific shell invocations with a cross-platform semantic filesystem scanner that produces an Abstract Syntax Tree (AST) & Dependency Graph representation of the target repository:
- Extracts structural tokens, symbol cross-references, call graphs, and type definitions.
- Computes structural complexity metrics (Cyclomatic Complexity, Halstead Volume) to automatically assign Tier classifications (T1 Critical Core, T2 Module Interface, T3 Utility/Data).

## II. Topological Coverage & Invariant Verification Gate
Replaces filename string-matching with a Semantic AST Invariant Proof:
- `COVERAGE_GATE`: Evaluates whether 100% of exported symbols, functions, types, and mathematical models in the source corpus have matching formal specifications and test vectors in the target architecture.
- Generates a formal diff proof report (`semantic_coverage_proof.json`).

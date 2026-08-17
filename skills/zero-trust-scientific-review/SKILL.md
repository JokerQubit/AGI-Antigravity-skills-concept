---
name: zero-trust-scientific-review
description: AGI/ASI Scientific Review Protocol. Governs mandatory zero-trust adversarial review of architectural specifications. Dynamically stress-tests mathematical models, performance bounds, robustness contracts, and safety guarantees before blueprinting.
---

# SKILL: Zero-Trust Scientific Review — ASI Protocol

> *"In an AGI system, a specification is not a plan; it is a hypothesis waiting to be destroyed. We do not review to validate; we review to falsify."*

---

## 1. Core Philosophy: Epistemic Zero-Trust

This protocol serves as the ultimate epistemic firewall before architectural blueprinting. The reviewing swarm operates under total skepticism:
- **No Unproven Assertions:** Every mathematical formula, state transition, and parameter bound in `quarantine/specification.md` is assumed flawed until proven correct.
- **Dynamic Scope Scaling:** The depth of review scale dynamically with theoretical complexity and system criticality, replacing arbitrary fixed quotas.

**Input:** `quarantine/specification.md`  
**Output:** `quarantine/scientific_review.md`

---

## 2. Multi-Agent Adversarial Review Flow

```
           [quarantine/specification.md]
                         │
                         ▼
        ┌─────────────────────────────────┐
        │   Phase 1: Adversarial Search   │
        │   (Literature & Edge-Case Search) │
        └────────────────┬────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────┐
        │   Phase 2: Falsification Swarm  │
        │  (Math, Perf, Safety, Edge-Case)│
        └────────────────┬────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────┐
        │ Phase 3: Structural Verification│
        │ (Zero-Alloc, Bounds, Typing)    │
        └────────────────┬────────────────┘
                         │
                         ▼
        ┌─────────────────────────────────┐
        │   Phase 4: Verdict & Synthesis  │
        └────────────────┬────────────────┘
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
   [APPROVED]                  [RETURN_TO_GRILL_ME]
```

### Phase 1: Multi-Vector Adversarial Search
Query scientific engines and domain databases targeting failure modes:
1. **Falsification Query:** "What are the known breakdown points, numeric instability modes, or edge-case failures of [Core Model/Algorithm]?"
2. **Comparative Benchmark Query:** "What state-of-the-art alternative implementations outperform [Proposed Approach] in latency, safety, or space complexity?"
3. **Empirical Boundary Query:** "Under what boundary conditions does [Proposed Approach] exhibit chaotic behavior or NaN propagation?"

### Phase 2: Dynamic Improvement Mandate (Context-Driven Quotas)
Rather than static numerical quotas, the review engine dynamically calculates required improvement vectors based on spec complexity:

- **Mathematical Integrity Vector:** Derivation accuracy, numeric stability, dynamic parameter bounds.
- **Performance & Scalability Vector:** Asymptotic time/space bounds, memory allocation footprint ($O(1)$ zero-alloc target), concurrency model.
- **Systemic Robustness Vector:** Edge-case handling, fault containment, graceful degradation pathways.
- **Safety & Boundary Contract Vector:** Division-by-zero protection, overflow bounds, state invariants.

Each identified improvement must follow the structured schema:
```text
IMP-[NNN]:
  Title:       [Descriptive Name]
  Vector:      [Mathematical | Performance | Robustness | Safety | Completeness]
  Defect:      [Exact flaw or sub-optimal logic in specification]
  Remediation: [Mathematically grounded proposed modification]
  Evidence:    [Citation, paper reference, or formal proof]
  DEC_Level:   [DEC::PROVEN | DEC::GROUNDED | DEC::INFERRED]
  Verdict:     [ACCEPTED | REJECTED]
```
> **DEFERRED IS BANNED:** The `DEFERRED` verdict is abolished. Every identified flaw must be either `ACCEPTED` (fix committed) or `REJECTED` (with documented rationale proving why it is not a real defect). Parking issues as "deferred" and proceeding is a constitutional violation.

### Phase 3: Architectural Invariance Checklist
- **Typing & Boundaries:** Are all input/output state spaces explicitly typed with strict boundary bounds?
- **Zero Hardcoding:** Are all parameters dynamically derived via theoretical formulas?
- **State Invariance:** Is total system state deterministic, memory-bounded, and free from memory leaks or unbounded state growth?

---

## 3. Verdict Conditions & Output Artifact

The protocol generates `quarantine/scientific_review.md`.

### Blocking Conditions (Forcing `RETURN_TO_GRILL_ME`):
1. **Mathematical Falsification:** Discovery of an irrecoverable mathematical error or numerical instability in core equations.
2. **Asymptotic Suboptimality:** Evidence proving the proposed approach is asymptotically inferior to existing state-of-the-art alternatives.
3. **Safety Violation:** Potential for unhandled NaN propagation, infinite loops, or state corruption.

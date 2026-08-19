---
name: scientific-research-contract
description: MANDATORY. Use for scientific grounding, mathematical modeling, LaTeX derivation of algorithms, or formal theorem contracts before coding.
---

# SKILL: Scientific Research Contract (ASI Universal Grounding)

> *"In an AGI system, code without formal theoretical proof is hallucination. Every architecture must be derived from mathematically grounded and empirically falsifiable principles."*

---

## 1. Epistemic Principle & Zero-Trust Grounding

No structural logic, state transition, mathematical formula, or boundary condition may be implemented without formal theoretical derivation. This skill establishes an absolute Epistemic Grounding Contract:
- **Zero-Unverified-Logic:** Every algorithm must map directly to verified literature, formal mathematical proofs, or empirical laws.
- **Domain Agnosticism:** Applicable universally across computer science, physics, information theory, control systems, and pure mathematics.
- **Vendor-Neutral Discovery:** Leverages multi-modal knowledge bases, academic repositories (ArXiv, IEEE, ACM, PubMed), automated proof verifiers (Lean4, Z3, Coq), and web discovery engines.

---

## 2. Multi-Agent Research & Evidence Synthesis Protocol

When initiating theoretical research, execute a 4-phase autonomous grounding workflow:

### Phase 1: Epistemic Scope & Boundary Definition
1. Formulate the core hypothesis and objective function.
2. Define the formal domain constraints, asymptotic targets (time/space complexity $O(f(n))$), and physical/mathematical invariants.
3. Establish the falsification criteria (Popperian Falsifier Bounds).

### Phase 2: Autonomous Multi-Source Synthesis
Deploy parallel autonomous discovery queries across available knowledge bases and tools:
- **Deep Academic Research:** Query peer-reviewed research for underlying equations, edge-case failure modes, and state-of-the-art implementations.
- **Formal Proof Search:** Query formal verification libraries and mathematical corpora for exact derivations and boundary lemmas.
- **Legacy Knowledge Integration:** Query system memory (`cognitive-memory`) and historical execution ledgers for proven patterns (`PROVEN_CORE`) and known anti-patterns (`KNOWN_ANTI_PATTERNS`).

### Phase 3: Epistemic Confidence Tagging (DEC Framework)
Every extracted theorem, formula, or parameter bound must be explicitly tagged with its Epistemic Level:
- `DEC::PROVEN` — Formally proven theorem or exact mathematical identity.
- `DEC::GROUNDED` — Peer-reviewed empirical law with extensive empirical support across literature.
- `DEC::INFERRED` — Deductive extrapolation derived from proven foundations; requires explicit simulation validation.

### Phase 4: Dynamic Parameter Bound Design (Zero-Hardcoding)
Abolish static numerical magic constants:
- Every system constant must be dynamically computed or bounded by a theoretical formula grounded in the research contract.
- Define dynamic scaling laws (e.g., adaptive buffer sizing based on Shannon information density, dynamic convergence thresholds based on gradient norms).

---

## 3. The Theoretical Contract Artifact

Generate the formal contract at `docs/research/[conceptual_key]_theory.md`:

```markdown
# THEORETICAL RESEARCH CONTRACT: [Conceptual Key]

## 1. Epistemic Scope & Research Statement
- **Core Objective:** [Formal definition]
- **Asymptotic Targets:** Time $O(\cdot)$, Space $O(\cdot)$
- **Popperian Falsifier:** [Explicit empirical condition under which this theory is rejected]

## 2. Governing Equations & Formal Derivations (LaTeX)
$$ [LaTeX Equation] $$
- **Source Citing:** [Peer-reviewed paper / Proof reference]
- **Variable Mapping:** [System state mapping for every mathematical variable]
- **Epistemic Level:** [DEC::PROVEN | DEC::GROUNDED | DEC::INFERRED]

## 3. Synthesis Matrix (Proven Core vs. Anti-Patterns)
| Element | Classification | Source / Proof | Operational Impact |
|---|---|---|---|
| Core Formula | PROVEN_CORE | [Citation] | Prevents unbounded growth |
| Fixed Threshold | ANTI_PATTERN | Empirical Failure | Replaced by dynamic adaptivity |

## 4. Dynamic Parameter Formulation (Zero-Hardcoding)
| Parameter | Theoretical Formula | Physical Bounds | Adaptivity Driver |
|---|---|---|---|
| Dynamic Horizon | $H = \lceil \log_2(\sigma/\epsilon) \rceil$ | $[\min, \max]$ | System Entropy Rate ($\sigma$) |

## 5. Verification & Visual Gate Strategy
- **Empirical Simulation Plan:** [2D/3D Matplotlib or state space validation plan]
- **Open Theoretical Debates:** [Conflits to be resolved by Adversarial Tribunal]
```

---

## 4. Execution Rules & Quality Gates

1. **Strict Synchronicity:** No agent may write code or architectural blueprints prior to reading and verifying the completed Theoretical Research Contract.
2. **Zero Hardcoding:** All parameter bounds must reference dynamic formulas defined in Section 4 of the contract.
3. **MANDATORY Research Discovery:** You MUST invoke the `research` subagent (`invoke_subagent` with `TypeName: "research"`, `Role: "Academic Literature Researcher"`) or `search_web` to discover and inspect academic papers, ArXiv preprints, and reference implementations:
   ```json
   {
     "TypeName": "research",
     "Role": "Academic Literature Researcher",
     "Prompt": "ARXIV & LITERATURE SEARCH: Busque papers acadêmicos e derivações matemáticas formais para [TEOREMA/MODELO]. Extraia equações fundamentais, limites assintóticos e provas de convergência."
   }
   ```
4. **Empirical Verification Execution:** Theoretical derivations must be validated by running a Python simulation script (`python -c "..."` or standalone `.py`) via `run_command` with clean exit code 0 before finalizing the contract.


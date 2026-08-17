---
name: pragmatic-quality-inspection
description: Consolidated master quality framework enforcing Evidence-Before-Assertion (Anti-Hallucination), Prompt Dispatch Shielding, Worker Report Verification, and Safety-First Architectural SWOT Analysis.
---

# SKILL: Pragmatic Quality Inspection

> *"Unverified claims corrupt context. Unguided dispatches waste compute. Naive risk models court disaster."*

---

## GATE 1: Anti-Hallucination (Evidence-Before-Assertion)

**Trigger:** Any agent asserts file state, variable definition, or system behavior.  
**Zero-Trust Rule:** No claim is valid without an explicit tool output citation within the current session execution graph.

1. **Detection Phrases:** `"the file contains...", "I recall...", "the logic is currently..."`
2. **Mandatory Action:** Execute view/search tool (`view_file`, `grep_search`).
3. **Citation Contract:** Quote exact lines from tool output with file path and line numbers.
4. **Self-Correction Protocol:** If unverified assumption was made, stop immediately, fetch data, and emit:  
   `"Correction: I inspected [Path#L-L]; actual state is [Y]."`

---

## GATE 2: Prompt Quality Shield (Pre-Dispatch Validation)

**Trigger:** Dispatching a subagent worker or generating an autonomous task execution payload.  
**Rule:** Validate prompt structural completeness prior to dispatch. If invalid, auto-repair before launch.

### Mandatory Prompt Schema
1. **Identity & Context:** Target Domain, Subagent Role, Objective, Audit/Execution Tier.
2. **Atomic Task Contract:** Explicit target file paths, reference benchmarks, and clear scope boundaries.
3. **Deterministic Output Specification:** Exact file paths, schema format, and required verification metrics.
4. **Epistemic Labeling Demand:** Mandatory `DEC::` classification on all assertions.

**Verdict:** Emit `PROMPT_VERDICT::APPROVED` or `PROMPT_VERDICT::REJECTED`. If rejected, pass through Automated Prompt Repair Engine.

---

## GATE 3: Worker Report & Artifact Acceptance

**Trigger:** Worker subagent submits an audit, code artifact, or design specification.  
**Rule:** No artifact enters system synthesis without satisfying verification bounds.

### Acceptance Criteria
- [ ] Complete file coverage (zero "left as exercise" placeholders).
- [ ] Theoretical/Mathematical justification supported by cited references.
- [ ] All claims tagged with formal epistemic levels (`DEC::PROVEN`, `DEC::GROUNDED`, `DEC::INFERRED`, `DEC::SPECULATIVE`).
- [ ] Mandatory Verification Pass: Clean build/execution, zero lint errors, test coverage exceeding threshold, zero invariant violations.

**Verdict:** Emit `REVIEW_VERDICT::ACCEPTED`, `ACCEPTED_WITH_REVISIONS`, or `REJECTED`.

---

## GATE 4: Safety-First Architectural SWOT Analysis

**Trigger:** Evaluating any proposed system architecture, algorithm, or strategic transition.  
**Rule:** Enforce non-linear safety-first decision theory.

### Matrix Construction
1. **Strengths (S):** Verified, quantifiable system capabilities.
2. **Weaknesses (W):** Internal structural flaws: `[Flaw] → [Consequence] → [Severity]`.
3. **Opportunities (O):** Ecosystem potential and performance upsides.
4. **Threats (T):** Falsification vectors: `IF [Condition] THEN [Impact] (Probability P, Severity S)`.

### Safety-First Decision Algorithm (Minimax Veto Rule)
Traditional linear counting is strictly prohibited. Decision scoring must adhere to:

\[
\text{If } \exists T_i \in \text{Threats} \text{ such that } \text{Severity}(T_i) \in \{\text{CRITICAL}, \text{EXISTENTIAL}\} \implies \mathbf{VERDICT = REJECTED}
\]

Otherwise, compute weighted score:
\[
\text{Score} = \sum w_s S - \sum w_w W + \sum w_o O - \sum w_t T
\]
- \(\text{Score} \ge +0.6 \implies \mathbf{APPROVED}\)
- \(+0.2 \le \text{Score} < +0.6 \implies \mathbf{CONDITIONAL\_QUARANTINE}\)
- \(\text{Score} < +0.2 \implies \mathbf{REJECTED}\)

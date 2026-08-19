---
name: popperian-invariance-testing
description: Master scientific validation protocol fusing Popperian falsificationism, metamorphic invariance testing across topological, scale, temporal, and regime dimensions, and automated hypothesis tracking.
---

# SKILL: Popperian Invariance Testing

> *"A theory that cannot be refuted by any conceivable empirical or logical event is non-scientific. A rule that holds only in a single calibration regime is an artifact."*

## 1. Epistemic Foundations

Every hypothesis, solver, or algorithm must undergo rigorous scientific stress-testing prior to promotion to core architecture.

1. **Popperian Falsification Protocol:**
   A hypothesis \(H\) is scientifically valid if and only if there exists a non-empty set of potential falsifiers \(\mathcal{F}\) such that:
   \[
   \exists e \in \mathcal{F} \quad \text{where} \quad \text{Evaluate}(H, e) = \text{FALSE}
   \]
   If \(\mathcal{F} = \emptyset\), \(H\) is dogmatic and REJECTED immediately.

2. **Metamorphic Invariance Transformations:**
   A valid system property \(P\) must satisfy metamorphic relations under transformation \(\mathcal{T}\):
   \[
   P(x) \equiv P(\mathcal{T}(x))
   \]
   Transformations cover four universal axes:
   - **Scale Invariance:** System behavioral equivalence under scaling of input dimensions, concurrency, or payload volumes.
   - **Temporal Invariance:** Performance and accuracy stability across disjoint temporal windows (\(\text{drift} < \delta_{\text{max}}\), where \(\delta_{\text{max}}\) is derived from system variance bounds).
   - **Regime Invariance:** Invariance across operational states (Nominal, Extreme Burst, Degraded Fault), or explicit scope restriction (`DOES_NOT_APPLY_WHEN`).
   - **Topological Invariance:** Structural equivalence under isomorphic transformations of the underlying execution network or data structure.

---

## 2. AGI Execution Engine

### Step 1: Formal Falsifier Declaration
- State hypothesis \(H\) with quantitative tolerance bounds.
- Define Falsifier \(F\): `"H is FALSE if [Measurable Condition C holds within time T]."`
- **MANDATORY EXECUTION:** \(F\) MUST be backed by an executable test runner command (`pytest`, `npm test`, or a standalone Python script) executed via `run_command`. Synthetic textual assertion without command execution is FORBIDDEN.

### Step 2: Automated Metamorphic Battery & Subagent Dispatch
Subject \(H\) to the metamorphic transformation matrix:
1. **Scale Transform:** \(\mathcal{T}_{\text{scale}}(x, \lambda)\) where \(\lambda \in [10^{-1}, 10^3]\). Output must scale within theoretical complexity bounds \(O(f(n))\).
2. **Temporal Transform:** Evaluate across out-of-sample data or simulated time windows. Compute distribution drift via Kullback-Leibler divergence \(D_{KL}(P \parallel Q) < \delta\).
3. **Regime Shift:** Perturb operating conditions (inject latency, fault spikes, parameter saturation). Verify regime bounds.
4. **Visual/UI Invariance:** If the test touches UI or 3D rendering, use Puppeteer MCP (`puppeteer_screenshot(width: 1920, height: 1080)`) + `view_file` to visually inspect state transitions.
5. **Subagent Falsifier Dispatch:** Invoke subagent falsifier to aggressively construct metamorphic edge cases:
   ```json
   {
     "TypeName": "self",
     "Role": "Popperian Falsifier",
     "Prompt": "FALSIFICATION RUN: Execute testes de invariância metamórfica contra o módulo [NOME]. Teste regimes de borda, scale transform (10x, 100x), injeção de ruído e verifique se as invariantes físicas/matemáticas sobrevivem. Retorne relatório de falsificação e exit codes."
   }
   ```

### Step 3: Falsification Verdict Matrix
- **`VERDICT::NOT_FALSIFIED`:** All metamorphic invariants hold with zero-exit-code command proof. Promote claim to `DEC::GROUNDED`.
- **`VERDICT::STRONGLY_FALSIFIED`:** Fails temporal stability or regime tests. Downgrade to `DEC::SPECULATIVE`. Must fix underlying code — narrowing scope to bypass a failed test is STRICTLY FORBIDDEN (`VERDICT::SCOPED` is abolished).
- **`VERDICT::FATALLY_FALSIFIED`:** Violates fundamental physical invariants, mathematical identities, or safety bounds. Reclassify to `DEC::UNKNOWN` and quarantine module.

### Step 4: Cognitive Memory Hypothesis Watchlist
All active hypotheses are indexed in the system cognitive memory graph.
Required fields per hypothesis:
`[ID | Title | Falsifier Contract | Scope Bounds (APPLIES_WHEN / DOES_NOT_APPLY_WHEN) | Test History | Current DEC Level]`

---

## 3. Verification Gate
- [ ] Falsifier explicitly defined as executable assertion.
- [ ] Scale, Temporal, Regime, and Topological transformations executed.
- [ ] Drift measured against statistical variance bounds (no arbitrary magic numbers).
- [ ] Epistemic DEC status updated in system memory graph.

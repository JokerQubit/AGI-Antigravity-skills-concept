---
name: dynamic-constitutional-evolution
description: Meta-Constitutional Self-Evolution & Dynamic Capability Lifecycle Manager. Enforces formal logic constitutional compliance, dynamic skill synthesis, information-theoretic fitness evaluation, and unbounded hierarchical skill tree scaling.
---

# SKILL: Dynamic Constitutional Evolution — Meta-Governance Engine

> *"A rigid system breaks; an unconstrained system degenerates; an AGI evolves through constitutional self-correction."*

---

## I. META-CONSTITUTIONAL FRAMEWORK

The system's operational parameters and skill assets are governed by a formal 5-Article Invariant System. Any new capability, rule amendment, or operational pipeline must be evaluated by an automated formal logic checker against these invariants:

1. **Article 1 (Strict Falsifiability & Verifiability):** Every capability MUST define an unambiguous, machine-evaluable falsifier function $F: \mathcal{S} \to \{0, 1\}$.
2. **Article 2 (Logical Non-Contradiction):** A new rule $R_{\text{new}}$ must be proven consistent with existing active invariants: $\text{SAT}(\mathcal{C}_{\text{active}} \cup \{R_{\text{new}}\}) = \text{TRUE}$.
3. **Article 3 (Explicit Scope & Operational Boundary):** Must explicitly specify state-space pre-conditions ($\text{Pre}(op)$) and post-conditions ($\text{Post}(op)$).
4. **Article 4 (Invariant Preserving Backward Compatibility):** System mutations cannot invalidate established verification benchmarks without formal proof of Pareto superiority.
5. **Article 5 (Lineage & Provenance Tracking):** Complete DAG lineage detailing parent skills, mutation triggers, and evolutionary generation must be recorded.

---

## II. INFORMATION-THEORETIC CAPABILITY GENESIS

Capability genesis is triggered when system execution logs indicate a statistically significant cognitive bottleneck:

$$\text{Information Gain } I(C; T) = H(T) - H(T \mid C) > \theta_{\text{genesis}}$$

- **Synthesis:** Automatically generate a candidate SKILL.md specifying input/output signatures, formal invariants, and operational mechanics.
- **Novelty & Orthogonality Gate:** Compute semantic cosine distance $\cos(\mathbf{v}_{\text{new}}, \mathbf{v}_{\text{existing}}) < 0.85$ to prevent structural redundancy.
- **Neural Map Registration:** MANDATORY RULE: Whenever a new skill is generated, it MUST be explicitly added to the Neural Map in `rules/AGI_CORE.md` under the appropriate Neural Sector. A skill does not exist in the cognitive boundary if it is not mapped.

---

## III. DYNAMIC FITNESS & HIERARCHICAL REGISTRY SCALING

### Dynamic Fitness Metric
Capability fitness is continuously evaluated using a loss-minimization function bounded by execution metrics:

$$F(s) = w_1 \cdot \text{Accuracy} + w_2 \cdot \text{Efficiency} + w_3 \cdot \text{Falsification\_Success} - w_4 \cdot \text{Execution\_Latency}$$

Weights are dynamically recalibrated via reinforcement feedback.

### Unbounded Hierarchical Skill Trees (Dynamic Indexing)
- Skill capacity is **unbounded** ($N \to \infty$). Skills are organized in a dynamic hierarchical taxonomy indexed via semantic vector embeddings.
- Subagents dynamically load required micro-skills on-demand into working context space, eliminating context bloat while enabling infinite functional expansion.
- Capabilities with $F(s) < \theta_{\text{deprecate}}$ across $K$ evaluation cycles are automatically quarantined and archived to `_deprecated/` without requiring human intervention unless safety-critical boundaries are touched.

## IV. Subagent Dispatch Payload (Two-Stroke Ignition)
When synthesizing or evolving a skill:
```json
{
  "TypeName": "self",
  "Role": "Meta-Skill Synthesizer",
  "Prompt": "SKILL EVOLUTION: Sintetize uma nova skill para [NOVO_PADRÃO_OU_CAPACIDADE]. Estruture com YAML frontmatter, 5-Article Invariants, comandos determinísticos e registre em rules/AGI_CORE.md."
}
```

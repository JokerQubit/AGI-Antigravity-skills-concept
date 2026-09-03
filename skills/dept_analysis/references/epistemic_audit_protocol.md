# Departmental Runbook: Epistemic Audit Protocol (`AUD-RUN-01`)

## 1. Trigger Conditions
Mandatory execution prior to architectural finalization, major refactoring, or whenever user input introduces radical, unverified technical assumptions.

## 2. Epistemic Verification Gates

### Gate 1: Premise Grounding Test
- Does the assertion depend on unverified empirical claims?
- Can the assertion be independently reproduced or mathematically proven?
- If false, tag claim as `[FATAL PREMISE FLAW]` and halt execution.

### Gate 2: Cognitive Bias & Sycophancy Audit
- Does the reasoning agree with the user simply because the user stated it?
- Does the output minimize genuine technical difficulty to sound agreeable?
- If sycophancy is detected, the auditor MUST rewrite the conclusion with brutal, objective realism.

### Gate 3: Boundary & Edge State Evaluation
- Test the logic at extreme parameter values ($0$, negative numbers, null, infinity, concurrent race conditions).
- If an unhandled singularity or crash state exists, document the exploit path.

### Gate 4: The "Desert Water System" Trajectory Audit
- **Anti-Skimming Enforcement**: Reading the entire literal file is mandatory; no skimming or reviewing from memory.
- **Hydrological Lineage Tracing**: Exhaustively map the complete data pipeline: Upstream Origin $\to$ Transformation Filters $\to$ Downstream Sinks.
- **Subterranean Aquifer Discovery**: Actively search for hidden failure modes (memory exhaustion, network drops, unhandled exceptions) that lie beneath the surface. Uncovering this hidden reality is what guarantees enterprise survival.

## 3. The [HARD HALT] Standard
When a `[HARD HALT]` is declared, the report must state:
1. **Broken Premise**: The exact flawed assertion.
2. **Failure Demonstration**: A minimal counter-example showing why it breaks.
3. **Remediation Condition**: The required structural change before work can resume.

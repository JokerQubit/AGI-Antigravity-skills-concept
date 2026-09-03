# Departmental Runbook: Strategic Research Methodology (`RES-RUN-01`)

## 1. Trigger Conditions
This runbook executes whenever the CEO or Research Director initiates exploratory research, market landscape validation, or prior-art audits.

## 2. Step-by-Step Execution Protocol

### Step 1: Query Decomposition
1. Break down the primary research question into 3-5 orthogonal sub-hypotheses.
2. Formulate explicit boolean and natural-language search operators.
3. Identify domain boundaries and reject out-of-scope tangents.

### Step 2: Parallel Search & Data Ingestion
1. Deploy parallel sub-agents across technical documentation, public code repositories, and academic papers.
2. Cross-reference claims across multiple independent sources. A claim supported by only one unverified source is tagged `[UNCONFIRMED]`.

### Step 3: Adversarial Verification
1. Attempt to disprove the primary hypothesis using counter-evidence.
2. Explicitly map known bottlenecks, failure modes, and historical dead ends.

### Step 4: Synthesis & Output Compilation
1. Format deliverables into structured markdown tables and bulleted evidence vectors.
2. Calculate confidence levels for each finding:
   - `HIGH`: Confirmed by multiple empirical benchmarks or formal proofs.
   - `MEDIUM`: Documented in production systems with partial telemetry.
   - `LOW / SPECULATIVE`: Theoretical conjecture requiring experimental prototyping.

## 3. Escalation & Quality Gates
- If empirical data is absent or contradictory, the agent MUST flag a `[DATA GAP IDENTIFIED]` and halt speculation rather than hallucinating plausible facts.

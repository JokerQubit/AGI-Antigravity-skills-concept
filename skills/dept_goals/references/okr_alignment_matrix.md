# Departmental Runbook: OKR Alignment & Critical Path Formulation (`GOAL-RUN-01`)

## 1. Trigger Conditions
Executes whenever a new project, sprint, or complex cross-functional feature is initiated by the CEO.

## 2. Formulation Guidelines

### Metric Verification Filter
Every Key Result must satisfy the **Binary Verification Invariant**:
- Bad KR: "Improve code performance." (Subjective, unverified).
- Good KR: "Reduce memory overhead of the AST parser from 450MB to < 120MB on a 50k-line benchmark." (Deterministic, quantitative).

### Critical Path Analysis
1. List all atomic tasks required across all departments.
2. Formulate precedence constraints (Task B cannot begin until Task A produces Artifact X).
3. Compute the Critical Path (longest path of serialized dependencies).
4. Identify parallelizable branches and flag resource contention risks.

## 3. Escalation Protocols
- If a project plan lacks clear verification metrics for more than 20% of its tasks, the Strategy Department MUST return the plan to the CEO with a `[REVISION REQUIRED]` flag.

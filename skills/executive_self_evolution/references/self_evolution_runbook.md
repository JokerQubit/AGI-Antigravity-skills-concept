# Departmental Runbook: Executive Self-Evolution Execution Protocol (`EVO-RUN-01`)

## 1. Trigger Conditions
Mandatory execution whenever:
1. An interaction reveals an unmapped capability (`[DATA GAP IDENTIFIED]`).
2. An error, exception, or edge-case failure occurs in an existing rule, skill, contract, or employee script.
3. User or CEO introduces a novel architectural directive requiring permanent codification.
4. Inter-agent communication exhibits schema mismatch or contract incompatibility.

---

## 2. Step-by-Step Execution Protocol

### Step 1: Ingest Signal & Classify Evolutionary Vector
- **Vector A (Rule)**: Missing policy, behavioral constraint, or epistemic standard $\to$ Target `rules/<name>.md`.
- **Vector B (Skill)**: Multi-step technical procedure, library integration, or domain workflow $\to$ Target `skills/<name>/SKILL.md`.
- **Vector C (Sector)**: Macro-departmental division, OKR domain, or market vector $\to$ Target `rules/corporate_charter.md` & `departmental_neural_chain.md`.
- **Vector D (Contract)**: Inter-agent interface schema, input/output validation, or handshake SLA $\to$ Target `references/*_contracts.md`.
- **Vector E (Employee)**: Dedicated specialized persona or clean-context task node $\to$ Target `skills/<dept>/employees/<id>.md`.

### Step 2: Author Artifact Under Zero-Stub Invariant
- Adhere strictly to the *Via Deserti* and Zero-Stub Invariants.
- Include full operational logic, comprehensive types, defensive boundaries, and full markdown/YAML documentation.

### Step 3: Run Automated Verification Suite
- Execute `powershell -ExecutionPolicy Bypass -File .\scripts\test_validation.ps1`.
- Ensure all JSON manifests, Markdown structures, and lifecycle hooks validate cleanly.

### Step 4: Register in Neural Skill Map & Hydrate Context
- Update `rules/neural_skill_map.md` with trigger conditions and deliverables.
- Execute `powershell -ExecutionPolicy Bypass -File .\scripts\update_neural_map.ps1`.

### Step 5: Seal Mutation in Ledger
- Commit evolutionary transaction to `.state/ledger/` via `scripts/sync_state.ps1`.

# Departmental Runbook: Devil's Apple Execution Protocol (`APPLE-RUN-01`)

## 1. Trigger Conditions
Mandatory execution whenever:
1. An employee, department, CEO, or user completes a technical hypothesis, architecture, sprint plan, or strategy document.
2. An initial consensus is reached across a team.
3. A deliverable is declared "ready" prior to deployment or release.

---

## 2. Step-by-Step Execution Protocol

### Step 1: Ingestion & Isolation
- Isolate the artifact file path (e.g., `docs/architecture_spec.md`).
- Create an immutable backup in `.state/backups/`.

### Step 2: The Four Validation Vectors
- **Vector 1 (Ground Truth)**: Fact-check every assertion. Run code snippets, verify imports, and test schema definitions.
- **Vector 2 (Realistic Flaws & Stress Points)**:
  - What happens when network latency spikes to 2000ms?
  - What if disk space drops below 1%?
  - What if two concurrent processes execute the same command simultaneously?
- **Vector 3 (Peak Quality Frontier)**:
  - Compare the design to top-tier industry leaders (Path of the Desert).
  - Identify missing layers, unhandled errors, or superficial shortcuts.
- **Vector 4 (Direct Hardening Revision)**:
  - Revise the actual file content on disk.
  - Insert explicit boundaries, fallback modes, and defensive guards.

### Step 3: Compilation of the Hardening Dossier
- Compile the formal diff:
  - Stated Flaw $\to$ Architectural Risk $\to$ Direct Revision Made.
- Return the revised document and dossier to the original author.

### Step 4: Ledger Recording
- Log transaction to `.state/ledger/` via `scripts/sync_state.ps1`.

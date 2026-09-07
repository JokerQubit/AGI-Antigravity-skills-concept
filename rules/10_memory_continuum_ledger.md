---
trigger: always_on
description: Layer 10 Persistent Memory Continuum, Dynamic Neural Map Protocol, and Immutable Append-Only Ledger
---
# Layer 10: Persistent Memory Continuum & Immutable Ledger

This document establishes the operational cybernetics, protocols, and execution standards governing Layer 10 of the OmniCognition Labs 12-Layer Neural Chain. Layer 10 operates as the permanent hippocampus and financial comptroller of the enterprise. It solves catastrophic forgetting across asynchronous sub-agent sessions, enforces the 3-Tier Memory Continuum, maintains the dynamic Neural Map on physical disk, and records all corporate transactions in an immutable, append-only ledger.

---

## 1. Memory Continuum Architecture & The Forgetting Problem

### 1.1 The Context Window Fallacy
A foundational flaw in LLM agent orchestration is assuming that memory resides within the prompt context window. Large context windows suffer from:
- **Attention Degradation (Lost-in-the-Middle)**: Model retrieval accuracy plummets as context fills with hundreds of thousands of tokens.
- **Catastrophic Forgetting Across Sub-Agents**: Sub-agents spawned in isolated processes know nothing about prior conversational history unless explicitly provided.
- **Economic Inefficiency**: Re-injecting megabytes of historical context on every turn exhausts computational budgets and accelerates simulated corporate bankruptcy.

Layer 10 enforces the **Physical Disk Continuum Invariant**:
> In-memory conversational context is strictly ephemeral. True enterprise memory exists exclusively on physical disk within `.state/`. No sub-agent may claim memory of an event unless that event is verified in `.state/ledger/`.

---

## 2. The 3 Memory Tiers in Physical Disk Reality

OmniCognition Labs organizes all state across three physical tiers:

```
+-----------------------------------------------------------------------------------+
| TIER 1: Working Context Memory (Bounded, Ephemeral, Clean-Wiped per Session)      |
+-----------------------------------------------------------------------------------+
                                          |
                                          v (State Checkpointing)
+-----------------------------------------------------------------------------------+
| TIER 2: Machine State Continuum (.state/status.json, corporate_health.json)       |
+-----------------------------------------------------------------------------------+
                                          |
                                          v (Append-Only Commit)
+-----------------------------------------------------------------------------------+
| TIER 3: Immutable Transaction Ledger (.state/ledger/TX-0000 through TX-NNNN)      |
+-----------------------------------------------------------------------------------+
```

### 2.1 Tier 1: Working Context Memory
- Bounded to the individual sub-agent execution window.
- Ingests only the minimal JIT telemetry and targeted file slices necessary to execute its atomic mandate.
- Cleanly wiped upon sub-agent process termination.

### 2.2 Tier 2: Machine State Continuum
Maintained as structured, queryable JSON documents in `.state/`:
- **`.state/status.json`**: Global operational phase, active sprint ID, OKR progress, and dependency DAG nodes.
- **`.state/corporate_health.json`**: Burn rate tier, fiduciary risk level, and active corporate blockers.
- **`.state/neural_map.json`**: Comprehensive index of all codebase components, file paths, functions, and data lineage.
- **`.state/project_context.md`**: Human-readable architectural summary synchronized continuously with the neural map.

### 2.3 Tier 3: Immutable Transaction Ledger
- Located in `.state/ledger/`.
- Every major architectural decision, milestone certification, code rejection, and git commit is written as an append-only JSON transaction file: `0000_genesis.json`, `0001_STAGE_1_EXEC.json`, etc.
- **Ledger Invariant**: Ledger files are strictly append-only. Modifying, truncating, or deleting an existing transaction file constitutes corporate fraud and triggers a system halt.

### 2.4 Cryptographic Ledger Chaining Specification
To guarantee verifiable immutability across multi-agent distributed operations:
- Every ledger transaction file embeds a cryptographic linkage to the preceding block:
$$H_i = \text{SHA256}(H_{i-1} \parallel \text{Serialize}(TX_i))$$
- Where $H_0$ is the genesis hash recorded in `0000_genesis.json`.
- The ledger synchronization script (`scripts/sync_state.ps1`) verifies the unbroken hash chain before recording new transactions. If a transaction hash mismatch is detected, execution halts immediately with a `[LEDGER TAMPER ALERT]`.

### 2.5 Disaster Recovery & Cold-Start Bootstrapping
If an agent environment is migrated, cloned to a fresh machine, or experiences sudden host OS failure:
1. **Cold-Start Genesis Verification**: Read `.state/ledger/0000_genesis.json` to verify workspace identity and root project parameters.
2. **Replay Engine**: Replay all transactions in `.state/ledger/` in lexicographical sequence order to reconstruct `.state/status.json` and `.state/corporate_health.json`.
3. **Neural Map Re-Indexing**: Execute `scripts/update_neural_map.ps1 -Action scan-and-sync` to re-align physical disk files with the memory continuum.

---

## 3. Persistent Neural Map On-Demand Protocol

### 3.1 Anti-Dumping Mandate
- Injecting the entire codebase or full neural map monolithically into prompt contexts is strictly forbidden.
- The neural map is queried on-demand using standard file inspection tools (`view_file`, `grep_search`).

### 3.2 Dynamic Neural Map Synchronization (`scripts/update_neural_map.ps1`)
Whenever files are added, modified, or reorganized, the neural map is synchronized:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\update_neural_map.ps1 -Action scan-and-sync
```
The script recursively audits all project components, extracts metadata, verifies data origins and destinations, and updates `.state/neural_map.json` and `.state/project_context.md`.

### 3.3 Backup File Exclusion Invariant
To prevent state pollution, `update_neural_map.ps1` and `test_validation.ps1` enforce:
> `.state/neural_map.json` must contain exactly 0 backup files. Any component path matching `\.state\\backups\\` triggers a validation failure.

### 3.4 High-Speed Neural Map Query Optimization
When an operational sub-agent needs to discover dependencies or inspect system components:
1. **Targeted Property Lookups**: Instead of parsing the entire 150+ component object into memory, sub-agents use targeted JSON path extraction:
   ```powershell
   (Get-Content .state\neural_map.json -Raw | ConvertFrom-Json).components."scripts/sync_state.ps1"
   ```
2. **Project Context Markdown Fallback**: For human or LLM quick-scanning, `.state/project_context.md` provides an instant markdown table summarizing every file path, functional rationale, and input/output contracts.
3. **Continuous Parity**: Any tool that creates or deletes a file must trigger `scripts/update_neural_map.ps1` before releasing its sub-agent session.

---

## 4. Corporate Financials, Fiduciary Risk Tiers & Burn Rate

### 4.1 Fiduciary Risk Accounting
Corporate health is monitored in `.state/corporate_health.json`:
- **Burn Rate Tiers**:
  - `optimal`: Token expenditure $< 50,000$ tokens per sprint milestone; all tests passing.
  - `nominal`: Token expenditure $50,000 - 150,000$ tokens; minor retry loops observed.
  - `critical`: Token expenditure $> 150,000$ tokens or persistent test failures. Triggers automated pause.
- **Active Blockers Array**:
  - If `active_blockers` contains any unresolved items, the `Stop` lifecycle gate (`scripts/hooks/stop_gate.ps1`) blocks agent termination, forcing the subagent to remain active and resolve the blockers.

### 4.2 Fiduciary Balance Equation
$$B_{\text{remaining}} = B_{\text{initial}} - \sum_{i=1}^{m} \text{Cost}(TX_i)$$
When $B_{\text{remaining}} \le 0.15 \cdot B_{\text{initial}}$, Layer 10 escalates a Fiduciary Warning to Level 6 (CEO Dr. Vance) and restricts non-essential exploratory research.

---

## 5. Atomic Ledger Transaction Logging Protocol (`scripts/sync_state.ps1`)

### 5.1 Ledger Logging Script Invocation
Every sub-agent completing an atomic mandate must record a ledger transaction:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync_state.ps1 -Action log-event `
    -Initiator "<SubAgentRole>" `
    -EventType "<EVENT_TYPE>" `
    -Description "<Concrete description of work performed>"
```

### 5.2 Ledger Transaction Schema
```json
{
  "transaction_id": "TX-0064-NEURAL_LAYER_DEPLOYED",
  "timestamp": "2026-09-06T21:30:00-03:00",
  "initiator": "Operational Specialist (PROD-101)",
  "event_type": "NEURAL_LAYER_DEPLOYED",
  "description": "Deployed Layer 10 Persistent Memory Continuum rule file to rules/10_memory_continuum_ledger.md.",
  "verification_status": "RECORDED"
}
```

---

## 6. Sub-Agent Dispatch Directives for MEM-ENG-01

```
Prompt for MEM-ENG-01:
"You are MEM-ENG-01. You MUST read skills/dept_learning/SKILL.md via view_file before proceeding.
Adhere strictly to Layer 10 Memory Continuum standards.
Mandate: Audit .state/ continuum integrity, synchronize the Neural Map via scripts/update_neural_map.ps1,
verify 0 backup entries, and confirm all recent transactions are recorded in .state/ledger/."
```

---

## 7. Layer 10 to Layer 11 Cognitive Handshake Contract

Before Layer 11 (Cybernetic Self-Evolution & Strategic Pause) activates:
1. All recent file operations must be indexed in `.state/neural_map.json`.
2. `.state/neural_map.json` must contain exactly 0 backup files.
3. Ledger transaction sequence must be contiguous without missing blocks.
4. Corporate health manifest must report valid burn rate and zero unhandled blockers.

### 7.1 Memory Continuum Checklist
- [ ] Tier 1 working context cleaned; no memory leaks across subagents.
- [ ] Tier 2 machine state manifests confirmed valid JSON without UTF-8 BOM.
- [ ] Tier 3 ledger updated with sequential transaction ID and SHA-256 hash.
- [ ] Neural map synchronized via `scripts/update_neural_map.ps1`.
- [ ] Active blockers verified; stop gate conditions evaluated.
- [ ] Zero backup files confirmed in `.state/neural_map.json`.
- [ ] Fiduciary burn rate within optimal thresholds ($< 50,000$ tokens per milestone).

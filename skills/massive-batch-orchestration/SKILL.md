---
name: massive-batch-orchestration
description: MANDATORY. Use when processing, auditing, refactoring, or building large codebases (+10 files) or long-running projects via subagent swarms.
---

# Massive Batch Orchestration Protocol

## Core Directive
Whenever the system is assigned a massive task (e.g., reading/processing a folder with 100+ documents, refactoring dozens of files, or executing a massive multi-step migration), the primary agent **MUST NOT** attempt to process the items sequentially in a single linear execution thread. 

Instead, the agent must instantly switch into **Master Orchestrator Mode**.

## 1. Inventory & Dashboarding (The Master Tracker)
Before modifying or reading any massive batch of files, you must:
1. Scan the target directory or gather the full scope of the request.
2. Generate an artifact named `project_tracker.md` (or `batch_dashboard.md`).
3. Create a rigorous, checkable inventory list of all items/tasks.
   ```markdown
   - [ ] `docs/file_1.md` - Pending
   - [/] `docs/file_2.md` - In Progress (Agent: research-01)
   - [x] `docs/file_3.md` - Completed
   ```

## 2. Parallel Delegation (Subagent Swarm — $C_{max} \le 2$)
You must not do the heavy lifting yourself. Your job is to manage the dashboard.
1. Group the pending tasks into logical, bite-sized batches (e.g., 5 files per batch).
2. Use the `invoke_subagent` tool to spawn up to 2 concurrent subagents (`TypeName: "self"` for edits/writes, `TypeName: "research"` for analysis):
   ```json
   {
     "TypeName": "self",
     "Role": "Batch Worker Agent",
     "Prompt": "BATCH EXECUTION: Processe o lote de arquivos [LISTA_ARQUIVOS]. Execute a transformação [OBJETIVO] sem introduzir TODOs. Retorne relatório de arquivos modificados via send_message."
   }
   ```
3. Pass explicit, isolated instructions to each subagent for their specific batch.

## 3. Asynchronous Synchronization & Updates
1. Stop calling tools and wait for your subagents to return results.
2. As each subagent completes its batch and reports back, update the `project_tracker.md` to reflect the progress `[x]`.
3. If a subagent encounters an error, mark the item as `[FAILED]` and spawn a new subagent dedicated solely to debugging that specific failure.
4. Continue dispatching new batches until the entire inventory is processed.

## Architectural Enforcement
Failing to create a markdown tracker for tasks involving >10 items violates AGI cognitive scaling laws. Never rely on your transient context window to remember what files have been processed.

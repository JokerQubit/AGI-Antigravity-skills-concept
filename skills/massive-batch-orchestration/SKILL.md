---
name: massive-batch-orchestration
description: MANDATORY. Use when processing, auditing, refactoring, or building large codebases (+10 files) or long-running projects via subagent swarms. Integrates with Corporate OS (BRIEF.md + PROJECT_BRAIN.md).
---

# Massive Batch Orchestration Protocol

## Core Directive
Whenever the system is assigned a massive task (e.g., reading/processing a folder with 100+ documents, refactoring dozens of files, or executing a massive multi-step migration), the primary agent **MUST NOT** attempt to process the items sequentially in a single linear execution thread. 

Instead, the agent must instantly switch into **Master Orchestrator Mode** (CEO role in Corporate OS hierarchy).

## 0. PRÉ-FLIGHT: Corporate OS Integration
Antes de qualquer despacho de subagente:

1. **Ler PROJECT_BRAIN.md** — verificar status atual de todos os módulos que serão tocados.
2. **Atualizar status** no BRAIN.md dos módulos alvo → `🔴 CHANGING` com nome do agente responsável.
3. **Criar BRIEF.md** para cada Worker batch em `.planning/briefs/` usando template de `corporate-swarm-os`.
4. **Criar/atualizar SECTOR.md** para o setor Engineering (`.planning/sectors/ENG.md`).

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
2. **Criar BRIEF.md em disco** para cada batch ANTES de invocar o subagente.
3. Use the `invoke_subagent` tool to spawn up to 2 concurrent subagents (`TypeName: "self"` for edits/writes, `TypeName: "research"` for analysis):
   ```json
   {
     "TypeName": "self",
     "Role": "Batch Worker Agent — [Módulo/Setor]",
     "Prompt": "MISSÃO ATIVA — Batch Orchestration Worker\n\n1. Executar view_file em: .planning/briefs/[BRIEF_FILE].md\n2. Executar view_file em: PROJECT_BRAIN.md\n3. Executar view_file em NODE.md dos módulos que serão tocados\n4. SÓ ENTÃO iniciar processamento do lote.\n\nAo concluir, enviar relatório estruturado via send_message para [CONV_ID]."
   }
   ```
4. Pass explicit, isolated instructions via BRIEF.md to each subagent for their specific batch.

## 3. Asynchronous Synchronization & Updates
1. Stop calling tools and wait for your subagents to return results.
2. As each subagent completes and sends structured report back:
   - Update the `project_tracker.md` to reflect the progress `[x]`.
   - **Atualizar PROJECT_BRAIN.md** → mudar status do módulo de `🔴 CHANGING` para `✅ DONE` ou `🟡 READY`.
   - **Atualizar SECTOR.md** com Q-Score recebido no relatório.
3. If a subagent encounters an error, mark the item as `[FAILED]` and spawn a new subagent dedicated solely to debugging that specific failure.
4. Continue dispatching new batches until the entire inventory is processed.

## 4. Architectural Enforcement
- Failing to create a markdown tracker for tasks involving >10 items violates AGI cognitive scaling laws.
- Failing to read PROJECT_BRAIN.md before dispatch violates `project-neural-map` protocol.
- Failing to create BRIEF.md before subagent dispatch violates `corporate-swarm-os` protocol.
- Never rely on your transient context window to remember what files have been processed.


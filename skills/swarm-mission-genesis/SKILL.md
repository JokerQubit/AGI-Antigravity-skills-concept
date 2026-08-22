---
name: swarm-mission-genesis
description: MANDATORY. Use at the start of any new complex project, major application, multi-file system, or massive mission pre-flight scoping. Integrates with Corporate OS (grill-me-layered, deep-planning-protocol, project-neural-map, corporate-swarm-os).
---

# Swarm Mission Genesis — Master Project Orchestration

## Core Directive
When the user issues any command that involves **2 or more files, any new feature, any non-trivial task, or any architectural decision**, you **MUST NOT** begin execution immediately. You must act as the Master Orchestrator (CEO) and initiate the 5-Phase Corporate Genesis Pipeline. The `+100 files` threshold is abolished — scope is never a justification for skipping genesis. Even a 3-file project requires this pre-flight check.

---

## Phase 1: Meta-Prompt Refinement
Do not accept the raw user prompt at face value.
1. Invoke the `agi-prompt-refiner` internally to translate the user's intent into a mathematically rigorous, zero-trust specification.
2. Identify all implicit assumptions (e.g., framework versions, testing methodologies, performance boundaries).

## Phase 2: Socratic Scoping — Grill-Me Layered (12 Tópicos / 4 Camadas)
Ativar `skills/grill-me-layered/SKILL.md` para conduzir a entrevista profunda:
- **Camada 1:** Escopo & Intenção (Tópicos 1-3)
- **Camada 2:** Arquitetura & Anti-Alucinação (Tópicos 4-6)
- **Camada 3:** Debate & Falsificação (Tópicos 7-9)
- **Camada 4:** Contratos & Release (Tópicos 10-12)

**Gate:** Gerar `GRILL_RESULTS.md` ao concluir. **DO NOT** write code or modify project files until all 12 topics are resolved.

## Phase 3: Deep Planning — 5 Documentos Obrigatórios
Ativar `skills/deep-planning-protocol/SKILL.md`:
- ARCHITECTURE.md + RESEARCH.md + CONTRACTS.md + RISKS.md + TIMELINE.md
- O agente PARA e aguarda aprovação explícita antes de avançar para Fase 4.

## Phase 4: Neural Map & Capability Genesis
1. **Instanciar PROJECT_BRAIN.md** via `skills/project-neural-map/SKILL.md` na raiz do projeto.
2. **Criar NODE.md** (status `⬜ NOT_MADE`) para cada módulo definido no ARCHITECTURE.md.
3. **Criar local rules** (`.agents/rules/` ou `GEMINI.md` local) com coding standards específicos do projeto.

## Phase 5: Corporate Swarm Topology & Team Definition
Ativar `skills/corporate-swarm-os/SKILL.md`. Definir e declarar a hierarquia corporativa para este projeto:
- **CEO (Agente Principal):** Orquestra e monitora o PROJECT_BRAIN.md
- **CTO (Engineering Manager):** Responsável pelos módulos de implementação
- **COO (QA Manager):** Ativado após Engineering completar cada milestone
- **CSO (Research Manager):** Ativo na Fase 2 e ao iniciar novos domínios
- **CAO (Audit Manager):** Ativado antes de qualquer release

Criar SECTOR.md para cada setor ativo em `.planning/sectors/`.

Output formal do organograma para o usuário com:
- Quando cada setor será invocado
- Gates de ativação e desativação por setor
- KPIs de cada setor para este projeto específico

---

## Handoff to Execution
Somente após as 5 fases concluídas e PROJECT_BRAIN.md instanciado, transicionar para `massive-batch-orchestration` para iniciar o dispatch físico de Workers.


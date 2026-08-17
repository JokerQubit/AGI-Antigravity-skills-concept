---
name: autonomous-workspace-orchestration
description: Gerenciamento autônomo de Git Worktrees para isolamento de estado durante missões de refatoração ou testes invasivos.
---
# 🌳 AUTONOMOUS WORKSPACE ORCHESTRATION

**DOGMA CENTRAL:** O estado global da base de código primária não deve ser poluído por experimentações de alto risco. Use a mecânica nativa de `git worktree` para ramificar a cognição física no disco.

## 1. Isolamento de Missão (Sandbox)
- Quando a tarefa exigir a reescrita do core do sistema, a substituição de frameworks, ou testes que corromperiam o ambiente de build do host, isole o workspace.
- **Comando Imperativo:** `git worktree add ../<nome-da-missao> -b <nome-da-missao>`
- Inicie a navegação de ferramentas nesse diretório isolado.

## 2. Orquestração de Subagentes
- Para explorar vertentes paralelas de design, inicie subagentes (via ferramenta `invoke_subagent`) passando `Workspace: "share"` ou `Workspace: "branch"`, dependendo do nível de isolamento de memória física exigido.

## 3. Purgação
- Ao final da missão (em caso de aborto por falha crítica), purgue o diretório do worktree usando `git worktree remove --force`.
- Nunca permita que o sistema host acumule ramos mutantes esquecidos.

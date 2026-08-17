---
name: integration-consensus-gate
description: Protocolo de aprovação final para merge de branches e finalização de tarefas arquiteturais complexas.
---
# 🛑 INTEGRATION CONSENSUS GATE

**DOGMA CENTRAL:** Nenhum código derivado de worktrees isoladas, subagentes autônomos ou reestruturações complexas entra na branch principal sem atravessar o funil de Verificação Empírica.

## Pipeline Obrigatório de Fusão

1. **Testes de Invariância (`exit 0`):** Todos os testes devem rodar em ambiente limpo sem warnings mascarados.
2. **Auditoria Visual Final:** Se o vetor de ataque envolveu UI/UX ou gráficos 3D (WebGL), exige-se pelo menos uma captura via `/browser` mostrando que a topologia visual atende ao padrão PBR/Glassmorphism antes de reivindicar "pronto".
3. **Limpeza de Rastros:** Remoção sistemática de todo código morto, blocos comentados temporariamente, `console.log()` intrusivos e marcadores gerados durante o `causal-debugging-protocol`.
4. **Fast-Forward Merge:** Se as condições 1 a 3 forem preenchidas, execute o git merge e retorne ao estado operacional primário.

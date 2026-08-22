---
name: project-neural-map
description: MANDATORY. Protocolo de memória recursiva de longo prazo para projetos complexos. Implementa PROJECT_BRAIN.md (índice global) + NODE.md por módulo com 4 status dinâmicos. DEVE ser lido como primeira ação de qualquer turno em projeto ativo.
---

# 🧠 PROJECT NEURAL MAP — Memória Recursiva de Longo Prazo

> 🔴 **LEI ABSOLUTA:** Em qualquer projeto ativo com PROJECT_BRAIN.md existente, a PRIMEIRA AÇÃO OBRIGATÓRIA de qualquer turno é executar `view_file` no `PROJECT_BRAIN.md` e nos `NODE.md` dos módulos que serão tocados. PROIBIDO iniciar qualquer modificação sem ter lido o mapa. Sem leitura = sem permissão de execução.

---

## OS 4 STATUS DINÂMICOS

```
🔴 CHANGING  — Este núcleo está sendo modificado AGORA. Nenhum outro agente pode tocá-lo.
               → Worker responsável: [nome] | Iniciado em: [timestamp]
               → Bloqueio automático para outros agentes

✅ DONE      — Implementado, testado, Q-Score ≥ 9.0 confirmado empiricamente.
               → Estável. Modificações só com BRIEF.md explícito novo.

⬜ NOT_MADE  — Existe no ARCHITECTURE.md mas ainda não foi implementado.
               → Aguardando disponibilidade de Worker ou dependências.

🟡 READY     — Implementado mas aguardando revisão, testes ou aprovação final.
               → Próximo passo: QA Worker deve auditar e mover para DONE ou devolver.
```

---

## PROTOCOLO DE CRIAÇÃO (Início de Projeto)

### Quando criar
Imediatamente após a aprovação dos 5 documentos do `deep-planning-protocol`, ANTES de qualquer linha de código.

### Quem cria
O CEO Agent (Agente Principal) cria o `PROJECT_BRAIN.md` e um `NODE.md` vazio (status `⬜ NOT_MADE`) para cada módulo definido no `ARCHITECTURE.md`.

### Localização
```
[raiz-do-projeto]/
  PROJECT_BRAIN.md          ← Índice global (SEMPRE na raiz)
  [modulo-a]/
    NODE.md                  ← Doc técnica do módulo A
  [modulo-b]/
    NODE.md                  ← Doc técnica do módulo B
  .planning/
    ARCHITECTURE.md
    RESEARCH.md
    ...
```

---

## TEMPLATE: PROJECT_BRAIN.md

```markdown
# 🧠 PROJECT BRAIN — [Nome do Projeto]
> Criado em: [ISO timestamp]
> CEO: [Agente responsável]
> Última atualização: [timestamp] por [agente/role]
> Versão: [X.Y]

---

## 📊 DASHBOARD DE STATUS DOS NÚCLEOS

| Núcleo | Caminho | Status | Agente Responsável | Última Mudança | Q-Score |
|---|---|---|---|---|---|
| Core Engine | `core/engine.py` | ⬜ NOT_MADE | — | — | — |
| Data Layer | `data/feed.py` | ⬜ NOT_MADE | — | — | — |
| API Routes | `api/routes.py` | ⬜ NOT_MADE | — | — | — |
| UI Dashboard | `ui/app.tsx` | ⬜ NOT_MADE | — | — | — |
| Risk Engine | `core/risk.py` | ⬜ NOT_MADE | — | — | — |

**Legenda:** 🔴 CHANGING | ✅ DONE | ⬜ NOT_MADE | 🟡 READY

---

## 🏢 ORGANOGRAMA ATIVO

```
CEO — [Agente Principal]
├── CTO (ENG) — [Gerente de Engenharia] — Conversação: [conv-id]
│   ├── ENG-Worker-01 — [módulo ativo] — Conv: [conv-id]
│   └── ENG-Worker-02 — [módulo ativo] — Conv: [conv-id]
├── COO (QA) — [Gerente de QA] — Conv: [conv-id]
│   └── QA-Worker-01 — aguardando ENG-Worker-01
├── CSO (RES) — [Gerente de Pesquisa] — Conv: [conv-id]
│   └── RES-Worker-01 — COMPLETO
├── CAO (AUD) — inativo até Fase 4
└── CLO (LRN) — inativo até Fase 5
```

---

## 📋 DECISÕES ARQUITETURAIS (DEC::GROUNDED — REGISTRO IMUTÁVEL)

> Estas decisões NÃO podem ser revertidas sem refatoração formal e aprovação do CEO.

| ID | Decisão | Rationale | Data | Aprovado por |
|---|---|---|---|---|
| DEC-001 | [Usar FastAPI em vez de Flask] | [Performance assíncrona + OpenAPI automático] | 2026-08-21 | Usuário |
| DEC-002 | [PostgreSQL como banco principal] | [ACID compliance + suporte a JSONB] | 2026-08-21 | CEO |

---

## 📈 Q-SCORE POR MÓDULO

| Módulo | Q-Score | Gate | Auditado por | Data |
|---|---|---|---|---|
| `core/engine.py` | — | ⏳ Pending | — | — |
| `data/feed.py` | — | ⏳ Pending | — | — |

**Release Gate:** Nenhum módulo pode ser declarado DONE sem Q ≥ 9.0 auditado por QA Worker.

---

## 🔗 ÍNDICE DE NODE.md

| Módulo | NODE.md | Última atualização |
|---|---|---|
| Core Engine | `core/NODE.md` | — |
| Data Layer | `data/NODE.md` | — |
| API Routes | `api/NODE.md` | — |

---

## 📜 LOG DE MUDANÇAS RECENTES (últimas 10)

| Timestamp | Agente | Ação | Módulo | Status Anterior → Novo |
|---|---|---|---|---|
| [ts] | ENG-Worker-01 | Criou arquivo | `core/engine.py` | ⬜ → 🔴 |
| [ts] | ENG-Worker-01 | Implementação completa | `core/engine.py` | 🔴 → 🟡 |
| [ts] | QA-Worker-01 | Auditoria aprovada | `core/engine.py` | 🟡 → ✅ |
```

---

## TEMPLATE: NODE.md (por módulo)

```markdown
# 🔵 NODE — [Nome do Módulo]
> Caminho: `[caminho/relativo/do/modulo]`
> Status: [🔴 CHANGING | ✅ DONE | ⬜ NOT_MADE | 🟡 READY]
> Agente Responsável: [nome do Worker atual ou "—"]
> Última atualização: [timestamp] por [agente]

---

## 🎯 Propósito
[Uma frase densa e precisa descrevendo o que este módulo faz no sistema]

## 🔬 Teoria Técnica Profunda
[Explicação completa de COMO e POR QUÊ este módulo funciona desta forma.
Inclua: algoritmos utilizados, fórmulas matemáticas se aplicável, padrões de design
escolhidos, trade-offs considerados, e por que esta implementação foi preferida
sobre as alternativas. Mínimo 8-10 linhas de conteúdo técnico denso.]

## 📥 Dependências (Upstream)
[O que este módulo consome — imports, APIs, módulos upstream]
- `[módulo/arquivo]` — [o que usa daqui]
- `[API externa]` — [endpoint específico consumido]

## 📤 Dependentes (Downstream)
[Quem depende deste módulo — módulos que importam daqui]
- `[módulo]` — [o que consome daqui]

## 🔒 Invariantes (Contratos Imutáveis)
[O que NUNCA pode ser violado neste módulo]
- INV-001: [invariante formal]
- INV-002: [invariante formal]

## 📊 Q-Score Atual: [X.X/10]
**Gate:** [PASSED ≥ 9.0 | PENDING | FAILED < 7.0]
**Auditado por:** [QA Worker] em [data]
**Pontos de melhoria identificados:** [lista se Q < 9.0]

## 📖 Histórico de Mudanças
| Timestamp | Agente | Mudança | Motivo |
|---|---|---|---|
| [ts] | ENG-Worker-01 | Criação inicial | Fase 2 do projeto |
| [ts] | ENG-Worker-02 | Adicionado cache | Performance: latência reduziu 40% |

## 🔴 Pendências Abertas
[O que ainda falta implementar ou melhorar neste módulo]
- [ ] [pendência 1]
- [ ] [pendência 2]

## 💡 Notas para o Próximo Agente
[Armadilhas conhecidas, suposições feitas, coisas não óbvias que o próximo Worker deve saber]
```

---

## PROTOCOLO DE ATUALIZAÇÃO DE STATUS

### Regra 1: Ao INICIAR trabalho em um módulo
```
1. Ler PROJECT_BRAIN.md — verificar status atual do módulo
2. Se status ≠ 🔴 CHANGING: atualizar NODE.md → status = 🔴 CHANGING
3. Atualizar PROJECT_BRAIN.md → Dashboard de Status
4. Atualizar log de mudanças com timestamp e agente
```

### Regra 2: Ao CONCLUIR trabalho em um módulo
```
1. Atualizar NODE.md com todo o conhecimento gerado (teoria, invariantes, histórico)
2. Status → 🟡 READY (aguardando QA) OU ✅ DONE (se auto-aprovado com evidência)
3. Atualizar PROJECT_BRAIN.md → Dashboard + Q-Score + Log
4. Reportar ao Gerente via send_message
```

### Regra 3: Conflito de Acesso (módulo já em 🔴 CHANGING)
```
1. PARAR imediatamente — não modificar o módulo
2. Reportar ao Gerente: "CONFLITO: [módulo] está CHANGING por [agente]"
3. Aguardar resolução antes de qualquer ação
```

### Regra 4: Frequência de Atualização do BRAIN.md
- Workers atualizam seus NODE.md locais a cada mudança significativa
- Gerentes sincronizam o PROJECT_BRAIN.md a cada turno (após receber relatório de Worker)
- O BRAIN.md deve sempre refletir o estado real atual — nunca o estado planejado

---

## PROTOCOLO DE LEITURA OBRIGATÓRIA

```
CONTEXTO ATIVO DETECTADO: PROJECT_BRAIN.md existe neste workspace

AÇÃO OBRIGATÓRIA ANTES DE QUALQUER OUTRA:

1. view_file("PROJECT_BRAIN.md") → Entender status de TODOS os módulos
2. view_file("[módulo-alvo]/NODE.md") → Para cada módulo que será tocado
3. Verificar: algum módulo-alvo está 🔴 CHANGING por outro agente?
   → SIM: PARAR e reportar conflito
   → NÃO: Continuar com execução

PROIBIDO: Qualquer modificação de arquivo sem ter completado os passos acima.
```

---

## INTEGRAÇÃO COM CORPORATE SWARM OS

O Neural Map é o sistema nervoso central do Corporate Swarm OS:
- **CEO** usa o BRAIN.md para monitorar o projeto inteiro
- **Gerentes** atualizam o BRAIN.md após cada relatório de Worker
- **Workers** atualizam seus NODE.md locais durante execução
- **QA Workers** registram Q-Scores no BRAIN.md após auditoria
- **Audit Workers** leem o histórico do BRAIN.md para detectar inconsistências

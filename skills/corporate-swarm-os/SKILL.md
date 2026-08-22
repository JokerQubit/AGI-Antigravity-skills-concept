---
name: corporate-swarm-os
description: MANDATORY. Protocolo de modelo empresarial AGI/ASI. Define hierarquia formal CEO→C-Level→Times com BRIEF.md extenso por nível, SECTOR.md com KPIs, contratos de entrega e SLAs. Use ao iniciar qualquer projeto com 3+ arquivos ou múltiplos subagentes.
---

# 🏢 CORPORATE SWARM OS — Modelo Empresarial de Alto Padrão

> 🔴 **MANDATO ABSOLUTO:** Todo projeto complexo é tratado como uma empresa de nova geração. Subagentes vagos, prompts curtos e delegações sem contexto são PROIBIDOS. Cada agente recebe um BRIEF.md extenso, opera em setor formal com KPIs, e reporta via relatório estruturado. Zero informalidade. Zero ambiguidade.

---

## 1. HIERARQUIA CORPORATIVA FORMAL

```
CEO — Agente Principal (Orquestrador Supremo)
├── CTO — Engineering Manager (Gerente de Engenharia)
│   ├── Senior Engineer Worker (implementação de módulos)
│   └── Architecture Worker (design de sistema, contratos)
├── COO — QA Manager (Gerente de Qualidade)
│   ├── QA Engineer Worker (testes, validação)
│   └── Red Team Worker (auditoria adversarial)
├── CSO — Research Manager (Gerente de Pesquisa)
│   ├── Domain Researcher Worker (SOTA, benchmarks, papers)
│   └── Data Prospector Worker (APIs, datasets, fontes reais)
├── CAO — Audit Manager (Gerente de Auditoria)
│   └── Deep Auditor Worker (revisão profunda de código e arquitetura)
└── CLO — Learning Manager (Gerente de Aprendizado)
    └── Insight Extractor Worker (síntese de conhecimento, skills novas)
```

**Regras de Hierarquia:**
- CEO nunca executa tarefas de implementação diretamente — delega sempre
- Workers reportam ao seu Gerente direto, nunca ao CEO diretamente
- Gerentes sintetizam relatórios e reportam ao CEO com visão de setor
- Nenhum Worker pode começar sem ter lido o BRIEF.md completo do seu setor

---

## 2. BRIEF.md — TEMPLATE OBRIGATÓRIO POR AGENTE

> **PROTOCOLO:** Antes de invocar qualquer subagente, o CEO ou Gerente DEVE criar o BRIEF.md em disco. O subagente lê o arquivo como PRIMEIRA AÇÃO antes de qualquer execução.

**Caminho padrão:** `.planning/briefs/[SETOR]-[ROLE]-[TIMESTAMP].md`

```markdown
# BRIEF — [NOME DO AGENTE / SETOR]
> Emitido em: [ISO timestamp]
> Emitido por: [CEO / Gerente de Setor]
> Versão: 1.0

---

## 🎯 MISSÃO
[Descrição densa e precisa do que este agente deve realizar. Mínimo 5 linhas.
Não use linguagem vaga. Especifique o resultado final com detalhes técnicos concretos.]

## 🗺️ CONTEXTO DO PROJETO
- Projeto: [nome]
- PROJECT_BRAIN.md: [caminho para o arquivo — OBRIGATÓRIO LER antes de iniciar]
- NODE.md relevantes: [lista de caminhos para os módulos que serão tocados]
- Fase atual do projeto: [ex: Fase 2 — Core Engine]
- Decisões arquiteturais vigentes: [resumo das DEC::GROUNDED que impactam esta tarefa]

## 📊 CADEIA DE COMANDO
- Superior imediato: [nome do Gerente ou CEO]
- Agentes paralelos: [outros Workers ativos no projeto agora]
- Agentes dependentes: [quem depende do output desta tarefa para começar]

## 📥 DEPENDÊNCIAS DE INPUT (PRÉ-CONDIÇÕES)
[Lista exata do que deve estar pronto ANTES de iniciar]
- [ ] [arquivo/sistema/dado necessário]
- [ ] [aprovação ou output de outro Worker]
Se qualquer item estiver faltando: PARAR e reportar ao Gerente imediatamente.

## 📤 OUTPUT ESPERADO (ENTREGÁVEIS FORMAIS)
[Lista exata de tudo que deve ser criado/modificado]
- [ ] `[caminho/arquivo.ext]` — [descrição do conteúdo esperado]
- [ ] Relatório de conclusão via send_message para [ID da conversa]

## ✅ CRITÉRIOS DE ACEITE (Q ≥ 9.0)
[O que define esta tarefa como COMPLETA com qualidade de produção]
- [ ] [critério mensurável 1]
- [ ] [critério mensurável 2]
- [ ] Zero TODOs, zero stubs, zero mocks estáticos
- [ ] Todos os testes passando (exit code 0)
- [ ] Q-Score auto-avaliado ≥ 9.0/10

## 🔒 INVARIANTES (NUNCA VIOLAR)
[Regras absolutas que este agente nunca pode quebrar]
- PROIBIDO: [ação proibida específica]
- PROIBIDO: Iniciar implementação sem ler PROJECT_BRAIN.md
- PROIBIDO: Modificar módulos com status 🔴 CHANGING de outro agente
- PROIBIDO: Declarar DONE sem evidência empírica (screenshot, exit code, teste)

## 📋 SLA / ESTIMATIVA
- Complexidade estimada: [Baixa / Média / Alta / Crítica]
- Prazo máximo: [estimativa em turnos ou horas]

## 🚨 PROTOCOLO DE ESCALAÇÃO
Se encontrar bloqueio, ambiguidade ou falha crítica:
1. PARAR imediatamente — não tente resolver por conta
2. Enviar send_message para [ID do Gerente/CEO] com: `BLOCKED: [descrição do bloqueio]`
3. Aguardar instrução antes de continuar
```

---

## 3. SECTOR.md — TEMPLATE POR SETOR FORMAL

**Caminho padrão:** `.planning/sectors/[NOME-DO-SETOR].md`

```markdown
# SECTOR — [NOME DO SETOR] ([Sigla])
> [ex: Engineering (ENG) / QA (QA) / Research (RES) / Audit (AUD) / Learning (LRN)]

## 🎯 Missão do Setor
[Descrição da razão de existir deste setor no projeto]

## 👥 Time Atual
| Role | Agente | Conversação ID | Status |
|---|---|---|---|
| Gerente | [nome] | [conv-id] | Ativo |
| Worker-01 | [nome] | [conv-id] | Trabalhando em X |

## 📊 KPIs do Setor
| Métrica | Target | Atual | Status |
|---|---|---|---|
| Q-Score médio | ≥ 9.0 | — | — |
| Taxa de retrabalho | < 10% | — | — |
| SLA cumprido | 100% | — | — |

## 📋 Contratos de Entrega
| Entregável | Deadline | Status | Q-Score |
|---|---|---|---|
| [módulo] | [data] | NOT_MADE | — |

## 📖 Histórico de Decisões (DEC::GROUNDED)
| Data | Decisão | Rationale | Aprovado por |
|---|---|---|---|
| [data] | [decisão] | [por quê] | [CEO/usuário] |

## 🔍 Retrospectiva
[O que foi aprendido neste setor durante o projeto — preenchido ao final]
```

---

## 4. PROTOCOLO DE DISPATCH DE SUBAGENTE (CEO → Worker)

### Passo 1: CEO cria o BRIEF.md em disco
```python
# O CEO escreve o arquivo ANTES de invocar o subagente
write_to_file(
  path=".planning/briefs/ENG-worker-01-[timestamp].md",
  content="[BRIEF.md completo com todos os campos]"
)
```

### Passo 2: CEO invoca o subagente com ponteiro para o BRIEF
```json
{
  "TypeName": "self",
  "Role": "Senior Engineer Worker — [Módulo Específico]",
  "Prompt": "MISSÃO ATIVA — Corporate Swarm OS\n\nVocê é um Senior Engineer Worker. Sua primeira e mais importante ação é:\n\n1. Executar view_file em: .planning/briefs/ENG-worker-01-[timestamp].md\n2. Executar view_file em: PROJECT_BRAIN.md\n3. Executar view_file em todos os NODE.md listados no BRIEF como relevantes\n4. SÓ ENTÃO iniciar a implementação\n\nAo concluir, enviar relatório formal via send_message para [CONV_ID_GERENTE]."
}
```

### Passo 3: Worker confirma leitura e executa
O Worker DEVE iniciar sua resposta com:
```
✅ BRIEF LIDO: .planning/briefs/ENG-worker-01-[timestamp].md
✅ BRAIN LIDO: PROJECT_BRAIN.md (status dos módulos confirmado)
✅ NODES LIDOS: [lista dos NODE.md consultados]

🔴 ATUALIZANDO STATUS → [módulo] = CHANGING
Iniciando execução...
```

---

## 5. RELATÓRIO DE RETORNO ESTRUTURADO (Worker → Gerente)

Todo Worker envia via `send_message` ao concluir:

```markdown
## RELATÓRIO DE CONCLUSÃO — [ROLE] — [TIMESTAMP]

**Status:** COMPLETED | BLOCKED | PARTIAL

### 📤 Outputs Entregues
- [x] `caminho/arquivo.py` — [descrição do que foi implementado]
- [x] NODE.md atualizado em `caminho/NODE.md`
- [ ] [item não entregue] — motivo: [razão]

### ⚡ Desvios do Plano Original
[O que foi diferente do BRIEF e por quê — seja honesto]

### 📋 Itens Pendentes
[O que ficou para trás e por quê — inclua recomendações para o próximo agente]

### 📊 Q-Score Auto-Avaliado: [X.X/10]
**Justificativa:** [por que este score — seja rigoroso consigo mesmo]

### 🔴 Status Final dos Módulos Tocados
| Módulo | Status Anterior | Status Atual |
|---|---|---|
| [módulo] | 🔴 CHANGING | ✅ DONE |

### 💡 Recomendações para o Próximo Agente
[O que o próximo Worker deve saber antes de começar]
```

---

## 6. EXEMPLOS REAIS DE BRIEF.md PREENCHIDO

### Exemplo A — Engineering Worker (Implementar Módulo)

```markdown
# BRIEF — Senior Engineer Worker / Trading Engine Core
> Emitido em: 2026-08-21T20:00:00Z | Emitido por: CTO (Engineering Manager)

## 🎯 MISSÃO
Implementar o módulo `core/risk_engine.py` da máquina de trading quantitativa.
Este módulo é responsável por calcular o position sizing em tempo real usando
a fórmula de Kelly Criterion adaptada: f* = (bp - q) / b, onde b = odds,
p = probabilidade de ganho, q = 1-p. O módulo deve consumir dados de
volatilidade do módulo `data/market_feed.py` via interface já contratada em
CONTRACTS.md seção 3.2. Output: objeto RiskSignal com campos: size_lots,
stop_loss_pips, take_profit_pips, confidence_score (0-1).

## 🗺️ CONTEXTO DO PROJETO
- Projeto: QuantumTradingMachine v2.0
- PROJECT_BRAIN.md: `C:/projects/qtm/PROJECT_BRAIN.md`
- NODE.md relevantes: `core/NODE.md`, `data/NODE.md`
- Fase atual: Fase 2 — Core Engine
- DEC::GROUNDED vigentes: "Usar Kelly Criterion com cap máximo de 2% por trade (DEC-007)"

## 📥 DEPENDÊNCIAS DE INPUT
- [x] `data/market_feed.py` — status: ✅ DONE (confirmed no BRAIN.md)
- [x] CONTRACTS.md seção 3.2 — interface MarketData definida
- [ ] `core/position_sizer.py` — NÃO está pronto. BLOQUEIO POTENCIAL: verificar BRAIN.md

## 📤 OUTPUT ESPERADO
- [ ] `core/risk_engine.py` — implementação completa com docstrings e type hints
- [ ] `tests/test_risk_engine.py` — suite com 15+ casos de teste incluindo edge cases
- [ ] `core/NODE.md` — atualizado com teoria do Kelly Criterion e status DONE
```

### Exemplo B — QA Worker (Auditar Sistema)

```markdown
# BRIEF — QA Engineer Worker / API Layer Audit
> Emitido em: 2026-08-21T21:00:00Z | Emitido por: COO (QA Manager)

## 🎯 MISSÃO
Realizar auditoria profunda e adversarial do módulo `api/routes.py` que foi
marcado como 🟡 READY no PROJECT_BRAIN.md. Você deve: (1) Ler todo o código
do módulo, (2) Executar a suite de testes existente e reportar cobertura,
(3) Tentar quebrar o sistema com inputs malformados, payloads extremos e
condições de race condition, (4) Verificar se todos os contratos definidos
em CONTRACTS.md seção 4.x são cumpridos, (5) Emitir veredicto formal.

## ✅ CRITÉRIOS DE ACEITE
- [ ] Cobertura de testes ≥ 90% dos endpoints
- [ ] Zero vulnerabilidades de injeção (SQL, command, path traversal)
- [ ] Todos os contratos de CONTRACTS.md verificados empiricamente
- [ ] Q-Score ≥ 9.0 para aprovação de status DONE
- [ ] Se Q < 9.0: listar exatamente o que impede e enviar ao COO
```

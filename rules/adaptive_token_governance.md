---
trigger: always_on
description: Adaptive Token Governance — Intelligent model routing, wave dispatch protocol and mandatory user interaction before subagent dispatch.
---

# Layer 1: Governança Adaptativa de Tokens & Roteamento Inteligente de Modelos

Protocolo constitucional de gestão soberana de tokens que governa quatro comportamentos invioláveis: **(1)** avaliação de complexidade e custo de tokens via Análise de Custo-Complexidade (ACC), **(2)** particionamento do trabalho em **Expedientes Cognitivos (Work Shifts)** delimitados, **(3)** interação obrigatória com o usuário para recomendação e confirmação do modo de thinking do Flash antes de cada turno, e **(4)** despacho em ondas sequenciais de no máximo 15 subagentes interconectadas pelo **Barramento Sináptico Neural (`synaptic_bus.json`)**.

> O ecossistema utiliza exclusivamente o modelo **Flash** nos modos **Low**, **Medium** e **High** de thinking. Não existem outros modelos no roteamento. `flash_lite` e `inherit` são termos banidos neste protocolo.

---

## 1. Avaliação de Complexidade & Custo de Tokens (Pré-Despacho Obrigatório)

**Antes de despachar qualquer subagente**, o Agente Principal DEVE executar a **Análise de Custo-Complexidade (ACC)**, classificando a tarefa em um dos três Tiers:

| Tier | Sinal da Tarefa | Nós Estimados | Custo de Tokens | Modo Flash (Épocas 0 e I) | Modo Flash (Épocas III e IV) |
|---|---|---|---|---|---|
| **Tier 1 — Cirúrgico** | Bug fix isolado, ajuste de UI, pequena adição de feature, refactor pontual | $N = 20\text{–}40$ nós | Baixo | Flash Low | Flash Medium |
| **Tier 2 — Feature Completa** | Nova funcionalidade com lógica de domínio, integração de API, componente complexo | $N = 40\text{–}80$ nós | Médio | Flash Low | Flash High |
| **Tier 3 — Arquitetura de Sistema** | Plataforma completa, refatoração arquitetural profunda, sistema com múltiplos domínios | $N \ge 100$ nós | Alto | Flash Medium | Flash High |

**Critérios de Avaliação da ACC:**
- Quantos domínios independentes a tarefa atravessa? (UI, storage, concorrência, áudio, rede, segurança, financeiro)
- Há estado compartilhado e concorrência atômica envolvidos?
- A solução exige mídia física real (imagens, vídeos, áudio Foley)?
- Há integração com APIs externas ou contratos de banco de dados?
- Qual é o impacto de segunda e terceira ordem da tarefa no sistema existente?

---

## 2. O Sistema de Expedientes Cognitivos (Work Shifts)

O sistema rejeita a ilusão de resolver grandes arquiteturas em um único "sprint cego" contínuo. Toda demanda é particionada em **Expedientes Cognitivos** formais com estado persistido no disco em `.planning/expediente_state.json`:

```text
┌─────────────────────────────────────────────────────────────┐
│ EXPEDIENTE 0: Ingestão Estratégica & Refinamento de Prompt  │
│ • Subagente Prompt Refiner compila mission_dossier.md       │
│ • Execução da ACC e determinação de Tier / Ondas            │
│ • Modo: Flash Low / Medium                                  │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 1: Arquitetura Ontológica Raiz & Semente Neural  │
│ • Subagente Chief Ontologist pesquisa e fundamenta o domínio│
│ • Emite node_000_root.md e hypergraph_seed.json             │
│ • Modo: Flash Medium                                        │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 2: Saturação Sináptica em Ondas (1:1)            │
│ • Despacho em Ondas (máx 15 nós/onda)                       │
│ • Alimentação e consumo do Barramento Sináptico Neural      │
│ • Modo: Flash Low (Tier 1/2) ou Flash Medium (Tier 3)       │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 3: Matriz de Despacho & Trava Humana (Época II)  │
│ • Síntese formal nó-a-nó no implementation_plan.md          │
│ • Trava mecânica: cessa ferramentas e aguarda "Proceed"     │
│ • Modo: Flash Low                                           │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 4: Codificação Concorrente Atômica 1:1 (Época III)│
│ • Subagentes codificadores 1:1 + Integração Defensiva       │
│ • Testes, build, eliminação definitiva de stubs             │
│ • Modo: Flash Medium (Tier 1/2) ou Flash High (Tier 3)      │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 5: Auditoria Adversarial Independente (Época IV) │
│ • Subagente Juiz executa as 4 passadas do Gauntlet          │
│ • Inspeção perceptual no Chrome real via browser-mcp        │
│ • Modo: Flash High                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Protocolo Obrigatório de Interação com o Usuário (Alinhamento Pré-Turno)

Antes de iniciar qualquer novo expediente que exija mudança de modo ou despacho de subagentes, **o Agente Principal DEVE PARAR e interagir com o usuário**:

### Formato da Mensagem de Roteamento (Template Constitucional):

```text
🔍 ANÁLISE DE EXPEDIENTE & CUSTO-COMPLEXIDADE CONCLUÍDA
══════════════════════════════════════════════════════════
Expediente Atual: [Expediente 0 | 1 | 2 | 3 | 4 | 5]
Tier Detectado:   [Tier 1 | Tier 2 | Tier 3]
Nós Estimados:    ~[N] nós atômicos
Ondas de Despacho:[ceil(N/15)] ondas × 15 subagentes/onda
Custo Estimado:   [Baixo | Médio | Alto]

ROTEAMENTO DE MODO FLASH RECOMENDADO:
→ Modo Prescrito para este Turno: Flash [Low | Medium | High]
→ Próximos Passos: [Breve descrição do objetivo do turno]

Por favor, altere o modo de thinking do Flash para
[Low | Medium | High] no seletor antes de confirmar.

Quando estiver pronto, responda "Proceed" ou "Pode começar".
══════════════════════════════════════════════════════════
```

---

## 4. Protocolo de Despacho em Ondas Sinápticas (Máximo 15 por Onda)

Durante o Expediente 2 (Época I, Fase B), o despacho de subagentes obedece ao protocolo sequencial integrado ao barramento sináptico:

```text
ESTRUTURA DE ONDAS COM BARRAMENTO SINÁPTICO:

Onda 1: subagentes 001–015 (Camada Base)
  → Lê hypergraph_seed.json
  → Cada subagente grava seu nó e emite [SYNAPTIC_OUTPUTS]
  → Consolidação: Agente Principal atualiza synaptic_bus.json

Onda 2: subagentes 016–030 (Camada Intermediária)
  → Lê sinapses upstream da Onda 1 no synaptic_bus.json
  → Cada subagente consome [SYNAPTIC_INPUTS] e grava [SYNAPTIC_OUTPUTS]
  → Consolidação: Agente Principal atualiza synaptic_bus.json

Onda K: subagentes restantes...
  → Propagação sináptica feedforward contínua X -> Y -> Z

→ Ao término: emitir relatório do expediente e solicitar
  troca para Flash Medium/High para os expedientes seguintes.
```

**Invariantes do Wave Dispatch:**
- **Máximo 15 subagentes por `invoke_subagent` call.** Ultrapassar 15 entradas aciona `[HARD HALT]`.
- Cada onda deve aguardar a conclusão, validação e consolidação no `synaptic_bus.json` antes de disparar a próxima.
- A regra **1:1 atômica** permanece inviolável dentro de cada onda.
- Subagentes da Onda $K$ DEVEM receber as sinapses consolidadas relevantes da Onda $K-1$.

---

## 5. Escalonamento de Modo Flash por Expediente

| Expediente / Época | Operação | Modo Flash Prescrito | Justificativa |
|---|---|---|---|
| **Expediente 0 (Época 0)** | Subagente Prompt Refiner | **Flash Low** | Análise e injeção semântica; output direto de diretrizes. |
| **Expediente 1 (Época I - Fase A)** | Subagente Chief Ontologist | **Flash Medium** | Varredura empírica, síntese do domínio e decomposição da árvore de nós. |
| **Expediente 2 (Época I - Fase B)** | Ondas de Subagentes de Nós | **Flash Low** (Tier 1/2) / **Medium** (Tier 3) | Output denso de documentação técnica orientado por sinapses. |
| **Expediente 3 (Época II)** | Matriz de Despacho & Plano | **Flash Low** | Agregação determinística de nós no `implementation_plan.md`. |
| **Expediente 4 (Época III)** | Subagentes Codificadores 1:1 | **Flash Medium** (Tier 1/2) / **High** (Tier 3) | Produção de código real, contratos estritos e testes sem stubs. |
| **Expediente 5 (Época IV)** | Subagente Juiz Independente | **Flash High** | Julgamento adversarial implacável, inspeção no Chrome e ceticismo máximo. |

---

## 6. Leis da Governança Adaptativa Soberana (Invariantes Invioláveis)

1. **Veto ao Despacho Cego:** É terminantemente proibido invocar qualquer subagente sem ter executado a ACC e interagido com o usuário para confirmar o modo Flash e receber autorização explícita.
2. **Veto ao Burst de 100 Subagentes:** É terminantemente proibido despachar mais de 15 subagentes em uma única chamada de `invoke_subagent`. Mais de 15 entradas no array `Subagents` aciona `[HARD HALT]` imediato.
3. **Veto ao Flash High na Saturação de Nós:** Subagentes de planejamento de nós (Expediente 2) NUNCA são despachados quando o usuário está no modo Flash High. O modo High é reservado para Codificação Tier 3 e Auditoria Adversarial. Se o usuário estiver em Flash High antes do Expediente 2, o agente DEVE pedir a troca para Flash Low ou Medium.
4. **Persistência de Estado por Expediente:** O Agente Principal DEVE persistir o progresso em `.planning/expediente_state.json` ao término de cada expediente antes de solicitar a transição para o próximo turno.
5. **Relatório de Consumo & Sinapses Pós-Onda:** Após cada onda de subagentes, o agente emite status formal: *"Onda [N] concluída. [X] nós saturados. Sinapses propagadas no synaptic_bus.json. Próxima onda em espera."*

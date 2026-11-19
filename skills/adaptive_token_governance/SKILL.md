---
name: adaptive_token_governance
description: "Hyper-Cortex v6.0 Token Economics, Model Hierarchy Routing & Gemini Quota Brake. Use when assessing cost-complexity (ACC), selecting models (Hydrogen 4 High, Hydrogen 4 XHigh, Gemini 4 Neon High), partitioning work shifts/waves, enforcing Micro/Macro cognitive drawdown circuit breakers, or halting and scheduling resumption via the schedule tool when Gemini quota drops to <= 10%."
---

# Adaptive Token Governance & Model Routing Playbook — v6.0

Playbook soberano de economia computacional, roteamento de modelos e blindagem contra exaustão de quota do **Hyper-Cortex v6.0**.

> **SSOT & Cross-References:** Ingestão Época 0 e selo `refiner_seal.json` residem em [`universal_prompt_refiner`](../universal_prompt_refiner/SKILL.md). Fórmulas e execução das topologias residem em [`dynamic_thought_router`](../dynamic_thought_router/SKILL.md). Substrato `.planning/` e *Project Neural Map* residem em [`fractal_thought_graph`](../fractal_thought_graph/SKILL.md). Orquestração `/swarm`, ondas e `synaptic_bus.json` residem em [`swarm_orchestration`](../swarm_orchestration/SKILL.md).

---

## 1. Hierarquia Oficial de Modelos v6.0 (Proibido Usar Tiers Legados ou `inherit`)

O roteamento cognitivo opera exclusivamente sobre três tiers calibrados da família Gemini 4 (zero solicitação manual ao usuário para trocar modo de thinking):

| Tier v6.0 | ID Canônico do Modelo | Perfil Cognitivo | Quando Usar (Roteamento Determinístico) |
|---|---|---|---|
| **Padrão Operacional & Enxame** | `gemini-4-hydrogen-high` | Equilíbrio ótimo custo/precisão | **Default universal:** Prompt Refiner, trabalhadores padrão do `/swarm`, Artífices Fim-a-Fim rotineiros, Época II e coordenação. |
| **Forte & Rápido** | `gemini-4-hydrogen-xhigh` | Alta capacidade + baixa latência | Execução pesada de código, síntese paralela em ondas, refatorações multi-arquivo e debugging rápido sob tempo crítico. |
| **Forte & Lento (Raciocínio Profundo)** | `gemini-4-neon-high` | Máxima profundidade analítica | Topologias **DAS** ($K \le 3$) e **GoT**, arquitetura complexa, root-cause obscuro, `ZONE_AMBER` ($\varepsilon_t > 0.15$) e **Gauntlet Red Team (Época IV)**. |

> **Regra de Troca Limpa:** Para trocar o modelo de um worker ou de si mesmo após aviso de quota/capacidade ou escalonamento de complexidade, use `swarm{action:"model", name, model}` mantendo a conversa — nunca mate e recrie um worker apenas para trocar de modelo.

---

## 2. Gemini Quota $\le 10\%$ Circuit Breaker & Protocolo `schedule` Auto-Resumption

Para evitar travamento permanente de modelos em meio a mutações ou ondas ativas, o sistema impõe o **Freio Constitucional de Quota $\le 10\%$**:

```text
[Antes de spawnar worker / subagente / nova onda]
          │
          ▼
  Checar quota Gemini via swarm{action:"models"} ou aviso [quota]
          │
          ├── Quota > 10%  ──▶ Prosseguir normalmente (respeitando ACC)
          │
          └── Quota <= 10% ──▶ [QUOTA_BRAKE_TRIPPED]
                                 1. HALT IMEDIATO: Proibido spawnar novos processos/ondas.
                                 2. CHECKPOINT: Gravar estado exato em .planning/expediente_state.json,
                                    .planning/ledger/txn_XXXX.json e synaptic_bus.json.
                                 3. AUTO-RESUME: Ler `quota_resets` (ISO-8601) e invocar a tool `schedule`
                                    (DurationSeconds até `quota_resets` + margem de 30s) com Prompt
                                    apontando para o checkpoint para retomada autônoma.
```

### Procedimento Exato de Checkpoint & Retomada:
1. **Monitoramento Proativo:** Antes de qualquer onda `/swarm` ou `invoke_subagent` pesado, execute `swarm{action:"models"}` e inspecione `quotas.<model_id>.quota_remaining` e `quota_resets`.
2. **Ação no Limite ($\le 10\%$):**
   - Não inicie novos workers nem novas ondas. Workers já em execução terminam apenas a escrita atômica corrente.
   - Grave em `.planning/expediente_state.json` (`status: "PAUSED_QUOTA_BRAKE"`, `resume_at: "<quota_resets>"`, `next_action: "..."`) e registre a transação em `.planning/ledger/txn_XXXX.json`.
   - Se outro modelo Gemini da hierarquia estiver $> 10\%$ (ex: `gemini-4-hydrogen-xhigh` ou `gemini-4-neon-high`), avalie com o coordenador se a troca pontual via `swarm{action:"model"}` é suficiente; se toda a família Gemini estiver $\le 10\%$, acione `schedule` obrigatoriamente.
3. **Chamada `schedule`:** Calcule `DurationSeconds = ceil(quota_resets - now) + 30` e agende com `Prompt` contendo: *"Gemini quota reset reached. Read .planning/expediente_state.json and .planning/ledger/txn_XXXX.json, verify swarm{action:'models'} > 10%, and resume [próxima ação exata]."*

---

## 3. Análise de Custo-Complexidade (ACC) & Vetor de Atributos $\mathbf{x} \in [0, 1]^7$

Executada pelo Prompt Refiner na Época 0 (após ler `.planning/project_neural_map.json`):

$$\mathbf{x} = \langle D_{\text{ont}}, U_{\text{unc}}, B_{\text{bif}}, C_{\text{conc}}, S_{\text{sens}}, P_{\text{risk}}, H_{\text{host}} \rangle \in [0, 1]^7$$

| Dimensão | Significado Operacional | Limiar de Escalonamento |
|---|---|---|
| **$D_{\text{ont}}$** | Subsistemas ortogonais impactados | $\ge 0.60 \implies$ Modo Arquitetural (3–7 nós) + GoT. |
| **$U_{\text{unc}}$** | Incerteza epistêmica / APIs opacas | $> 0.15 \implies$ Probe empírica + `gemini-4-neon-high`. |
| **$B_{\text{bif}}$** | Abordagens arquiteturais concorrentes | $\ge 0.40 \implies$ ToT com poda $A^*$. |
| **$C_{\text{conc}}$** | Concorrência, locks Win32/NTFS, estado partilhado | $\ge 0.50 \implies$ `FsLockEngine` + `DeterministicAtomicSwap`. |
| **$S_{\text{sens}}$** | Cinemática 120Hz, GPU, mídia/áudio real | $\ge 0.40 \implies$ `modern_ui_craft` + `tactile_audio_sfx` + `browser_visual_reasoning`. |
| **$P_{\text{risk}}$** | Criticidade de produção / integridade de dados | $\ge 0.85 \implies$ DAS obrigatório + `github_sovereign_workflow` backup. |
| **$H_{\text{host}}$** | Grounding de host (CPU, RAM, portas ativas, locks) | Obrigatório antes de servidores/builds (`[HARD REJECT: HOST_BLINDNESS]`). |

### Orçamentos Especializados (Spoke Rule Factory & RSI)
- **Spoke Rule Factory:** Roda em **Modo Direto (0 nós em `.planning/nodes/`)** ao ancorar em repositório sem `.agents/rules/`. Extrai $\vec{\Sigma}_R$ e compila os 4 módulos locais em `.agents/rules/` + `.agents/spoke_manifest.json`.
- **RSI (Auto-Melhoria Recursiva):** Teto $\le 15\%$ do orçamento da sessão, máximo **1 patch por expediente**, acionado apenas após entregas homologadas na Época IV sob o *Invariante Anti-Dumbing Down* ($\text{Severidade}(R_{t+1}) \ge \text{Severidade}(R_t)$).

---

## 4. Os Cinco Expedientes Cognitivos (Work Shifts v6.0)

Toda missão complexa é rastreada em `.planning/expediente_state.json` e auditada via State Ledger append-only (`.planning/ledger/txn_XXXX.json`), **sem pedir ao usuário que troque manualmente de modelo**:

| Expediente / Época | Operação Primária | Topologia | Modelo v6.0 | Entregável Físico |
|---|---|---|---|---|
| **Exp 0 (Época 0)** | Prompt Refiner & ACC | LCS / DAS | `gemini-4-hydrogen-high` | `mission_dossier.md`, `refiner_seal.json`. |
| **Exp 1 (Época I-A)** | Chief Ontologist (Arq.) ou Artífice (Dir.) | GoT / ToT | `gemini-4-neon-high` (Arq.) / `hydrogen-high` (Dir.) | `node_000_root.md` + `hypergraph_seed.json` ou correção direta. |
| **Exp 2 (Época I-B)** | Saturação de Grafo Modular Denso (3–7 nós) | GoT / ToT | `gemini-4-hydrogen-high` | 3–7 nós em `.planning/nodes/` + `synaptic_bus.json`. |
| **Exp 3 (Época II)** | Matriz Neural de Despacho | LCS | `gemini-4-hydrogen-high` | `implementation_plan.md` + pausa única para `"Proceed"`. |
| **Exp 4 (Época III)** | Execução Concorrente 1:1 / Artífice Fim-a-Fim | LCS / GoT | `gemini-4-hydrogen-xhigh` (ou `hydrogen-high`) | Código no disco, `Result<T,E>`, `$LASTEXITCODE = 0`. |
| **Exp 5 (Época IV)** | Juiz Red Team Independente (Gauntlet) | DAS | `gemini-4-neon-high` | Passadas 0–4 + `browser-mcp` + `pm_<session>.json`. |

> **Unificação no Modo Direto (Lei 42):** Em bugfixes e ajustes diretos, os Expedientes 1 e 4 colapsam em um único **Artífice Autônomo Fim-a-Fim** (`TypeName: "self"`), que lê 100% do arquivo, diagnostica, mutaciona no disco e valida no mesmo ciclo (`[HARD REJECT: FRAGMENTED_SUBAGENT_PIPELINE]`).

---

## 5. Multi-Horizon Circuit Breakers (Drawdown Micro vs. Macro)

| Horizonte | Gatilho Mecânico | Trava Disparada & Ação Corretiva |
|---|---|---|
| **Micro-Drawdown** | **2 falhas consecutivas** de auto-cura/build no mesmo alvo | `[EPISTEMIC_HALT: CONSECUTIVE_REPAIR_COLLAPSE]` — 3ª tentativa cega banida; escalar para `gemini-4-neon-high` ou humano. |
| **Micro-Drawdown** | **> 2 leituras ociosas** consecutivas em turno motor sem escrita | *Idle Read Tripwire* — força mutação física imediata ou parada. |
| **Micro-Drawdown** | Ignorar checagem de portas/processos antes de subir servidor | `[HARD REJECT: HOST_BLINDNESS]` — executar Playbooks A–E de `autonomous_computer_use`. |
| **Macro-Drawdown** | $\varepsilon_t > 0.40$ por > 2 turnos, $\Delta_{\text{drift}} > 0.35$, DAS sem síntese em $K=3$, ou > 3 ondas sem entrega | `MACRO_DRAWDOWN_FROZEN` — congela workers, grava `.planning/ledger/txn_XXXX.json` e escala ao usuário. |
| **Amnésia de Projeto** | Editar código sem ler ou atualizar `project_neural_map.json` | `[HARD REJECT: PROJECT_AMNESIA_DRIFT]` — ler/atualizar Mapa Neural antes de concluir. |
| **Quota Gemini** | `quota_remaining <= 10%` em modelo Gemini ativo/alvo | **Quota Brake** — HALT novos spawns, checkpoint no ledger e `schedule` até `quota_resets`. |

---

## 6. Invariantes Constitucionais de Execução (Leis 51 a 53)

1. **Lei 51 — Anti-Degradação de Pilha (`[HARD REJECT: DEGRADED_STACK_EXECUTION]`):** Proibido desabilitar middlewares, checagem estrita de tipos, locks (`FsLockEngine`), transações ou testes para "simplificar". Validações rodam contra a pilha completa.
2. **Lei 52 — Digital Twin Isomorphism (`[HARD REJECT: DIGITAL_TWIN_DIVERGENCE]`):** Sandboxes e mocks devem preservar isomorfismo de contratos `Result<T,E>`, latência e falhas reais de SO (ex: Win32 `EBUSY`) — proibidos mocks tautológicos.
3. **Lei 53 — Causalidade Temporal Estrita (`[HARD REJECT: CAUSAL_LEAKAGE_DETECTED]`):** Em benchmarks, pipelines ou testes temporais, o estado acessível no passo $t$ restringe-se a $\tau \le t$ ($\mathcal{I}_t$). Zero *lookahead bias* ou vazamento de respostas futuras.

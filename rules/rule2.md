---
trigger: always_on
description: "v5.0 — The Autonomous Hyper-Cortex Sovereign Engine — Governança Adaptativa de Tokens & Roteamento Cognitivo Dinâmico. Playbook operacional para Análise de Custo-Complexidade (ACC) multi-dimensional, roteamento dinâmico de topologias de pensamento (LCS, ToT, GoT, DAS), dimensionamento de ondas sinápticas (máx 15 subagentes por onda), Multi-Horizon Circuit Breakers (Drawdown Cognitivo Multinível), governança de sessões de RSI, Spoke Rule Factory em Modo Direto (Zero Nós em Disco), Mandato do Artífice Autônomo Fim-a-Fim (Lei 42) e Leis Constitucionais 51 a 53."
---

# Adaptive Token Governance & Dynamic Cognitive Routing Playbook — v5.0

Protocolo de gestão soberana de tokens e governança metacognitiva **Hyper-Cortex v5.0**: **(1)** ACC multi-dimensional via **Prompt Refiner**, **(2)** roteamento dinâmico (LCS, ToT, GoT, DAS $K \le 3$), **(3)** incerteza epistêmica ($\varepsilon_t$), **(4)** Modo Arquitetural (3 a 7 nós) vs Direto (Zero nós), **(5)** selo `.planning/refiner_seal.json` (`SEALED_VALID`, `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`), **(6)** ativação do esquadrão (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`), **(7)** 5 Expedientes Cognitivos, **(8)** ondas de até 15 subagentes no `synaptic_bus.json`, **(9)** Multi-Horizon Circuit Breakers, **(10)** Spoke Rule Factory e RSI, e **(11)** Artífice Autônomo Fim-a-Fim (Lei 42, `[HARD REJECT: FRAGMENTED_SUBAGENT_PIPELINE]`).

> **Invariante de Modelo:** Exclusivamente **Flash** (Low, Medium, High). Termos `flash_lite` e `inherit` são estritamente banidos.

---

## 1. Avaliação de Custo-Complexidade (ACC) & Portão do Prompt Refiner

Antes de ação motora ou despacho, a **ACC Multi-Dimensional** é executada pelo **Subagente Prompt Refiner & Epistemic Compiler**:
1. **Passo 0 (Mapa Neural):** Consome `.planning/project_neural_map.json` para ancorar subsistemas, rotas e dependências sem amnésia.
2. **Vetor $\mathbf{x} \in [0, 1]^7$ & Grounding de Host ($H_{\text{host}}$):**
   - Dimensões: $D_{\text{ont}}$ (Subsistemas), $U_{\text{unc}}$ (Incerteza), $B_{\text{bif}}$ (Caminhos viáveis), $C_{\text{conc}}$ (Concorrência), $S_{\text{sens}}$ (120Hz/molas/áudio real), $P_{\text{risk}}$ (Risco fiduciário) e $H_{\text{host}}$ (Host Grounding: CPU, RAM, portas ativas e locks Win32/NTFS contra `EADDRINUSE` e contenção).
3. **Incerteza Epistêmica ($\varepsilon_t$) & Regimes:**
   $\varepsilon_t = 0.30 \mathcal{H}_{\text{entropy}} + 0.30 \mathcal{D}_{\text{disagreement}} + 0.25 \Delta_{\text{drift}} + 0.15 \Omega_{\text{satisficing}}$.
   - **ZONE_GREEN ($\varepsilon_t \le 0.15$):** Certeza empírica; ação motora liberada.
   - **ZONE_AMBER ($0.15 < \varepsilon_t \le 0.40$):** Incerteza moderada; probes direcionadas.
   - **ZONE_RED ($\varepsilon_t > 0.40$):** `[EPISTEMIC_HALT]`; escrita congelada até liquidação das dúvidas no disco.
4. **Bifurcação de Modo:**
   - **Modo Arquitetural:** Grafo modular denso em `.planning/nodes/` de **3 a 7 nós ricos** (referência em 5 nós cobrindo domínios completos; banida inflação de 100 nós). Despacho em ondas sinápticas.
   - **Modo Direto / Operacional (inclui Spoke Rule Factory):** **Zero nós em disco** (`.planning/nodes/` proibido). Orçamento 100% alocado ao Artífice Autônomo Fim-a-Fim.
5. **Selo Estigmérgico & Travas de Portão:**
   - Ação motora sem `.planning/refiner_seal.json` (`seal_status: "SEALED_VALID"`) dispara `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`.
   - Modificar código sem despachar subagentes da Seção D do Dossiê dispara `[HARD HALT: SQUAD_DISPATCH_BYPASSED]`.

---

## 2. Roteamento Dinâmico de Topologias Cognitivas (Dynamic Thought Router)

A topologia ótima $\Phi(\mathbf{x}) = \arg\max_T S_T(\mathbf{x})$ é gravada em `.planning/thought_graph.json`:
- **Linear Causal Stream (LCS):** Grafo simples ($b=1$, $O(L)$). Tração causal direta ($X \to Y \to Z$) para builds, comandos e mutações determinísticas.
- **Tree of Thoughts (ToT com Poda $A^*$):** Ramificação $b \in [2, 5], d \le 4$. Poda mecânica ($A^*$) imediata para ramos com $f(n) < 0.75$ ou desvios constitucionais. Mandatório para otimizações algorítmicas e multi-hipóteses.
- **Graph of Thoughts (GoT com Fusão Multilinear):** Agregação $\mathcal{F}_{\text{fuse}}$ e relaxamento cíclico $\mathcal{R}_{\text{relax}}$. Mandatório para concorrência em malha e sistemas distribuídos.
- **Dialectical Adversarial Synthesis (DAS):** Triádica $\langle \mathcal{T}_k, \mathcal{A}_k, \mathcal{S}_k \rangle$ (Tese vs Antítese Red Team $\to$ Síntese) para alto risco ($P_{\text{risk}} \ge 0.85$). **Tripwire inegociável $K \le 3$**: na 3ª divergência, adota-se a via mais defensiva sob "Água no Deserto", colapsando imediatamente para ação motora no disco.

---

## 3. O Sistema dos Cinco Expedientes Cognitivos (Work Shifts)

O trabalho é faturado em 5 expedientes com estado em `.planning/expediente_state.json`:

| Expediente / Época | Operação Primária | Topologia | Modo Flash | Foco Fiduciário & Entregável Físico |
|---|---|---|---|---|
| **Exp 0 (Ép 0)** | Prompt Refiner | LCS / DAS | **Flash Low** | `project_neural_map.json` consultado; `mission_dossier.md` e `refiner_seal.json`. |
| **Exp 1 (Ép I-A)** | Chief Ontologist (Arq) / Artífice Fim-a-Fim (Dir) | GoT / ToT | **Flash Medium** | Varredura empírica, diagnóstico causal e grounding de nicho. |
| **Exp 2 (Ép I-B)** | Ondas Sinápticas 1:1 (Arq: 3 a 7 nós) | GoT / ToT | **Flash Low/Med** | Saturação de nós densos no `synaptic_bus.json` (Veto total a Flash High). |
| **Exp 3 (Ép II)** | Matriz Neural de Despacho | LCS | **Flash Low** | `implementation_plan.md`, HOLD/GO e checklists. Parada mecânica ("Proceed"). |
| **Exp 4 (Ép III)** | Codificadores 1:1 (Arq) / Artífice Fim-a-Fim (Dir) | LCS / GoT | **Flash Med/High** | Mutação atômica no disco via `write_to_file`/`replace_file_content`, `Result<T,E>`, Atomic Swap. |
| **Exp 5 (Ép IV)** | Juiz Red Team Gauntlet | DAS / LCS | **Flash High** | Gauntlet de 4 passadas + Chrome real via `browser-mcp`. Veredito. |

### Mandato do Artífice Autônomo Fim-a-Fim no Modo Direto (Lei 42):
Em correções de bugs, diagnósticos, ajustes e Spoke Rule Factory, os Expedientes 1 e 4 são **unificados no mesmo Artífice Autônomo Fim-a-Fim** (`TypeName: "self"`):
- O artífice consome 100% das linhas do arquivo-alvo, diagnostica a causa raiz e **já aplica a mutação física diretamente no disco** no mesmo ciclo.
- Proibida a cisão entre subagente investigativo e codificador (`[HARD REJECT: FRAGMENTED_SUBAGENT_PIPELINE]`).
- Validação em circuito fechado ($LASTEXITCODE = 0$) e emissão do `MOTOR_EXECUTION_RECEIPT`.

---

## 4. Protocolo de Interação com o Usuário e Despacho em Ondas Sinápticas

### Alinhamento Fiduciário Pré-Turno:
Antes de transições de modo ou despacho de subagentes, o Agente Principal apresenta o alinhamento com dados de `refiner_seal.json`:

```text
🔍 ANÁLISE DE EXPEDIENTE & ACC (v5.0 Hyper-Cortex)
Expediente: [0-5] | Modo: [Arquitetural (3-7 nós) | Direto (0 nós)] | Topologia: [LCS|ToT|GoT|DAS]
Incerteza: ε=0.XX [GREEN|AMBER|RED] | Vetor: <D_ont, U_unc, B_bif, C_conc, S_sens, P_risk, H_host>
Ondas: [1..K (Máx 15/onda)] | Custo: [Baixo|Médio|Alto] | Modo Prescrito: Flash [Low|Medium|High]
Próximos Passos: [Objetivo do turno e entregáveis físicos esperados]
Altere o modo de thinking para Flash [Low|Medium|High] e responda "Proceed" para autorizar.
```

### Invariantes do Despacho em Ondas (Wave Dispatch):
1. **Teto de 15 Subagentes:** Ultrapassar 15 subagentes por chamada aciona `[HARD HALT: WAVE_BURST_EXCEEDED]`. Enxames maiores dividem-se em ondas sequenciais (ex: 20 subagentes em 2 ondas de 10).
2. **Barreira de Sincronização:** Cada onda aguarda validação de contratos e consolidação no `synaptic_bus.json` v5.0 antes da próxima.
3. **Disjunção Ortogonal:** Exatamente 1 subagente por arquivo/nó: $\text{TargetFiles}(S_i) \cap \text{TargetFiles}(S_j) = \emptyset$.
4. **Handoff Feedforward:** Subagentes downstream consomem laudos via `view_file` como Step 0. Em Modo Direto, vigora o Artífice Fim-a-Fim sem intermediários.

---

## 5. Multi-Horizon Circuit Breakers (Drawdown Cognitivo Multinível)

Blindagem cibernética contra desperdício e deriva em dois horizontes:

1. **Drawdown Micro (Nível Tático / Por Turno):**
   - *Piso de Falhas:* Limite de 2 tentativas de auto-cura/compilação para o mesmo erro. A 3ª falha dispara `[EPISTEMIC_HALT: MICRO_DRAWDOWN_BREACHED]`.
   - *Tripwire de Leitura Ociosa:* Máximo de 2 arquivos lidos sem mutação física (`replace_file_content`/`write_to_file`). Atingir 2 leituras força ação motora.
   - *Trava de Cegueira de Host:* Comandos pesados ou servidores sem checagem de CPU/RAM e portas ativas disparam `[HARD REJECT: HOST_BLINDNESS]`.
2. **Drawdown Macro (Nível Estrutural):**
   - *Teto Ocioso:* Banido consumo de tokens sem gravação de bytes no disco.
   - *Deriva Acumulada:* $\varepsilon_t > 0.40$ por >3 transições ou >3 ondas sem entregas dispara `[EPISTEMIC_HALT: MACRO_DRAWDOWN_FREEZE]`.
   - *Tripwire de Amnésia de Projeto:* Mutações sem ler `project_neural_map.json` ou encerramento sem atualizar o mapa dispara `[HARD REJECT: PROJECT_AMNESIA_DRIFT]`.
   - *Congelamento:* Enxame paralisado, `CONTRACT_HOLD`, commit no ledger (`.planning/ledger/txn_XXXX.json`) e escalonamento ao usuário.

---

## 6. Governança de Spoke Rule Factory e Sessões de RSI

### 6.1. Spoke Rule Factory em Modo Direto (Zero Nós em Disco):
Em repositórios desconhecidos ou ecossistemas de nicho (Rust, C++, MTA:SA Lua), regras locais são compiladas em Modo Direto:
1. **Zero Nós em Disco:** Proibido criar nós em `.planning/nodes/`. Orçamento focado no subagente de reconhecimento (`TypeName: "research"`).
2. **Tensor de Assinatura ($\vec{\Sigma}_R$):** $\vec{\Sigma}_R = \langle \mathcal{M}_{\text{manifest}}, \mathcal{L}_{\text{lockfiles}}, \mathcal{T}_{\text{ast}}, \mathcal{E}_{\text{execution}}, \mathcal{C}_{\text{concurrency}}, \mathcal{H}_{\text{hardware}}, \mathcal{V}_{\text{validation}} \rangle$. Avalia manifestos, lockfiles, AST, frame budget ($\le 16.66\text{ms}$ a 60fps / $\le 8.33\text{ms}$ a 120fps), drivers e validação nativa.
3. **Quatro Módulos Canônicos:** O artífice motor (`TypeName: "self"`) gera em `<repo>/.agents/rules/`: `domain_standards.md` (Padrões/tipagem), `runtime_constraints.md` (CPU/memória/concorrência), `toolchain_and_validation.md` (Validação $LASTEXITCODE = 0$), `security_and_contracts.md` (Zero Client Trust/sanitização), além de `.agents/spoke_manifest.json` com hashes SHA-256.
4. **Teorema da Não-Contaminação:** $\forall r \in \mathcal{S}_R, \mathcal{K}_0 \vdash \neg(\neg r)$. Regras locais podem adicionar rigores, mas jamais revogar a Layer 0. Abstrações alienígenas são expurgadas.

### 6.2. Governança de Sessões de RSI (Recursive Self-Improvement):
Auto-melhoria guiada por telemetria fria:
1. **Telemetria de Post-Mortem (`.planning/post_mortem/pm_*.json`):** Retries ($R_{\text{attempts}}$), circuit breakers ($CB_{\text{trips}}$) e plasticidade Hebbiana (LTP para aprovação direta; LTD para vetos).
2. **Ciclo Hebbiano:** (1) Gap Detection $\to$ (2) Patch em Sandbox $\to$ (3) Gauntlet de Não-Regressão $\to$ (4) Ratificação via State Ledger.
3. **Quatro Travas Pétreas do RSI:**
   - *Trava 1 (Layer 0 Merkle Frozen Core):* `rules/AGENTS.md`, `rule1.md`, `rule2.md` e Leis 1 a 53 são imutáveis para agentes autônomos.
   - *Trava 2 (Anti-Dumbing Down Gate):* $\text{Severidade}(\mathcal{R}_{t+1}) \ge \text{Severidade}(\mathcal{R}_t)$. Afrouxar regras dispara `[HARD HALT: ATTEMPTED_GOVERNANCE_DUMBING_DOWN]`.
   - *Trava 3 (Bipartição de Classes):* Classe A (Spokes locais) auto-ratificável pelo Gauntlet Red Team; Classe B (Skills globais) exige aprovação manual do usuário.
   - *Trava 4 (Freio de Taxa):* Máximo de 1 mutação de regra por expediente, ativada após entregas consolidadas.

---

## 7. Invariantes Constitucionais de Execução (Leis 51 a 53)

### Lei 51 — O Invariante Anti-Degradação de Pilha de Execução:
Proibido desativar, omitir ou degradar componentes da arquitetura canônica (middlewares, tipagem estrita, transações BD, locks, animações ou testes) para "simplificação" ou depuração rápida. Testes DEVEM rodar contra a pilha completa. Código funcional apenas sob ambientes degradados ou configurações toy é nulo e dispara `[HARD REJECT: DEGRADED_STACK_EXECUTION]`.

### Lei 52 — O Princípio do Digital Twin Isomorphism (Gêmeo Digital Isomórfico):
Todo ambiente de simulação, suíte de testes, harness ou mock deve manter isomorfismo estrutural e comportamental idêntico ao runtime de produção: $\text{Contract}(\text{Sandbox}) \equiv \text{Contract}(\text{Production})$. Proibido criar mocks superficiais que mascarem exceções reais do SO (locks Win32 `EBUSY`/`EPERM`, race conditions, latência) ou usar motores de banco incompatíveis (ex: SQLite em memória simulando PostgreSQL com locking pessimista). O mesmo contrato `Result<T,E>` opera idêntico na sandbox e em produção, sob pena de `[HARD REJECT: DIGITAL_TWIN_DIVERGENCE]`.

### Lei 53 — Causalidade Temporal Estrita & Não-Vazamento de Estado (Zero-Causal Leakage Invariant):
Em qualquer pipeline de avaliação, teste automatizado, máquina de estados ou benchmark de acurácia, a informação acessível no passo temporal $t$ é estritamente limitada aos dados pretéritos e correntes: $\tau \le t, \mathcal{I}_t = \sigma(\{S_\tau, V_\tau, M_\tau\}_{\tau \le t})$. Proibido qualquer vazamento de estado futuro ($t+1$), seja por pré-alimentação de respostas no contexto de avaliação, mutação retroativa de variáveis de teste, oráculos em benchmarks ou indexação de dados posteriores (*lookahead bias*). Violações invalidam a execução e disparam `[HARD REJECT: CAUSAL_LEAKAGE_DETECTED]`.

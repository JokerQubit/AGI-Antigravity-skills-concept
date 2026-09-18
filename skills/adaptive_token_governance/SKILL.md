---
name: adaptive_token_governance
description: "v5.0 — The Autonomous Hyper-Cortex Sovereign Engine — Governança Adaptativa de Tokens & Roteamento Inteligente de Modelos. Playbook operacional para Análise de Custo-Complexidade (ACC), dimensionamento de eixos via assinatura de problema (vetor x in [0, 1]^6), escalonamento Flash Thinking coordenado com o dynamic_thought_router (LCS, ToT com poda A*, GoT com fusão multilinear, DAS com tripwire K <= 3), regimes de incerteza epistêmica (epsilon) e gestão por expedientes cognitivos (Work Shifts)."
---

# Adaptive Token Governance & Model Routing Playbook — v5.0 (The Autonomous Hyper-Cortex)

Protocolo operacional de gestão soberana de tokens que governa sete comportamentos invioláveis: **(1)** chancela e avaliação de custo-complexidade (ACC) via extração compulsória do **Vetor de Assinatura do Problema ($\mathbf{x} \in [0, 1]^6$)** pelo **Prompt Refiner Ubíquo**, **(2)** classificação mandatória da missão em **Modo Arquitetural** ($N \ge 100$ nós) ou **Modo Direto / Operacional** (Zero nós em disco), **(3)** dimensionamento de eixos ontológicos e seleção determinística da topologia cognitiva via **Dynamic Thought Router** (`skills/dynamic_thought_router`), **(4)** emissão mandatória do selo estigmérgico (`.planning/refiner_seal.json`) antes de qualquer ação motora sob pena de `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`, **(5)** ativação imediata do esquadrão do blueprint do Dossiê antes de qualquer mutação de código (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`), **(6)** particionamento do trabalho em **Expedientes Cognitivos (Work Shifts)** com persistência e State Ledger (`.planning/ledger/`), e **(7)** escalonamento de modos **Flash Thinking (Low, Medium, High)** calibrado pelas **Zonas de Incerteza Epistêmica ($\varepsilon_t$)** e pela topologia ativa.

> O ecossistema utiliza exclusivamente o modelo **Flash** nos modos **Low**, **Medium** e **High** de thinking. Não existem outros modelos no roteamento. `flash_lite` e `inherit` são termos banidos neste protocolo.

---

## 1. Avaliação de Complexidade & Custo de Tokens (Pré-Despacho Obrigatório pelo Prompt Refiner Ubíquo)

**Antes de despachar qualquer subagente ou executar qualquer alteração de código**, a **Análise de Custo-Complexidade (ACC)** DEVE ser executada compulsoriamente pelo **Subagente Especialista: Prompt Refiner & Epistemic Compiler**:
- **Chancela no Expediente 0 (Macro-ACC & Assinatura de Problema):** No início da missão, o Prompt Refiner avalia a demanda do usuário, extrai o vetor $\mathbf{x}$, classifica o modo de missão (Arquitetural vs. Direto), dimensiona os eixos ontológicos com base na física do problema, calcula o número de ondas ($\lceil N/15 \rceil$ se arquitetural), determina a topologia inicial do Dynamic Thought Router e emite o `mission_dossier.md` com o blueprint do esquadrão tático e o selo inicial de governança.
- **Chancela Ubíqua Pré-Turno (Micro-ACC sob TaaS):** Em todo e qualquer turno subsequente (Expedientes 1 a 5), antes de despachar subagentes de onda ou codificação, o Prompt Refiner disseca a intervenção do usuário do turno atual, recalcula o vetor $\mathbf{x}$, audita a incerteza $\varepsilon_t$, recalibra as ondas e emite o selo criptográfico/estigmérgico `.planning/refiner_seal.json` com status `SEALED_VALID`.
- **Trava Mecânica de Portão:** Se o Agente Principal tentar executar ferramentas motoras (`write_to_file`, `replace_file_content`, `run_command`) ou despachar outros subagentes sem o selo válido do Prompt Refiner do turno, a operação é sumariamente abortada via `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`.

### 1.1. Vetor de Assinatura do Problema ($\mathbf{x}$) & Dimensionamento de Eixos:
Toda demanda é decomposta no vetor normalizado:
$$\mathbf{x} = \langle D_{\text{ont}}, U_{\text{unc}}, B_{\text{bif}}, C_{\text{conc}}, S_{\text{sens}}, P_{\text{risk}} \rangle \in [0, 1]^6$$

1. **$D_{\text{ont}}$ (Dimensionalidade Ontológica):** Quantidade de subsistemas independentes impactados (UI, Storage, Concorrência, Rede, Áudio, SO).
2. **$U_{\text{unc}}$ (Incerteza Epistêmica $\varepsilon$):** Nível de ausência de documentação, opacidade de APIs ou comportamento estocástico externo.
3. **$B_{\text{bif}}$ (Fator de Bifurcação de Decisão):** Número de abordagens viáveis concorrentes para solucionar a demanda.
4. **$C_{\text{conc}}$ (Complexidade de Concorrência & Estado Compartilhado):** Risco de race conditions, deadlocks ou inconsistência transacional.
5. **$S_{\text{sens}}$ (Sensibilidade Sensorial & Fiduciária):** Requisitos de cinemática 120fps, isolamento de GPU, micro-ativos ópticos reais ou áudio Foley real.
6. **$P_{\text{risk}}$ (Criticidade de Risco de Produção):** Gravidade do modo de falha para a integridade de dados e sobrevivência corporativa.

**Dimensionamento de Eixos Ontológicos com Base na Assinatura:**
- Se $C_{\text{conc}} \ge 0.5$: ativação mandatória do Eixo de Concorrência & Sincronização em Tempo Real (Locks otimistas, filas lock-free, zero alocação no frame quente).
- Se $S_{\text{sens}} \ge 0.5$: ativação mandatória dos Eixos de HCI & Cinemática de Molas de 2ª Ordem e Mídia Fotográfica/Áudio Físico Real via `generate_image` e `sfx_tool.py`.
- Se $D_{\text{ont}} \ge 0.6$: ativação do Eixo de Sistemas em Malha com fusão multilinear GoT no `synaptic_bus.json`.
- Se $P_{\text{risk}} \ge 0.7$: ativação do Eixo de Engenharia do Caos e Modos Silenciosos de Falha com pre-mortem formal T+6 meses.

### 1.2. Integração com o Dynamic Thought Router:
As pontuações de adequação das topologias de pensamento são calculadas determinísticamente a partir de $\mathbf{x}$:
$$S_{\text{LCS}}(\mathbf{x}) = (1 - B_{\text{bif}}) \cdot (1 - U_{\text{unc}}) \cdot (1 - C_{\text{conc}}) \cdot (1 - D_{\text{ont}})$$
$$S_{\text{ToT}}(\mathbf{x}) = B_{\text{bif}} \cdot (1 - C_{\text{conc}}) \cdot \left(\frac{1 + U_{\text{unc}}}{2}\right)$$
$$S_{\text{GoT}}(\mathbf{x}) = D_{\text{ont}} \cdot C_{\text{conc}} \cdot \left(\frac{1 + S_{\text{sens}}}{2}\right)$$
$$S_{\text{DAS}}(\mathbf{x}) = P_{\text{risk}} \cdot \max(U_{\text{unc}}, B_{\text{bif}}) \cdot \left(\frac{1 + D_{\text{ont}}}{2}\right)$$

A topologia ótima $\Phi(\mathbf{x}) = \arg\max_{T} S_T(\mathbf{x})$ governa o estilo de raciocínio da fase e é registrada em `.planning/thought_graph.json`.

### 1.3. Sessão Soberana v5.0 & Escalonamento Flash Thinking:
A intensidade computacional de Thinking no modelo Flash é governada conjuntamente pela **Topologia Ativa** e pelas **Zonas de Incerteza Epistêmica ($\varepsilon_t$)**:
- **`ZONE_GREEN` ($0.00 \le \varepsilon_t \le 0.15$):** Certeza determinística. Roteamento para **Flash Low** (ou **Flash Medium** durante codificação atômica complexa).
- **`ZONE_AMBER` ($0.15 < \varepsilon_t \le 0.40$):** Atrito probabilístico. Roteamento obrigatório para **Flash Medium** ou **Flash High**. Dispara checagens empíricas antes de escrita.
- **`ZONE_RED` ($\varepsilon_t > 0.40$):** Ambiguidade crítica. Disparo de `[EPISTEMIC_HALT]`. Congelamento imediato de mutações.

| Expediente / Época | Topologia Cognitiva | Regime $\varepsilon$ | Modo Flash Prescrito | Justificativa |
|---|---|---|---|---|
| **Expediente 0 (Época 0)** | LCS / Análise Forense | $\varepsilon \le 0.15$ | **Flash Low** | Extração do vetor $\mathbf{x}$, ACC, classificação de modo e Dossiê Universal. |
| **Expediente 1 (Época I - Fase A)** | ToT / GoT Semente / Dupla Inv. | $0.15 < \varepsilon \le 0.40$ | **Flash Medium** | Varredura empírica, formulação ontológica ou investigação causal contrastiva (Alfa vs. Beta). |
| **Expediente 2 (Época I - Fase B)** | GoT / ToT Coordenados | $\varepsilon \le 0.25$ | **Flash Low ou Medium** | Saturação sináptica em ondas 1:1 com poda fiduciária $A^*$ e fusão $\mathcal{F}_{\text{fuse}}$. |
| **Expediente 3 (Época II)** | LCS / Matriz de Despacho | $\varepsilon \le 0.15$ | **Flash Low** | Síntese determinística nó-a-nó, checklists binários e parada mecânica para aprovação. |
| **Expediente 4 (Época III)** | LCS / GoT Motor 1:1 | $\varepsilon \le 0.15$ | **Flash Medium ou High** | Mutação atômica no disco via ferramentas motoras (`TypeName: "self"`), `Result<T,E>`, zero stubs. |
| **Expediente 5 (Época IV)** | DAS (Dialética Adversarial) | Incerteza Red Team | **Flash High** | Gauntlet adversarial de 4 passadas + inspeção perceptual no Chrome real via `browser-mcp`. |

---

## 2. O Sistema de Expedientes Cognitivos (Work Shifts v5.0)

O sistema rejeita a ilusão de resolver grandes arquiteturas em um único "sprint cego" contínuo. Toda demanda é particionada em **Expedientes Cognitivos** formais com estado persistido no disco em `.planning/expediente_state.json` e auditado no State Ledger (`.planning/ledger/`):

```text
┌─────────────────────────────────────────────────────────────┐
│ EXPEDIENTE 0: Ingestão Estratégica & Refinamento de Prompt  │
│ • Subagente Prompt Refiner compila mission_dossier.md       │
│ • Extração do vetor x, classificação de modo e ACC          │
│ • Roteamento inicial Dynamic Thought Router                 │
│ • Modo: Flash Low                                           │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 1: Arquitetura Ontológica Raiz & Semente Neural  │
│ • Subagente Chief Ontologist (Arq.) ou Dupla Inv. (Direto)  │
│ • Emite node_000_root.md / seed.json ou inv_001/inv_002.md  │
│ • Topologia: ToT (poda A*) ou GoT (fusão de contratos)      │
│ • Modo: Flash Medium                                        │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 2: Saturação Sináptica em Ondas (1:1)            │
│ • Despacho em Ondas (máx 15 subagentes/onda)                │
│ • Barramento Sináptico Neural (synaptic_bus.json v5.0)      │
│ • Topologia: GoT multilinear e ToT coordenados              │
│ • Modo: Flash Low ou Flash Medium                           │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 3: Matriz de Despacho & Trava Humana (Época II)  │
│ • Síntese formal nó-a-nó no implementation_plan.md          │
│ • Checklists binários extensivos e trava mecânica "Proceed" │
│ • Topologia: Linear Causal Stream (LCS)                     │
│ • Modo: Flash Low                                           │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 4: Codificação Concorrente Atômica 1:1 (Época III)│
│ • Subagentes codificadores motores 1:1 (TypeName: "self")   │
│ • Mutação física direta no disco, Result<T,E>, zero stubs   │
│ • Modo: Flash Medium ou Flash High                          │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 5: Auditoria Adversarial Independente (Época IV) │
│ • Subagente Juiz executa as 4 passadas do Gauntlet          │
│ • Inspeção perceptual no Chrome real via browser-mcp        │
│ • Topologia: Dialectical Adversarial Synthesis (DAS)        │
│ • Modo: Flash High                                          │
└─────────────────────────────────────────────────────────────┘
```

### Persistência de Estado Estigmérgico (`.planning/expediente_state.json`):
```json
{
  "state_version": "5.0.0",
  "current_expediente": 2,
  "expediente_name": "Saturação Sináptica em Ondas",
  "status": "IN_PROGRESS",
  "problem_signature_vector": {
    "D_ont": 0.75,
    "U_unc": 0.20,
    "B_bif": 0.60,
    "C_conc": 0.85,
    "S_sens": 0.70,
    "P_risk": 0.80
  },
  "active_thought_topology": "GRAPH_OF_THOUGHTS",
  "epistemic_uncertainty_epsilon": 0.12,
  "epistemic_zone": "ZONE_GREEN",
  "recommended_flash_mode": "Medium",
  "current_wave": 2,
  "total_waves": 7,
  "nodes_completed": 30,
  "nodes_target": 105,
  "ledger_last_transaction": "txn_0004.json",
  "last_synaptic_sync": "2026-09-17T20:20:00Z"
}
```

---

## 3. Protocolo Obrigatório de Interação com o Usuário (Alinhamento Pré-Turno v5.0)

Antes de iniciar qualquer novo expediente ou turno que exija mudança de modo ou despacho de subagentes, **o Agente Principal DEVE PARAR e interagir com o usuário**, alimentando a mensagem obrigatoriamente com os dados auditados do selo estigmérgico `.planning/refiner_seal.json` emitido pelo Prompt Refiner:

### Formato da Mensagem de Roteamento (Template Constitucional v5.0):

```text
🔍 ANÁLISE DE EXPEDIENTE & CUSTO-COMPLEXIDADE v5.0
══════════════════════════════════════════════════════════
Expediente Atual:    [Expediente 0 | 1 | 2 | 3 | 4 | 5]
Modo de Missão:      [Arquitetural (N >= 100 Nós) | Direto / Operacional (Zero Nós)]
Assinatura Vetor x:  <D_ont={..}, U_unc={..}, B_bif={..}, C_conc={..}, S_sens={..}, P_risk={..}>
Topologia Router:    [Linear Causal Stream (LCS) | Tree of Thoughts (ToT) | Graph of Thoughts (GoT) | Dialectical Synthesis (DAS)]
Regime Epistêmico:   [ZONE_GREEN (ε <= 0.15) | ZONE_AMBER (0.15 < ε <= 0.40) | ZONE_RED (HALT)]
Nós em Disco:        [≥ 100 nós em .planning/nodes/ | 0 nós (Plano Direto)]
Ondas de Despacho:   [Ondas 1..K | Despacho Concorrente de Squad]
Custo Estimado:      [Baixo | Médio | Alto]

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

## 5. Leis da Governança Adaptativa Soberana (Invariantes Invioláveis v5.0)

1. **Veto ao Despacho Cego:** É terminantemente proibido invocar qualquer subagente sem ter executado a ACC, mapeado o vetor $\mathbf{x}$ e interagido com o usuário para confirmar o modo Flash e receber autorização explícita.
2. **Veto ao Burst de 100 Subagentes:** É terminantemente proibido despachar mais de 15 subagentes em uma única chamada de `invoke_subagent`. Mais de 15 entradas no array `Subagents` aciona `[HARD HALT]` imediato.
3. **Veto ao Flash High na Saturação de Nós:** Subagentes de planejamento de nós (Expediente 2) NUNCA são despachados quando o usuário está no modo Flash High. O modo High é reservado para Codificação (Expediente 4) e Auditoria Adversarial (Expediente 5). Se o usuário estiver em Flash High antes do Expediente 2, o agente DEVE pedir a troca para Flash Low ou Medium.
4. **Persistência de Estado por Expediente:** O Agente Principal DEVE persistir o progresso em `.planning/expediente_state.json` ao término de cada expediente antes de solicitar a transição para o próximo turno.
5. **Relatório de Consumo & Sinapses Pós-Onda:** Após cada onda de subagentes, o agente emite status formal: *"Onda [N] concluída. [X] nós saturados. Sinapses propagadas no synaptic_bus.json. Próxima onda em espera."*
6. **Veto ao Despacho e Execução sem Selo do Prompt Refiner (`[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`) e sem Ativação do Esquadrão (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`):** É expressamente proibido ao Agente Principal despachar qualquer subagente adicional, disparar ondas sinápticas, modificar arquivos (`write_to_file`, `replace_file_content`) ou executar comandos de modificação (`run_command`) sem que o **Subagente Prompt Refiner & Epistemic Compiler** tenha sido previamente despachado no turno atual e persistido o selo criptográfico `.planning/refiner_seal.json` com `seal_status: "SEALED_VALID"` e hash coincidente com o prompt cru do usuário. Adicionalmente, assim que o Dossiê for emitido, os subagentes especializados listados na Seção D do dossiê DEVEM ser despachados imediatamente antes de qualquer mutação de código, sob pena de `[HARD HALT: SQUAD_DISPATCH_BYPASSED]`. O Dossiê Universal (`.planning/mission_dossier.md`) é o único artefato de ingestão permitido — a distinção entre dossiê cirúrgico e arquitetural está extinta.
7. **Circuit Breakers Cognitivos & Tripwires de Consumo (Anti-Runaway Protocol):** É terminantemente proibido consumir tokens em investigações circulares infinitas. O sistema opera sob dois tripwires de proteção financeira e cognitiva:
   - *Tripwire de Leitura Ociosa (Idle Read Tripwire):* Em turnos operacionais de implementação ou correção, é proibido ler mais de 2 arquivos consecutivos sem realizar uma alteração física (`replace_file_content` ou `write_to_file`). Atingir 2 leituras força o despacho da ação motora ou parada.
   - *Tripwire de Falhas Consecutivas:* Limite estrito de 2 tentativas de remediação para o mesmo erro. A persistência do erro na 3ª tentativa dispara `[EPISTEMIC_HALT]` mandatório para intervenção humana ou reavaliação causal.
8. **Livro-Razão Transacional Imutável (State Ledger Append-Only Invariant):** Nenhuma transição de expediente, homologação de época ou mutação de barramento sináptico é concluída sem o registro de uma transação imutável numerada em `.planning/ledger/txn_XXXX.json` (contendo timestamp, hash do commit, estado de contratos e assinatura do fiduciário), além da sincronização em `.planning/expediente_state.json`.
9. **O Mandato do Roteamento Dinâmico de Topologias (Lei 44):** Toda deliberação de engenharia deve instanciar dinamicamente a topologia mental matematicamente adequada via `skills/dynamic_thought_router` (LCS, ToT com poda $A^*$, GoT com fusão multilinear ou DAS dialética). Proibido linearizar problemas combinatórios ou deliberar reflexivamente sobre micro-mutações determinísticas.
10. **Poda Fiduciária & Tripwire Dialético de Convergência (Lei 45):** Em árvores (ToT), ramos com $f(n) < 0.75$ sofrem poda imediata. Em debates dialéticos (DAS), impõe-se convergência estrita em $K \le 3$ iterações; na 3ª iteração sem consenso, adota-se compulsoriamente a via mais defensiva ("Água no Deserto").
11. **Monitoramento Contínuo de Deriva de Objetivo (Lei 46):** Rastreamento invariante de $\Delta_{\text{drift}} \le 0.35$. Ultrapassar o limiar aciona `[EPISTEMIC_HALT: GOAL_DRIFT_BOUNDARY_VIOLATION]`.
12. **Plasticidade Sináptica & Aprendizado Estigmérgico (Lei 47):** Conhecimento inscrito imutavelmente em `synaptic_bus.json` e no ledger. Vedada regressão epistêmica ou repetição de investigações já consolidadas.

### 5.1. Catálogo dos Cinco Gatilhos de `[EPISTEMIC_HALT]`:
1. `HALT_CRITICAL_UNCERTAINTY` ($\varepsilon_t > 0.40$): Incerteza crítica no tensor convexa de 4 componentes.
2. `HALT_CONFIRMATION_BIAS_LOOP`: Repetição de premissa teórica por 2 turnos sem probe física no disco.
3. `HALT_GOAL_DRIFT_EXCEEDED` ($\Delta_{\text{drift}} > 0.35$): Mutação fora dos arquivos do dossiê.
4. `HALT_PREMATURE_CONVERGENCE`: Proposta de encerramento sem contrastar hipóteses alternativas ou Red Team.
5. `HALT_CONSECUTIVE_REPAIR_COLLAPSE`: Duas tentativas consecutivas de auto-cura falham ($LASTEXITCODE \ne 0$).

### 5.2. Matriz de Calibração Anti-Satisficing:
| Dimensão Técnica | Anti-Pattern (Satisficing) | Padrão dos Titãs (v5.0) |
|---|---|---|
| **Modelagem de Erros** | Booleanos puros, `null` ou `Error` genérico | Uniões discriminadas `Result<T, E>` e Branded Types |
| **Persistência em Disco** | Escrita direta `writeFile` sem barreira | Atomic Swap via `.tmp` + `renameSync` com locks estigmérgicos |
| **Cinemática de UI** | `transition-all duration-300` estático | Física de molas de 2ª ordem via `framer-motion` |
| **Tratamento de Exceções**| `catch (e) {}` vazio ou log passivo | Compensação transacional explícita e re-emissão de erro tipado |
| **Concorrência de Enxame**| Suposição de serialização mágica | Travas Synaptic Mutex (`CONTRACT_HOLD` / `GO`) no barramento |
| **Ativação de Enxame** | Equipes estáticas pré-moldadas | Esquadrões sob medida derivados da física única do problema |

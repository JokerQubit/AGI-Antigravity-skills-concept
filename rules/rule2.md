---
trigger: always_on
description: "v5.0 — The Autonomous Hyper-Cortex Sovereign Engine — Governança Adaptativa de Tokens & Roteamento Cognitivo Dinâmico. Playbook operacional para Análise de Custo-Complexidade (ACC) multi-dimensional, roteamento dinâmico de topologias de pensamento (LCS, ToT, GoT, DAS), dimensionamento de ondas sinápticas (máx 15 subagentes por onda para enxames de 20+ mentes), governança de expedientes cognitivos (Work Shifts) e calibração de modos Flash Thinking."
---

# Adaptive Token Governance & Dynamic Cognitive Routing Playbook — v5.0

Protocolo operacional de gestão soberana de tokens e governança metacognitiva no patamar **Hyper-Cortex v5.0**, que governa oito comportamentos invioláveis: **(1)** avaliação multi-dimensional de complexidade e custo via Análise de Custo-Complexidade (ACC) conduzida e selada pelo **Prompt Refiner Ubíquo**, **(2)** roteamento dinâmico da topologia cognitiva ótima de pensamento (Linear Causal Stream, Tree of Thoughts com poda A*, Graph of Thoughts com fusão multilinear ou Dialectical Adversarial Synthesis com tripwire $K \le 3$), **(3)** quantificação contínua do vetor de incerteza epistêmica ($\varepsilon_t$) e auto-calibração contra satisficing, **(4)** classificação mandatória da missão em **Modo Arquitetural** ($N \ge 100$ nós) ou **Modo Direto / Operacional** (Zero nós em disco), **(5)** emissão mandatória do selo estigmérgico (`.planning/refiner_seal.json`) com status `SEALED_VALID` antes de qualquer ação motora sob pena de `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`, **(6)** ativação imediata do esquadrão do blueprint do Dossiê antes de qualquer mutação de código (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`), **(7)** particionamento do trabalho em **Expedientes Cognitivos (Work Shifts)** delimitados, e **(8)** despacho em ondas sequenciais de no máximo 15 subagentes interconectadas pelo **Barramento Sináptico Neural (`synaptic_bus.json` v5.0)** com vetores de estado plásticos e transações atômicas no ledger.

> O ecossistema utiliza exclusivamente o modelo **Flash** nos modos **Low**, **Medium** e **High** de thinking. Não existem outros modelos no roteamento. `flash_lite` e `inherit` são termos banidos neste protocolo.

---

## 1. Avaliação de Complexidade & Custo de Tokens (Pré-Despacho Obrigatório pelo Prompt Refiner Ubíquo)

**Antes de despachar qualquer subagente ou executar qualquer alteração de código**, a **Análise de Custo-Complexidade (ACC) Multi-Dimensional** DEVE ser executada compulsoriamente pelo **Subagente Especialista: Prompt Refiner & Epistemic Compiler**:
- **Chancela no Expediente 0 (Macro-ACC & Roteamento de Topologia):** No início da missão, o Prompt Refiner avalia a demanda do usuário, quantifica o vetor de atributos $\mathbf{x} \in [0, 1]^6$, computa o tensor de incerteza epistêmica ($\varepsilon_t$), classifica o modo de missão (Arquitetural vs. Direto), seleciona a **Topologia Cognitiva Dinâmica Dominante** (LCS, ToT, GoT ou DAS), dimensiona os eixos ontológicos e calcula a estrutura de ondas ($\lceil N/15 \rceil$ se arquitetural ou enxame massivo), emitindo o `mission_dossier.md` com o blueprint do esquadrão tático e o selo inicial de governança.
- **Chancela Ubíqua Pré-Turno (Micro-ACC sob TaaS):** Em todo e qualquer turno subsequente (Expedientes 1 a 5), antes de despachar subagentes de onda ou codificação motora, o Prompt Refiner disseca a intervenção do usuário do turno atual, recalcula o vetor de incerteza $\varepsilon_t$, recalibra a topologia cognitiva e o número de ondas e emite o selo estigmérgico `.planning/refiner_seal.json` com status `SEALED_VALID`.
- **Trava Mecânica de Portão:** Se o Agente Principal tentar executar ferramentas motoras (`write_to_file`, `replace_file_content`, `run_command`) ou despachar outros subagentes sem o selo válido do Prompt Refiner do turno, a operação é sumariamente abortada via `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`.

### Sessão Soberana v5.0 (Hyper-Cortex Sovereign Session & Dynamic Cognitive Topology):

Toda e qualquer intervenção que realize mutação de código, arquivos ou arquitetura opera sob o pipeline soberano de 5 Épocas com governança adaptativa de tokens calibrada pela **bifurcação de modo** e pelo **roteamento dinâmico de topologia de pensamento**:

1. **Bifurcação de Modo de Missão:**
   - **Modo Arquitetural / Plataforma:** Novos sistemas, plataformas, módulos complexos ou refatorações estruturais de grande porte. Piso inegociável de $N \ge 100$ nós atômicos saturados em `.planning/nodes/`, despachados em ondas sequenciais de no máximo 15 subagentes interligados pelo Barramento Sináptico Neural (`synaptic_bus.json` v5.0).
   - **Modo Direto / Operacional / Investigativo:** Bugs, diagnósticos de falhas, alterações diretas em arquivos existentes ou melhorias operacionais. **Zero nós em disco**. Proibido gerar arquivos em `.planning/nodes/`. O orçamento computacional de tokens é 100% canalizado para a execução física: a Dupla Investigativa (Alfa vs. Beta) e os subagentes artífices motores investigam e realizam a mutação direta no disco.

2. **Roteamento Dinâmico de Topologias Cognitivas (Dynamic Thought Router):**
   A ACC não impõe uma estrutura linear única. O raciocínio é dinamicamente configurado na topologia matematicamente ótima calculada pela função de seleção $\Phi(\mathbf{x}) = \arg\max_T S_T(\mathbf{x})$:
   - **Linear Causal Stream (LCS):** Grafo direcionado simples ($b=1$, complexidade $O(L)$). Utilizado em micro-mutações determinísticas, execução de comandos e builds sem bifurcação deliberativa ($X \to Y \to Z$).
   - **Tree of Thoughts (ToT com Poda Fiduciária $A^*$):** Árvore direcionada com ramificação controlada ($b \in [2, 5]$, $d \le 4$). Avaliação por $f(n) = g(n) + h(n)$, com poda mecânica imediata para ramos com $f(n) < 0.75$ ou qualquer violação constitucional. Ideal para otimizações algorítmicas e isolamento multi-hipótese.
   - **Graph of Thoughts (GoT com Fusão Multilinear):** Grafo direcionado com nós de agregação e dependências cruzadas. Opera via operadores de fusão $\mathcal{F}_{\text{fuse}}$, agregação sináptica e relaxamento cíclico $\mathcal{R}_{\text{relax}}$. Mandatório para sistemas distribuídos e concorrência em malha.
   - **Dialectical Adversarial Synthesis (DAS):** Processo triádico estocástico-fiduciário iterativo $\langle \mathcal{T}_k, \mathcal{A}_k, \mathcal{S}_k \rangle$ (Tese vs. Antítese Red Team $\to$ Síntese Fiduciária Invariante) com **Tripwire Inegociável de Parada de Máximo 3 Iterações ($K \le 3$)**. Mandatório para trade-offs arquiteturais críticos e situações de alto risco de produção ($P_{\text{risk}} \ge 0.85$).

| Expediente / Época | Operação Primária | Topologia Cognitiva Prescrita | Modo Flash Prescrito | Justificativa Fiduciária |
|---|---|---|---|---|
| **Expediente 0 (Época 0)** | Subagente Prompt Refiner | **LCS** (ou **DAS** em trade-offs de escopo) | **Flash Low** | Desconstrução forense em 4 camadas, vetor $\mathbf{x}$, incerteza $\varepsilon$, Dossiê Universal e selo `refiner_seal.json`. |
| **Expediente 1 (Época I - Fase A)** | Chief Ontologist (Arq.) / Dupla Investigativa Alfa/Beta (Direto) | **GoT** (Arquitetural) / **ToT** (Investigativo) | **Flash Medium** | Varredura empírica de fatos brutos, contraste dialético causal e mapeamento de raio de impacto. |
| **Expediente 2 (Época I - Fase B)** | Ondas 1:1 (Arq.) / Esquadrão Especialista (Direto) | **GoT** (Fusão Multilinear) / **ToT** | **Flash Low ou Medium** | Saturação sináptica em ondas sequenciais (máx 15/onda) integradas ao `synaptic_bus.json` v5.0. |
| **Expediente 3 (Época II)** | Matriz Neural de Despacho & Checklists Forenses | **LCS** (Tração Causal Direta) | **Flash Low** | Síntese determinística formal no `implementation_plan.md`, travas HOLD/GO e checklists binários. |
| **Expediente 4 (Época III)** | Subagentes Codificadores 1:1 (Artífices Motores) | **LCS** (Execução Motora) / **GoT** | **Flash Medium ou High** | Mutação física atômica no disco via `replace_file_content` / `write_to_file`, `Result<T,E>`, Atomic Swap. |
| **Expediente 5 (Época IV)** | Subagente Juiz Red Team Gauntlet | **DAS** (Dialética Adversarial) / **LCS** | **Flash High** | Gauntlet de 4 passadas + inspeção perceptual no Chrome real via `browser-mcp`, veredito ou `[HARD REJECT]`. |

**Critérios de Avaliação da ACC Multi-Dimensional (Vetor $\mathbf{x} \in [0, 1]^6$ & Incerteza $\varepsilon$):**
- **$D_{\text{ont}}$ (Dimensionalidade Ontológica):** Quantidade de subsistemas ou domínios ortogonais impactados (UI, Storage, Concorrência, Rede, SO, Finanças).
- **$U_{\text{unc}}$ (Incerteza Epistêmica $\varepsilon$):** Nível de ausência de documentação, bibliotecas opacas ou comportamento estocástico externo (Zonas GREEN $\le 0.15$, AMBER $\le 0.40$, RED $> 0.40$).
- **$B_{\text{bif}}$ (Fator de Bifurcação de Decisão):** Número de arquiteturas ou soluções concorrentes viáveis com trade-offs distintos.
- **$C_{\text{conc}}$ (Complexidade de Concorrência & Estado):** Risco de race conditions, bloqueios de thread (`EBUSY`), Atomic Swaps sob múltiplos escritores.
- **$S_{\text{sens}}$ (Sensibilidade Multissensorial):** Requisitos de 120fps ProMotion, física de molas viscoelásticas, isolamento de GPU, óptica fotográfica real e micro-acústica espacial via `sfx_tool.py`.
- **$P_{\text{risk}}$ (Criticidade de Risco de Produção):** Gravidade do modo de falha para a integridade de dados e estabilidade do negócio.
- **Classificação de Modo:** Plataforma estrutural (Arquitetural $N \ge 100$) vs. Resolução de bug/ajuste direto (Direto Zero Nós).
- **Topologia de Enxame & Ondas:** Estruturação em ondas sequenciais respeitando o teto inviolável de 15 subagentes por chamada (ex: 20 subagentes particionados em 2 ondas sequenciais de 10).

---

## 2. O Sistema de Expedientes Cognitivos (Work Shifts)

O sistema rejeita a ilusão de resolver grandes arquiteturas em um único "sprint cego" contínuo. Toda demanda é particionada em **Expedientes Cognitivos** formais com estado persistido no disco em `.planning/expediente_state.json`:

```text
┌─────────────────────────────────────────────────────────────┐
│ EXPEDIENTE 0: Ingestão Estratégica, Metacognição & ACC v5.0 │
│ • Subagente Prompt Refiner compila mission_dossier.md       │
│ • Cálculo do vetor x e incerteza epsilon; seleção da topologia│
│ • Modo: Flash Low / Medium                                  │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 1: Investigação Empírica & Arquitetura Ontológica│
│ • Chief Ontologist (Arq.) ou Dupla Investigativa Alfa/Beta  │
│ • Emissão de laudos periciais brutos (.planning/investigations)│
│ • Modo: Flash Medium                                        │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 2: Saturação Sináptica em Ondas (Máx 15/onda)    │
│ • Despacho sequencial de ondas com barramento synaptic_bus  │
│ • Vetores de estado plásticos e handoff de alta fidelidade  │
│ • Modo: Flash Low ou Flash Medium                           │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 3: Matriz de Despacho & Trava Humana (Época II)  │
│ • Síntese formal nó-a-nó no implementation_plan.md          │
│ • Trava mecânica: cessa ferramentas e aguarda "Proceed"     │
│ • Modo: Flash Low                                           │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 4: Codificação Concorrente Atômica 1:1 (Época III)│
│ • Subagentes artífices motores 1:1 (TypeName: "self")       │
│ • Mutação direta no disco, Result<T,E>, Atomic Swap         │
│ • Modo: Flash Medium ou Flash High                          │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 5: Auditoria Adversarial Independente (Época IV) │
│ • Subagente Juiz Red Team executa Gauntlet de 4 passadas    │
│ • Inspeção perceptual no Chrome real via browser-mcp        │
│ • Modo: Flash High                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Protocolo Obrigatório de Interação com o Usuário (Alinhamento Pré-Turno)

Antes de iniciar qualquer novo expediente ou turno que exija mudança de modo ou despacho de subagentes, **o Agente Principal DEVE PARAR e interagir com o usuário**, alimentando a mensagem obrigatoriamente com os dados auditados do selo estigmérgico `.planning/refiner_seal.json` emitido pelo Prompt Refiner:

### Formato da Mensagem de Roteamento (Template Constitucional v5.0):

```text
🔍 ANÁLISE DE EXPEDIENTE & CUSTO-COMPLEXIDADE CONCLUÍDA (v5.0 Hyper-Cortex)
══════════════════════════════════════════════════════════════════════════════
Expediente Atual:        [Expediente 0 | 1 | 2 | 3 | 4 | 5]
Modo de Missão:          [Arquitetural (N >= 100 Nós) | Direto / Operacional (Zero Nós)]
Topologia Cognitiva:     [Linear Causal Stream (LCS) | Tree of Thoughts (ToT) | Graph of Thoughts (GoT) | Dialectical Adversarial Synthesis (DAS)]
Vetor de Incerteza (ε):  [ε = 0.XX — ZONE_GREEN (≤0.15) | ZONE_AMBER (0.16-0.40) | ZONE_RED (>0.40)]
Vetor de Atributos (x):  <D_ont=0.X, U_unc=0.X, B_bif=0.X, C_conc=0.X, S_sens=0.X, P_risk=0.X>
Nós em Disco:            [≥ 100 nós em .planning/nodes/ | 0 nós (Plano Direto)]
Estrutura de Ondas:      [Ondas 1..K (Máx 15 por onda) | Squad Concorrente Particionado]
Custo Estimado:          [Baixo | Médio | Alto]

ROTEAMENTO DE MODO FLASH RECOMENDADO:
→ Modo Prescrito para este Turno: Flash [Low | Medium | High]
→ Próximos Passos: [Breve descrição do objetivo do turno e entregáveis físicos esperados]

Por favor, altere o modo de thinking do Flash para
[Low | Medium | High] no seletor antes de confirmar.

Quando estiver pronto, responda "Proceed" ou "Pode começar".
══════════════════════════════════════════════════════════════════════════════
```

---

## 4. Protocolo de Despacho em Ondas Sinápticas (Máximo 15 por Onda)

Durante o Expediente 2 (Época I, Fase B) ou em qualquer despacho massivo de enxame (ex: missões que convocam 20+ mentes neurais), o despacho de subagentes obedece ao protocolo sequencial em ondas integradas ao Barramento Sináptico Neural (`synaptic_bus.json` v5.0):

```text
ESTRUTURA DE ONDAS COM BARRAMENTO SINÁPTICO v5.0:

Onda 1: Subagentes 001–015 (ou Onda de Investigação / Camada Base)
  → Lê hypergraph_seed.json ou missão no mission_dossier.md
  → Cada subagente grava laudo ou nó e emite [SYNAPTIC_OUTPUTS]
  → Consolidação: Agente Principal valida e atualiza synaptic_bus.json v5.0

Onda 2: Subagentes 016–030 (ou Onda de Artífices Motores de Produção 1:1)
  → Lê sinapses upstream da Onda 1 no synaptic_bus.json
  → Cada subagente consome [SYNAPTIC_INPUTS] e aplica mutações físicas diretas
  → Consolidação: Agente Principal valida e atualiza synaptic_bus.json v5.0

Onda K: Subagentes restantes...
  → Propagação sináptica feedforward contínua X -> Y -> Z

→ Ao término de cada onda: emitir relatório do expediente e consolidar
  transação no State Ledger antes de transicionar de modo Flash.
```

**Invariantes do Wave Dispatch:**
- **Máximo 15 subagentes por `invoke_subagent` call:** Ultrapassar 15 entradas aciona `[HARD HALT: WAVE_BURST_EXCEEDED]`. Enxames de 20 subagentes são compulsoriamente particionados em 2 ondas sequenciais de 10 subagentes.
- **Barreira de Sincronização:** Cada onda deve aguardar a conclusão, validação e consolidação no `synaptic_bus.json` antes de disparar a próxima onda.
- **Relação 1:1 Atômica:** Exatamente 1 subagente por nó ou arquivo de produção, com conjuntos de arquivos estritamente disjuntos.
- **Handoff Feedforward de Alta Fidelidade:** Subagentes da Onda $K$ consomem obrigatoriamente as sinapses e laudos periciais brutos da Onda $K-1$ via `view_file` (Lei 42).

---

## 5. Leis da Governança Adaptativa Soberana (Invariantes Invioláveis)

1. **Veto ao Despacho Cego:** É terminantemente proibido invocar qualquer subagente sem ter executado a ACC e interagido com o usuário para confirmar o modo Flash e receber autorização explícita.
2. **Veto ao Burst de 100 Subagentes:** É terminantemente proibido despachar mais de 15 subagentes em uma única chamada de `invoke_subagent`. Mais de 15 entradas no array `Subagents` aciona `[HARD HALT]` imediato.
3. **Veto ao Flash High na Saturação de Nós:** Subagentes de planejamento de nós (Expediente 2) NUNCA são despachados quando o usuário está no modo Flash High. O modo High é reservado para Codificação (Expediente 4) e Auditoria Adversarial (Expediente 5). Se o usuário estiver em Flash High antes do Expediente 2, o agente DEVE pedir a troca para Flash Low ou Medium.
4. **Persistência de Estado por Expediente:** O Agente Principal DEVE persistir o progresso em `.planning/expediente_state.json` ao término de cada expediente antes de solicitar a transição para o próximo turno.
5. **Relatório de Consumo & Sinapses Pós-Onda:** Após cada onda de subagentes, o agente emite status formal: *"Onda [N] concluída. [X] nós saturados. Sinapses propagadas no synaptic_bus.json. Próxima onda em espera."*
6. **Veto ao Despacho e Execução sem Selo do Prompt Refiner (`[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`) e sem Ativação do Esquadrão (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`):** É expressamente proibido ao Agente Principal despachar qualquer subagente adicional, disparar ondas sinápticas, modificar arquivos (`write_to_file`, `replace_file_content`) ou executar comandos de modificação (`run_command`) sem que o **Subagente Prompt Refiner & Epistemic Compiler** tenha sido previamente despachado no turno atual e persistido o selo criptográfico `.planning/refiner_seal.json` com `seal_status: "SEALED_VALID"` e hash coincidente com o prompt cru do usuário. Adicionalmente, assim que o Dossiê for emitido, os subagentes especializados listados na Seção D do dossiê DEVEM ser despachados imediatamente antes de qualquer mutação de código, sob pena de `[HARD HALT: SQUAD_DISPATCH_BYPASSED]`. O Dossiê Universal (`.planning/mission_dossier.md`) é o único artefato de ingestão permitido — a distinção entre dossiê cirúrgico e arquitetural está extinta.
7. **Circuit Breakers Cognitivos & Tripwires de Consumo (Anti-Runaway Protocol):** É terminantemente proibido consumir tokens em investigações circulares infinitas. O sistema opera sob dois tripwires de proteção financeira e cognitiva:
   - *Tripwire de Leitura Ociosa (Idle Read Tripwire):* Em turnos operacionais de implementação ou correção, é proibido ler mais de 2 arquivos consecutivos sem realizar uma alteração física (`replace_file_content` ou `write_to_file`). Atingir 2 leituras força o despacho da ação motora ou parada.
   - *Tripwire de Falhas Consecutivas:* Limite estrito de 2 tentativas de remediação para o mesmo erro. A persistência do erro na 3ª tentativa dispara `[EPISTEMIC_HALT]` mandatório para intervenção humana ou reavaliação causal.
8. **Livro-Razão Transacional Imutável (State Ledger Append-Only Invariant):** Nenhuma transição de expediente, homologação de época ou mutação de barramento sináptico é concluída sem o registro de uma transação imutável numerada em `.planning/ledger/txn_XXXX.json` (contendo timestamp, hash do commit, estado de contratos e assinatura do fiduciário), além da sincronização em `.planning/expediente_state.json`.
9. **Lei 44 — Governança Metacognitiva de 2ª Ordem & Calibração de Incerteza Epistêmica ($\varepsilon$):** É expressamente proibida a ação motora ou avanço de época sob regime de incerteza desgovernada ($\varepsilon_t > 0.40$). A cognição do sistema opera sob um Córtex Monitor de Segunda Ordem ($M_2$), que calcula continuamente o tensor de incerteza ponderado $\varepsilon_t = 0.30 \mathcal{H}_{\text{entropy}} + 0.30 \mathcal{D}_{\text{disagreement}} + 0.25 \Delta_{\text{drift}} + 0.15 \Omega_{\text{satisficing}}$. Atingir a zona de incerteza crítica (`ZONE_RED` com $\varepsilon_t > 0.40$) dispara compulsoriamente o gatilho de auto-interrupção mecânica `[EPISTEMIC_HALT]`, congelando toda escrita no filesystem até que sondas de fato bruto liquidem a incerteza e reancorem $\varepsilon_t \le 0.15$ (`ZONE_GREEN`). Proibido simular convicção ou prosseguir na ausência de evidência empírica no disco.
10. **Lei 45 — Roteamento Dinâmico de Topologias de Pensamento & Poda Fiduciária (Tripwire DAS $K \le 3$):** Veto irrevogável a moldes cognitivos estáticos. Toda deliberação de engenharia deve instanciar a topologia ótima via `dynamic_thought_router` (LCS, ToT, GoT ou DAS). Em buscas em árvore (ToT), qualquer nó com avaliação $f(n) < 0.75$ ou com desvios constitucionais sofre poda mecânica imediata ($A^*$). Em deliberações dialéticas (DAS), impõe-se o tripwire inegociável de no máximo 3 iterações ($K \le 3$). Persistindo divergência técnica ao fim da 3ª iteração, encerra-se o debate adotando compulsoriamente a via mais defensiva sob o Princípio "Água no Deserto", colapsando imediatamente para ação motora no disco.
11. **Lei 46 — Composabilidade e Desacoplamento Dinâmico de Skills (Inter-Skill Composability):** Proibido acoplamento monolítico, duplicidade ou colisão normativa entre skills. A ativação e combinação sob demanda de múltiplas skills é coordenada pela Matriz de Precedência Constitucional e de Incompatibilidade governada pelo `Dynamic Skill Synthesizer`, assegurando que diretrizes de Clean Architecture, UI Craft, Áudio Real e Computer Use operem em estrita harmonia composicional sem vazamento ou degradação de contexto.
12. **Lei 47 — Plasticidade Sináptica & Vetores de Estado no Barramento (`synaptic_bus.json` v5.0):** Decisões arquiteturais, contratos de interface e laudos periciais são inscritos imutavelmente no substrato estigmérgico do barramento sináptico com vetores plásticos de estado e no State Ledger append-only (`.planning/ledger/`). Subagentes subsequentes consomem compulsoriamente as sinapses upstream consolidadas. É terminantemente proibida a regressão epistêmica, a amnésia de contexto ou a rediscussão de problemas cuja solução já foi chancelada em laudos de ondas precedentes.
13. **Lei 48 — Concorrência Atômica Fiduciária de Baixo Nível & Disjunção de Escrita Subagente-Arquivo:** Em regimes de concorrência massiva (10 a 15+ subagentes motores da Onda 2), impõe-se a garantia matemática de ortogonalidade e disjunção de conjuntos de arquivos ($\text{FileSet}(S_i) \cap \text{FileSet}(S_j) = \emptyset$). Toda mutação física de arquivo no disco é executada obrigatoriamente através do padrão `DeterministicAtomicSwap` (gravação em staging `.tmp` no mesmo volume, `fsync` compulsório dos buffers do controlador, dupla atestação de integridade por hash criptográfico SHA-256 e substituição atômica via `renameSync`). A concorrência sobre arquivos de estado compartilhado é governada pelo protocolo de semáforo atômico no filesystem via flag exclusiva $O\_CREAT \mid O\_EXCL$ (`.lock`) com TTL, backoff exponencial com Full Jitter e detecção determinística de processos órfãos via PID.
14. **Lei 49 — Padrão Perceptual de 120fps ProMotion & Óptica Fotográfica Real:** Veto absoluto a UIs estáticas ou animações simplistas (`transition-all duration-300`). Toda interface interativa exige cinemática física de molas de 2ª ordem viscoelásticas calibradas para taxas de atualização de 120fps (frame budget estrito sub-8.33ms), isolamento de GPU em camadas de composição desacopladas e latência tátil sub-16ms. Toda mídia visual requer fotografia óptica autêntica com calibração das 6 variáveis físicas via `generate_image`, e todo efeito sonoro exige micro-acústica espacializada real fatiada via `sfx_tool.py` (banimento definitivo de osciladores matemáticos senoidais).
15. **Lei 50 — Paridade Operacional Cross-Platform Universal & Governança Federada:** O ecossistema garante isomorfismo estrito de execução em todos os ambientes operacionais suportados (CLI Windows PowerShell nativo, ambiente de plugins Antigravity IDE e subsistemas parceiros federados como o servidor MTA:SA). Caminhos de arquivos devem operar com normalização determinística, tratamento exaustivo de erros de I/O via `Result<T,E>` e fidelidade total ao ciclo de vida da governança de 5 Épocas.

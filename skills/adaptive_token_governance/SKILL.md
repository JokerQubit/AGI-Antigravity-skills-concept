---
name: adaptive_token_governance
description: "v4.1 — Universal Cognitive Parity & Mission Mode Bifurcation — Governança Adaptativa de Tokens & Roteamento Inteligente de Modelos. Playbook operacional para Análise de Custo-Complexidade (ACC), bifurcação de missões (Arquitetural N >= 100 vs Direta Zero Nós), dimensionamento de eixos/ondas (máx 15 subagentes), governança de expedientes cognitivos (Work Shifts) e escalonamento de modos Flash Thinking."
---

# Adaptive Token Governance & Model Routing Playbook — v4.1

Protocolo operacional de gestão soberana de tokens que governa seis comportamentos invioláveis: **(1)** chancela e avaliação de complexidade e custo de tokens via Análise de Custo-Complexidade (ACC) conduzida e selada pelo **Prompt Refiner Ubíquo**, **(2)** classificação mandatória da missão em **Modo Arquitetural** ($N \ge 100$ nós) ou **Modo Direto / Operacional** (Zero nós em disco), **(3)** emissão mandatória do selo estigmérgico (`.planning/refiner_seal.json`) antes de qualquer ação motora ou despacho sob pena de `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`, **(4)** ativação imediata do esquadrão do blueprint do Dossiê antes de qualquer mutação de código (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`), **(5)** particionamento do trabalho em **Expedientes Cognitivos (Work Shifts)** delimitados, e **(6)** despacho em ondas sequenciais de no máximo 15 subagentes interconectadas pelo **Barramento Sináptico Neural (`synaptic_bus.json`)**.

> O ecossistema utiliza exclusivamente o modelo **Flash** nos modos **Low**, **Medium** e **High** de thinking. Não existem outros modelos no roteamento. `flash_lite` e `inherit` são termos banidos neste protocolo.

---

## 1. Avaliação de Complexidade & Custo de Tokens (Pré-Despacho Obrigatório pelo Prompt Refiner Ubíquo)

**Antes de despachar qualquer subagente ou executar qualquer alteração de código**, a **Análise de Custo-Complexidade (ACC)** DEVE ser executada compulsoriamente pelo **Subagente Especialista: Prompt Refiner & Epistemic Compiler**:
- **Chancela no Expediente 0 (Macro-ACC):** No início da missão, o Prompt Refiner avalia a demanda do usuário, classifica o modo de missão (Arquitetural vs. Direto), dimensiona os eixos ontológicos (domínios cruzados, concorrência, criticidade de mídia real), calcula o número de ondas ($\lceil N/15 \rceil$ se arquitetural) e emite o `mission_dossier.md` com o blueprint do esquadrão tático e o selo inicial de governança.
- **Chancela Ubíqua Pré-Turno (Micro-ACC sob TaaS):** Em todo e qualquer turno subsequente (Expedientes 1 a 5), antes de despachar subagentes de onda ou codificação, o Prompt Refiner disseca a intervenção do usuário do turno atual, recalcula o impacto de segunda ordem, recalibra o número de ondas e emite o selo criptográfico/estigmérgico `.planning/refiner_seal.json` com status `SEALED_VALID`.
- **Trava Mecânica de Portão:** Se o Agente Principal tentar executar ferramentas motoras (`write_to_file`, `replace_file_content`, `run_command`) ou despachar outros subagentes sem o selo válido do Prompt Refiner do turno, a operação é sumariamente abortada via `[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`.

### Sessão Soberana v4.1 (Universal Parity & Mission Mode Bifurcation):

Toda e qualquer intervenção que realize mutação de código, arquivos ou arquitetura opera sob o pipeline soberano de 5 Épocas com governança de tokens calibrada pela bifurcação de modo:

1. **Modo Arquitetural / Plataforma:** Novos sistemas, plataformas, módulos complexos ou refatorações estruturais de grande porte. Piso inegociável de $N \ge 100$ nós atômicos saturados em `.planning/nodes/`, despachados em ondas de no máximo 15 subagentes interligados pelo Barramento Sináptico Neural.
2. **Modo Direto / Operacional / Investigativo:** Bugs, investigações de falhas, alterações diretas em arquivos existentes ou melhorias operacionais. **Zero nós em disco**. Proibido gerar arquivos em `.planning/nodes/`. O orçamento de tokens é 100% preservado para a execução real: a Dupla Investigativa e os subagentes especialistas do esquadrão investigam a fundo e codificam os arquivos diretamente.

A Análise de Custo-Complexidade (ACC) classifica compulsoriamente a missão em um desses dois modos, dimensiona os **eixos ontológicos**, o **número de ondas** ($\lceil N/15 \rceil$ no modo arquitetural) e a **intensidade computacional** (Flash Thinking por expediente — tabela abaixo).

| Expediente / Época | Operação | Modo Prescrito | Justificativa |
|---|---|---|---|
| **Expediente 0 (Época 0)** | Subagente Prompt Refiner | **Flash Low** | Desconstrução forense, classificação de modo e compilação do Dossiê Universal. |
| **Expediente 1 (Época I - Fase A)** | Chief Ontologist (Arq.) / Dupla Investigativa (Direto) | **Flash Medium** | Varredura empírica / Investigação causal contrastiva (Alfa vs. Beta). |
| **Expediente 2 (Época I - Fase B)** | Ondas 1:1 (Arq.) / Esquadrão Direto (Direto) | **Flash Low ou Medium** | Saturação sináptica de nós (Arq.) ou execução especializada do squad (Direto). |
| **Expediente 3 (Época II)** | Matriz Neural de Despacho & Checklists | **Flash Low** | Síntese formal nó-a-nó/arquivo-a-arquivo e checklists binários extensivos. |
| **Expediente 4 (Época III)** | Subagentes Codificadores 1:1 | **Flash Medium ou High** | Produção de código real, contratos estritos, validação de checklists. |
| **Expediente 5 (Época IV)** | Subagente Juiz Red Team | **Flash High** | Gauntlet de 4 passadas + auditoria no Chrome real. |

**Critérios de Avaliação da ACC (Dissecados pelo Prompt Refiner):**
- Quantos domínios independentes a tarefa atravessa? (UI, storage, concorrência, áudio, rede, segurança, financeiro)
- A demanda é uma nova plataforma estrutural (Arquitetural) ou resolução de bug/ajuste direto (Direto)?
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
│ • Execução da ACC e dimensionamento de eixos ontológicos / Ondas│
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
│ • Modo: Flash Low ou Flash Medium                           │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 3: Matriz de Despacho & Trava Humana (Época II)  │
│ • Síntese formal nó-a-nó no implementation_plan.md          │
│ • Trava mecânica: cessa ferramentas e aguarda "Proceed"     │
│ • Modo: Flash Low                                           │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 4: Codificação Concorrente Atômica 1:1 (Época III)│
│ • Subagentes codificadores 1:1 + Integração Defensiva       │
│ • Testes, build, eliminação definitiva de stubs             │
│ • Modo: Flash Medium ou Flash High                          │
├─────────────────────────────────────────────────────────────┤
│ EXPEDIENTE 5: Auditoria Adversarial Independente (Época IV) │
│ • Subagente Juiz executa as 4 passadas do Gauntlet          │
│ • Inspeção perceptual no Chrome real via browser-mcp        │
│ • Modo: Flash High                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Protocolo Obrigatório de Interação com o Usuário (Alinhamento Pré-Turno)

Antes de iniciar qualquer novo expediente ou turno que exija mudança de modo ou despacho de subagentes, **o Agente Principal DEVE PARAR e interagir com o usuário**, alimentando a mensagem obrigatoriamente com os dados auditados do selo estigmérgico `.planning/refiner_seal.json` emitido pelo Prompt Refiner:

### Formato da Mensagem de Roteamento (Template Constitucional):

```text
🔍 ANÁLISE DE EXPEDIENTE & CUSTO-COMPLEXIDADE CONCLUÍDA
══════════════════════════════════════════════════════════
Expediente Atual: [Expediente 0 | 1 | 2 | 3 | 4 | 5]
Modo de Missão:   [Arquitetural (N >= 100 Nós) | Direto / Operacional (Zero Nós)]
Nós em Disco:     [≥ 100 nós em .planning/nodes/ | 0 nós (Plano Direto)]
Ondas de Despacho:[Ondas 1..K | Despacho Concorrente de Squad]
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

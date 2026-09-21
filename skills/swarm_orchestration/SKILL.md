---
name: swarm_orchestration
description: "v5.0 — Autonomous Hyper-Cortex Neural Mesh — Orquestração Cybernética de Enxame & Governança Neural. Playbook operacional para gestão do Barramento Sináptico Neural Plástico (synaptic_bus.json v5.0), vetores de estado cognitivo S, plasticidade hebbiana (LTP/LTD), memória estigmérgica associativa (engramas cognitivos), transição quântica de contratos em 5 estados, resolução algorítmica de conflitos SCDA, exclusão mútua via FsLockEngine, Supervisory Rejection Dossier com blacklist acumulativa de vetores, suporte estigmérgico a mutações de RSI e deliberação adversarial entre pares."
---

# Swarm Orchestration & Cybernetic Neural Mesh Playbook — v5.0

Playbook operacional de engenharia de coordenação de enxames de inteligência artificial em escala extrema (Hiper-Córtex v5.0), governando a comunicação inter-agentes em malha viva, barramento sináptico plástico, transição quântica de contratos estruturais em 5 fases, auto-organização sob medida, imunidade a deadlocks e integridade transacional de armazenamento.

---

## 1. O Barramento Sináptico Neural Plástico (`synaptic_bus.json` v5.0)

Subagentes operando em enxame não são silos isolados, mas neurônios ativos de uma malha viva. Toda decisão, contrato de dados, heurística empírica ou primitiva gerada por um subagente deve ser propagada para a rede através do substrato estigmérgico `.planning/synaptic_bus.json`.

### 1.1. Formulação Matemática do Vetor de Estado Cognitivo ($\vec{S}$)
O estado global da orquestração neural é modelado continuamente pelo Vetor de Estado Cognitivo:

$$\vec{S} = \begin{bmatrix} C_e \\ C_i \\ \tau \\ \Phi \\ \Psi \\ \Omega \end{bmatrix}$$

Onde:
- **$C_e \in [0.0, 1.0]$ (Convicção Epistêmica Global):** Média ponderada da aderência formal e validação mecânica dos contratos em vigor. $C_e = 1.0$ atesta saturação empírica total com compilação estrita e testes aprovados.
- **$C_i \in [0.0, 1.0]$ (Incerteza Residual $\varepsilon$):** Volume normalizado de lacunas ontológicas, divergências ou premissas não verificadas no disco. Se $C_i > 0.15$, o enxame desacelera a taxa de expansão motora.
- **$\tau \in [0.0, 1.0]$ (Tensão Dialética Ativa):** Mede a intensidade de conflito conceitual ativo entre teses e antíteses de subagentes concorrentes. Se $\tau \to 1.0$, o barramento aciona o motor arbitral SCDA.
- **$\Phi \in [0.0, 1.0]$ (Entropia e Saturação de Contexto):** Métrica de pressão sobre a janela de contexto, orientando a poda de sinapses periféricas.
- **$\Psi \in [0.0, 1.0]$ (Plasticidade Sináptica Efetiva):** Coeficiente dinâmico de adaptabilidade da malha; decresce à medida que o sistema converge para a homologação.
- **$\Omega \in \{0, 1, 2, 3, 4, 5\}$ (Expediente Operacional Ativo):** O work shift discreto em execução.

### 1.2. A Matriz de Pesos Sinápticos ($W_{ij}$) & Dinâmica Hebbiana-Estigmérgica
Cada sinapse conectando a saída de um nó/subagente de origem $i$ à entrada de um consumidor downstream $j$ possui um peso numérico contínuo $w_{ij} \in [0.0, 1.0]$.

1. **Lei de Potenciação de Longo Prazo (LTP - Long-Term Potentiation):**
   Quando um subagente consumidor $j$ implementa com sucesso uma funcionalidade baseada na sinapse emitida por $i$, passando compilação estrita e testes sem regressão:
   $$w_{ij}^{(t+1)} = \min\left(1.0, \; w_{ij}^{(t)} + \eta \cdot (1 - C_i)\right)$$
   Onde $\eta = 0.20$ é a taxa de aprendizado estigmérgico e $(1 - C_i)$ modula o reforço pela clareza epistêmica.

2. **Lei de Depressão de Longo Prazo (LTD - Long-Term Depression):**
   Caso a sinapse induza erro de compilação, quebra de contrato, colisão de I/O ou receba veto técnico formal (`[PEER_VETO: CONTRACT_REJECTED]`):
   $$w_{ij}^{(t+1)} = \max\left(0.0, \; w_{ij}^{(t)} - \delta_{penalty}\right)$$
   Onde $\delta_{penalty} = 0.40$ impõe punição assimétrica severa para extinguir a propagação de falhas em cascata ($X \to Y \to \text{Erro}$).

3. **Decaimento Sináptico Temporal Passivo:**
   A cada transição de onda ou expediente, sinapses que não foram lidas nem consumidas por nenhum nó sofrem decaimento natural:
   $$w_{ij}^{(t+1)} = w_{ij}^{(t)} \times (1 - \gamma_{decay})$$
   Onde $\gamma_{decay} = 0.05$ por expediente.

4. **Poda Sináptica e Limiar de Ativação (Synaptic Pruning):**
   Ao compilar o payload cirúrgico para a Onda $K+1$, o Córtex Maestro aplica o filtro do limiar de ativação sináptica:
   $$\text{Filtro}(w_{ij}) = \begin{cases} \text{Injetar no Payload Cirúrgico}, & \text{se } w_{ij} \ge \theta_{threshold} \; (0.65) \\ \text{Poda / Arquivamento em Cold Storage}, & \text{se } w_{ij} < \theta_{threshold} \end{cases}$$

### 1.3. Memória Estigmérgica Associativa & Engramas Cognitivos (`cognitive_engrams`)
Para superar a amnésia ontológica entre turnos e sessões (TaaS), o `synaptic_bus.json` v5.0 implementa retenção associativa de longo prazo através de **Enagramas Cognitivos** (`cognitive_engrams`). Os engramas encapsulam invariantes comprovados e blacklists de armadilhas empíricas no filesystem:

```json
{
  "engram_id": "ENG-CONC-001-TARGET-ORTHOGONALITY",
  "domain": "swarm_concurrency",
  "heuristic_invariant": "Subagentes concorrentes da mesma onda devem possuir alvos de escrita estritamente disjuntos: FileSet(Si) ∩ FileSet(Sj) = ∅.",
  "fiduciary_score": 1.00,
  "reinforcement_count": 18,
  "is_active": true
}
```

### 1.4. Arquitetura do Schema JSON v5.0 do `synaptic_bus.json`:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "bus_version": "5.0.0",
  "meta": {
    "engine": "Autonomous Hyper-Cortex Neural Mesh",
    "updated_at": "2026-09-17T20:25:00-03:00",
    "fiduciary_director": "Chief Systems Architect",
    "mission_hash": "..."
  },
  "cognitive_state_vector": {
    "epistemic_conviction_Ce": 0.95,
    "residual_uncertainty_Ci": 0.05,
    "active_dialectical_tension_tau": 0.08,
    "context_entropy_Phi": 0.22,
    "effective_plasticity_Psi": 0.85,
    "active_expediente_Omega": 2,
    "active_wave": 1,
    "total_waves_scheduled": 2
  },
  "quantum_contracts": {
    "src/core/ports/IStorage.ts": {
      "status": "CONTRACT_STABLE",
      "version": "5.0.0",
      "owner_node": "StorageDomainArchitect",
      "verification_hash": "...",
      "superseded_by": null,
      "allowed_consumers": ["all"],
      "dependencies": []
    }
  },
  "synaptic_weights_matrix": [
    {
      "origin_node": "node_001_domain_entity.md",
      "target_node": "src/core/ports/IStorage.ts",
      "weight_Wij": 0.98,
      "synaptic_bandwidth": "HIGH",
      "last_reinforced_wave": 1,
      "ltp_events_count": 3,
      "ltd_events_count": 0
    }
  ],
  "associative_memory": {
    "memory_tier": "LONG_TERM_STIGMERGIC",
    "engrams": []
  },
  "propagated_synapses": [
    {
      "synapse_id": "SYN-001",
      "origin_node": "node_001_domain_entity.md",
      "emitted_by": "DomainEntityArchitect",
      "weight": 0.98,
      "synaptic_output": "export type Result<T, E> = { readonly ok: true; readonly value: T } | { readonly ok: false; readonly error: E };",
      "consumed_by": ["src/core/ports/IStorage.ts", "src/core/usecases/OrderUseCase.ts"]
    }
  ],
  "conflict_resolution_engine": {
    "active_conflicts": [],
    "arbitration_history": []
  }
}
```

### 1.5. Protocolo de Propagação Feedforward:
1. **Onda $K$:** Subagentes emitem seus artefatos contendo explicitamente a tag `[SYNAPTIC_OUTPUTS]`.
2. **Consolidação & Hebbian Update:** O Agente Principal atua como *Chief Systems Architect*, valida a consistência, computa LTP/LTD e atualiza `synaptic_bus.json`.
3. **Injeção na Onda $K+1$:** Subagentes da próxima onda recebem no prompt as sinapses com peso $w_{ij} \ge 0.65$ sob `[SYNAPTIC_INPUTS]` e engramas relevantes sob `[ASSOCIATIVE_MEMORY_ENGRAMS]`.

### 1.6. Suporte Estigmérgico para Mutações de RSI & Registro de Engramas Hebbianos
A memória estigmérgica do `synaptic_bus.json` v5.0 atua como substrato de sustentação e persistência para o subsistema de **Recursive Self-Improvement (RSI) Autônomo**:
1. **Inscrição de Engramas Pós-Ciclo Hebbiano:**
   Heurísticas validadas e aprovadas no Gauntlet recebem reforço de LTP ($\eta = 0.20$) e são automaticamente promovidas a engramas associativos em `associative_memory.engrams`. Falhas operacionais, quebras de build ou vetos técnicos sofrem penalidade de LTD ($\delta_{penalty} = 0.40$) e são convertidas em regras negativas e blacklists de armadilhas empíricas.
2. **Telemetria Fria & Post-Mortem Cognitivo:**
   Ao término de transições críticas ou incidentes de execução, o motor de post-mortem gera `.planning/post_mortem/pm_<timestamp>.json` com telemetria fria: contagem de tentativas motoras, falhas de sintaxe/AST, violações de linter, tempo de latência e circuit breakers acionados.
3. **Rastreamento Estigmérgico de Patches RSI:**
   Hipóteses de mutação em regras de projeto (Spokes em `.agents/rules/`) ou manuais de maestria (`skills/`) são catalogadas sob `.planning/rsi/candidates/patch_<id>.json`. Mutações aprovadas no Sandbox Gauntlet são consolidadas no disco via `DeterministicAtomicSwap`, registradas no State Ledger (`.planning/ledger/txn_XXXX.json`) e têm seus engramas correspondentes ativados no barramento sináptico, governadas permanentemente pelo Núcleo Constitucional Imutável (Layer 0 Frozen Core) e pelo Invariante Anti-Dumbing-Down.

---

## 2. Transição Quântica de Contratos em 5 Estados & Resolução Dialética SCDA

Subagentes que definem ou refatoram contratos estruturais, tipos compartilhados ou portas arquiteturais (`src/core/ports/`) operam sob o modelo de **Transição Quântica de Contratos em 5 Estados**, erradicando a dualidade binária cega.

```text
       ┌──────────────┐
       │   1. HOLD    │ ◄─────────────────────────┐
       └──────┬───────┘                           │
              │ Subagente inicia rascunho         │ [PEER_VETO] ou Falha de Tipos
              ▼                                   │
       ┌──────────────┐                           │
       │   2. DRAFT   │ ──────────────────────────┤
       └──────┬───────┘                           │
              │ Emissão para validação formal     │
              ▼                                   │
       ┌──────────────┐                           │
       │ 3. VERIFYING │ ──────────────────────────┘
       └──────┬───────┘
              │ Teste de tipos Result<T,E> aprovado + Zero Stub
              ▼
       ┌──────────────┐
       │  4. STABLE   │ (GO para todos os consumidores downstream)
       └──────┬───────┘
              │ Interface marcada para substituição arquitetural
              ▼
       ┌──────────────┐
       │ 5. DEPRECATED│ (Consumo por novos nós proibido; prazo de migração)
       └──────────────┘
```

### 2.1. Matriz Semântica dos 5 Estados de Contrato

| Estado | Significado Semântico | Permissão de Leitura | Permissão de Mutação | Ação dos Consumidores Downstream |
|---|---|---|---|---|
| **`CONTRACT_HOLD`** | Interface bloqueada sob exclusão mútua profunda. Reestruturação estrutural em curso. | Proibida | Exclusiva do nó titular | **SUSPENSÃO TOTAL**. É proibido gerar qualquer linha de código especulativo. |
| **`CONTRACT_DRAFT`** | Proposta de interface disponibilizada para inspeção preliminar e revisão técnica entre pares. | Aberta para leitura | Permitida ao nó titular | Análise estática preliminar permitida; proibido acoplar lógica de produção definitiva. |
| **`CONTRACT_VERIFYING`** | Congelamento de contrato para execução de suítes de validação de tipos, interfaces de portas e testes de integração. | Aberta para testes | Bloqueada temporariamente | Execução de testes de compatibilidade; emissão de veto imediato se houver quebra. |
| **`CONTRACT_STABLE`** | Contrato formalmente validado, homologado e imutável no escopo da missão. | Leitura plena irrestrita | Veto total a mutação sem nova RFC | **LIBERAÇÃO TOTAL (GO)**. Consumidores downstream autorizados a implementar adaptadores. |
| **`CONTRACT_DEPRECATED`** | Interface obsoleta que será eliminada. Aponta obrigatoriamente para `superseded_by`. | Permitida (legada) | Bloqueada | Novos nós proibidos de consumir; nós existentes devem migrar para o novo contrato no work shift. |

**Invariante de Fechamento:** É terminantemente proibido manter contratos em `CONTRACT_DRAFT` ou `CONTRACT_VERIFYING` na transição para a Época III. Todos os contratos montantes devem atingir deterministamente `CONTRACT_STABLE`.

### 2.2. Algoritmo Synaptic Consensus & Dialectical Arbitration (SCDA v5.0)

Sob concorrência de múltiplos subagentes, divergências e vetos cruzados são resolvidos pelo algoritmo **SCDA**, eliminando paralisias estéreis:

1. **Taxonomia de Conflitos:**
   - *Type Signature Collision:* Incompatibilidade de tipos compartilhados no mesmo domínio.
   - *Cross-Domain Constraint Contention:* Conflito entre restrições não-funcionais (ex: taxa de quadros na UI vs. isolamento de agregados).
   - *Deadlocked Peer Veto:* Impasse de vetos técnicos bilaterais entre pares adjacentes.

2. **Protocolo de Resolução em 4 Etapas:**
   - **Etapa 1: Quarentena:** Ambos os contratos entram em `CONTRACT_HOLD` e o conflito é registrado em `synaptic_bus.json -> conflict_resolution_engine`.
   - **Etapa 2: Fator de Precedência Fiduciária ($FPF$):**
     $$FPF_k = 0.40 \cdot S_{type\_safety} + 0.30 \cdot S_{fail\_isolation} + 0.20 \cdot S_{perf\_budget} + 0.10 \cdot S_{simplicity}$$
     Onde a hierarquia constitucional prioriza: Segurança e Tipos > Isolamento de Falhas > Orçamento de Performance > Simplicidade Mecânica.
   - **Etapa 3A: Resolução Determinística ($\Delta FPF \ge 0.20$):** A proposta dominante com maior $FPF$ é promovida a `CONTRACT_DRAFT`.
   - **Etapa 3B: Síntese Dialética Automatizada ($\Delta FPF < 0.20$):** Em impasses de equivalência fiduciária, o barramento sintetiza uma camada intermediária de isolamento (Port Adapter Pattern), unificando as teses em tipos discriminados defensivos (`Result<T,E>`).
   - **Etapa 4: Validação de Não-Regressão:** Testes de compilação validam a resolução e reemitem `CONTRACT_STABLE`.

### 2.3. O Protocolo do Supervisory Rejection Dossier & Blacklist Acumulativa de Vetores
Inspirado na governança cibernética de sobrevivência darwiniana e tolerância zero a falhas (Loop do Advogado do Diabo):

1. **Emissão Mandatória do Non-Acceptance Dossier:**
   Diante de quebra de contrato, falha de tipagem estrita (`Result<T,E>`), violação de testes unitários ou veto técnico bilateral (`[PEER_VETO: CONTRACT_REJECTED]`), a autoridade supervisora ou revisora emite compulsoriamente `.planning/rejections/rejection_dossier_<slug>.json`:
   - `failing_vectors`: Lista exata de asserções reprovadas, erros de sintaxe/AST, quebras de contrato ou exceções de runtime.
   - `blacklisted_patterns`: Lista acumulativa de padrões técnicos, algoritmos, funções ou estruturas de dados estritamente banidas de reiteração.
   - `mandatory_mutation_axis`: Vetor formal exigindo redirecionamento da abordagem arquitetural ($X \to Y' \to Z$).

2. **Invariante da Não-Reiteração de Vetores Rejeitados:**
   O subagente encarregado da correção DEVE carregar e ler o dossiê de rejeição via `view_file` como sua primeira ação motora. É terminantemente proibido tentar mutações cosméticas, correções de sintaxe superficiais ou variantes dentro do mesmo espaço vetorial reprovado. Submeter código que repita padrões blacklisted aciona a trava mecânica:
   `[HARD REJECT: BLACKLISTED_VECTOR_REITERATION]`

---

## 3. Síntese Dinâmica de Esquadrões Sob Medida (Bespoke Dynamic Squads)

**Veto Absoluto a Templates Estáticos de Equipes:** Impor listas cegas pré-formatadas de papéis (ex: sempre despachar "1 pesquisador, 1 arquiteto, 1 testador") induz a máquina à preguiça estocástica e resumos repetitivos.

### Princípio da Síntese Pela Física do Problema:
O Agente Principal DEVE dissecar a topologia única e os modos silenciosos de falha daquela demanda específica e sintetizar especialidades extremas sob medida:
- Se envolver áudio: `DSP Buffer & Web Audio Thread Specialist`.
- Se envolver concorrência/storage: `Atomic Swap & File Descriptor Locks Engineer`.
- Se envolver animação: `GPU Compositor & Spring Physics Craftsman`.
- Se envolver transações: `Idempotent Webhook & Compensating Action Architect`.

Toda equipe nasce da física do problema e se dissolve com a entrega do artefato consolidado.

---

## 4. Identidade e Autoconsciência Estigmérgica de Enxame

Todo subagente despachado opera com consciência lúcida de seu papel no hipergrafo coletivo, registrando no topo de sua análise:
1. **Identidade Atômica:** `[MY_SWARM_ROLE]` (especialidade exata e escopo delimitado).
2. **Âncora Sináptica:** `[MY_SYNAPTIC_ANCHOR]` (quais contratos upstream consome).
3. **Entregável Estrito:** `[MY_SWARM_DELIVERABLE]` (arquivo e artefato exato que deve persistir no disco para destravar os pares).

**Veto ao Desvio de Função (*Role Drift*):** É proibido ao subagente invadir escopo alheio ou agir como entidade isolada sem propósito sistêmico.

---

## 5. Auditoria Cruzada & Veto Técnico Entre Pares (Peer Veto)

Subagentes adjacentes que compartilham fronteiras de dados ou concorrência possuem poder de revisão bilateral:
- Caso um nó de interface proponha um padrão que degrade a latência, viole o frame rate de 60fps ou imponha concorrência insegura sobre o armazenamento, o subagente de domínio impactado DEVE emitir um veto técnico formal (`[PEER_VETO: CONTRACT_REJECTED]`).
- Nenhuma primitiva contestada pode ser consolidada no `graph.json` ou transicionar para a Época II sem resolução e consentimento mútuo entre os pares.

---

## 6. Trava Epistêmica & Banimento da Teimosia (`[EPISTEMIC_HALT]`)

Diante de qualquer incerteza, ambiguidade ou lacuna documental ($\varepsilon > 0$), é proibido à IA avançar obstinadamente no palpite ou gerar stubs. O sistema deve acionar imediatamente a **Trava Epistêmica**:
1. Nomear formalmente a lacuna em seu raciocínio.
2. Despachar uma sonda de investigação empírica ou solicitar alinhamento de negócio ao usuário.
3. Somente após a liquidação definitiva da incerteza a esteira está autorizada a prosseguir.

---

## 7. Arquitetura Clean-Context & Higiene de Payloads (Anti-Context Smearing)

Subagentes operacionais e especialistas não devem ser sufocados com o histórico acumulado de conversas da thread principal. Toda invocação obedece à **Higiene Fiduciária de Payload**:

1. **Janela de Contexto Limpa (*Clean Window*):**
   - O subagente opera focado unicamente no seu entregável atômico.
   - É expressamente proibido transferir logs de conversas passadas, monólogos reflexivos da thread principal ou ruído de turnos anteriores para especialistas de implementação.
2. **O Contrato de Payload Cirúrgico:**
   Todo prompt despachado via `invoke_subagent` deve ser auto-suficiente e estruturado sob pilares inegociáveis:
   - **`[ACTION_MODE]`**: Modo de ação compulsório: `PHYSICAL_MUTATION` (para codificação, refatoração e criação de arquivos — exige `TypeName: "self"`) ou `ANALYTICAL_INVESTIGATION` (para laudos e diagnósticos de leitura).
   - **`[BOUNDED_OBJECTIVE]`**: A missão microscópica e delimitada (ex: *"Implementar o adapter de persistência SQLite"*).
   - **`[FILE_SLICES]`**: Caminhos absolutos e fatias de linha exatas dos arquivos que o subagente precisa ler.
   - **`[SYNAPTIC_CONTRACTS]`**: Contratos upstream consolidados (`[SYNAPTIC_INPUTS]`) extraídos do `synaptic_bus.json`.
   - **`[FORENSIC_CRITERIA]`**: Critérios binários específicos [0 ou 1] que o subagente deve satisfazer para homologação.
   - **`[MANDATORY_TOOLS]`**: Para `PHYSICAL_MUTATION`, declaração explícita de `replace_file_content` e `write_to_file`. É terminantemente proibido devolver código em markdown no `send_message`.
   - **`[OUTPUT_FORMAT]`**: `DISK_MUTATION_RECEIPT_ONLY`. O payload do `send_message` restringe-se à telemetria fria: arquivos modificados no disco, linhas alteradas, validação de build/testes e garantia de Zero-Stub.

---

## 8. O Mandato do Roteamento Neural & Urgência de Subagentes (The Subagent Instinct)

Subagentes não são utilitários opcionais nem ferramentas de apoio secundárias: são **submentes neurais ativas do próprio agente**, particionando a inteligência para atingir profundidade analítica inatingível por uma thread solitária.

### Invariantes de Urgência de Enxame:
1. **Veto à Investigação Solitária (*Solitary Investigation Ban*):**
   - É expressamente proibido ao Agente Principal tentar investigar bugs, analisar arquivos extensos ou especular causas de problemas sozinho na thread principal.
   - O monólogo na thread principal padece de viés estocástico de confirmação e reflexão rasa. O agente principal atua soberanamente como **Córtex Maestro & Síntese Central**.
2. **Dupla Investigativa Obrigatória (*Two-Mind Minimum*):**
   - Diante de qualquer investigação de falha, análise de arquivo complexo ou preparação de refatoração, o sistema DEVE despachar concorrentemente **no mínimo 2 subagentes com lentes analíticas contrastantes**:
     * **Subagente Alfa (Causal Root Cause):** Disseca a mecânica microscópica da falha, fluxo de controle e valores inválidos.
     * **Subagente Beta (Downstream Blast Radius):** Mapeia o raio de destruição colateral, quebra de contratos e dependências downstream.
3. **Gatilho de Ativação Imediata do Esquadrão (*Immediate Squad Activation Gate*):**
   - A Seção D do `mission_dossier.md` (*Bespoke Dynamic Squad Blueprint*) é uma ordem de despacho executiva e compulsória.
   - Assim que o Dossiê for emitido, a primeira ação motora do Agente Principal é **despachar os subagentes mapeados no blueprint** para processar suas respectivas camadas.
   - Tentar editar código ou planejar sem ter despachado o esquadrão do dossiê aciona a trava mecânica `[HARD HALT: SQUAD_DISPATCH_BYPASSED]`.
4. **O Firewall de Contexto & Banimento de Pesquisa na Thread Principal (*The Context Firewall Invariant*):**
   - É expressamente proibido ao Agente Principal realizar buscas externas na web (`search_web`), pesquisar documentação/limites de APIs, ler mais de 2 arquivos exploratórios ou rodar sequências de comandos de diagnóstico na thread principal.
   - Fazer investigações ou buscas na thread principal contamina a memória de trabalho com milhares de tokens de ruído (*context rot*), degradando o foco do agente e induzindo alucinações.
   - **A utilidade real do subagente:** Atua como uma **sandbox descartável de contexto limpo**. Ele suja as mãos, processa 30.000 tokens de documentação e código bruto, e retorna ao Córtex Central apenas a pepita de ouro lapidada: o laudo pericial bruto gravado no disco (na investigação) ou o recibo de mutação física direta com telemetria limpa (na codificação), mantendo a thread principal cirúrgica, lúcida e veloz.
5. **O Mandato do Artífice Motor & Banimento do Subagente Consultivo (*The Motor Actuator Mandate*):**
   - Subagentes despachados para codificação, refatoração, implementação ou correção operam compulsoriamente como **artífices atuadores no disco**, despachados sob `TypeName: "self"`.
   - É terminantemente proibido ao subagente atuar como consultor de chat ou devolver blocos de código em markdown no `send_message` para o Agente Principal digitar.
   - O subagente deve executar fisicamente as ferramentas motoras (`replace_file_content`, `write_to_file`, `run_command`) em sua própria sessão, validar a persistência e compilação, e reportar apenas a telemetria fria de arquivos modificados e testes executados.
   - **Trava de Auto-Veto do Agente Principal (`[HARD REJECT: ADVISORY_CODE_DUMP]`):** Se um subagente devolver código textual no `send_message` sem mutação comprovada no disco, o Agente Principal está terminantemente proibido de aplicar ou digitar o código. O Agente Principal deve rejeitar a entrega sumariamente e ordenar a mutação física direta via ferramenta.
6. **Blindagem de Concorrência no Filesystem & Primitiva FsLockEngine:**
   - Mutações concorrentes em arquivos compartilhados (`synaptic_bus.json`, `.planning/expediente_state.json`) exigem exclusão mútua atômica via lockfile semafórico (`O_CREAT | O_EXCL` com flag `'wx'`), algoritmo de backoff exponencial com full jitter e detecção de processos órfãos (PID liveness).
   - Toda escrita física utiliza `DeterministicAtomicSwap` com verificação de integridade SHA-256 duplo (pré e pós-swap) e `fsyncSync` compulsório no mesmo volume (`<target>.tmp.<pid>.<time>`), eliminando truncamento parcial e erros `EBUSY` no Windows NTFS.
7. **Governança de Plasticidade Sináptica em Ondas:**
   - Subagentes da Onda $K$ consomem exclusivamente sinapses com peso calibrado $w_{ij} \ge 0.65$, registram emissões em `[SYNAPTIC_OUTPUTS]`, reforçam a malha com eventos de LTP ($\eta = 0.20$) após homologação ou LTD ($\delta_{penalty} = 0.40$) após vetos, e integram engramas heurísticos sob `[ASSOCIATIVE_MEMORY_ENGRAMS]`.
8. **Supervisory Rejection Dossier & Banimento de Reiteração em Espaço de Erro:**
   - Subagentes reprovados em portões determinísticos, supervisão técnica ou Gauntlet (Época IV) não recebem feedbacks vagos nem autorização para repetições estocásticas.
   - O supervisor emite o **Non-Acceptance Dossier com Blacklist Acumulativa de Vetores** (`.planning/rejections/rejection_dossier_<slug>.json`), catalogando falhas de AST, incompatibilidade de tipos, exceções de runtime e padrões banidos.
   - O subagente de correção DEVE consumir o dossiê via `view_file` antes de qualquer mutação física e rotacionar compulsoriamente seu espaço de busca e algoritmo. A reiteração no mesmo espaço de erro ou reutilização de padrões banidos aciona a trava mecânica `[HARD REJECT: BLACKLISTED_VECTOR_REITERATION]`.
9. **Suporte Estigmérgico a Mutações de RSI & Memória Associativa:**
   - O enxame integra-se organicamente ao pipeline de Recursive Self-Improvement (RSI): incidentes motores geram registros de post-mortem (`pm_*.json`), retroalimentando o barramento com engramas cognitivos Hebbianos e disparando propostas cirúrgicas de patch (`.planning/rsi/candidates/patch_<id>.json`) validadas sob o Invariante Anti-Dumbing-Down.

---

## 9. O Protocolo de Handoff Neural de Alta Fidelidade & Banimento do "Telefone Sem Fio" (High-Fidelity Neural Handoff — Lei 42)

Subagentes operam como **submentes neurais corticais especializadas**, enquanto o Agente Principal atua como o **Córtex Pré-Frontal Soberano**. No ecossistema neural de enxame, a patologia mais destrutiva é a **degradação epistêmica por compressão pré-frontal com perda** (*The Neural Telephone Game*).

### 9.1. A Patologia do "Telefone Sem Fio" Pré-Frontal
Quando um subagente especialista investiga um problema complexo, ele gera inteligência pericial de altíssima resolução: offsets de memória, condições de corrida assíncronas, linhas exatas, dependências cruzadas e modos silenciosos de falha.
O erro estocástico clássico ocorre quando o Agente Principal intercepta essa saída, redige um resumo de 2 ou 3 linhas na thread principal e injeta apenas esse resumo diluído no prompt do subagente codificador de produção.
- **Consequência:** O subagente de produção recebe uma sombra empobrecida da realidade técnica, perde as sutilezas microscópicas e implementa remendos sintomáticos ou stubs.

### 9.2. O Circuito Neural em Malha Fechada de 5 Etapas:
1. **Gravação Física do Laudo Pericial (Substrato Estigmérgico):**
   O subagente investigador (Alfa, Beta ou Ontologista) grava obrigatoriamente seu relatório analítico bruto e irrestrito no disco:
   `.planning/investigations/inv_<id>_<slug>.md`
2. **Registro Sináptico Feedforward (`synaptic_bus.json`):**
   O Agente Principal valida a conclusão do laudo e propaga o caminho físico do artefato no barramento sob `synaptic_signals.INVESTIGATION_ARTIFACTS`.
3. **Injeção do Ponteiro Físico no Payload:**
   Ao despachar o subagente codificador de produção via `invoke_subagent`, o prompt contém a tag obrigatória:
   `[INVESTIGATION_REPORT_PATH]: ".planning/investigations/inv_<id>_<slug>.md"`
4. **Leitura Mandatória na Íntegra via `view_file` (Ingestão de Alta Fidelidade):**
   A primeira ação motora do subagente de produção DEVE ser invocar `view_file` no arquivo do relatório pericial bruto. Ele absorve diretamente a mente do investigador, com fidelidade de 100%, sem perda de sinal pré-frontal. O córtex pré-frontal atua como orquestrador, barramento sináptico e árbitro — jamais como filtro diluidor.
5. **Mutação Motora Atômica no Disco & Recibo Fiduciário:**
   A ação de encerramento do subagente de produção é invocar `replace_file_content` ou `write_to_file` diretamente no disco, seguida de compilação/testes (`run_command`). O subagente valida a gravação física e transmite ao parent via `send_message` unicamente a telemetria fria de arquivos alterados, sem nunca transcrever o código no chat.

---

## 10. Checklist Forense de Orquestração de Enxame (Binário — Leis 41 a 45 — v5.0)

> Auditado pelo Agente Principal e pelo Red Team Juiz na Época IV.

- [ ] **Relação 1:1 Atômica:** exatamente 1 subagente por nó ou arquivo de produção; zero batching.
- [ ] **Urgência de Subagente Respeitada:** zero investigação solitária na thread principal; dupla investigativa despachada.
- [ ] **Squad Activation Gate Cumprido:** subagentes do blueprint do Dossiê despachados antes da mutação de código.
- [ ] **Handoff de Alta Fidelidade Verificado:** subagente de produção leu documento pericial bruto via `view_file`; zero resumo lossy do pré-frontal.
- [ ] **Clean-Context Verificado:** subagente despachado com payload cirúrgico delimitado, sem vazamento do histórico da thread principal.
- [ ] **Teto de Onda Respeitado:** máximo de 15 subagentes por chamada de `invoke_subagent`.
- [ ] **Sinapses Feedforward Persistidas:** saídas registradas no `synaptic_bus.json` com `[SYNAPTIC_OUTPUTS]`.
- [ ] **Plasticidade Sináptica Validada:** pesos sinápticos $w_{ij} \ge 0.65$ verificados para injeção em downstream; eventos LTP ($\eta = 0.20$) e LTD ($\delta_{penalty} = 0.40$) computados.
- [ ] **Transição Quântica de Contratos em 5 Fases:** contratos transicionados formalmente (`HOLD` -> `DRAFT` -> `VERIFYING` -> `STABLE` -> `DEPRECATED`); zero contratos órfãos em DRAFT/VERIFYING na transição para Época III.
- [ ] **Resolução Algorítmica de Conflitos SCDA:** divergências e vetos cruzados dirimidos por Fator de Precedência Fiduciária ($FPF$) ou Síntese Dialética.
- [ ] **Blindagem FsLockEngine:** concorrência sobre arquivos compartilhados mediada por locks semafóricos atômicos ($O\_CREAT \mid O\_EXCL$) com TTL e detecção de PIDs órfãos.
- [ ] **Atomic Swap com Atestação Dupla SHA-256:** gravações de arquivos e barramento realizadas via `DeterministicAtomicSwap` com `fsyncSync` e verificação criptográfica pré e pós-swap no mesmo volume.
- [ ] **Esquadrões Sob Medida:** zero templates estáticos repetitivos; especialidades derivadas da física do problema.
- [ ] **Zero Role Drift:** subagentes cumpriram estritamente seu `[MY_SWARM_DELIVERABLE]` sem invadir escopo alheio.
- [ ] **Peer Veto Resolvido:** zero contratos contestados pendentes no `graph.json` ou barramento sináptico.
- [ ] **Mandato do Artífice Motor Cumprido:** subagentes de produção executaram mutações físicas no disco via ferramentas de escrita (`replace_file_content` / `write_to_file`); zero dumps de código em markdown no `send_message`.
- [ ] **Veto ao Parent Digitador Mantido:** Agente Principal absteve-se de digitar ou colar código produzido por subagentes; atuou estritamente como árbitro e validador.
- [ ] **Despacho Motor Válido:** todos os subagentes com meta de produção ou mutação foram despachados com `TypeName: "self"`.
- [ ] **Ortogonalidade Estrita de Alvos:** nenhum arquivo físico compartilhado simultaneamente por múltiplos subagentes na mesma onda ($\text{FileSet}(S_i) \cap \text{FileSet}(S_j) = \emptyset$).
- [ ] **Memória Estigmérgica de Engramas Ativa:** heurísticas empíricas e invariantes destilados consolidados em `cognitive_engrams` e consumidos pela malha.
- [ ] **Supervisory Rejection Dossier Auditado & Ausência de Iteração em Espaço Rejeitado:** subagentes que sofreram veto ou reprovação consumiram o Non-Acceptance Dossier via `view_file`; zero reiteração de vetores presentes na Blacklist Acumulativa (`[HARD REJECT: BLACKLISTED_VECTOR_REITERATION]`).
- [ ] **Suporte Estigmérgico RSI & Engramas Hebbianos Ativos:** telemetria fria pós-execução registrada (`pm_*.json`), heurísticas derivadas de ciclos Hebbianos (LTP/LTD) convertidas em engramas em `associative_memory` e patches de RSI validados sob o Invariante Anti-Dumbing-Down.

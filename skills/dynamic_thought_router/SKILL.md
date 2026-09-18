---
name: dynamic_thought_router
description: "v5.0 — The Autonomous Hyper-Cortex Sovereign Engine. Playbook operacional e motor de roteamento cognitivo dinâmico. Governa a seleção determinística e transição fluida entre 4 topologias de pensamento em tempo de execução: Linear Causal Stream (ações mecânicas determinísticas), Tree of Thoughts (busca algorítmica com Poda Fiduciária A*), Graph of Thoughts (sistemas em malha com fusão multilinear e relaxamento cíclico) e Dialectical Adversarial Synthesis (decisões críticas de trade-off via Tese, Antítese Red Team e Síntese invariante com tripwire K <= 3). Interconectado estigmergicamente com .planning/thought_graph.json e synaptic_bus.json v5.0."
---

# Dynamic Thought Router Operations Playbook (v5.0 — The Autonomous Hyper-Cortex)

Playbook técnico e operacional do motor metacognitivo soberano do ecossistema. Elimina em definitivo a rigidez da bifurcação binária estática da v4.1 (Modo Arquitetural de 100 nós vs Modo Direto Zero Nós) e institucionaliza o roteamento dinâmico e contínuo de topologias de pensamento baseadas na física real do problema.

---

## 1. Núcleo Conceitual & As Quatro Topologias Cognitivas

O ecossistema rejeita a imposição arbitrária de uma única estrutura de pensamento para problemas de naturezas distintas. A cognição do agente é configurada dinamicamente na topologia que maximiza o rigor de engenharia minimizando a queima de tokens e a latência epistêmica:

| Topologia | Estrutura Matemática | Complexidade | Caso de Uso Primário |
|---|---|---|---|
| **Linear Causal Stream (LCS)** | Grafo direcionado simples ($\text{in-deg} \le 1, \text{out-deg} \le 1$) | $\mathcal{O}(L)$ | Micro-mutações pontuais, comandos diretos, execução de checklists e builds. |
| **Tree of Thoughts (ToT)** | Árvore enraizada com poda ($b \in [2,5], d \le 4$) | $\mathcal{O}(b^d)$ com Poda $A^*$ | Otimizações algorítmicas, isolamento de bugs multi-hipótese, desenho de schemas. |
| **Graph of Thoughts (GoT)** | Grafo direcionado com fusão ($\mathcal{F}_{\text{fuse}}$) | $\mathcal{O}(\vert\mathcal{V}\vert + \vert\mathcal{E}\vert)$ | Sistemas em malha, Clean Architecture com dependências cruzadas, barramento sináptico. |
| **Dialectical Synthesis (DAS)**| Tríade iterativa $\langle \mathcal{T}, \mathcal{A}, \mathcal{S} \rangle$ ($K \le 3$) | $\mathcal{O}(K \cdot \text{Delib})$ | Trade-offs fiduciários de alto risco, escolhas de design concorrentes inconciliáveis. |

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                      TAXONOMIA DAS TOPOLOGIAS COGNITIVAS DINÂMICAS v5.0                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. LINEAR CAUSAL STREAM (LCS)        │ 2. TREE OF THOUGHTS (ToT COM PODA A*)                     │
│    [v0] ──> [v1] ──> [v2] ──> [vf]   │                    [Root]                                 │
│    • Branching Factor: b = 1         │                   /   |   \                               │
│    • Complexidade: O(L)              │                [v1] [v2] [v3] (Poda: v3 reprovado)        │
│    • Aplicação: Ações determinísticas│               /   \   |                                   │
│                                      │            [v1.1][v1.2] [v2.1]                            │
│                                      │            • Branching Factor: b in [2, 5], Depth <= 4     │
│                                      │            • Heurística: f(n) = g(n) + h(n)               │
├──────────────────────────────────────┼───────────────────────────────────────────────────────────┤
│ 3. GRAPH OF THOUGHTS (GoT - FUSÃO)   │ 4. DIALECTICAL ADVERSARIAL SYNTHESIS (DAS)                │
│       [v1: GPU]    [v2: Storage]     │                 [Problema / Trade-off]                    │
│           \            /             │                           │                               │
│            v          v              │            ┌──────────────┴──────────────┐                │
│         [v3: Aggregator / Fusion]    │            ▼                             ▼                │
│            /          \              │     [TESE CONSTRUTIVA]          [ANTÍTESE RED TEAM]       │
│           v            v             │     • Max Utilidade/Perf        • Caça Modos de Falha     │
│      [v4: Layout]   [v5: Cache]      │            │                             │                │
│    • in-degree >= 1, out-degree >= 1 │            └──────────────┬──────────────┘                │
│    • Operador: F_fuse(V) -> v_agg    │                           ▼                               │
│    • Aplicação: Sistemas em malha    │                 [SÍNTESE FIDUCIÁRIA]                      │
│                                      │                 • Contrato Invariante Transcendente       │
│                                      │                 • Tripwire de Parada: K <= 3 iterações    │
└──────────────────────────────────────┴───────────────────────────────────────────────────────────┘
```

---

## 2. Especificação Rigorosa das Quatro Topologias

### 2.1. Topologia 1: Linear Causal Stream (LCS)
- **Definição Formal:** Grafo direcionado simples $\mathcal{G}_{\text{LCS}} = (\mathcal{V}, \mathcal{E})$, onde para todo vértice $v_i \in \mathcal{V}$:
  $$\text{in-degree}(v_i) \le 1 \quad \text{e} \quad \text{out-degree}(v_i) \le 1$$
  com ordenação causal estrita $v_0 \to v_1 \to \dots \to v_L$.
- **Invariantes Operacionais:**
  1. **Zero Bifurcação Especulativa:** O pensamento avança de forma puramente dedutiva sem abrir ramos concorrentes.
  2. **Tração Causal Estrita ($X \to Y \to Z$):** Cada elo da cadeia decorre mecanicamente do anterior.
  3. **Latência de Raciocínio Sub-16ms:** Foco na velocidade de despacho de ferramentas motoras.
- **Domínio de Aplicação:**
  - Micro-mutações cirúrgicas de código onde a causa raiz já está comprovada empiricamente.
  - Execução de sequências determinísticas de build, lint, execução de testes unitários ou auditorias de checklists.
  - Transições atômicas de expedientes quando não há ambiguidade técnica ou de requisitos.
- **Tripwire de Abandono Imediato:** Se durante o fluxo LCS surgir qualquer ambiguidade, falha inesperada com hipóteses concorrentes ($b \ge 2$) ou incerteza técnica ($\varepsilon > 0$), o LCS é imediatamente abortado e o motor comuta para ToT ou DAS (`[TOPOLOGY_SWITCH: LCS -> ToT]`).

### 2.2. Topologia 2: Tree of Thoughts (ToT - Poda Fiduciária & Heurística $A^*$)
- **Definição Formal:** Árvore direcionada enraizada $\mathcal{T} = (\mathcal{V}, \mathcal{E}, v_0)$ com:
  - Fator de ramificação controlado: $b \in [2, 5]$.
  - Profundidade máxima estrita: $d \le 4$ (proteção matemática contra explosão combinatória de contexto).
- **Função de Avaliação Fiduciária ($A^*$ Heuristic):**
  Cada nó de pensamento $n \in \mathcal{V}$ é avaliado pela equação:
  $$f(n) = g(n) + h(n)$$
  onde:
  - $g(n)$: Custo computacional e de tokens acumulado da raiz $v_0$ até $n$.
  - $h(n)$: Estimativa fiduciária de conformidade e distância até o fechamento correto:
    $$h(n) = \sum_{j=1}^{M} w_j \cdot c_j(n)$$
    com conformidade $c_j(n) \in [0, 1]$ e pesos fiduciários normalizados ($\sum w_j = 1$):
    - *Tipagem estrita `Result<T,E>` e ausência de stubs:* peso $0.35$.
    - *Complexidade de tempo/espaço assintótica e memória:* peso $0.25$.
    - *Resiliência a concorrência e ausência de deadlocks:* peso $0.25$.
    - *Clareza arquitetural e facilidade de manutenção:* peso $0.15$.
- **Mecanismo de Poda Fiduciária Dura (Hard Fiduciary Pruning):**
  - **Limiar de Poda:** Se $f(n) < \theta_{\text{prune}}$ ($\theta_{\text{prune}} = 0.75$), o ramo é imediatamente podado.
  - **Veto Constitucional Imediato:** Qualquer ramo que proponha violação de lei constitucional (ex: `any`, omitir tratamentos de erro, áudio sintético senoidal ou stubs) recebe $f(n) = -\infty$ e é sumariamente extirpado.
- **Domínio de Aplicação:**
  - Otimização de algoritmos de baixo nível (concorrência lock-free vs mutex, anéis de buffers, filas atômicas).
  - Isolamento de falhas elusivas com múltiplas hipóteses causais mutuamente exclusivas.
  - Desenho de schemas de banco de dados e migrações com múltiplos caminhos de retrocompatibilidade.

### 2.3. Topologia 3: Graph of Thoughts (GoT - Malhas Cíclicas & Fusão Multilinear)
- **Definição Formal:** Grafo direcionado geral $\mathcal{G}_{\text{GoT}} = (\mathcal{V}, \mathcal{E})$ onde:
  - Vértices admitem múltiplos predecessores e sucessores ($\text{in-degree}(v) \ge 1, \text{out-degree}(v) \ge 1$).
  - O grafo suporta arestas de realimentação (*feedback loops*) temporais governadas por épocas discretas $t \in \mathbb{N}$.
- **Primitivas e Operadores de Grafo:**
  1. **Operador de Fusão de Pensamento ($\mathcal{F}_{\text{fuse}}$):**
     $$\mathcal{F}_{\text{fuse}}: \mathcal{P}(\mathcal{V}) \to \mathcal{V}_{\text{agg}}$$
     Recebe um conjunto de pensamentos derivados de ramos ontológicos ortogonais (ex: $v_{\text{gpu}}$ da UI, $v_{\text{acid}}$ do storage, $v_{\text{sec}}$ da autenticação) e sintetiza um nó consolidado satisfazendo simultaneamente todas as restrições de fronteira.
  2. **Operador de Agregação de Sinapses ($\mathcal{A}_{\text{synaptic}}$):**
     Consome sinais do `synaptic_bus.json` com resolução de conflitos via ordenação topológica condicional de dependências.
  3. **Operador de Relaxamento Cíclico ($\mathcal{R}_{\text{relax}}$):**
     Detecta acoplamentos circulares entre subsistemas ($A \to B \to A$) e desacopla o contrato através de uma porta abstrata (`IPortInterface`) e emissão assíncrona de eventos.
- **Domínio de Aplicação:**
  - Design e refatoração de sistemas modulares complexos com dependências cruzadas (Clean Architecture desacoplada).
  - Orquestração de ondas de subagentes onde especialistas concorrentes emitem contratos simultâneos interdependentes.
  - Sistemas de tempo real onde parâmetros físicos de subsistemas colidem e exigem convergência harmônica.

### 2.4. Topologia 4: Dialectical Adversarial Synthesis (DAS - Tese, Antítese, Síntese)
- **Definição Formal:** Processo fiduciário iterativo governado pela tríade:
  $$\langle \mathcal{T}_k, \mathcal{A}_k, \mathcal{S}_k \rangle, \quad k \in \{1, 2, \dots, K_{\max}\}, \quad K_{\max} = 3$$
- **As Três Forças Fiduciárias:**
  1. **Tese Construtiva ($\mathcal{T}_k$):** Formulação da melhor solução técnica sob a ótica da utilidade, performance de pico e viabilidade de implementação.
  2. **Antítese Adversarial Red Team ($\mathcal{A}_k$):** Dissecação implacável da tese sob a premissa de colapso. O Red Team identifica condições de corrida, vazamentos de recursos em 72h contínuas, saturação de I/O e modos silenciosos de falha.
  3. **Síntese Fiduciária Invariante ($\mathcal{S}_k$):** Criação de um novo contrato ou modelo de arquitetura que incorpora blindagens contra todos os vetores expostos pela Antítese $\mathcal{A}_k$, preservando a utilidade da Tese $\mathcal{T}_k$.
- **Mecanismo de Convergência & Tripwire Anti-Looping (Lei 45):**
  - A cada iteração afere-se a métrica de discordância residual:
    $$\Delta_{\text{epistemic}} = \text{Divergência}(\mathcal{T}_k, \mathcal{A}_k)$$
  - Se $\Delta_{\text{epistemic}} \le \epsilon_{\text{threshold}}$, a Síntese $\mathcal{S}_k$ é ratificada e convertida em ação motora.
  - Se $k = 3$ e persistir divergência, o sistema proíbe nova iteração de debate. Aplica-se compulsoriamente a **Regra de Desempate Fiduciário:** adota-se a alternativa mais defensiva, conservadora e robusta ("Caminho Mais Árduo / Água no Deserto"), encerrando o pensamento e executando a alteração física imediatamente.

---

## 3. O Motor de Roteamento Dinâmico em Tempo de Execução

```text
                                 [DEMANDA DE ENGENHARIA / ATUALIZAÇÃO]
                                                    │
                                                    ▼
                                ┌────────────────────────────────────────┐
                                │  EXTRAÇÃO DO VETOR DE ATRIBUTOS (x)    │
                                │  x = <D_ont, U_unc, B_bif, C_conc,     │
                                │       S_sens, P_risk> in [0, 1]^6      │
                                └────────────────────┬───────────────────┘
                                                     │
                                                     ▼
                                ┌────────────────────────────────────────┐
                                │  FUNÇÃO DE SELEÇÃO DE TOPOLOGIA        │
                                │  Calcula S_LCS, S_ToT, S_GoT, S_DAS    │
                                │  Phi(x) = argmax_T S_T(x)              │
                                └────────────────────┬───────────────────┘
                                                     │
         ┌──────────────────────┬───────────────────┴───────────────────┬──────────────────────┐
         ▼                      ▼                                       ▼                      ▼
  [Phi(x) == LCS]        [Phi(x) == ToT]                         [Phi(x) == GoT]        [Phi(x) == DAS]
         │                      │                                       │                      │
  Tração Causal          Árvore Heurística                       Malha de Pensamento    Ciclo Triádico
  Linear Direta          com Poda A*                             com Fusão Multilinear  Tese vs Antítese
  (Micro-Mutações)       (Algoritmos/Busca)                      (Sistemas Concorrentes)(Trade-offs Críticos)
         │                      │                                       │                      │
         └──────────────────────┴───────────────────┬───────────────────┴──────────────────────┘
                                                    │
                                                    ▼
                               ┌────────────────────────────────────────┐
                               │  ESTIGMERGIA & PERSISTÊNCIA FÍSICA     │
                               │  .planning/thought_graph.json          │
                               │  Sincronização com synaptic_bus.json   │
                               └────────────────────────────────────────┘
```

### 3.1. Vetor de Atributos da Demanda ($\mathbf{x}$)
Toda solicitação ou intervenção tem seus parâmetros mapeados no vetor normalizado:
$$\mathbf{x} = \langle D_{\text{ont}}, U_{\text{unc}}, B_{\text{bif}}, C_{\text{conc}}, S_{\text{sens}}, P_{\text{risk}} \rangle \in [0, 1]^6$$

1. **$D_{\text{ont}}$ (Dimensionalidade Ontológica):** Quantidade de domínios ortogonais impactados (UI, Banco, Rede, SO, Concorrência).
   - $0.0$: Tarefa restrita a um único domínio ou arquivo.
   - $1.0$: Tarefa transversal que afeta $\ge 4$ domínios arquiteturais simultaneamente.
2. **$U_{\text{unc}}$ (Incerteza Epistêmica $\varepsilon$):** Ausência de documentação, bibliotecas opacas ou comportamento estocástico externo.
   - $0.0$: Contratos explícitos, tipos nativos conhecidos e ambiente determinístico.
   - $1.0$: Caixa preta completa, ausência de especificações e APIs sem telemetria.
3. **$B_{\text{bif}}$ (Fator de Bifurcação de Decisão):** Número de abordagens viáveis para resolver o problema.
   - $0.0$: Única forma canônica de implementar.
   - $1.0$: $\ge 3$ arquiteturas concorrentes válidas com trade-offs distintos.
4. **$C_{\text{conc}}$ (Complexidade de Concorrência & Estado Compartilhado):** Risco de race conditions, bloqueios de thread ou inconsistência transacional.
   - $0.0$: Execução síncrona monothread sem estado mutável compartilhado.
   - $1.0$: Sistema distribuído, locks assíncronos, Atomic Swaps sob múltiplos escritores.
5. **$S_{\text{sens}}$ (Sensibilidade Multissensorial & Fiduciária):** Requisitos de cinemática de 120fps, isolamento de GPU, micro-ativos ópticos reais ou áudio Foley real.
   - $0.0$: Lógica interna de backend puro sem interface perceptiva.
   - $1.0$: UI altamente tátil, animações de molas de 2ª ordem e sintetização acústica física.
6. **$P_{\text{risk}}$ (Criticidade de Risco de Produção):** Gravidade do modo de falha para a integridade do negócio.
   - $0.0$: Script descartável de análise temporária.
   - $1.0$: Núcleo financeiro, persistência crítica de banco, autenticação ou integridade de arquivos do usuário.

### 3.2. Função de Pontuação das Topologias
As pontuações de adequação são calculadas deterministamente por:

$$S_{\text{LCS}}(\mathbf{x}) = (1 - B_{\text{bif}}) \cdot (1 - U_{\text{unc}}) \cdot (1 - C_{\text{conc}}) \cdot (1 - D_{\text{ont}})$$

$$S_{\text{ToT}}(\mathbf{x}) = B_{\text{bif}} \cdot (1 - C_{\text{conc}}) \cdot \left(\frac{1 + U_{\text{unc}}}{2}\right)$$

$$S_{\text{GoT}}(\mathbf{x}) = D_{\text{ont}} \cdot C_{\text{conc}} \cdot \left(\frac{1 + S_{\text{sens}}}{2}\right)$$

$$S_{\text{DAS}}(\mathbf{x}) = P_{\text{risk}} \cdot \max(U_{\text{unc}}, B_{\text{bif}}) \cdot \left(\frac{1 + D_{\text{ont}}}{2}\right)$$

### 3.3. Matriz de Decisão & Regras de Prioridade Determinística
A seleção da topologia $\Phi(\mathbf{x})$ obedece à regra:
$$\Phi(\mathbf{x}) = \arg\max_{T \in \{\text{LCS}, \text{ToT}, \text{GoT}, \text{DAS}\}} S_T(\mathbf{x})$$

#### Regras de Override e Travas Fiduciárias Supremas:
1. **Regra de Ouro da Dialética:** Se $P_{\text{risk}} \ge 0.85$ e $B_{\text{bif}} \ge 0.5$, a topologia **DAS (Dialectical Adversarial Synthesis)** é mandatória, independentemente das outras pontuações. Nenhuma decisão de alto risco e alta bifurcação pode ser tomada sem confronto formal de Antítese Red Team.
2. **Regra de Ouro da Concorrência em Malha:** Se $C_{\text{conc}} \ge 0.7$ e $D_{\text{ont}} \ge 0.6$, a topologia **GoT (Graph of Thoughts)** é mandatória para permitir fusão multilinear e exclusão mútua sináptica.
3. **Regra de Tração Mecânica LCS:** Se $B_{\text{bif}} \le 0.2$, $U_{\text{unc}} \le 0.2$ e $D_{\text{ont}} \le 0.3$, a topologia **LCS (Linear Causal Stream)** é mandatória. Qualquer tentativa de usar ToT ou Dialética neste quadrante é considerada *Cosplay Acadêmico* e desperdício de tokens, acionando corte de poda.

---

## 4. Persistência Estigmérgica no Disco (`.planning/thought_graph.json`)

Para garantir auditabilidade soberana e interoperabilidade de enxame, a topologia de pensamento ativa é persistida em disco a cada deliberação:

```json
{
  "router_version": "5.0.0",
  "current_topology": "DIALECTICAL_ADVERSARIAL_SYNTHESIS",
  "input_vector": {
    "D_ont": 0.75,
    "U_unc": 0.60,
    "B_bif": 0.80,
    "C_conc": 0.70,
    "S_sens": 0.40,
    "P_risk": 0.90
  },
  "topology_scores": {
    "LCS": 0.012,
    "ToT": 0.192,
    "GoT": 0.368,
    "DAS": 0.630
  },
  "active_nodes": [
    {
      "id": "thesis_001",
      "type": "THESIS",
      "statement": "Utilização de SQLite WAL nativo com busy_timeout de 5000ms para persistência concorrente.",
      "score": 0.82
    },
    {
      "id": "antithesis_001",
      "type": "ANTITHESIS",
      "statement": "Sob 10 subagentes paralelos em SSD lento, o checkpoint do WAL causa picos de I/O bloqueando a main thread acima de 16ms.",
      "vulnerability_severity": "HIGH"
    },
    {
      "id": "synthesis_001",
      "type": "SYNTHESIS",
      "statement": "SQLite WAL isolado em worker thread desacoplada com anel de escrita atômico e flush em lote compensado.",
      "status": "RATIFIED_GO"
    }
  ],
  "tripwire_status": {
    "current_iteration": 1,
    "max_iterations": 3,
    "is_converged": true
  }
}
```

---

## 5. Exemplares Contrastivos de Roteamento (Pedagogia Contrastiva — Lei 36)

### 5.1. Anti-Pattern 1: Flattening Cego (Linearização Forçada de Problema Combinatório)
```text
[CENÁRIO]: Otimização de concorrência com 10 writers simultâneos em SQLite WAL.
[CONDUTA REDUCIONISTA]:
O agente abre o arquivo e implementa linearmente um lock simples com mutex booleano na thread principal.
[AUTÓPSIA DA FALHA]:
Sob regime de concorrência massiva da Onda 2, o primeiro writer bloqueia a thread, gerando starvation e estouro de SLA de latência (degradando para 450ms). O agente foi incapaz de explorar alternativas porque forçou um problema combinatório em uma cadeia linear direta, ignorando filas atômicas e workers dedicados.
```

### 5.2. Anti-Pattern 2: Over-Deliberation / Academic Cosplay (Prolixidade Reflexiva)
```text
[CENÁRIO]: Ajustar o padding de um botão de 12px para 16px e a cor do hover para #1e293b.
[CONDUTA REDUCIONISTA]:
O agente instancia Tree of Thoughts com 5 ramificações, debate a tese e a antítese sobre a semiologia das cores durante 40.000 tokens e gera equações matemáticas fictícias para o espaçamento do botão.
[AUTÓPSIA DA FALHA]:
Queima fiduciária absurda de tokens para uma micro-mutação mecânica determinística (B_bif = 0, U_unc = 0). Violou a regra de tração mecânica do LCS e cometeu Cosplay Acadêmico explícito.
```

### 5.3. Padrão Titã v5.0: Roteamento Cirúrgico & Colapso Determinístico
```text
[CENÁRIO]: Decisão de persistência: SQLite em memória vs SQLite em disco com WAL vs Flat Files JSON sob concorrência de 10 subagentes.
[CONDUTA TITÃ v5.0]:
1. Mapeamento Vetorial: D_ont=0.7, U_unc=0.3, B_bif=0.8, C_conc=0.9, S_sens=0.0, P_risk=0.9.
2. Roteamento: S_DAS=0.76 (Dominante) -> Instancia Dialectical Adversarial Synthesis.
3. Ciclo 1:
   - Tese: SQLite WAL em disco com conexão compartilhada.
   - Antítese Red Team: Lock contention no WAL checkpoint gera EBUSY em Windows NTFS em concorrência concorrente direta.
   - Síntese: SQLite em arquivo desacoplado por domínio com conexão dedicada em modo WAL e Atomic Swap em caso de gravação de snapshot.
4. Convergência: Atingida na Iteração 1. Colapsa imediatamente para emissão de contrato em synaptic_bus.json com status 'GO'.
```

---

## 6. Checklist Forense de Governança Topológica (Binário — Leis 41, 44 & 45)

> Auditado pelo Agente Principal e pelo Red Team Juiz na Época IV.

- [ ] **1. Mapeamento Vetorial Concluído:** Vetor $\mathbf{x}$ calculado com todas as 6 dimensões formalmente fundamentadas.
- [ ] **2. Topologia Ótima Selecionada:** $\Phi(\mathbf{x})$ executado com justificativa e persistência no disco.
- [ ] **3. Poda Fiduciária Aplicada (se ToT):** Ramos com $f(n) < 0.75$ formalmente podados; zero ramos com violações constitucionais.
- [ ] **4. Fusão de Contratos Validada (se GoT):** Operador $\mathcal{F}_{\text{fuse}}$ produziu contrato unificado sem quebra de portas arquiteturais.
- [ ] **5. Tripwire Dialético Respeitado (se DAS):** Convergência obtida em $K \le 3$ iterações; zero debate circular no Thinking.
- [ ] **6. Zero Cosplay Acadêmico:** Nenhuma fórmula matemática inserida sem relação causal direta com a física do problema.
- [ ] **7. Conexão com o Barramento Sináptico:** Sinapses resultantes emitidas no `synaptic_bus.json` com status `GO`.
- [ ] **8. Zero-Stub Permanente:** Todas as decisões resultam em contratos executáveis sem `TODO`, `pass` ou retornos fictícios.
- [ ] **9. Null-Vocabulary Estrito:** Ausência de preâmbulos servis, bajulação ou desculpas em toda a deliberação.
- [ ] **10. Persistência Estigmérgica:** Arquivo `.planning/thought_graph.json` sincronizado e gravado fisicamente no disco.

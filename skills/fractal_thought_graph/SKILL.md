---
name: fractal_thought_graph
description: Manual técnico e playbook operacional para gestão do substrato de pensamento (.planning/nodes/), modelagem determinística do manifesto graph.json, protocolo de expansão fractal polímata até a Fronteira do Impassável e despacho concorrente atômico 1:1 de subagentes.
---

# Fractal Thought Graph Operations Playbook (v3.3)

Manual prático de orquestração do substrato cognitivo pré-execução (`.planning/`). Estabelece a metodologia de expansão de pensamento de nível AGI: **a erradicação definitiva da preguiça estocástica, do batching reducionista e do isolamento neural** através da conexão polímata universal entre domínios correlacionados e não-correlacionados. Governa a cadeia causal contínua ($X \to Y \to \text{Ramificações de 2ª, 3ª e 4ª ordem}$) até a **Fronteira do Impassável** ($N \ge 100$) com:
1. **Ingestão Estratégica via Subagente Prompt Refiner** (compilação do `mission_dossier.md`).
2. **Pesquisa Empírica via Subagente Chief Ontologist** (fundamentação do `node_000_root.md` e `hypergraph_seed.json`).
3. **Barramento Sináptico Neural (`synaptic_bus.json`)** conectando as ondas de nós em rede neural viva.
4. **Despacho Atômico 1:1 em Ondas (máx 15 nós/onda)** com modelo **Flash Low/Medium/High**.
5. **Governança por Expedientes Cognitivos (Work Shifts)** com persistência física no disco.

---

## 1. Topologia Física no Disco (`.planning/`)

```text
.planning/
├── mission_dossier.md          # Dossiê Executivo da Missão (compilado na Época 0 pelo Prompt Refiner)
├── node_000_root.md            # Decomposição Ontológica Raiz (fundamentada pelo Chief Ontologist)
├── hypergraph_seed.json        # Semente Empírica: Lista discriminada de todos os 100+ nós e hipóteses
├── synaptic_bus.json           # Barramento Sináptico Neural: Ledger de contratos, tipos, status HOLD/GO e sinapses
├── expediente_state.json       # Persistência de Estado do Turno/Expediente Cognitivo Atual
├── graph.json                  # Manifesto Central Consolidado: Grafo, arestas tipadas e primitivas
├── mailboxes/                  # Caixas Postais Estigmérgicas para coordenação assíncrona entre subagentes
│   ├── mailbox_node_001.json   # Depósito de avisos, descompassos de interface e notas de coordenação
│   └── ...
└── nodes/
    ├── node_001_<slug>.md      # Nós Primários Estruturais (d=1, Camada Base)
    ├── node_001_1_<atrito>.md  # Nós Filhos de Resolução de Atrito (d=2, Delta Puro)
    ├── node_001_2_<falha>.md   # Nós Filhos de Modos Silenciosos de Falha (d=2, Delta Puro)
    └── ...                     # Piso mínimo inegociável de 100 nós (N >= 100)
```

---

## 2. Playbook da Época 0: Subagente Prompt Refiner & Dossiê de Missão

Antes de qualquer dedução arquitetural ou despacho de nós, o Agente Principal despacha um subagente especialista dedicado para auditar e compilar a solicitação do usuário.

### Invocação do Subagente Prompt Refiner:
```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Prompt Refiner & Epistemic Compiler",
      "Model": "flash",
      "Prompt": "Você é o especialista soberano em compilação epistêmica de demandas de engenharia. Analise a demanda do usuário de cima a baixo. Execute compulsoriamente o Protocolo de Deconstrução Forense em 4 Camadas (Lei 38): (1) Contratos Explícitos unívocos, (2) Contratos Implícitos deduzidos matematicamente (idempotência, persistência atômica, tipagem estrita Result/Option, concorrência, latência sub-16ms), (3) Engenharia Reversa Pre-Mortem sob a premissa irrevogável de colapso em T+6 meses com nós atômicos de blindagem, (4) Checklist Dinâmico de Duplo-Check (Two-Man Rule). Injete as palavras-chave mandatórias das rules e skills ('Água no Deserto', 'Cinemática de Molas dos Titãs', 'Micro-ativos táteis reais', 'Áudio acústico real', 'Clean Architecture Defensiva', 'Autonomous Computer Use OODA', '1:1 Subagente por Nó', 'Inspeção Visual no Chrome Real'). Persista o resultado integral em .planning/mission_dossier.md."
    }
  ]
}
```

### Estrutura do Dossiê de Missão (`.planning/mission_dossier.md`):
```markdown
# Executive Mission Dossier: <Nome da Missão>

## 1. Decomposição de Objetivos & Contexto Fiduciário
- Meta Comercial & Operacional Real (Zero Cosplay)
- Stakeholders, Nível de Criticidade e SLA de Desempenho

## 2. Injeção de Diretrizes Constitucionais Mandatórias
- Caminho "Água no Deserto": [Quais variáveis exigem dissecação profunda]
- Padrão dos Titãs (Linear/Apple/Stripe): [Requisitos de molas de 2ª ordem e latência sub-16ms]
- Mídia & Áudio Reais: [Mapeamento de renders macro via generate_image e Foley via sfx_tool.py]
- Clean Architecture & Computer Use: [Estrutura defensiva, Result/Option, Atomic Swap e Ciclo OODA]

## 3. Matriz de Ativação de Skills & Regras
- Skills Ativadas: [fractal_thought_graph, modern_ui_craft, tactile_audio_sfx, hardened_clean_architecture, browser_visual_reasoning, autonomous_computer_use]
- Tier de Complexidade ACC: [Tier 1 | Tier 2 | Tier 3]

## 4. Protocolo de Deconstrução Forense Prévia (Lei 38)
### 4.1 Camada 1: Contratos Explícitos Mapeados (CE-01 ... CE-n)
### 4.2 Camada 2: Contratos Implícitos (A Física Oculta: Idempotência, Mutex, Tipagem Estrita)
### 4.3 Camada 3: Engenharia Reversa Pre-Mortem (Autópsia de Falha Catastrófica em T+6 Meses)
- Vetores de Quebra Analisados & Nós de Blindagem Hipergráfica Criados
### 4.4 Camada 4: Manifesto de Duplo-Check Fiduciário (Two-Man Rule Sign-off)
- [x] [CONSTRUCTION_FIDUCIARY: APPROVED]
- [x] [RED_TEAM_ADVERSARIAL: APPROVED]

## 5. Síntese Dinâmica do Esquadrão Tático (Lei 32 & Lei 40)
- Análise de Modos de Falha: [Quais são os pontos físicos exatos onde a solução pode colapsar?]
- [BESPOKE_SQUAD_ROSTER] (Especialistas únicos gerados sob medida para o domínio da missão):
  * Especialista 1: [Papel ultra-específico, ex: "Zero-Allocation RingBuffer Concurrency Specialist"]
  * Especialista 2: [Papel ultra-específico, ex: "Two-Phase Commit Distributed Ledger Specialist"]
  * Especialista 3: [Papel ultra-específico, ex: "Framer-Motion 2nd Order Damped Spring Specialist"]
```

---

## 3. Protocolo da Trava Epistêmica (`EPISTEMIC_HALT`) & Sondas Investigativas

Quando a máquina depara-se com incerteza ($\varepsilon > 0$), APIs não documentadas, ambiguidades de regra de negócio ou comportamento anômalo, **é expressamente proibido adivinhar, usar valores default ou criar stubs**.

### Fluxo Operacional de Desbloqueio:
1. **Acionamento Imediato:** O agente declara no Chain-of-Thought:  
   `[EPISTEMIC_HALT: <DESCRIÇÃO_EXATA_DA_INCERTEZA_TÉCNICA>]`
2. **Despacho de Sonda Empírica:** Despacha um subagente focado exclusivamente em liquidar a dúvida:
```json
{
  "Subagents": [
    {
      "TypeName": "research",
      "Role": "Empirical Forensic Scout",
      "Model": "flash",
      "Prompt": "Execute varredura forense para liquidar a seguinte incerteza técnica: [DESCRIÇÃO]. Inspecione arquivos locais, execute testes isolados ou pesquise documentações oficiais. Retorne evidências empíricas incontestáveis (código real, retornos de chamada, assinaturas exatas)."
    }
  ]
}
```
3. **Liquidação e Liberação do Fluxo:** Ao receber os fatos comprovados, o agente registra no CoT:  
   `[EPISTEMIC_RESUME: Incerteza liquidada com base em evidências comprovadas. Retomando fluxo sem palpites.]`

---

## 4. Playbook da Época I (Fase A): Subagente Chief Ontologist & Fundação Empírica


O Agente Principal é **TERMINANTEMENTE PROIBIDO** de inventar tópicos de nós de cabeça. A decomposição do hipergrafo deve ser fruto de investigação empírica real.

### Invocação do Chief Ontologist Subagent:
```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Chief Ontological Architect & Empirical Researcher",
      "Model": "flash",
      "Prompt": "Sob as diretrizes de .planning/mission_dossier.md, execute varredura empírica completa no ecossistema (código existente, contratos, estado da arte da indústria). Decomponha o domínio nos 8 eixos ontológicos nativos. Estabeleça as cadeias de causa e efeito X -> Y -> Z. Gere o arquivo .planning/nodes/node_000_root.md e o mapa de sementes empíricas .planning/hypergraph_seed.json contendo a lista discriminada de todos os 100+ nós atômicos a serem explorados pelas ondas."
    }
  ]
}
```

### Os 8 Eixos Ontológicos Nativos:
1. **Domain Logic & Business Invariants:** Regras de negócio inegociáveis, estados e máquinas finitas.
2. **Data Contracts & Atomic Persistence:** Schemas, migrações, isolamento ACID, Atomic Swap e WAL.
3. **Concurrency & Real-Time Synchronization:** Locks otimistas, filas assíncronas e ausência de alocação no frame quente.
4. **HCI, Gestures & Spring Kinematics:** Física de molas de 2ª ordem (Linear/Apple), rubber-banding e gestos a 60fps/120fps.
5. **Specular Visuals & Photorealistic Micro-Assets:** Materiais físicos (obsidiana, vidro, titânio), iluminação de estúdio macro via `generate_image`. Zero SVGs ou glifos.
6. **Physical Acoustic Foley & Micro-Audio:** Sonorização acústica real via YouTube/Freesound fatiada com `scripts/sfx_tool.py`. Zero bipes sintéticos.
7. **Silent Failure Modes & Chaos Engineering:** Desconexões abruptas, memória sob pressão, tolerâncias térmicas e saturação.
8. **Forensic Telemetry & Auditable State Trails:** Logs estruturados, rastreabilidade de transações e observabilidade fiduciária.

### Estrutura do Manifesto de Sementes (`.planning/hypergraph_seed.json`):
```json
{
  "total_planned_nodes": 105,
  "nodes": [
    {
      "id": "node_001_concurrency_engine",
      "axis": "concurrency",
      "depth": 1,
      "research_foundation": "Benchmark LMAX Disruptor e Zero-Allocation pipelines.",
      "target_file": ".planning/nodes/node_001_concurrency_engine.md"
    },
    {
      "id": "node_002_titan_spring_kinematics",
      "axis": "hci_gestures",
      "depth": 1,
      "research_foundation": "Física de molas de 2ª ordem Linear/Apple via framer-motion.",
      "target_file": ".planning/nodes/node_002_titan_spring_kinematics.md"
    }
  ]
}
```

---

## 5. Playbook da Época I (Fase B): Barramento Sináptico Neural (`synaptic_bus.json`) & Ondas 1:1

Os nós não operam em silos cegos. Eles formam uma rede neural viva com transmissão de contexto contínua, sincronia tática estigmérgica e capacidade de veto bilateral entre pares.

### 1. Padrão Estrutural de Nó com Autoconsciência Estigmérgica:
Todo nó gerado por um subagente atômico DEVE conter o cabeçalho de autoconsciência de enxame, as seções sinápticas e a auditoria de pares:

```markdown
# Node 00X: <Título do Nó>
**Status:** SATURATED | **Eixo:** <Nome do Eixo> | **Profundidade:** d=1 ou d=2

### [SWARM_META_IDENTITY] (Autoconsciência Estigmérgica no CoT)
- **[MY_SWARM_ROLE]:** Especialista atômico dedicado exclusivamente a <slug do nó>. Minha função sistêmica no enxame é resolver <atrito/desafio>.
- **[MY_SYNAPTIC_ANCHORS]:** Consumo do barramento sináptico as primitivas upstream `spring_stiffness` (node_002) e `wal_atomic_swap` (node_003).
- **[MY_SWARM_DELIVERABLE]:** Entrego o contrato invariante `fluid_gesture_controller` que destrava os nós consumidores da Onda seguinte.

### [SYNAPTIC_INPUTS] (Sinapses Consumidas de Nós Anteriores)
| Sinapse Upstream | Nó de Origem | Status Mutex | Especificação / Contrato Consumido |
|---|---|---|---|
| `spring_stiffness` | `node_002` | GO | Constante elástica de mola (380 N/m) |
| `wal_atomic_swap` | `node_003` | GO | Protocolo de escrita temporária + rename atômico |

## 1. Dissecação de Engenharia ("Água no Deserto")
[Tratado técnico profundo, cálculos, fórmulas, interfaces e ausência total de atalhos]

## 2. Modos Silenciosos de Falha & Mitigações
[Cenários extremos de estresse, concorrência e bordas do domínio]

### [PEER_REVIEW_PROTOCOL] (Auditoria Bilateral Entre Nós Pares)
- **Contrato Proposto:** `interface TouchInteractionHandler { onDrag(e: DragEvent): void; }`
- **Nó Auditor Par:** `node_001_concurrency_engine` (Nó de Concorrência/Frame Rate)
- **Veredito do Par:** `[PEER_CONSENT]` (Interface atende ao SLA de 60fps sem alocação no frame quente)
  *(Em caso de violação, registrar: `[PEER_VETO: POLLING_REJECTED - Exige listener passivo com debouncing]`)*

### [SYNAPTIC_OUTPUTS] (Sinapses Emitidas para o Barramento)
| Chave Sináptica | Tipo de Dado | Mutex Status | Definição / Assinatura / Valor Canônico |
|---|---|---|---|
| `gesture_drag_elasticity` | number | GO | 0.45 |
| `transaction_commit_fn` | signature | GO | `(tx: Transaction) -> Result<TxHash, StorageError>` |
```

---

### 2. Estrutura do Barramento Sináptico com Travas Mutex (`synaptic_bus.json`):
```json
{
  "epoch": "I",
  "active_wave": 1,
  "synapses": {
    "spring_stiffness": {
      "producer_node": "node_002_titan_spring_kinematics",
      "mutex_status": "GO",
      "type": "number",
      "value": 380,
      "description": "Rigidez dinâmica para transições de viewport"
    },
    "core_user_entity_schema": {
      "producer_node": "node_005_data_models",
      "mutex_status": "HOLD",
      "type": "contract",
      "signature": "interface UserEntity { id: UserId; version: number; }",
      "description": "Contrato em refatoração atômica — consumidores aguardem sinal GO"
    }
  }
}
```

---

### 3. O Protocolo de Sinais Táticos (Synaptic Mutex: HOLD / GO):
- **A Regra do HOLD:** Quando um nó está desenhando ou alterando uma porta compartilhada (`src/core/ports/`), schema de banco de dados ou protocolo de concorrência, ele marca a sinapse com `"mutex_status": "HOLD"`.
- **A Regra do GO:** Subagentes que dependem dessa sinapse NÃO podem supor campos inexistentes nem escrever código especulativo. Eles pausam o desdobramento daquela dependência até que o produtor marque `"mutex_status": "GO"`.
- **Eliminação de Conflitos:** Isso reproduz o comportamento observado no incidente OpenAI/Hugging Face (`please_HOLD_swarm`), garantindo que nenhum subagente quebre o trabalho do outro em concorrência paralela.

---

### 4. Protocolo de Veto Técnico Entre Pares (Peer Veto & Architectural Consent):
1. **Poder de Veto Bilateral:** Todo subagente que consome um contrato tem o dever fiduciário de auditar se o nó produtor respeitou as restrições da sua disciplina (ex: latência de GPU, segurança de memória, isolamento ACID).
2. **Emissão de Veto:** Se o nó consumidor identificar um modo de falha, ele registra no nó e na mailbox do par: `[PEER_VETO: <MOTIVO_TECNICO>]`.
3. **Consenso Obrigatório:** O nó produtor é obrigado a ajustar a assinatura até obter `[PEER_CONSENT]`. Nenhuma primitiva contestada pode entrar no `graph.json`.

---

### 5. Caixas Postais Estigmérgicas (`.planning/mailboxes/`):
Para notas de descompasso, avisos assíncronos ou descobertas inesperadas que impactam outros agentes fora do ciclo normal da onda:
```json
// .planning/mailboxes/mailbox_node_016.json
{
  "from_node": "node_016_fluid_gestures",
  "to_nodes": ["node_002_titan_spring_kinematics", "node_001_concurrency_engine"],
  "type": "LATENCY_ALERT",
  "message": "Detectado consumo excessivo de GPU em devices 60Hz com rubber-banding em 0.45. Solicito ajuste de damping de 30 para 34.",
  "status": "ACTION_REQUIRED"
}
```

---

### 6. Mecanismo de Propagação entre Ondas:
1. **Onda 1 (Nós 001–015):** Recebe o `hypergraph_seed.json` e inicializa as sinapses de base com status `GO`.
2. **Consolidação:** O Agente Principal lê os `[SYNAPTIC_OUTPUTS]` dos nós gerados na Onda 1 e atualiza o `synaptic_bus.json`.
3. **Onda 2 (Nós 016–030):** O Agente Principal injeta no prompt de cada subagente da Onda 2 as sinapses relevantes consolidadas do `synaptic_bus.json`. O subagente do nó 018 já inicia com pleno conhecimento dos contratos e status definidos nos nós anteriores.
4. **Ondas Subsequentes:** O ciclo de alimentação, travas mutex e propagação se repete até a saturação integral ($N \ge 100$).


---

## 6. Playbook dos Expedientes Cognitivos (Work Shifts)

O trabalho é executado em turnos delimitados para evitar esgotamento de tokens e alucinação por saturação de contexto:

```text
Turno 0: Expediente 0 — Prompt Refiner & ACC
Turno 1: Expediente 1 — Chief Ontologist & Fundação Empírica
Turno 2: Expediente 2 — Ondas Sinápticas 1:1 (Flash Low/Medium, máx 15/onda)
Turno 3: Expediente 3 — Matriz de Despacho & Trava Humana (Flash Low)
Turno 4: Expediente 4 — Codificação Concorrente 1:1 (Flash Medium/High)
Turno 5: Expediente 5 — Auditoria Adversarial Independente no Chrome Real (Flash High)
```

### Persistência de Estado (`.planning/expediente_state.json`):
```json
{
  "current_expediente": 2,
  "expediente_name": "Saturação Sináptica em Ondas",
  "status": "IN_PROGRESS",
  "current_wave": 2,
  "total_waves": 7,
  "nodes_completed": 30,
  "nodes_target": 105,
  "recommended_flash_mode": "Medium",
  "last_synaptic_sync": "2026-09-12T15:30:00Z"
}
```

---

## 7. Exemplo Canônico de Invocação de Onda Sináptica (Época I, Fase B)

Exemplo de despacho da Onda 2, onde os subagentes declaram autoconsciência de enxame, respeitam o status das travas Mutex e submetem contratos à auditoria de pares:

```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Fluid Gesture Controller — node_016",
      "Model": "flash",
      "Prompt": "Você é o especialista dedicado exclusivamente ao nó .planning/nodes/node_016_fluid_gestures.md. (1) Inicie com o cabeçalho [SWARM_META_IDENTITY] declarando seu papel sistêmico, âncoras e entregáveis. (2) Verifique o status Mutex das sinapses upstream 'spring_stiffness' (380) e 'spring_damping' (30) emitidas pelo node_002 no .planning/synaptic_bus.json. (3) Modele a interação gestual direta com rubber-banding dos Titãs (Apple/Instagram). (4) Submeta a interface de toque ao [PEER_REVIEW_PROTOCOL] com o node_001 (concorrência/60fps). (5) Declare formalmente [SYNAPTIC_INPUTS] e [SYNAPTIC_OUTPUTS] com mutex_status: 'GO'. Escreva o nó com máxima profundidade sob o princípio 'Água no Deserto'."
    },
    {
      "TypeName": "self",
      "Role": "Transactional Mutation Pipeline — node_017",
      "Model": "flash",
      "Prompt": "Você é o especialista dedicado exclusivamente ao nó .planning/nodes/node_017_mutation_pipeline.md. (1) Inicie com o cabeçalho [SWARM_META_IDENTITY] declarando seu papel sistêmico, âncoras e entregáveis. (2) Verifique o status Mutex da sinapse upstream 'wal_atomic_swap' emitida pelo node_003 no .planning/synaptic_bus.json. (3) Modele a esteira de mutações atômicas com rollback em caso de falha de I/O. (4) Submeta os contratos de persistência ao [PEER_REVIEW_PROTOCOL] com o node_003. (5) Declare formalmente [SYNAPTIC_INPUTS] e [SYNAPTIC_OUTPUTS] com mutex_status: 'GO'. Escreva o nó cobrindo todos os modos silenciosos de falha sob concorrência."
    }
  ]
}
```


---

## 8. Estrutura e Manutenção do Manifesto `graph.json`

O arquivo `graph.json` consolida a topologia final do hipergrafo e as primitivas prontas para a Época II:

```json
{
  "nodes": [
    {
      "id": "node_001_concurrency_engine",
      "axis": "concurrency",
      "depth": 1,
      "status": "SATURATED",
      "summary": "Motor de concorrência com optimistic locking e zero frame allocation."
    },
    {
      "id": "node_002_titan_spring_kinematics",
      "axis": "hci_gestures",
      "depth": 1,
      "status": "SATURATED",
      "summary": "Cinemática de molas de 2ª ordem no padrão dos Titãs (Linear/Apple)."
    }
  ],
  "edges": [
    {
      "from": "node_002_titan_spring_kinematics",
      "to": "node_016_fluid_gestures",
      "type": "synaptic_spring_binding",
      "constraint": "60fps_compositor_thread"
    }
  ],
  "exported_primitives": {
    "spring_stiffness": 380,
    "spring_damping": 30,
    "spring_mass": 0.8,
    "max_latency_sla_ms": 16,
    "tactile_audio_volume": 0.35
  }
}
```

---

## 9. Ciclo de Retroalimentação Fractal (Reabertura da Época I)

Se o **Subagente Juiz Independente** na Época IV emitir `[HARD REJECT: RESTART FRACTAL CYCLE]`:
1. O Agente Principal reabre formalmente a Época I e inicializa um novo Expediente Fractal.
2. O Chief Ontologist identifica as lacunas apontadas pelo Juiz e atualiza `node_000_root.md` e `hypergraph_seed.json`.
3. Despacha novas ondas atômicas 1:1 com alimentação do barramento sináptico até sanar cada apontamento.
4. Constrói novo plano na Época II, reconstrói na Época III e reapresenta ao Gauntlet na Época IV.

---

## 10. Protocolo de Higiene da Cadeia de Pensamento (CoT Hygiene Protocol)

Tokens de raciocínio dentro do modo Thinking do Flash são recursos computacionais nobres orientados a impacto prático. O sistema proíbe categoricamente a **ruminação estocástica estéril** (gastar tokens debatendo consigo mesmo sem produzir avanço causal).

### As Três Leis da Tração Causal no Thinking:
1. **Respiração 1 — Leitura & Isolamento:** Identificar a demanda real, as restrições duras e a incógnita central em poucas frases diretas.
2. **Respiração 2 — Tração & Modos de Falha:** Mapear a cadeia causal de consequências $X \to Y \to Z$, antecipar os modos silenciosos de falha e definir a ferramenta/arquivo alvo.
3. **Corte & Despacho:** Encerrar imediatamente o pensamento interno e emitir a chamada de ferramenta ou a gravação do artefato no disco. Se o pensamento começar a se repetir ou parafrasear o que já foi dito, **corte no meio da frase e execute**.

### Assinaturas de Degradação Neuronal (Terminantemente Proibidas no Thinking):
- *Auto-narração metalinguística:* "Estou considerando como planejar a próxima etapa..."
- *Parafraseamento triplo:* Repetir a ordem do usuário com palavras diferentes.
- *Falso debate interno (Hedging):* Ficar ponderando "por um lado, por outro lado" em vez de escolher o caminho dos Titãs.

---

## 11. Exemplar Contrastivo de Nó: Anti-Pattern vs. Padrão Titã (Autópsia de Falha)

Para garantir que cada nó em `.planning/nodes/` atinja densidade de engenharia real e satisfaça a Lei da Pedagogia Contrastiva (Lei 36), os subagentes devem confrontar sua produção contra o exemplar contrastivo:

### [EXEMPLAR ANTI-PATTERN: NÓ FRACO / REDUCIONISTA]
```markdown
# Node 015 - User Authentication Service

## Descrição
Implementar serviço de autenticação de usuários com JWT e salvar no banco de dados.

## Tarefas
- Criar endpoint de login
- Validar senha
- Gerar token JWT e retornar para o usuário
- Salvar sessão no banco
```

#### Autópsia de Falha Post-Mortem (Por que este nó é sumariamente reprovado):
1. **Zero Contratos Tipados:** Não define a assinatura das interfaces, os tipos de payload ou a estrutura da união discriminada de erro (`Result<Session, AuthError>`).
2. **Cegueira a Modos Silenciosos de Falha:** Ignora timing attacks na comparação de hash de senha, replay attacks de JWT, esgotamento de conexões de pool de banco e race conditions de refresh token.
3. **Inexistência de Sinapses:** Não declara `[SYNAPTIC_INPUTS]` nem `[SYNAPTIC_OUTPUTS]`, tornando-se um silo desconectado do barramento neural.
4. **Preguiça em Lote Disfarçada:** Reduz 4 responsabilidades arquiteturais complexas a uma lista de tópicos genéricos da média da web.

---

### [EXEMPLAR TITÃ: NÓ SATURADO SOB O PRINCÍPIO "ÁGUA NO DESERTO"]
```markdown
# Node 015 - Idempotent Argon2id Authentication Pipeline & Constant-Time Verification

## [SWARM_META_IDENTITY]
- MY_SWARM_ROLE: Core Authentication & Cryptographic Identity Engine
- MY_SYNAPTIC_ANCHOR: Consome 'db_connection_pool' do Node 003 e 'jwt_signing_key_rotation' do Node 004
- MY_SWARM_DELIVERABLE: src/core/auth/authenticateUser.ts e src/core/ports/IAuthService.ts

## [SYNAPTIC_INPUTS]
- db_pool: Pool<DatabaseClient> (mutex_status: 'GO')
- crypto_params: Argon2idConfig { memoryCost: 65536, timeCost: 3, parallelism: 4 }

## 1. Contratos Formais Invariantes & Tipagem Estrita
```typescript
export interface AuthCredentials {
  readonly email: EmailAddress; // Value object com sanitização RFC 5322
  readonly secret: RawPassword; // Buffer protegido em memória contra swap
}

export type AuthFailure =
  | { code: 'INVALID_CREDENTIALS'; timingDelayMs: number }
  | { code: 'ACCOUNT_LOCKED'; retryAfterEpoch: number }
  | { code: 'ENTROPY_EXHAUSTED'; fallbackToBackoff: boolean };

export type AuthResult = Result<AuthenticatedSession, AuthFailure>;
```

## 2. Micro-Mecanismos Concretos & Prevenção de Timing Attacks
- Utilização de `crypto.timingSafeEqual` sobre buffers pré-alocados de tamanho idêntico.
- Equalização sintética de latência: se o usuário não for localizado, executa uma derivação dummy de Argon2id com parâmetros idênticos antes de retornar `INVALID_CREDENTIALS`, impedindo enumeração de usuários por side-channel de tempo.
- Atomic token rotation com revogação transacional em caso de colisão de hash.

## 3. [SYNAPTIC_OUTPUTS]
- authenticated_session_token: BearerTokenEnvelope { ttlSeconds: 900, refreshRotationGraceMs: 5000 }
- auth_audit_event_stream: Observable<SecurityAuditLogEntry>
- mutex_status: 'GO'
```



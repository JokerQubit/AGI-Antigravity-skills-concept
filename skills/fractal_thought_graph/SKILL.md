---
name: fractal_thought_graph
description: "Hyper-Cortex v6.0 Project Neural Map & Lean Modular Thought Graph. Use when creating or refreshing .planning/project_neural_map.json and PROJECT_NEURAL_MAP.md (architecture topology, API/type contracts, dependency graph, ADRs, anti-pattern registry), decomposing Architectural missions into a 3-7 node Lean Modular Graph in .planning/nodes/, compiling Epoch II implementation_plan.md dispatch matrices, or reopening Epoch I after a Gauntlet [HARD REJECT]."
---

# Fractal Thought Graph & Project Neural Map Playbook — v6.0

Manual operacional do substrato cognitivo persistido em disco (`.planning/`). Governa dois pilares críticos do **Hyper-Cortex v6.0**:
1. **O Mapa Neural de Elite do Projeto (`.planning/project_neural_map.json` + `PROJECT_NEURAL_MAP.md`)** — memória viva anti-amnésia obrigatória em **100% das missões**.
2. **A Bifurcação de Planejamento Estrutural:** **Grafo Modular Denso (3 a 7 nós ricos, âncora áurea em 5 nós)** no Modo Arquitetural vs. **Zero nós em disco (`nodes_floor: 0`)** no Modo Direto.

> **SSOT & Cross-References:** Classificação de modo e Dossiê residem em [`universal_prompt_refiner`](../universal_prompt_refiner/SKILL.md). Fórmulas de ToT ($A^*$), GoT ($\mathcal{F}_{\text{fuse}}$) e `thought_graph.json` residem em [`dynamic_thought_router`](../dynamic_thought_router/SKILL.md). Schema completo do `synaptic_bus.json`, contratos em 5 fases e execução `/swarm` residem em [`swarm_orchestration`](../swarm_orchestration/SKILL.md). Hierarquia de modelos e Quota Brake $\le 10\%$ residem em [`adaptive_token_governance`](../adaptive_token_governance/SKILL.md).

---

## 1. Padrão de Elite do Project Neural Map (Lei 47 — Anti-Amnesia Invariant)

Todo repositório ativo mantém dois artefatos sincronizados: `.planning/project_neural_map.json` (máquina) e `PROJECT_NEURAL_MAP.md` (leitura humana e onboarding rápido). Encerrar ou mutar subsistemas sem consultar e atualizar o mapa dispara `[HARD REJECT: PROJECT_AMNESIA_DRIFT]`.

### 1.1. Os 6 Domínios Obrigatórios do Mapa Neural
| Seção | Conteúdo Exigido (Zero Generalidades) |
|---|---|
| **1. Architecture Topology** | Camadas (Domain, Ports, Adapters, UI, Kernel), bounded contexts, entrypoints reais, boundaries de processo/thread e runtime alvo (Web, Rust, Lua/DX9, etc.). |
| **2. API & Type Contracts** | Interfaces públicas exportadas, uniões discriminadas `Result<T, E>`, schemas JSON/SQL, eventos IPC/HTTP e invariantes de mutação/locks. |
| **3. Dependency Graph** | Arestas `module -> dependency` internas, pacotes externos críticos, recursos compartilhados com contenção (`synaptic_bus.json`, WAL, portas TCP). |
| **4. ADR Decisions** | Registro conciso de *Architecture Decision Records* (`ADR-001...`): contexto, decisão adotada, alternativas descartadas e consequências/trade-offs. |
| **5. Failure & Anti-Pattern Registry** | Falhas já encontradas no projeto, armadilhas de SO/runtime (ex: Win32 `EBUSY`, `EADDRINUSE`, hydration mismatch) e padrões explicitamente banidos. |
| **6. Refresh Metadata & Triggers** | Timestamp ISO-8601, commit SHA base, cobertura verificada e dono da última atualização. |

### 1.2. Schema Canônico (`.planning/project_neural_map.json`)
```json
{
  "map_version": "6.0.0",
  "project_name": "<repo_name>",
  "updated_at": "2026-11-19T13:40:00Z",
  "base_commit": "<git_sha>",
  "architecture_topology": {
    "runtime_stack": ["TypeScript", "Node.js", "React"],
    "layers": [
      { "name": "core/domain", "path": "src/core/domain", "responsibility": "Entidades puras e Result<T,E>", "dependencies": [] },
      { "name": "adapters/infra", "path": "src/adapters/infra", "responsibility": "AtomicSwap, FsLockEngine, SQLite WAL", "dependencies": ["core/domain"] }
    ],
    "entrypoints": ["src/main.ts"]
  },
  "api_and_type_contracts": [
    {
      "contract_id": "IStoragePort",
      "file": "src/core/ports/IStoragePort.ts",
      "signature": "saveAtomic(key: string, payload: Uint8Array): Promise<Result<void, StorageError>>",
      "invariants": ["SHA-256 pre/post swap", "O_CREAT|O_EXCL lock"]
    }
  ],
  "dependency_graph": {
    "edges": [
      { "from": "src/adapters/infra/sqliteStore.ts", "to": "src/core/ports/IStoragePort.ts", "kind": "implements" }
    ],
    "shared_resources": ["data/app.db", ".planning/synaptic_bus.json"]
  },
  "adr_decisions": [
    {
      "id": "ADR-001",
      "title": "WAL por domínio + AtomicSwap para snapshots",
      "status": "ACCEPTED",
      "decision": "Isolar escrita WAL e usar staging .tmp + fsync + rename.",
      "rejected": ["JSON compartilhado sem lock (EBUSY em NTFS)"]
    }
  ],
  "failure_and_antipattern_registry": [
    {
      "id": "FAIL-001",
      "symptom": "EBUSY ao sobrescrever config em workers paralelos no Windows",
      "root_cause": "Escrita concorrente sem FsLockEngine e rename no mesmo volume",
      "banned_pattern": "fs.writeFileSync direto em arquivo compartilhado"
    }
  ]
}
```

### 1.3. Gatilhos Obrigatórios de Auto-Refresh
1. **Step 0 (Leitura Obrigatória):** Prompt Refiner e qualquer worker leem `project_neural_map.json` antes de planejar ou editar. Se não existir no repositório, sua criação é o primeiro passo estrutural.
2. **Refresh Incremental Obrigatório:** Atualiza-se ambos (`project_neural_map.json` + `PROJECT_NEURAL_MAP.md`) sempre que: (a) um novo módulo, porta ou rota é criado; (b) uma assinatura pública ou schema muda; (c) uma decisão arquitetural (ADR) é tomada; (d) um bug novo revela um modo de falha reutilizável; ou (e) antes do sign-off da Época IV e commit no GitHub.

---

## 2. Topologia Física no Disco (`.planning/`) & Bifurcação de Modo

```text
.planning/
├── project_neural_map.json     # [SEMPRE] Mapa Neural Estrutural (máquina)
├── mission_dossier.md          # [Época 0] Dossiê Executivo do Prompt Refiner
├── refiner_seal.json           # [Época 0] Selo Estigmérgico do Turno
├── synaptic_bus.json           # [Enxame] Barramento neural, contratos 5 fases e engramas
├── thought_graph.json          # [Router] Topologia ativa (LCS / ToT / GoT / DAS)
├── expediente_state.json       # [Shifts] Estado do expediente e checkpoint de quota
├── ledger/                     # [Sempre] State Ledger append-only (txn_XXXX.json)
├── post_mortem/                # [Pós-Época IV] Telemetria fria pm_<session>.json
├── graph.json                  # [MODO ARQUITETURAL APENAS] Manifesto consolidado de nós/arestas
├── hypergraph_seed.json        # [MODO ARQUITETURAL APENAS] Semente dos 3-7 nós densos
└── nodes/                      # [MODO ARQUITETURAL APENAS] 3 a 7 nós ricos (padrão áureo = 5)
    ├── node_000_root.md
    ├── node_001_domain_ports.md
    ├── node_002_storage_infra.md
    ├── node_003_concurrency_kernel.md
    ├── node_004_ui_perceptual_craft.md
    └── node_005_audit_contracts.md
```
*(No root do repositório ou em `.planning/`: manter `PROJECT_NEURAL_MAP.md` sincronizado com `project_neural_map.json`.)*

> **Regra de Ouro do Modo Direto:** Se `mission_type == "DIRECT_OPERATIONAL"`, `.planning/nodes/`, `node_000_root.md`, `hypergraph_seed.json` e `graph.json` **NÃO são criados** (`nodes_floor: 0`). O plano vai direto para `implementation_plan.md` e a execução roda via **Artífice Autônomo Fim-a-Fim** (`TypeName: "self"`).

---

## 3. Época I: Chief Ontologist (Modo Arquitetural) & Grafo Modular Denso (3–7 Nós)

Em missões `ARCHITECTURAL`, o **Chief Ontologist** (`gemini-4-neon-high`) consome o `project_neural_map.json` e o `mission_dossier.md`, varre empiricamente o código existente e decompõe o sistema em **3 a 7 nós densos** (âncora em **5 nós**) cobrindo os **8 Eixos Ontológicos Nativos**:
1. *Domain Logic & Business Invariants* (`Result<T,E>`, máquinas de estado)
2. *Data Contracts & Atomic Persistence* (schemas, WAL, `DeterministicAtomicSwap`)
3. *Concurrency & Real-Time Synchronization* (`FsLockEngine`, filas lock-free, zero alocação em frame quente)
4. *HCI, Gestures & Spring Kinematics* (molas 2ª ordem, 60fps/120Hz)
5. *Specular Visuals & Photorealistic Micro-Assets* (`generate_image`, zero SVG genérico/emoji)
6. *Physical Acoustic Foley & Micro-Audio* (`scripts/sfx_tool.py` CC0, Spatial HRTF)
7. *Silent Failure Modes & Chaos Engineering* (desconexões, Win32 `EBUSY`, pressão de memória)
8. *Forensic Telemetry & Auditable State Trails* (logs estruturados, zero erros de console)

### 3.1. Anatomia Obrigatória de Cada Nó Denso (`node_00X_<slug>.md`)
Cada nó equivale a dezenas de nós fragmentados pela densidade técnica (*"Água no Deserto"*):
- **`[SWARM_META_IDENTITY]`:** `[MY_SWARM_ROLE]`, `[MY_SYNAPTIC_ANCHOR]`, `[MY_SWARM_DELIVERABLE]`.
- **`[SYNAPTIC_INPUTS]` & `[SYNAPTIC_OUTPUTS]`:** Contratos consumidos e emitidos no `synaptic_bus.json`.
- **Contratos Tipados & Micro-Mecanismos:** Assinaturas exatas `Result<T,E>`, algoritmos concretos, zero pseudo-código vago.
- **Modos Silenciosos de Falha & Pre-Mortem T+12 Meses:** Cenários de corrida, *timing attacks*, leaks e mitigações.
- **`[PEER_REVIEW_PROTOCOL]`:** Validação bilateral com nós pares (`[PEER_CONSENT]` ou `[PEER_VETO]`).
- **Checklist Forense Binário `[0 | 1]`:** Critérios objetivos verificáveis na Época IV.

### 3.2. Manifesto `graph.json`
Consolida `nodes[]` (com `id`, `axis`, `status: "SATURATED"`, `target_files[]`, `checklist_ref`), `edges[]` (dependências tipadas entre nós) e `exported_primitives{}` (constantes calibradas como `spring_stiffness`, `max_latency_sla_ms`).

---

## 4. Época II: Matriz Neural de Despacho (`implementation_plan.md`)

Emitida antes da Época III com `RequestFeedback: true` para aprovação humana única (`"Proceed"`):
1. **Matriz 1:1 Nó/Arquivo vs. Worker/Artífice:** `FileSet` estritamente disjuntos, modelo atribuído (`gemini-4-hydrogen-high` / `gemini-4-hydrogen-xhigh` / `gemini-4-neon-high`) e dependências.
2. **Mapa de Contratos Sinápticos:** Todos os contratos estruturais em `CONTRACT_STABLE` (zero `DRAFT`/`VERIFYING` restantes).
3. **Checklists Forenses Binários:** Critérios específicos por alvo (zero-stub, tipagem, stack completa Lei 51, digital twin Lei 52, causalidade Lei 53).
4. **Sequenciamento de Handoffs & Backup Git:** Ordem das ondas, proporção de verificadores (1 verificador para 2–4 autores) e ponto de backup via `github_sovereign_workflow`.

---

## 5. Ciclo de Retroalimentação Fractal & Higiene de CoT

- **Reabertura da Época I:** Se o Juiz Red Team emitir `[HARD REJECT: RESTART FRACTAL CYCLE]` na Época IV, atualize `project_neural_map.json` (registrando a falha), ajuste `node_000_root.md` / `hypergraph_seed.json`, sature apenas os nós afetados e reapresente ao Gauntlet.
- **Higiene do Chain-of-Thought:** Proibida ruminação circular ou auto-narração (*"Estou considerando..."*). Cada ciclo de pensamento segue: **Isolar incógnita $\to$ Traçar causa e modo de falha ($X \to Y \to Z$) $\to$ Executar ferramenta no disco**.
- **Exemplar Contrastivo de Nó:**
  - *Fraco (Reprovado):* `"Node 015 - Auth: criar login, validar senha e gerar JWT"` (sem tipos `Result`, sem timing-safe compare, sem sinapses).
  - *Titã (Aprovado):* `"Node 015 - Argon2id Constant-Time Auth"` com `AuthCredentials`, `AuthFailure` discriminado, `crypto.timingSafeEqual` + dummy Argon2id anti-enumeração, `[SYNAPTIC_INPUTS/OUTPUTS]` e checklist binário.

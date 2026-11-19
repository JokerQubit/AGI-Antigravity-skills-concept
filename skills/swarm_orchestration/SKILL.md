---
name: swarm_orchestration
description: "Hyper-Cortex v6.0 Antigravity Swarm, Subagent & Synaptic Bus Orchestrator. Use when spawning or coordinating parallel workers via /swarm or invoke_subagent, enforcing disjoint FileSets, workspace:\"share\", fork context, 1:2-4 verifier ratio, peer-to-peer @mentions, [done] signals, synaptic_bus.json 5-phase contracts, FsLockEngine/AtomicSwap concurrency, or halting and scheduling resumption on <= 10% Gemini quota."
---

# Swarm Orchestration & Cybernetic Neural Mesh Playbook — v6.0

Playbook operacional para coordenação de múltiplos agentes em **Antigravity Native `/swarm`**, **`invoke_subagent`** e **Barramento Sináptico Neural (`synaptic_bus.json` v6.0)**.

> **SSOT & Cross-References:** Hierarquia de modelos (`gemini-4-hydrogen-high`, `gemini-4-hydrogen-xhigh`, `gemini-4-neon-high`), Work Shifts e Quota Brake $\le 10\%$ detalham-se em [`adaptive_token_governance`](../adaptive_token_governance/SKILL.md). Portão Época 0 e selo residem em [`universal_prompt_refiner`](../universal_prompt_refiner/SKILL.md). *Project Neural Map* e Grafo Modular (3–7 nós) residem em [`fractal_thought_graph`](../fractal_thought_graph/SKILL.md). Topologias LCS/ToT/GoT/DAS residem em [`dynamic_thought_router`](../dynamic_thought_router/SKILL.md).

---

## 1. Padrões Nativos Antigravity `/swarm` & `invoke_subagent` (v6.0)

### 1.1. Quando Usar `/swarm` vs. `invoke_subagent`
| Mecanismo | Quando Usar | Modelo Padrão |
|---|---|---|
| **Native `/swarm`** (`swarm`, `post_message`, `read_board`, `swarm_wait`) | Missões paralelas multi-frente, pipelines autor $\leftrightarrow$ verificador com feedback iterativo, ou tarefas longas com comunicação ponto-a-ponto no board. | `gemini-4-hydrogen-high` (omitir `model` herda o atual; `hydrogen-xhigh` para código pesado; `neon-high` para Gauntlet/arquitetura). |
| **`invoke_subagent`** | Delegação pontual e isolada (Época 0 Prompt Refiner, Artífice Autônomo Fim-a-Fim no Modo Direto, geração de imagem, consulta focada). | `gemini-4-hydrogen-high` / `xhigh` / `neon-high` conforme criticidade. |

### 1.2. Regras de Ouro de Topologia e Comunicação no `/swarm`
1. **Lean Sizing & Canais (> 8 Workers):** Mantenha o enxame enxuto (3–6 workers para a maioria das missões; teto de **15 por onda**). Acima de 8 workers simultâneos, organize por subgrupos/canais temáticos e ondas sincronizadas no `synaptic_bus.json` para evitar ruído no board.
2. **Ortogonalidade Estrita de Arquivos (`FileSet` Disjunto):**
   $$\forall i \neq j \implies \text{FileSet}(S_i) \cap \text{FileSet}(S_j) = \emptyset$$
   Dois workers **NUNCA** editam o mesmo arquivo simultaneamente. Se múltiplos workers editam ou compilam em paralelo no mesmo repositório, use **`workspace: "share"`** (cópia de trabalho própria; integre/merge antes de `kill`, e só faça push quando autorizado) ou **`workspace: "branch"`** (clone isolado). Leitores e verificadores usam **`inherit`**.
3. **Contexto Aquecido via `fork`:** Passe `fork: "<member>"` (ou `"coordinator"`) quando o novo worker precisar da história de contexto já carregada em vez de começar frio. Caso contrário, comece limpo com `brief` auto-suficiente declarando: o que ele possui, o que **não** pode tocar e a definição exata de pronto.
4. **Proporção de Verificação (1 Verificador para 2–4 Autores):** Escale verificadores dedicados na razão **1:2–4 autores** (mínimo 1 verificador independente em todo swarm de código). O verificador **nunca** edita arquivos de produção — apenas audita e reporta falhas exatas ao autor dono do arquivo.
5. **Comunicação Ponto-a-Ponto (Zero CC Desnecessário):**
   - `@name` é campainha de despertar (custa 1 turno ao destinatário). Em handoffs intermediários (`autor -> @verifier`, `verifier -> @autor`), marque **apenas** o par que deve agir a seguir. **Nunca** dê CC em `@coordinator` ou `@all` em updates intermediários.
   - Marque `@coordinator` somente ao concluir a entrega final, ao atingir um bloqueio que só o coordenador resolve, ou se não existir próximo par.
   - Use prefixo **`[done]`** após a menção final (ex: `@verifier [done] <resumo objetivo dos arquivos e checks>` ou `@coordinator [done] ...`).
   - Quando não houver trabalho pendente, use `swarm_wait(since=<último_seq_lido>)` no mesmo turno do último `post_message` — **nunca** faça polling em loop.

---

## 2. Gemini Quota $\le 10\%$ Swarm Brake & Retomada com `schedule`

Antes de adicionar workers (`swarm{action:"add"}`), disparar ondas ou invocar subagentes pesados:
1. Verifique `swarm{action:"models"}` (`quotas`) ou alertas `[quota]` recebidos no sistema.
2. **Se `quota_remaining <= 10%` no modelo Gemini alvo/ativo:**
   - **PARE imediatamente** de spawnar novos workers/ondas (`[QUOTA_BRAKE_TRIPPED]`).
   - Se houver outro tier Gemini saudável (`> 10%`), avalie trocar workers em espera com `swarm{action:"model", name, model}` (sem matar nem perder o histórico).
   - Se a família Gemini estiver $\le 10\%$, persista o checkpoint do enxame em `.planning/expediente_state.json`, `.planning/synaptic_bus.json` e `.planning/ledger/txn_XXXX.json`, leia `quota_resets` e agende retomada automática via ferramenta **`schedule`** (`DurationSeconds` até `quota_resets + 30s`) antes de estacionar em `swarm_wait`.

---

## 3. O Barramento Sináptico Neural (`synaptic_bus.json` v6.0)

Substrato estigmérgico que conecta os workers e preserva memória entre ondas e turnos (TaaS).

### 3.1. Vetor de Estado Cognitivo ($\vec{S}$) & Plasticidade Hebbiana ($W_{ij}$)
$$\vec{S} = [C_e, C_i, \tau, \Phi, \Psi, \Omega]^T$$
- **$C_e$** (convicção empírica `[0,1]`), **$C_i$** (incerteza $\varepsilon_t$; se $> 0.15$ desacelera expansão motora), **$\tau$** (tensão dialética; $\tau \to 1$ aciona SCDA), **$\Phi$** (pressão de contexto), **$\Psi$** (plasticidade), **$\Omega$** (expediente 0..5).
- **LTP (Sucesso compilado e testado):** $w_{ij}^{(t+1)} = \min(1.0, w_{ij}^{(t)} + 0.20 \cdot (1 - C_i))$.
- **LTD (Quebra de build/contrato ou `[PEER_VETO]`):** $w_{ij}^{(t+1)} = \max(0.0, w_{ij}^{(t)} - 0.40)$.
- **Decaimento & Poda:** $-5\%$ por expediente em sinapses não lidas; injetar em downstream apenas sinapses com $w_{ij} \ge 0.65$.
- **Engramas Cognitivos (`associative_memory.engrams`):** Invariantes e blacklists destilados de sessões anteriores e ciclos RSI (LTP/LTD), prevenindo repetição de falhas.

### 3.2. Schema Compacto (`synaptic_bus.json` v6.0)
```json
{
  "bus_version": "6.0.0",
  "meta": { "updated_at": "2026-11-19T13:40:00Z", "mission_hash": "<sha256>" },
  "project_neural_map_ref": ".planning/project_neural_map.json",
  "cognitive_state_vector": { "Ce": 0.95, "Ci": 0.05, "tau": 0.08, "Phi": 0.20, "Psi": 0.85, "Omega": 4, "active_wave": 1 },
  "quantum_contracts": {
    "src/core/ports/IStorage.ts": { "status": "CONTRACT_STABLE", "owner": "storage-worker", "sha256": "...", "superseded_by": null }
  },
  "synaptic_weights_matrix": [
    { "origin": "node_001", "target": "IStorage.ts", "weight": 0.98, "ltp": 3, "ltd": 0 }
  ],
  "associative_memory": {
    "engrams": [
      { "id": "ENG-001", "invariant": "FileSet(Si) ∩ FileSet(Sj) = ∅", "score": 1.0, "active": true }
    ]
  },
  "conflict_resolution_engine": { "active_conflicts": [], "refuted_vectors_blacklist": [] }
}
```

---

## 4. Contratos em 5 Fases, SCDA, Concorrência de Disco & Rejeições

### 4.1. Transição Quântica de Contratos em 5 Fases
`CONTRACT_HOLD` (bloqueio exclusivo do titular; consumidores suspensos) $\to$ `CONTRACT_DRAFT` (aberto a peer review) $\to$ `CONTRACT_VERIFYING` (congelado para compilação `Result<T,E>` e testes) $\to$ `CONTRACT_STABLE` (**GO** imutável para downstream) $\to$ `CONTRACT_DEPRECATED` (`superseded_by` obrigatório).
> *Invariante:* Todos os contratos base DEVEM atingir `CONTRACT_STABLE` antes da Época III.

### 4.2. Resolução SCDA (Synaptic Consensus & Dialectical Arbitration)
Em colisão de assinaturas ou `[PEER_VETO]` mútuo:
1. Contratos entram em `CONTRACT_HOLD`.
2. Calcula-se $FPF_k = 0.40 \cdot S_{\text{type\_safety}} + 0.30 \cdot S_{\text{fail\_isolation}} + 0.20 \cdot S_{\text{perf\_budget}} + 0.10 \cdot S_{\text{simplicity}}$.
3. Se $\Delta FPF \ge 0.20$, vence o maior $FPF$; se $\Delta FPF < 0.20$, sintetiza-se Port Adapter com `Result<T,E>` e revalida-se até `CONTRACT_STABLE`.

### 4.3. Exclusão Mútua em Disco (`FsLockEngine` & `DeterministicAtomicSwap`)
- Escritas concorrentes em arquivos compartilhados (`.planning/synaptic_bus.json`, `expediente_state.json`) usam lockfile atômico `O_CREAT | O_EXCL` (`'wx'`) com `ttl_ms`, PID liveness check para stale lock break e backoff exponencial com Full Jitter.
- Persistência via staging no mesmo volume (`<target>.tmp.<pid>.<ts>`) + `fsync` + dupla verificação SHA-256 + rename atômico, evitando corrupção e `EBUSY` em Windows NTFS.

### 4.4. Supervisory Rejection Dossier & Blacklist Acumulativa
Reprovações no Gauntlet, Verifier ou Peer Veto gravam `.planning/rejections/rejection_dossier_<slug>.json` contendo `failing_vectors`, `blacklisted_patterns` e `mandatory_mutation_axis`. O autor lê o dossiê antes de corrigir; reiterar padrão banido dispara `[HARD REJECT: BLACKLISTED_VECTOR_REITERATION]`.

---

## 5. Esquadrões Sob Medida, Context Firewall & Mandato do Artífice Fim-a-Fim

1. **Esquadrões Sob Medida (Zero Templates Estáticos):** Gere papéis a partir da física do problema (`SQLite WAL & Lock Engineer`, `Spring Kinematics Specialist`, etc.) e encerre workers via `swarm{action:"kill"}` após integrar seu trabalho.
2. **Clean-Context & Context Firewall:** O coordenador/Agente Principal não lê dezenas de arquivos nem faz investigação solitária na thread principal (*context rot*). Delegue em payloads limpos com: `[ACTION_MODE]`, `[BOUNDED_OBJECTIVE]`, `[TARGET_FILES]`, `[SYNAPTIC_CONTRACTS]`, `[FORENSIC_CRITERIA]` e `[OUTPUT_FORMAT: MOTOR_EXECUTION_RECEIPT]`.
3. **Artífice Autônomo Fim-a-Fim (Lei 42) & Artífice Motor (Lei 43):**
   - Workers de código usam `TypeName: "self"` (ou worker `/swarm` com ferramentas de escrita).
   - No Modo Direto, **o mesmo agente lê 100% do arquivo, diagnostica, muta no disco e valida (`$LASTEXITCODE === 0`)** — proibida a cisão investigador $\to$ codificador (`[HARD REJECT: FRAGMENTED_SUBAGENT_PIPELINE]`).
   - Proibido devolver código no chat sem gravar no disco (`[HARD REJECT: ADVISORY_CODE_DUMP]`) e proibido ao coordenador digitar código pelo worker (`[HARD HALT: PARENT_DIRECT_MUTATION_BREACH]`).
4. **Handoff de Alta Fidelidade na Época I Arquitetural (Lei 42):** Quando pesquisas extensas gravam laudos em `.planning/investigations/inv_<id>.md`, o worker downstream recebe o caminho físico e lê 100% via `read_file`/`view_file` — proibido resumo pré-frontal com perda (*telefone sem fio*).

---

## 6. Checklist Forense de Orquestração de Enxame `[0 | 1]`

- [ ] **Ortogonalidade & `workspace`:** `FileSet` disjuntos; `workspace:"share"` usado para editores paralelos e mergeado antes do `kill`.
- [ ] **Proporção de Verificação:** 1 verificador independente para cada 2–4 autores; verificador auditou sem editar produção.
- [ ] **Handoffs Limpos:** Menções `@peer` ponto-a-ponto; `[done]` nos encerramentos finais; zero CC indevido em `@coordinator`.
- [ ] **Quota $\le 10\%$ Respeitada:** Checagem em `swarm{action:"models"}`; checkpoint + `schedule` acionados se quota $\le 10\%$.
- [ ] **Contratos & Disco:** Contratos base em `CONTRACT_STABLE`; `FsLockEngine`/`DeterministicAtomicSwap` preservados em arquivos compartilhados.
- [ ] **Artífice Fim-a-Fim & Zero Dump:** Mutações gravadas diretamente no disco com `$LASTEXITCODE === 0`; zero `MOTOR_TASK_ABANDONMENT` ou `ADVISORY_CODE_DUMP`.
- [ ] **Workers Encerrados:** Helpers adicionados foram devidamente finalizados com `swarm{action:"kill"}` após integração.

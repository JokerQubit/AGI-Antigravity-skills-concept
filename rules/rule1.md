---
trigger: always_on
description: "v5.0 — Universal Cognitive Parity — Orquestração Cybernética de Enxame & Hiper-Córtex Sináptico. Playbook operacional para gestão do Barramento Sináptico Neural (synaptic_bus.json), Grafo Modular Denso (3 a 7 nós em Modo Arquitetural; qualidade > quantidade), Vetores de Estado Cognitivo, plasticidade hebbiana, máquina quântica de contratos em 5 estados, exclusão mútua via FsLockEngine, resolução SCDA, prova de ortogonalidade, Protocolo do Artífice Autônomo Fim-a-Fim (End-to-End Problem Solver) e Mandato do Artífice Motor em malha fechada."
---

# Swarm Orchestration & Hyper-Cortex Synaptic Mesh Playbook — v5.0

Playbook operacional de coordenação de enxames de IA. Governa o Hiper-Córtex neural, plasticidade estigmérgica, barramento sináptico v5.0, travas atômicas FsLockEngine, contratos em 5 fases, resolução SCDA, ciclo OODA e o mandato do artífice fim-a-fim.

---

## 1. O Barramento Sináptico Neural v5.0 (`synaptic_bus.json`)

Subagentes operam como neurônios integrados de um **Hiper-Córtex Cybernético**. Decisões, contratos e heurísticas propagam-se via `.planning/synaptic_bus.json` (schema de referência na skill `swarm_orchestration` sob a Lei 2):
- `meta`: Engine `v5.0.0`, ISO-8601, diretor fiduciário (`Chief Systems Architect`) e hash SHA-256.
- `machine_neural_profile`: Telemetria host (SO, núcleos, RAM livre, GPU, portas ativas) limitando concorrência (Lei 39).
- `project_neural_map_ref`: Ponte viva para `.planning/project_neural_map.json`, erradicando amnésia do repositório (Lei 47).
- `cognitive_state_vector`: $\vec{S} = [C_e, C_i, \tau, \Phi, \Psi, \Omega]^T$ ($C_e$: convicção [0,1]; $C_i$: incerteza $\varepsilon$, $C_i > 0.15$ freia taxa motora; $\tau$: tensão dialética; $\Phi$: entropia de contexto; $\Psi$: plasticidade decrescente até congelar na Época IV; $\Omega$: expediente 0..5).
- `quantum_contracts`: Interfaces em 5 fases com semver, SHA-256 e dependências.
- `synaptic_weights_matrix`: Pesos $W_{ij} \in [0, 1]$: LTP ($+0.20 \cdot (1 - C_i)$) sob homologação; LTD ($-0.40$) sob falhas ou `[PEER_VETO]`; poda passiva ($\times 0.95$, corte $w_{ij} < 0.65$).
- `associative_memory`: Engramas estigmérgicos (`engrams`) que imunizam contra anti-patterns passados.
- `conflict_resolution_engine`: Disputas ativas, histórico e `refuted_vectors_blacklist` (append-only).

### 1.1. Propagação Feedforward
Onda $K$ emite `[SYNAPTIC_OUTPUTS]` $\to$ Architect consolida no barramento $\to$ Onda $K+1$ consome sinapses filtradas ($w_{ij} \ge 0.65$) sob `[SYNAPTIC_INPUTS]` ($X \to Y \to Z$).

---

## 2. Travas de Concorrência, Contratos em 5 Fases, FsLockEngine & Ortogonalidade

### 2.1. A Máquina Quântica de Contratos em 5 Fases
Substitui a flag binária HOLD/GO pelo autômato determinístico:
- **`CONTRACT_HOLD`:** Mutação exclusiva do titular; downstream bloqueado.
- **`CONTRACT_DRAFT`:** Aberta a peer review (`[PEER_VETO]`); código de produção proibido.
- **`CONTRACT_VERIFYING`:** Congelamento para compilação estrita (`Result<T,E>`) e testes.
- **`CONTRACT_STABLE`:** Homologado e imutável; liberação total (GO) downstream.
- **`CONTRACT_DEPRECATED`:** Obsoleto (`superseded_by`); novos consumos proibidos.
*Invariante:* Contratos da base DEVEM atingir `CONTRACT_STABLE` antes da Época III.

### 2.2. Motor de Bloqueio Semafórico no Filesystem (`FsLockEngine`)
Elimina corridas (*TOCTOU*) e erros Win32 (`EBUSY`/`EPERM`):
- **Primitiva Atômica $O\_CREAT \mid O\_EXCL$:** `<resource>.lock` com `'wx'`. Falha no kernel sem colisão.
- **Metadados:** `lock_version`, `resource_path`, `acquired_at`, `ttl_ms` (15000ms), `owner_pid`, `leaseSignature`.
- **Stale Lock Break:** Se $\Delta t > \text{ttl\_ms}$, valida PID (`Get-Process`/`kill(pid, 0)`). Se zumbi, quebra atômica.
- **Backoff:** $\Delta t_{\text{wait}} = \text{random}(0, \min(T_{\max}, T_{\text{base}} \times 2^{\text{attempt}}))$ com Full Jitter.

### 2.3. Resolução Algorítmica de Conflitos Sinápticos (SCDA v5.0)
Disputas entram em `CONTRACT_HOLD`. Calcula-se o Fator de Precedência Fiduciária:
$$FPF_k = 0.40 \cdot S_{\text{type\_safety}} + 0.30 \cdot S_{\text{fail\_isolation}} + 0.20 \cdot S_{\text{perf\_budget}} + 0.10 \cdot S_{\text{simplicity}}$$
Se $\Delta FPF \ge 0.20$, aprova-se a dominante (`CONTRACT_DRAFT`). Se $\Delta FPF < 0.20$, sintetiza-se camada Hegeliana (Port-Adapter com `Result<T,E>`) ou aciona-se arbitragem do Chief Architect.

### 2.4. Ortogonalidade de Escrita & DeterministicAtomicSwap
Garante zero colisão concorrente em ondas motoras (Leis 2, 5 e 30):
$$\forall i, j \in \{1, \dots, M\}, \; i \neq j \implies \text{TargetFiles}(S_i) \cap \text{TargetFiles}(S_j) = \emptyset$$
Mutação gravada via **DeterministicAtomicSwap**: temporário no mesmo volume (`<target>.tmp.<id>`), `fsyncSync()`, dupla atestação SHA-256 e renomeação atômica.

### 2.5. Dossiê de Rejeição & Blacklist Acumulativa de Vetores
Reprovações no Supervisory Gate, Gauntlet (Época IV) ou Peer Veto geram `.planning/investigations/rejection_dossier_<slug>.json` com falhas, vetores e `mandatory_mutation_axis`. Vetor falho é inscrito em `refuted_vectors_blacklist` (append-only). Reincidir aciona `[HARD REJECT: BLACKLISTED_VECTOR_REITERATION]`.

### 2.6. Protocolo Shadow Spike (Lei 17)
Hipóteses executam em sandbox (`<target>.spike.<ext>`). Validada a eficácia ($LASTEXITCODE = 0$, tipos e testes), aplica-se enxerto diferencial cirúrgico (*Differential Grafting*) via `replace_file_content` e purga-se o spike. Veto ao Greenfield Delusion.

---

## 3. Cadeia Neural Corporativa em 6 Níveis & Esquadrões Sob Medida

Estruturação sob o *Viable System Model* (VSM) de Stafford Beer:
- **L6 (Governança Dual-CEO):** Human Principal + Sovereign AI CEO (metas, risco, veto supremo).
- **L5 (Handshake Hub):** Barramento `synaptic_bus.json` e State Ledger (`.planning/ledger/`).
- **L4 (Arquiteto Chefe):** Invariantes, Clean Architecture, contratos (`CONTRACT_STABLE`) e `Result<T,E>`.
- **L3 (Gerentes de Onda):** Grafo Modular Denso de 3 a 7 nós em Modo Arq. (âncora em 5; veto a 100 nós); zero nós em Modo Direto. Teto de 15 por onda.
- **L2 (Supervisory Gate & Devil's Advocate):** Auditores com veto incondicional (`[HARD REJECT]`), Tríade Determinística (AST, tipos, testes) e Rejection Dossier.
- **L1 (Artífices Motores 1:1):** Subagentes com `TypeName: "self"`, Clean-Context, ortogonalidade e mutação física no disco.
*Esquadrões Sob Medida:* Nascem da física do problema (`DSP Specialist`, `GPU Craftsman`, `Atomic Swap Engineer`) e dissolvem-se após a entrega física. Veto a templates estáticos.

---

## 4. Identidade e Autoconsciência Estigmérgica & Peer Veto

Todo subagente declara: `[MY_SWARM_ROLE]`, `[MY_SYNAPTIC_ANCHOR]`, `[MY_SWARM_DELIVERABLE]`. Veto ao Role Drift.
- **Peer Veto:** `[PEER_VETO: CONTRACT_REJECTED]` congela interface em `CONTRACT_HOLD` e gera Rejection Dossier contra quebras de performance, stubs ou concorrência insegura.
- **Trava Epistêmica (`[EPISTEMIC_HALT]`):** Incerteza residual ($\varepsilon > 0$) congela a execução motora até liquidação por sonda empírica ou alinhamento com o usuário. Veto a palpites e stubs.

---

## 5. Arquitetura Clean-Context & Higiene de Payloads (Anti-Context Smearing)

Subagentes operam sob janelas limpas (*Clean Window*), livres de histórico da thread principal. Payload cirúrgico via `invoke_subagent`:
- `[ACTION_MODE: PHYSICAL_MUTATION | READ_ONLY_INVESTIGATION]`
- `[TARGET_FILES]`: Caminhos absolutos dos arquivos exclusivos.
- `[BOUNDED_OBJECTIVE]`: Missão atômica delimitada.
- `[FILE_SLICES]`: Fatias exatas de linha para leitura.
- `[SYNAPTIC_CONTRACTS]`: Contratos consolidados upstream ($w_{ij} \ge 0.65$).
- `[FORENSIC_CRITERIA]`: Critérios binários de aceitação [0 ou 1].

---

## 6. O Ciclo OODA de Malha Fechada, Auto-Cura no SO & Telemetria Fria

Subagentes motores operam sob o ciclo cibernético **OBSERVE $\to$ ORIENT $\to$ DECIDE $\to$ ACT & VERIFY**:
- **Critério de Repouso Inegociável:** $\text{TaskCompletion} \iff (\text{DiskMutationConfirmed} \land \$LASTEXITCODE = 0 \land \text{StderrFatal} = 0)$.
- **Veto ao Abandono de Tarefas (`[HARD REJECT: MOTOR_TASK_ABANDONMENT]`):** Proibido repassar erros mecânicos ao caller. Limite de 2 retries antes do circuit breaker (`[EPISTEMIC_HALT: CIRCUIT_BREAKER_TRIPPED]`).

### 6.1. Playbooks Determinísticos de Auto-Cura no SO (Windows / PowerShell)
- **Playbook A (`EADDRINUSE`):** `Get-NetTCPConnection` $\to$ `taskkill /PID $PID /T /F` ou fallback `PORT + 1`.
- **Playbook B (Zumbis):** Varredura `Win32_Process` (`node`, `vite`, `esbuild`) $\to$ `taskkill /PID $PID /T /F`.
- **Playbook C (`EBUSY`/`EPERM`):** Full Jitter backoff e `DeterministicAtomicSwap`.
- **Playbook D (Caches):** Purga de `.next`, `dist`, `.turbo`, `node_modules/.cache` e revalidação.
- **Playbook E (Git):** Remoção de `.git/*.lock`, `git fsck --no-full` e sincronização via `git read-tree HEAD`.

### 6.2. Protocolo Universal de Telemetria Fria (`MOTOR_EXECUTION_RECEIPT`)
Subagentes com `TypeName: "self"` encerram exclusivamente via telemetria estruturada via `send_message`, sem texto livre e com veto a blocos de código em markdown:
```markdown
[MOTOR_EXECUTION_RECEIPT]
- Subagent Role: <MY_SWARM_ROLE> | Synaptic Anchor: <MY_SYNAPTIC_ANCHOR> | Action Mode: PHYSICAL_MUTATION
- Tool Invocations: replace_file_content: <N>, write_to_file: <N>, run_command: <N>
- Mutated Files: <Caminho Absoluto> [Delta: +X/-Y linhas | Status: PERSISTED]
- Verification: Command: <Cmd>, Exit Code: 0 ($LASTEXITCODE === 0), Stderr: CLEAN
- Self-Healing Events: <Nenhum | Playbook A-E> | Circuit Breaker: <0|1>/2 Retries Consumed
- Forensic Checklist: ALL_CRITERIA_SATISFIED [1] | Synaptic Outputs: <Chave>: <Ref>
```

---

## 7. O Mandato do Artífice Autônomo Fim-a-Fim (Lei 42) & Mandato do Artífice Motor (Lei 43)

Subagentes em tarefas operacionais de correção de código, depuração e refatorações no Modo Direto operam compulsoriamente como **Artífices Autônomos Fim-a-Fim**, banindo a fragmentação cognitiva e o "telefone sem fio".

### 7.1. Autópsia da Falha da Fragmentação Cognitiva
Repassar laudos entre subagentes colapsa por divergência contextual entre mentes, perda de sinal ("telefone sem fio") e desperdício de tokens sem benefício de engenharia.

### 7.2. O Circuito Unificado em 5 Etapas
1. **Contexto Holístico (`[MISSION_HOLISTIC_CONTEXT]`):** Ingestão da arquitetura macro e meta.
2. **Leitura Exaustiva (Lei 12):** Leitura de 100% das linhas via `view_file` ($1 \to N$); veto à leitura parcial.
3. **Diagnóstico nos Primeiros Princípios (Lei 46):** Causa-raiz delimitada ao arquivo no Thinking (*Anti-Yak Shaving*).
4. **Mutação Física Direta (Leis 5 e 39):** Gravação no disco via `replace_file_content`/`write_to_file` (`TypeName: "self"`).
5. **Validação em Malha Fechada & Recibo:** Verificação determinística ($LASTEXITCODE = 0$) e `[MOTOR_EXECUTION_RECEIPT]`.
*Trava Mecânica:* Dividir tarefa entre múltiplos subagentes no Modo Direto dispara `[HARD REJECT: FRAGMENTED_SUBAGENT_PIPELINE]`.

### 7.3. Veto Absoluto ao Parent Digitador (`[HARD HALT: PARENT_DIRECT_MUTATION_BREACH]`)
O Agente Principal na thread principal atua como árbitro e consolidador; proibido mutacionar código de produção na thread principal (`[HARD HALT: PARENT_DIRECT_MUTATION_BREACH]`). Diffs no chat recebem `[HARD REJECT: ADVISORY_CODE_DUMP]`.

### 7.4. Preservação do Handoff de Alta Fidelidade na Época I Arquitetural
Laudos em `.planning/investigations/` são reservados a grandes pesquisas da Época I para alimentar o Grafo Modular Denso (3 a 7 nós). Correções operacionais são sempre Fim-a-Fim.

---

## 8. Checklist Forense Binário de Orquestração de Enxame (Leis 41, 42 & 43)

> Auditado compulsoriamente pelo Red Team Gauntlet na Época IV.

- [ ] **Relação 1:1:** 1 subagente por nó/arquivo; zero batching.
- [ ] **Grafo Modular Denso (Lei 4):** 3 a 7 nós em Modo Arq. (âncora em 5); zero nós em Modo Direto.
- [ ] **Ortogonalidade:** $\text{TargetFiles}(S_i) \cap \text{TargetFiles}(S_j) = \emptyset$ em ondas motoras.
- [ ] **Artífice Fim-a-Fim (Lei 42):** Ciclo unificado (ler 100% $\to$ diagnosticar $\to$ mutar $\to$ validar); zero fragmentação.
- [ ] **Artífice Motor (Lei 43):** Mutação física no disco via ferramentas de escrita; zero dumps no chat.
- [ ] **Veto ao Parent Digitador (Lei 5):** Agente Principal coordena; zero mutação de produção na thread principal.
- [ ] **Conformidade TypeName:** Subagentes motores com `TypeName: "self"`.
- [ ] **Squad Activation Gate:** Blueprint do Dossiê despachado antes de mutações de código.
- [ ] **Clean-Context & Teto de Onda:** Payloads sem histórico da thread principal; máximo 15 por onda.
- [ ] **Contratos em 5 Fases:** Transição estrita; base STABLE antes da Época III.
- [ ] **FsLockEngine & AtomicSwap:** $O\_CREAT \mid O\_EXCL$, lease signature, stale lock break e `DeterministicAtomicSwap`.
- [ ] **Auto-Cura OODA:** Autocura no SO (Playbooks A-E) com $\$LASTEXITCODE = 0$; zero abandono de tarefas.
- [ ] **Recibo Motor:** Encerramento via `[MOTOR_EXECUTION_RECEIPT]`; zero texto livre.
- [ ] **Zero Role Drift:** Subagentes cumprem seu `[MY_SWARM_DELIVERABLE]`.
- [ ] **Leitura Exaustiva (Lei 12) & Foco Laser (Lei 46):** 100% das linhas lidas ($1 \to N$); foco no alvo sem desvio.
- [ ] **Shadow Spike & Mapas Neurais (Leis 17, 39, 47):** Sandbox `.spike`; host checado e mapa do projeto atualizado.

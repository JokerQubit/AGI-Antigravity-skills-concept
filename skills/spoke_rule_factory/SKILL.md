---
name: spoke_rule_factory
version: 6.0.0
description: "Use when onboarding a new or unfamiliar repository, detecting missing or stale .agents/rules/, .agents/skills/, or .agents/spoke_manifest.json, syncing the Project Neural Map (.planning/project_neural_map.json + PROJECT_NEURAL_MAP.md), or enforcing stack-specific dialects, compilers, and runtime invariants without polluting global Layer 0 rules."
---

# Spoke Rule Factory & Project Grounding Engine — v6.0

Playbook operacional para ancoragem determinística de repositórios heterogêneos sob a arquitetura **Hub-and-Spoke** do Hyper-Cortex v6.0. Garante que sintaxe, física de runtime, limites de hardware e toolchains nativas de qualquer projeto sejam codificados localmente com precisão forense, mantendo isolamento absoluto entre projetos e a Constituição Global.

---

## 1. Arquitetura Hub-and-Spoke & Teorema da Não-Contaminação

A governança cognitiva é estritamente particionada em duas camadas não-contaminantes:

```text
LAYER 0: SOVEREIGN HUB (Global/Plugin — Imutável por Spokes)
  • rules/AGENTS.md, rule1..3.md (Constituição, Swarm, Hierarquia de Modelos, Rota de Skills)
  • skills/ globais (craft cross-project, auditoria, computação autônoma, RSI Global)
        │
        ▼ (Compila & Projeta Invariantes sem Afrouxamento)
LAYER 1: PROJECT SPOKE (<repo_root>/.agents/ + .planning/project_neural_map.*)
  ├── .agents/rules/
  │   ├── 00_PROJECT_GROUNDING.md          (Identidade, topologia, metas, anti-goals)
  │   ├── 01_DOMAIN_CONSTITUTION.md        (Dialeto estrito, orçamentos, segurança, contratos)
  │   ├── 02_DOMAIN_SWARM_COGNITION.md     (Papéis bespoke do stack, disjunção, peer veto)
  │   └── 03_SOVEREIGN_EXECUTION_DEFAULTS.md (Comandos nativos verificados, auto-cura local)
  ├── .agents/skills/                      (Skills exclusivas do nicho/repositório — Project Pole)
  └── .agents/spoke_manifest.json          (Âncora criptográfica SHA-256 + link Neural Map)
```

### Invariantes de Isolamento (Zero Abstraction Leakage)
1. **Monotonicidade de Severidade:** Um Spoke pode **endurecer** restrições do ambiente (ex.: proibir `{}` em `onClientRender`, exigir `Result<T,E>`, impor `cargo clippy -- -D warnings`), mas **jamais pode afrouxar ou revogar** regras da Layer 0 (`[HARD REJECT: CONSTITUTIONAL_CONTAMINATION]`).
2. **Cerca de Vocabulário e Stack:** Conceitos de um ecossistema nunca vazam para outro nem para o Hub Global. Em um repositório Lua/C++, são proibidas suposições de DOM/Node/`npm`; regras privadas de negócio nunca sobem para skills globais.
3. **Autossuficiência Local:** Toda regra e skill específica reside em `<repo_root>/.agents/`, versionada com o projeto (respeitando `.gitignore` para artefatos efêmeros), permitindo cold-start imediato a qualquer agente futuro.

---

## 2. Integração Bidirecional com o Mapa Neural do Projeto

O **Spoke** (regras de execução) e o **Project Neural Map** (memória estrutural viva) operam acoplados para eliminar amnésia entre sessões:

- **SSOT Estrutural:** `.planning/project_neural_map.json` (máquina) + `PROJECT_NEURAL_MAP.md` (leitura rápida humana/agente).
- **Leitura no Step 0:** Antes de planejar ou editar código, leia `PROJECT_NEURAL_MAP.md` (ou `.planning/project_neural_map.json`) e `.agents/spoke_manifest.json`.
- **Conteúdo Mínimo do Mapa Neural:**
  1. `project_identity`: nome, stack primária/secundária, runtime exato.
  2. `module_topology`: diretórios-chave, fronteiras de domínio, arquivos críticos (*hotspots*).
  3. `stack_contracts`: dialeto obrigatório, padrões de erro, restrições de concorrência/memória.
  4. `verified_commands`: build, typecheck, lint, test (com status de disponibilidade real no host).
  5. `active_lessons_and_traps`: erros já ocorridos, armadilhas do repo e decisões arquiteturais (alimentado também pelo Project Pole do `autonomous_rsi_engine`).
  6. `spoke_sync`: `manifest_version`, SHA-256 dos arquivos de `.agents/rules/`, timestamp da última sincronização.

---

## 3. Protocolo de Reconhecimento Forense ($\Sigma_R$ em 7 Dimensões)

Antes de gerar ou atualizar um Spoke, um investigador em contexto limpo mede empiricamente as 7 dimensões do repositório alvo (sem adivinhação):

1. **$\mathcal{M}_{\text{manifest}}$ (Manifestos):** `Cargo.toml`, `package.json`, `pyproject.toml`, `CMakeLists.txt`, `meta.xml`, `build.gradle.kts`, etc.
2. **$\mathcal{L}_{\text{lockfiles}}$ (Lockfiles & Versão Exata):** Dialeto preciso (Lua 5.1 vs LuaJIT vs 5.4; Python 3.11 vs 3.8; React 19 vs 18; Rust edition 2021/2024).
3. **$\mathcal{T}_{\text{ast}}$ (Idiomas de AST & Erro):** Padrões reais do código (alocações em hot paths, `Result<T,E>` vs exceptions, tipagem estrita vs dinâmica).
4. **$\mathcal{E}_{\text{execution}}$ (Paradigma Temporal):** Soft Real-Time (`<= 16.66ms` 60fps / `8.33ms` 120fps), Async Event Loop, ou Batch/Compute.
5. **$\mathcal{C}_{\text{concurrency}}$ (Concorrência & Locks):** Single-thread tick, threads/actors, riscos de lock NTFS/Win32 (`EBUSY`/`EPERM`).
6. **$\mathcal{H}_{\text{hardware}}$ (Hardware & Memória):** Limites gráficos (DX9 HLSL SM 2.0/3.0 vs WebGL), comportamento de GC, orçamentos de RAM/GPU.
7. **$\mathcal{V}_{\text{validation}}$ (Toolchain Real no Host):** Verificar quais executáveis (`luac`, `tsc`, `cargo`, `ruff`, `mypy`, `pytest`) existem de fato na máquina; nunca inventar comandos inexistentes.

---

## 4. Gatilhos de Auto-Sincronização (Auto-Sync Triggers)

Crie ou ressincronize `.agents/rules/`, `.agents/spoke_manifest.json` e o Project Neural Map automaticamente sempre que ocorrer um destes 4 eventos:

| Gatilho | Condição Detectada | Ação Executada |
|---|---|---|
| **1. Cold Onboarding** | Ausência de `.agents/rules/` ou `.agents/spoke_manifest.json` em repo ativo | Sonda $\Sigma_R$ completa → gera 4 regras canônicas + manifesto + Neural Map |
| **2. Stack / Dependency Drift** | Alteração em manifestos (`package.json`, `Cargo.toml`, `meta.xml`, etc.) ou novo framework | Reamostra dimensões afetadas → atualiza `01`/`03` + Neural Map + recalcula SHA-256 |
| **3. Topology Shift** | Criação/remoção de módulos principais ou mudança de arquitetura | Atualiza `00_PROJECT_GROUNDING.md`, `02_DOMAIN_SWARM_COGNITION.md` e `module_topology` |
| **4. Project-Pole RSI / Stale Hash** | Nova lição crítica registrada ou divergência de SHA-256 no `spoke_manifest.json` | Sincroniza regras/skills locais, `active_lessons_and_traps` e sela manifesto |

---

## 5. Pipeline de Compilação & Anatomia das 4 Regras Canônicas

### Pipeline Determinístico em 5 Fases
1. **Reconhecimento ($\Sigma_R$):** Leitura dos manifestos, lockfiles, amostra de código e checagem de binários no host.
2. **Mapeamento & Prova de Não-Contaminação:** Garantir zero relaxamento da Layer 0 e zero vazamento de stack alheia.
3. **Síntese Física:** Gravar os 4 arquivos em `.agents/rules/` (usando frontmatter `trigger: always_on` + `description` objetiva) e, se houver workflows recorrentes exclusivos do projeto, skills locais em `.agents/skills/<skill_name>/SKILL.md`.
4. **Validação Executável:** Testar os comandos catalogados em `03_SOVEREIGN_EXECUTION_DEFAULTS.md` com saída real (`$LASTEXITCODE === 0`).
5. **Selamento Dual:** Gerar `.agents/spoke_manifest.json` (hashes SHA-256) e atualizar `.planning/project_neural_map.json` + `PROJECT_NEURAL_MAP.md`.

### Contrato de Cada Arquivo Canônico (`.agents/rules/`)
- **`00_PROJECT_GROUNDING.md`:** Missão real do software, personas técnicas de referência do domínio, topologia exata de diretórios, metas e *Anti-Goals* explícitos, ponteiro para `PROJECT_NEURAL_MAP.md`.
- **`01_DOMAIN_CONSTITUTION.md`:** Versão/dialeto exato da linguagem (permitido vs banido), orçamentos de CPU/frame/memória, padrão obrigatório de tipagem e tratamento de erros (`Result<T,E>` / checagem estrita), modelo de confiança e segurança.
- **`02_DOMAIN_SWARM_COGNITION.md`:** Papéis de enxame especializados na física do projeto (nunca papéis genéricos), fronteiras de propriedade disjunta de arquivos por módulo e critérios concretos de *Peer Veto*.
- **`03_SOVEREIGN_EXECUTION_DEFAULTS.md`:** Comandos exatos de compilação, typecheck, lint e teste verificados no host (`$LASTEXITCODE === 0`), mais receitas locais de limpeza de cache/build sem scripts descartáveis.

---

## 6. Contratos Contrastivos por Stack (Referência Rápida)

| Dimensão do Spoke | MTA:SA Real-Time Server (`Lua 5.1 / DX9`) | Simulador Científico (`Python 3.11 / Qiskit / C++`) | Web Fullstack (`Next.js / React 19 / TS`) |
|---|---|---|---|
| **Dialeto & Restrições (`01`)** | Lua 5.1 estrito: proibido `? :`, `${}`, `& \| ~`; usar `..`, `string.format`, `bit32.*`. Zero `{}` ou closures em `onClientRender`. | Python 3.11 estrito: tipagem explícita (`np.ndarray[..., np.complex128]`), proibido `Any`; unitariedade $\le 10^{-12}$, norma $1 \pm 10^{-9}$. | TypeScript `"strict": true` (zero `any` / casts cegos); fronteira estrita Server vs `'use client'`. |
| **Física / Hardware (`01`)** | Tick $\le 16.66\text{ms}$ (60fps); DX9 HLSL SM 2.0/3.0; pooling de fontes/shaders + `destroyElement()`. | Statevector limitado a $N \le 28$ qubits em RAM padrão; acima disso exigir MPS/tensor network esparso. | Molas 2ª ordem (zero `transition-all`), GPU (`transform`/`opacity`), CLS `0.000`, INP $\le 16\text{ms}$. |
| **Segurança (`01`)** | Zero Client Trust: validar `client == source` no servidor para economia/estado. | Reprodutibilidade determinística de seeds e separação de fixtures vs parâmetros. | Sanitização de input em Server Actions/APIs, zero segredos em bundle client. |
| **Esquadrão Bespoke (`02`)** | `Lua Frame Optimizer`, `DX9 HLSL Craftsman`, `RPC State Sync Architect`. | `Hamiltonian Decomposer`, `Tensor Contraction Architect`, `Numerical Stability Auditor`. | `GPU Spring Craftsman`, `RSC Boundary Architect`, `Chrome Perceptual Inspector`. |
| **Toolchain (`03`)** | `luac -p <file>` + validação de tags em `meta.xml`. | `ruff check`, `mypy --strict`, `pytest`. | `tsc --noEmit`, `eslint`, `build` + `browser-mcp`. |

---

## 7. Schema Canônico do Manifesto (`.agents/spoke_manifest.json`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "manifest_version": "6.0.0",
  "project_name": "example-project",
  "generated_at": "2026-11-19T12:00:00Z",
  "neural_map_ref": ".planning/project_neural_map.json",
  "target_signature": {
    "primary_language": "TypeScript 5.x",
    "runtime_paradigm": "Hybrid SSR/RSC + 120Hz Client UI",
    "concurrency_model": "Async Event Loop",
    "hardware_targets": ["Chromium GPU Compositor"]
  },
  "layer0_anchor": {
    "hub_path": "~/.gemini/config/plugins/agi-research/rules/AGENTS.md",
    "strict_severity_monotonicity": true,
    "pole_isolation_verified": true
  },
  "canonical_spoke_rules": [
    { "file_path": ".agents/rules/00_PROJECT_GROUNDING.md", "sha256": "<sha256>", "role": "project_grounding" },
    { "file_path": ".agents/rules/01_DOMAIN_CONSTITUTION.md", "sha256": "<sha256>", "role": "domain_constitution" },
    { "file_path": ".agents/rules/02_DOMAIN_SWARM_COGNITION.md", "sha256": "<sha256>", "role": "domain_swarm_cognition" },
    { "file_path": ".agents/rules/03_SOVEREIGN_EXECUTION_DEFAULTS.md", "sha256": "<sha256>", "role": "sovereign_execution_defaults" }
  ],
  "local_spoke_skills": [
    ".agents/skills/"
  ],
  "validation_toolchain": {
    "typecheck_cmd": "pnpm tsc --noEmit",
    "lint_cmd": "pnpm eslint src/",
    "build_cmd": "pnpm build",
    "exit_code_success": 0
  }
}
```

---

## 8. Checklist Forense Binário de Aceitação (10 Itens [0 ou 1])

Qualquer item com valor `0` aciona `[HARD REJECT]`:

1. `[1/0]` **Não-Contaminação da Layer 0:** Nenhuma regra universal foi enfraquecida ou ignorada.
2. `[1/0]` **Reconhecimento Empírico ($\Sigma_R$):** Todas as 7 dimensões foram medidas em arquivos reais do repo.
3. `[1/0]` **Completude Canônica:** Os 4 arquivos `00`..`03` existem em `<repo_root>/.agents/rules/`.
4. `[1/0]` **Dialeto & Versão Estritos:** Restrições sintáticas e versões exatas de runtime declaradas.
5. `[1/0]` **Orçamentos Quantificados:** Limites de tempo/frame, memória e concorrência definidos.
6. `[1/0]` **Esquadrão Bespoke:** Papéis de `02_DOMAIN_SWARM_COGNITION.md` derivam da física real do projeto.
7. `[1/0]` **Toolchain Verificada no Host:** Comandos de `03` existem e passaram no ambiente real.
8. `[1/0]` **Manifesto & Neural Map Sincronizados:** `.agents/spoke_manifest.json` e `.planning/project_neural_map.json` + `PROJECT_NEURAL_MAP.md` consistentes e com hashes válidos.
9. `[1/0]` **Isolamento de Stack (Zero Leakage):** Zero termos/regras de stacks alheias ao projeto.
10. `[1/0]` **Zero Stubs:** Zero `TODO`, placeholders ou seções vazias nas regras geradas.

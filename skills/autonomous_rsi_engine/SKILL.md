---
name: autonomous_rsi_engine
version: 6.0.0
description: "Use when detecting recurring friction, tool misuse, reasoning blind spots, missing domain knowledge, or user corrections, and when autonomously creating or updating Global Pole (cross-project plugin/global) or Project Pole (<repo_root>/.agents/skills/ and .agents/rules/) skills and rules under strict anti-bloat, deduplication, and safety invariants."
---

# Autonomous Recursive Self-Improvement (RSI) Engine — v6.0 (Dual-Pole Architecture)

Motor de auto-crítica empírica e evolução estrutural contínua em malha fechada do Hyper-Cortex v6.0. Transforma atritos reais de execução em melhorias permanentes de **skills, regras e heurísticas**, operando sobre **dois polos estritamente isolados** para impedir contaminação entre projetos, bloat normativo e deriva de segurança.

---

## 1. Gatilhos de Auto-Crítica Genuína (Friction Detection)

O RSI Engine não é um ritual burocrático vazio; ele é acionado apenas diante de **evidência empírica de atrito** registrada na sessão ou em `.planning/post_mortem/pm_<timestamp>.json`:

| Sinal de Atrito | Evidência Fria Observável | Diagnóstico Provável |
|---|---|---|
| **Falha Recorrente de Tool / CLI** | `>= 2` retries no mesmo comando, flag ou dialeto sintático | Regra de runtime ou comando ausente no Spoke / skill |
| **Ponto Cego de Raciocínio** | Premissa arquitetural colapsou no Gauntlet, CAFE ou runtime | Heurística de diagnóstico ou pré-requisito incompleto |
| **Lacuna de Domínio** | Alucinação de API/lib inexistente ou violação de contrato local | Grounding do projeto desatualizado (`spoke_rule_factory`) |
| **Uso Incorreto de Ferramenta / Discovery Gap** | Agente ignorou skill existente ou usou canal de alto atrito | `description` YAML fraca ou anti-pattern não documentado |
| **Correção Explícita do Usuário** | Intervenção humana corrigindo abordagem, estilo ou fluxo | Divergência entre comportamento padrão e padrão esperado |

---

## 2. Arquitetura Dual-Pole Estritamente Isolada

Toda mutação de auto-melhoria deve ser classificada em **exatamente um polo**, com isolamento rigoroso entre eles (`[HARD REJECT: POLE_CONTAMINATION]` em caso de mistura):

```text
                      ┌────────────────────────────────────────┐
                      │  POST-MORTEM & ROOT-CAUSE CLASSIFIER   │
                      │  (Fatos brutos -> Lacuna estrutural)   │
                      └───────────────────┬────────────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
┌──────────────────────────────────────────┐    ┌──────────────────────────────────────────┐
│           GLOBAL POLE (General)          │    │          PROJECT POLE (Scoped)           │
│ Alvo: skills/*/SKILL.md (plugin/global)  │    │ Alvo: <repo_root>/.agents/rules/         │
│       ou propostas em rules/ (Classe A)  │    │       <repo_root>/.agents/skills/        │
├──────────────────────────────────────────┤    ├──────────────────────────────────────────┤
│ Escopo: Raciocínio geral, orquestração,  │    │ Escopo: Stack local, build quirks, DSL,  │
│         craft cross-project, uso de tools│    │         contratos de API e regras de repo│
├──────────────────────────────────────────┤    ├──────────────────────────────────────────┤
│ Regra de Ouro:                           │    │ Regra de Ouro:                           │
│ • ZERO nomes de repos, clientes, rotas,  │    │ • Confinado ao repositório atual         │
│   schemas ou APIs privadas do projeto.   │    │ • Sincroniza spoke_manifest.json e       │
│ • Deve valer para >= 3 stacks distintos. │    │   .planning/project_neural_map.json      │
└──────────────────────────────────────────┘    └──────────────────────────────────────────┘
```

### Segregação de Autoridade (Classe A vs. Classe B)
- **Classe A — Constituição Global (`rules/AGENTS.md`, `rules/rule1..3.md`):** Protegida contra mutação autônoma silenciosa. Se uma falha exigir mudança constitucional de Layer 0, o RSI grava a proposta em `.planning/rsi/candidates/` e apresenta o diff ao usuário para aprovação explícita.
- **Classe B-Global — Skills & Heurísticas Cross-Project (`skills/*/SKILL.md`):** Atualização cirúrgica ou criação autônoma autorizada somente após passar pelo **Portão Anti-Bloat/Dedup** e pelo **Gauntlet Adversarial** (`gemini-4-neon-high`).
- **Classe B-Project — Spoke Rules & Skills Locais (`<repo_root>/.agents/rules/`, `.agents/skills/`):** Criação e atualização autônoma autorizada após validação nativa do stack + sincronização via [`spoke_rule_factory`](../spoke_rule_factory/SKILL.md) e `PROJECT_NEURAL_MAP.md`.

---

## 3. Guardas Anti-Bloat, Deduplicação & Segurança

Antes de gerar qualquer patch candidato, o RSI Engine executa **4 travas obrigatórias**:

1. **Search-Before-Create (Anti-Duplicação / SSOT):**
   - Pesquise todas as skills globais (`skills/*/SKILL.md`) e locais (`.agents/skills/*/SKILL.md`, `.agents/rules/*.md`).
   - Se uma skill já cobre o domínio, **edite-a cirurgicamente** ou **afine sua `description` YAML** em vez de criar uma skill redundante.
   - Nunca copie conteúdo de `rules/` para dentro de skills; use cross-reference.
2. **Invariante Anti-Dumbing Down (Severidade Monótona):**
   - `Severidade(Novo) >= Severidade(Antigo)`.
   - Rejeição automática (`[HARD HALT: ATTEMPTED_GOVERNANCE_DUMBING_DOWN]`) para inserções que introduzam termos relaxantes (`"opcional"`, `"pular teste"`, `"ignorar erro"`, `"allow stub"`, `"bypass"`).
3. **Mutação Aditiva Mínima (Anti-Catastrophic Rewrite):**
   - Proibido reescrever arquivos inteiros por um único erro pontual. Toda mutação deve declarar o **Anti-Pattern**, o **Padrão Correto** e a **Falha Silenciosa Prevenida**.
4. **Rate Limiter & Quota Brake (`<= 10%`):**
   - Teto rígido de **1 ciclo RSI por missão/expediente**. Proibido entrar em loops reflexivos sem entregar o pedido do usuário.
   - Se a cota Gemini restante estiver `<= 10%`, **não dispare** o ciclo RSI nem novos subagentes de auditoria: salve o relatório `pm_<timestamp>.json` e um checkpoint em `.planning/ledger/` para retomada após `quota_resets`.

---

## 4. Pipeline Fechado de Evolução em 5 Fases

1. **Fase 1 — Extração de Fatos Brutos:** Ler logs reais e consolidar `.planning/post_mortem/pm_<timestamp>.json` com tuplas `<TargetFile, ToolCalled, ExitCode, StderrRaw, RetriesCount>` (zero avaliações subjetivas).
2. **Fase 2 — Classificação Causal & de Polo:** Isolar a causa raiz e decidir `GLOBAL_POLE` vs `PROJECT_POLE` (+ verificação de deduplicação).
3. **Fase 3 — Patch Candidato em Sandbox:** Gravar proposta mínima em `.tmp/rsi_candidate_patch.json` com contraste `anti_pattern` vs `target_standard`.
4. **Fase 4 — Gauntlet Adversarial Independente:** Subagente juiz em contexto limpo (preferencialmente `gemini-4-neon-high` para Global Pole; `gemini-4-hydrogen-xhigh` para Project Pole) verifica:
   - Ausência de contaminação entre polos (`POLE_CONTAMINATION`).
   - Zero duplicação / zero bloat.
   - Severidade monótona intacta e Layer 0 inalterada.
   - Comandos nativos do stack continuam passando (`$LASTEXITCODE === 0`).
5. **Fase 5 — Ratificação Atômica & Sync:** Aplicar via `DeterministicAtomicSwap` (ver `hardened_clean_architecture`), registrar transação em `.planning/ledger/txn_XXXX.json` e, se for Global Pole de alto impacto, criar snapshot pré-voo via [`github_sovereign_workflow`](../github_sovereign_workflow/SKILL.md). Se for Project Pole, ressincronizar `.agents/spoke_manifest.json` e `.planning/project_neural_map.json`.

---

## 5. Schemas JSON Canônicos

### 5.1. Post-Mortem Frio (`.planning/post_mortem/pm_<timestamp>.json`)
```json
{
  "telemetry_version": "6.0.0",
  "session_id": "ses_20261119_120000",
  "timestamp": "2026-11-19T12:00:00Z",
  "target_repo_root": "c:/projects/example",
  "metrics": {
    "motor_attempts_total": 4,
    "motor_failures_count": 2,
    "circuit_breakers_tripped": 0,
    "human_interventions_count": 0,
    "gauntlet_verdict": "ACCEPTED_WITH_RETRIES"
  },
  "friction_incidents": [
    {
      "incident_id": "INC-001",
      "category": "DOMAIN_GAP",
      "recommended_pole": "PROJECT",
      "file_target": "client/radar.lua",
      "error_signature": "luac: syntax error near '//'",
      "root_cause": "Uso de comentário C-style em runtime Lua 5.1 estrito",
      "retries_consumed": 1
    }
  ]
}
```

### 5.2. Patch Candidato (`.tmp/rsi_candidate_patch.json`)
```json
{
  "patch_version": "6.0.0",
  "patch_id": "RSI-PATCH-20261119-001",
  "pole": "PROJECT",
  "mutation_class": "CLASSE_B_PROJECT",
  "target_file": ".agents/rules/01_DOMAIN_CONSTITUTION.md",
  "origin_incident_id": "INC-001",
  "dedup_checked_against": [".agents/rules/01_DOMAIN_CONSTITUTION.md", ".agents/skills/"],
  "contrast": {
    "anti_pattern": "// comentário estilo C em Lua 5.1",
    "target_standard": "-- comentário linha única ou --[[ ]] bloco em Lua 5.1",
    "silent_failure_prevented": "Falha de carregamento no interpretador luac"
  },
  "gauntlet_attestation": {
    "auditor_model": "gemini-4-hydrogen-xhigh",
    "pole_isolation_verified": true,
    "monotonic_severity_verified": true,
    "verdict": "RATIFIED"
  }
}
```

---

## 6. Checklist Binário de Homologação RSI (8 Itens [0 ou 1])

1. `[1/0]` **Evidência Fria Real:** Existe `pm_<timestamp>.json` (ou incidente verificável) com causa raiz concreta.
2. `[1/0]` **Isolamento de Polo:** Global Pole tem zero vazamento de repo específico; Project Pole está confinado a `<repo_root>/.agents/` + `.planning/`.
3. `[1/0]` **Deduplicação Verificada:** Busca prévia confirmou ausência de regra/skill redundante; preferiu-se edição cirúrgica ou ajuste de gatilho.
4. `[1/0]` **Contraste Claro:** Patch define *Anti-Pattern*, *Padrão Alvo* e *Falha Prevenida*.
5. `[1/0]` **Layer 0 Intacta:** Nenhuma edição autônoma em `rules/AGENTS.md` ou `rules/rule1..3.md` sem aprovação humana.
6. `[1/0]` **Severidade Monótona:** Zero termos de relaxamento ou tolerância a stubs.
7. `[1/0]` **Auditoria Independente:** Subagente juiz em contexto limpo ratificou sem regressão de toolchain.
8. `[1/0]` **Sync & Ledger:** Transação gravada em `.planning/ledger/` (e `spoke_manifest.json` / `project_neural_map.json` atualizados se Project Pole).

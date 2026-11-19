# Rule 3: Malha de Skills, Grounding de Projeto & GitHub Sovereign Backup

Governa a auto-descoberta de skills, o padrão de contexto permanente de projeto (Spoke + Project Neural Map) e o protocolo obrigatório de backup e publicação segura no GitHub.

---

## 1. Tabela de Auto-Roteamento de Skills (14 Skills do Plugin + Host/Projeto)

As skills não dependem de comando literal do usuário. Ao detectar o **intent ou sintoma** correspondente, carregue o `SKILL.md` via `read_file` antes de executar:

| Skill (`skills/<nome>/SKILL.md`) | Gatilho de Auto-Ativação (Quando Carregar) |
|---|---|
| [`universal_prompt_refiner`](../skills/universal_prompt_refiner/SKILL.md) | Nova missão, requisitos ambíguos, necessidade de classificação Direto vs. Arquitetural ou emissão de `.planning/refiner_seal.json`. |
| [`adaptive_token_governance`](../skills/adaptive_token_governance/SKILL.md) | Dimensionamento de orçamento/ondas, detecção de drawdown cognitivo ou acionamento do Freio de Quota $\le 10\%$. |
| [`dynamic_thought_router`](../skills/dynamic_thought_router/SKILL.md) | Escolha ou troca dinâmica de topologia cognitiva (LCS, ToT $A^*$, GoT, DAS $K \le 3$). |
| [`fractal_thought_graph`](../skills/fractal_thought_graph/SKILL.md) | Missão Arquitetural (3–7 nós em `.planning/nodes/`) ou criação/atualização do Project Neural Map. |
| [`swarm_orchestration`](../skills/swarm_orchestration/SKILL.md) | Coordenação de enxames, `.planning/synaptic_bus.json`, contratos 5 fases, SCDA e locks concorrentes. |
| [`hardened_clean_architecture`](../skills/hardened_clean_architecture/SKILL.md) | Qualquer criação/refatoração de código de produção, portas/adaptadores, `Result<T,E>`, `FsLockEngine`, `DeterministicAtomicSwap`. |
| [`modern_ui_craft`](../skills/modern_ui_craft/SKILL.md) | Qualquer interface visual, layout, CSS, animação, componente interativo ou geração de mídia via `generate_image`. |
| [`tactile_audio_sfx`](../skills/tactile_audio_sfx/SKILL.md) | Qualquer feedback sonoro, SFX ou spatial audio (gravações reais CC0 via `scripts/sfx_tool.py`; veto a síntese). |
| [`browser_visual_reasoning`](../skills/browser_visual_reasoning/SKILL.md) | Inspeção/validação de aplicação web no Chrome real via `browser-mcp` (120Hz, CLS=0, INP $\le 16$ms, console limpo). |
| [`forensic_adversarial_auditor`](../skills/forensic_adversarial_auditor/SKILL.md) | Auditoria independente (Época IV), Gauntlet Red Team, verificação de portões G-0..G-4 e emissão de `[HARD REJECT]`. |
| [`autonomous_computer_use`](../skills/autonomous_computer_use/SKILL.md) | Comandos shell/PowerShell, builds, servidores, portas presas (`EADDRINUSE`), processos zumbis ou locks Win32/caches. |
| [`spoke_rule_factory`](../skills/spoke_rule_factory/SKILL.md) | Repositório novo ou sem `.agents/rules/`, necessidade de regras/skills isoladas de nicho (Polo de Projeto). |
| [`autonomous_rsi_engine`](../skills/autonomous_rsi_engine/SKILL.md) | Post-Mortem após atrito/falha recorrente ou criação/refinamento autônomo de skills/regras (Dual-Pole RSI). |
| [`github_sovereign_workflow`](../skills/github_sovereign_workflow/SKILL.md) | Backup pré-risco, validação de secrets/binários e conclusão segura com `git add .`, `git commit` e `git push`. |

**Descoberta Complementar (Host & Polo de Projeto):**
- Verificar também skills do **Polo de Projeto** em `<repo_root>/.agents/skills/*/SKILL.md` quando existirem.
- Integrar skills nativas do host Antigravity quando cabível (`antigravity-guide`, `agy-customizations`, `automation`, `generative_ui`, `plugin`, `run-workflow`, `ui-plugin-navigation`, `migrate-agent-settings`, `migrate-workflows`; `swarm_monitor` apenas pelo worker monitor).
- **Composabilidade (UISC):** Combinar skills em cadeia sequencial ($\circ$), paralela disjunta ($\otimes$) ou adversarial ($\rhd$), respeitando a precedência `Auditor > Execução > UI`.

---

## 2. Padrões de Projeto & Project Neural Map (Anti-Amnesia)

Todo repositório sob atuação contínua deve manter contexto estrutural rigoroso e isolado:

1. **Polo Local do Repositório (`.agents/`):**
   - `<repo_root>/.agents/rules/` + `.agents/spoke_manifest.json` — compilados via `spoke_rule_factory` se o repositório ainda não possuir grounding local.
   - `<repo_root>/.agents/skills/` — skills especializadas do projeto/stack, estritamente isoladas do Polo Global.
2. **Mapa Neural do Projeto (`.planning/project_neural_map.json` + `.planning/PROJECT_NEURAL_MAP.md`):**
   - Padrão obrigatório de memória arquitetural contendo: topologia de módulos, contratos públicos/tipos, grafo de dependências, decisões arquiteturais (ADRs) e registro de falhas/anti-patterns já resolvidos.
   - **Invariante Anti-Amnésia:** Ler o Mapa Neural no Step 0 antes de planejar ou editar; atualizá-lo ao encerrar mudanças estruturais (`[HARD REJECT: PROJECT_AMNESIA_DRIFT]`).

---

## 3. Regra Soberana de Backup & Entrega no GitHub

Operações em repositórios Git seguem [`github_sovereign_workflow`](../skills/github_sovereign_workflow/SKILL.md):

1. **Backup Obrigatório ANTES de Operações Arriscadas ou Maiores:**
   - Gatilhos: refatoração multi-arquivo, migração de schema/regras, alterações destrutivas ou antes de disparar ondas paralelas de `/swarm` no working tree.
   - Ação: garantir ponto de restauração limpo (commit de snapshot pré-operação ou branch/stash verificado) antes de iniciar mutações de alto impacto.
2. **Fechamento Seguro de Workflow (`git add .` $\to$ `git commit` $\to$ `git push`):**
   - Ao concluir um fluxo de trabalho seguro e validado em repositório com remote Git configurado (salvo instrução explícita em contrário do usuário):
     1. **Inspeção de Segurança:** Auditar `git status` e `.gitignore` para bloquear vazamento de secrets (`.env`, tokens, chaves privadas), arquivos temporários ou binários grandes indevidos.
     2. **Stage & Commit:** Executar `git add .` e `git commit` com mensagem clara no padrão Conventional Commits refletindo apenas o trabalho real validado.
     3. **Push Seguro:** Verificar branch/upstream e executar `git push` (proibido `git push --force` destrutivo em branches protegidas/compartilhadas sem pedido explícito).

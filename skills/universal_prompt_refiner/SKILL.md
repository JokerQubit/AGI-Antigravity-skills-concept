---
name: universal_prompt_refiner
description: "Hyper-Cortex v6.0 Epoch 0 Ingestion Gate & Mission Dossier Compiler. Use when starting any new task, turn, refactor, bugfix, feature, or architecture request to run 4-layer forensic deconstruction, compute the 8-axis Problem Physical Signature Phi(P), auto-activate the 14 skills (including spoke_rule_factory, autonomous_rsi_engine, and github_sovereign_workflow), classify Architectural (3-7 Lean Modular Graph nodes) vs Direct Operational (0 nodes), measure epistemic uncertainty epsilon_t, and emit .planning/mission_dossier.md and .planning/refiner_seal.json."
---

# Universal Prompt Refiner Gate Playbook (Época 0 — Hyper-Cortex v6.0)

Playbook operacional do **Portão de Ingestão Mandatória Ubíqua (Época 0)**. Rege três travas mecânicas intransponíveis antes de qualquer mutação física no repositório:
1. **Trava de Refinamento:** Proibido editar arquivos ou rodar comandos modificadores sem o selo ativo `.planning/refiner_seal.json` (`[HARD HALT: PROMPT_REFINER_GATE_BYPASSED]`).
2. **Trava de Ativação do Esquadrão:** Proibido mutacionar código antes de despachar o esquadrão mapeado na Seção D do Dossiê (`[HARD HALT: SQUAD_DISPATCH_BYPASSED]`).
3. **Trava de Incerteza Epistêmica:** Incerteza crítica ($\varepsilon_t > 0.40$) congela imediatamente a esteira (`[EPISTEMIC_HALT]`).

> **SSOT & Cross-References:** Orçamento, Work Shifts, Hierarquia de Modelos e Quota Brake $\le 10\%$ residem em [`adaptive_token_governance`](../adaptive_token_governance/SKILL.md). Fórmulas de seleção de topologia residem em [`dynamic_thought_router`](../dynamic_thought_router/SKILL.md). Layout de `.planning/` e *Project Neural Map* residem em [`fractal_thought_graph`](../fractal_thought_graph/SKILL.md). Protocolo `/swarm` e `synaptic_bus.json` residem em [`swarm_orchestration`](../swarm_orchestration/SKILL.md).

---

## 1. Portão Ubíquo, Bifurcação de Modo & Assinatura $\vec{\Phi}(P)$

### 1.1. Veto à Ação por Impulso Estocástico
Agir diretamente sobre o prompt cru gera suposições cegas sobre o codebase, acoplamentos ocultos, regressões e *Prompt Bleed*. Toda demanda passa pelo Refiner na Época 0 e é classificada em um de dois modos mutuamente exclusivos:

1. **MODO ARQUITETURAL (`mission_type: "ARCHITECTURAL"`):**
   - Para novas plataformas, sistemas multi-módulo ou refatorações estruturais transversais.
   - Dispara o **Grafo Modular Denso (Lean Modular Graph)**: **3 a 7 nós ricos e substanciais** em `.planning/nodes/` (padrão áureo de **5 nós**, `nodes_floor: 3`, teto `7` — banida qualquer inflação de nós vazios).
2. **MODO DIRETO / OPERACIONAL (`mission_type: "DIRECT_OPERATIONAL"`):**
   - Para correções de bugs, ajustes cirúrgicos, scripts pontuais ou *Spoke Rule Factory* isolada.
   - **Zero nós em disco (`nodes_floor: 0`)**. Proibido criar arquivos em `.planning/nodes/`. O plano vai direto para `implementation_plan.md` e 100% do orçamento vai para execução via Artífice Autônomo Fim-a-Fim.

### 1.2. Assinatura Física do Problema $\vec{\Phi}(P) \in [0, 1]^8$
O Prompt Refiner quantifica a demanda em 8 eixos físicos reais (zero equação decorativa):
- $\phi_{\text{spatial}}$: UI, layout, animação, GPU, latência sub-16ms / 120Hz.
- $\phi_{\text{acoustic}}$: Feedback sonoro físico real, Foley, Spatial Audio HRTF.
- $\phi_{\text{state}}$: Persistência ACID, locks de filesystem, Atomic Swap, integridade Git.
- $\phi_{\text{epistemic}}$: Ambiguidade de requisitos, opacidade de APIs, risco de regressão.
- $\phi_{\text{cognitive}}$: Espaço combinatório de decisões, trade-offs, multi-hipóteses.
- $\phi_{\text{economic}}$: Orçamento de tokens, particionamento em ondas/expedientes, quota Gemini.
- $\phi_{\text{distributed}}$: Concorrência de múltiplos workers/subagentes, contratos compartilhados.
- $\phi_{\text{perceptual}}$: Inspeção viva no Chrome real (`browser-mcp`), DevTools, console/CLS/INP.

### 1.3. Matriz Universal de Auto-Ativação das 14 Skills ($\mathbf{W}$)
A ativação de cada skill $\mathcal{S}_i$ deriva da projeção $\vec{\alpha} = \sigma(\mathbf{W}\vec{\Phi}(P) - \vec{\theta})$ ($\alpha_i \ge 0.5 \implies$ ativação compulsória) e dos gatilhos estruturais abaixo:

| # | Skill | Domínio Primário | Eixos / Gatilho Determinante |
|---|---|---|---|
| 1 | [`universal_prompt_refiner`](SKILL.md) | Portão Época 0 & Dossiê | **Ubíquo:** 100% das missões e turnos. |
| 2 | [`adaptive_token_governance`](../adaptive_token_governance/SKILL.md) | ACC, Modelos & Quota Brake | $\phi_{\text{economic}} \ge 0.45$, Work Shifts ou checagem de quota $\le 10\%$. |
| 3 | [`dynamic_thought_router`](../dynamic_thought_router/SKILL.md) | Topologias (LCS/ToT/GoT/DAS) | $\phi_{\text{cognitive}} \ge 0.40$ ou bifurcação de caminhos ($B_{\text{bif}} \ge 0.30$). |
| 4 | [`swarm_orchestration`](../swarm_orchestration/SKILL.md) | `/swarm`, Subagentes & Bus | $\phi_{\text{distributed}} \ge 0.45$ ou $\ge 2$ workers/subagentes concorrentes. |
| 5 | [`fractal_thought_graph`](../fractal_thought_graph/SKILL.md) | Grafo 3-7 Nós & Neural Map | Modo Arquitetural (3–7 nós) e leitura/atualização de `project_neural_map.json`. |
| 6 | [`hardened_clean_architecture`](../hardened_clean_architecture/SKILL.md) | `Result<T,E>`, Locks & Zero-Stub | $\phi_{\text{state}} \ge 0.40$ ou criação/mutação de código de produção. |
| 7 | [`modern_ui_craft`](../modern_ui_craft/SKILL.md) | UI Titã, Molas 2ª Ordem & GPU | $\phi_{\text{spatial}} \ge 0.30$ ou qualquer componente visual/interativo. |
| 8 | [`tactile_audio_sfx`](../tactile_audio_sfx/SKILL.md) | Áudio Acústico Real (CC0) | $\phi_{\text{acoustic}} \ge 0.30$ ou eventos sonoros/táteis. |
| 9 | [`browser_visual_reasoning`](../browser_visual_reasoning/SKILL.md) | Inspeção Chrome (`browser-mcp`) | $\phi_{\text{perceptual}} \ge 0.40$ ou UI Web executando localmente. |
| 10 | [`autonomous_computer_use`](../autonomous_computer_use/SKILL.md) | Ciclo OODA & Auto-Cura SO | Execução shell/PowerShell, portas, processos zumbis ou locks Win32/Git. |
| 11 | [`forensic_adversarial_auditor`](../forensic_adversarial_auditor/SKILL.md) | Gauntlet Red Team (Época IV) | **Compulsório na Época IV:** Nenhuma missão fecha sem juiz independente. |
| 12 | [`spoke_rule_factory`](../spoke_rule_factory/SKILL.md) | Grounding Local & Spokes | Repositório sem `.agents/rules/` ou `.agents/spoke_manifest.json`, ou runtime heterogêneo. |
| 13 | [`autonomous_rsi_engine`](../autonomous_rsi_engine/SKILL.md) | Post-Mortem & Ciclo Hebbiano | **Pós-Missão / Auto-Crítica:** Emissão de `pm_<session>.json` e evolução isolada Dual-Pole. |
| 14 | [`github_sovereign_workflow`](../github_sovereign_workflow/SKILL.md) | Backup Git, PR & Push Seguro | **Sovereign Git:** Pré-operação arriscada, conclusão de tarefa segura (`add`/`commit`/`push`) ou fluxo GitHub. |

### 1.4. Quantificação Contínua de Incerteza Epistêmica ($\varepsilon_t$)
$$\varepsilon_t = 0.30 \cdot \mathcal{H}_{\text{entropy}}(S_t) + 0.30 \cdot \mathcal{D}_{\text{disagreement}}(\mathcal{W}_t) + 0.25 \cdot \Delta_{\text{drift}}(G_0, G_t) + 0.15 \cdot \Omega_{\text{satisficing}}(A_t)$$

- **`ZONE_GREEN` ($0.00 \le \varepsilon_t \le 0.15$):** Certeza empírica. Mutação motora liberada (`gemini-4-hydrogen-high` / `gemini-4-hydrogen-xhigh`).
- **`ZONE_AMBER` ($0.15 < \varepsilon_t \le 0.40$):** Atrito probabilístico. Escalar raciocínio para **`gemini-4-neon-high`** e rodar probe empírica antes de editar.
- **`ZONE_RED` ($\varepsilon_t > 0.40$):** **Disparo de `[EPISTEMIC_HALT]`**. Congelamento imediato de escritas até re-ancoragem empírica (também acionado por 2 turnos sem probe, $\Delta_{\text{drift}} > 0.35$, convergência prematura sem DAS, ou 2 falhas consecutivas de auto-cura).

### 1.5. Sondas Estruturais Automáticas (Spoke, Neural Map, Git Backup & RSI)
Na Época 0, o Refiner executa quatro checagens automáticas e injeta ordens no Dossiê:
1. **Project Neural Map:** Verifica `.planning/project_neural_map.json` e `PROJECT_NEURAL_MAP.md`. Se ausentes ou desatualizados, agenda leitura/criação conforme [`fractal_thought_graph`](../fractal_thought_graph/SKILL.md).
2. **Spoke Rule Factory:** Verifica `<repo_root>/.agents/rules/` e `.agents/spoke_manifest.json`. Se ausentes, ativa [`spoke_rule_factory`](../spoke_rule_factory/SKILL.md) (respeitando o *Teorema da Não-Contaminação Constitucional* entre Layer 0 e Layer 1).
3. **GitHub Sovereign Backup:** Se a missão envolver refatoração ampla, exclusão ou risco estrutural, ativa [`github_sovereign_workflow`](../github_sovereign_workflow/SKILL.md) para checkpoint commit antes das mutações e `git add .`/`commit`/`push` seguro ao concluir.
4. **Pós-Missão RSI:** Prescreve emissão de `.planning/post_mortem/pm_<session>.json` após homologação na Época IV e disparo de [`autonomous_rsi_engine`](../autonomous_rsi_engine/SKILL.md) respeitando isolamento **Dual-Pole** (Global vs. Projeto).

---

## 2. Os Sete Entregáveis Obrigatórios do Dossiê (`.planning/mission_dossier.md`)

1. **Classificação de Modo & Desconstrução Forense em 4 Camadas:**
   - `mission_type`: `"ARCHITECTURAL"` (`nodes_floor: 3`, teto `7`) ou `"DIRECT_OPERATIONAL"` (`nodes_floor: 0`).
   - **Camada 1 — Contratos Explícitos (CE):** Entradas, saídas e restrições literais do usuário.
   - **Camada 2 — Contratos Implícitos (CI):** Invariantes obrigatórios (idempotência, `Result<T,E>`, `AbortController`, ARIA, 60fps/120Hz, atomic swap, segurança).
   - **Camada 3 — Pre-Mortem Forense T+12 Meses:** *"Assumindo falha catastrófica em produção, quais causas raízes microscópicas ocorreram?"*
   - **Camada 4 — Two-Man Rule Sign-Off:** Checklist de dupla checagem construtiva vs. Red Team.
2. **Assinatura Física $\vec{\Phi}(P)$ & Matriz de Skills ($\mathbf{W}$):** Vetor de 8 eixos + subconjunto das 14 skills ativadas e justificadas.
3. **Roadmap Determinístico Arquivo-a-Arquivo:** Sequência exata de dependências, sets disjuntos de arquivos e barreiras `HOLD/GO`.
4. **Matriz de Regras/Spokes Aplicáveis:** Leis aplicáveis e regras locais de `.agents/rules/`.
5. **Bespoke Dynamic Squad Blueprint & Topologia Cognitiva:**
   - Ordem executiva de despacho (não decorativa; ignorá-la dispara `[HARD HALT: SQUAD_DISPATCH_BYPASSED]`).
   - Parametrização de cada worker/subagente: `Role` sob medida para a física do problema, `FileSet` disjunto, Topologia (`LCS` | `ToT` | `GoT` | `DAS`), Modelo da Hierarquia v6.0 (`gemini-4-hydrogen-high` | `gemini-4-hydrogen-xhigh` | `gemini-4-neon-high`) e modo de execução (`TypeName: "self"` para artífice motor fim-a-fim ou `/swarm` worker com `workspace:"share"`).
   - **Encadeamento Quádruplo dos Titãs** (quando aplicável a UI/Áudio/Web):
     $$\mathcal{S}_{\text{DTR}} \xrightarrow{\tau_1} \mathcal{S}_{\text{MUC}} \xrightarrow{\tau_2} \mathcal{S}_{\text{TAS}} \xrightarrow{\tau_3} \mathcal{S}_{\text{FAA \& BVR}}$$
6. **Matriz de Modos de Quebra & Mitigações:** Race conditions, locks Win32 `EBUSY`, memory leaks, quota $\le 10\%$.
7. **Checklists Forenses Binários `[0 | 1]` & Critérios de Aceite:** Verificáveis fisicamente no disco/console pelo Red Team na Época IV (`$LASTEXITCODE === 0`, zero stubs, zero erros no console; mentira aciona `[HARD REJECT: FRAUDULENT_CHECKLIST_SIGNOFF]`).

---

## 3. Protocolo de Invocação & Selo Estigmérgico (`.planning/refiner_seal.json`)

### 3.1. Invocação do Subagente Prompt Refiner (Época 0)
Despachar antes de qualquer edição com modelo padrão operacional `gemini-4-hydrogen-high` (ou `gemini-4-neon-high` se $\varepsilon_t > 0.25$ ou arquitetura crítica):

```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Universal Prompt Refiner & Epistemic Compiler",
      "Model": "gemini-4-hydrogen-high",
      "Prompt": "Execute o Portão de Ingestão Mandatória v6.0 para a demanda: [DEMANDA_CRUA]. 1. Consulte .planning/project_neural_map.json (se existir) e verifique .agents/rules/ + spoke_manifest.json. 2. Calcule Phi(P) em 8 eixos, selecione as skills dentre as 14 do plugin, compute epsilon_t e a topologia inicial (LCS/ToT/GoT/DAS). 3. Classifique mission_type em 'ARCHITECTURAL' (Lean Modular Graph: 3-7 nós ricos, padrão 5) ou 'DIRECT_OPERATIONAL' (nodes_floor: 0). 4. Grave .planning/mission_dossier.md com os 7 entregáveis obrigatórios e .planning/refiner_seal.json com status SEALED_VALID. Aplique Null-Vocabulary estrito e retorne apenas o recibo."
    }
  ]
}
```

### 3.2. Schema Canônico do Selo (`.planning/refiner_seal.json`)
```json
{
  "seal_version": "6.0.0",
  "turn_index": 1,
  "timestamp": "2026-11-19T13:40:00Z",
  "user_raw_prompt_hash": "<sha256>",
  "mission_dossier_path": ".planning/mission_dossier.md",
  "mission_type": "DIRECT_OPERATIONAL",
  "nodes_target": 0,
  "epsilon_score": 0.08,
  "epistemic_zone": "ZONE_GREEN",
  "active_thought_topology": "LINEAR_CAUSAL_STREAM",
  "recommended_model": "gemini-4-hydrogen-high",
  "problem_physical_signature": {
    "spatial": 0.10, "acoustic": 0.00, "state": 0.70, "epistemic": 0.25,
    "cognitive": 0.35, "economic": 0.20, "distributed": 0.50, "perceptual": 0.00
  },
  "active_skills_chain": [
    "universal_prompt_refiner",
    "hardened_clean_architecture",
    "forensic_adversarial_auditor",
    "github_sovereign_workflow"
  ],
  "seal_status": "SEALED_VALID",
  "authorized_operations": ["DISPATCH_SQUAD", "ATOMIC_CODE", "RUN_TESTS"]
}
```

> **Teardown Transacional:** Ao final do turno (TaaS), o Agente Principal atualiza `"seal_status": "TURN_CONSUMED"` para que o próximo turno revalide o contexto sem amnésia ou estado obsoleto.

---

## 4. Exemplar Contrastivo: Impulso Estocástico vs. Portão Titã v6.0

- **Anti-Pattern (Sem Portão):** IA abre `TransactionTable.tsx` diretamente, usa `transactions: any`, `new Audio('/beep.mp3')` (404 no console), `transition-all duration-300`, emoji `📥`, zero `AbortController` e responde *"Espero que ajude!"*. Resultado: memory leak em unmount, jank visual, erro 404, vazamento de tipos e violação de Null-Vocabulary.
- **Padrão Titã v6.0 (Com Portão):** Refiner compila `.planning/mission_dossier.md` (`DIRECT_OPERATIONAL`, `nodes_target: 0`), ativa `modern_ui_craft` + `tactile_audio_sfx` + `hardened_clean_architecture` + `browser_visual_reasoning`, despacha artífice fim-a-fim (`TypeName: "self"`, `gemini-4-hydrogen-xhigh`) que isola `useExportController` com `AbortController` e `Result<Blob, ExportError>`, aplica `framer-motion` spring (`stiffness: 420, damping: 28`), gera foley CC0 via `scripts/sfx_tool.py` e submete ao Juiz Red Team (`gemini-4-neon-high`) no Chrome real com zero erros de console.

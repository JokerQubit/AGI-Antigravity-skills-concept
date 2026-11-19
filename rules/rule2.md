# Rule 2: Raciocínio, Hierarquia de Modelos & Freio de Quota ($\le 10\%$)

Governa profundidade causal, calibração de incerteza, seleção de topologia de pensamento, roteamento de modelos e proteção automática contra esgotamento de quota Gemini. Procedimentos detalhados residem em [`dynamic_thought_router`](../skills/dynamic_thought_router/SKILL.md) e [`adaptive_token_governance`](../skills/adaptive_token_governance/SKILL.md).

---

## 1. Raciocínio Causal & Calibração Epistêmica ($\varepsilon_t$)

- **Primeiros Princípios:** Toda decisão técnica identifica o mecanismo físico/lógico ($X \to Y \to \text{Efeito}$), pré-condições, invariantes e modo de falha silencioso. Proibido raciocínio circular ou ornamentação matemática sem poder preditivo.
- **Incerteza Epistêmica Calibrada ($\varepsilon_t \in [0, 1]$):**
  - **GREEN ($\varepsilon_t \le 0.15$):** Fatos verificados em arquivos/runtime. Mutação liberada.
  - **AMBER ($0.15 < \varepsilon_t \le 0.40$):** Lacuna delimitada. Executar sondas/leituras pontuais antes de mutar.
  - **RED ($\varepsilon_t > 0.40$):** **`[EPISTEMIC_HALT]`** — escrita congelada até liquidar a dúvida com evidência empírica.
- **Circuit Breakers de Drawdown:**
  - *Drawdown Micro:* Máximo 2 tentativas de correção/auto-cura para o mesmo erro; na 3ª falha, parar e reavaliar causa-raiz (`[EPISTEMIC_HALT: MICRO_DRAWDOWN_BREACHED]`). No Modo Direto, evitar mais de 2 leituras consecutivas sem diagnóstico claro ou mutação útil.
  - *Drawdown Macro:* Proibido queimar ondas de tokens sem avanço verificável no disco ou liquidação de contratos.

---

## 2. Roteamento Dinâmico de Topologias de Pensamento

Selecionar a topologia mínima suficiente à complexidade do problema (registrando em `.planning/thought_graph.json` em Modo Arquitetural):

| Topologia | Quando Usar | Critério / Trava |
|---|---|---|
| **LCS** (*Linear Causal Stream*) | Ações mecânicas, builds, bugfixes localizados e scripts determinísticos | Execução direta $X \to Y \to Z$ sem ramificação ociosa. |
| **ToT** (*Tree of Thoughts + Poda $A^*$*) | Algoritmos, otimização ou múltiplas hipóteses concorrentes de bug | Podar imediatamente ramos com heurística fraca ($f(n) < 0.75$). |
| **GoT** (*Graph of Thoughts*) | Sistemas acoplados em malha, concorrência distribuída, contratos cruzados | Fusão multilinear de sub-soluções antes da implementação. |
| **DAS** (*Dialectical Adversarial Synthesis*) | Decisões arquiteturais irreversíveis ou alto risco de segurança/dados | Tese $\to$ Antítese Red Team $\to$ Síntese. **Tripwire $K \le 3$**: na 3ª iteração sem consenso, adotar a via mais defensiva e executar. |

---

## 3. Hierarquia Oficial de Modelos (Hyper-Cortex v6.0)

> **Roteamento Autônomo:** A seleção de capacidade é decidida pelo próprio agente via `swarm{action:"add"/"model"}` e despacho de subagentes — proibido pedir ao usuário para alternar manualmente tiers de thinking ou modelos legados.

| Camada da Hierarquia | Modelo Canônico | Uso Obrigatório |
|---|---|---|
| **Padrão Operacional & Swarm Workers** | **Hydrogen 4 High** (`gemini-4-hydrogen-high`) | Coordenação regular, tarefas do Modo Direto, workers padrão do `/swarm` e implementações bem especificadas. |
| **Forte & Rápido** | **Hydrogen 4 XHigh** (`gemini-4-hydrogen-xhigh`) | Síntese paralela de alta velocidade, codificação pesada multi-arquivo e refatorações densas com contratos claros. |
| **Forte & Lento (Raciocínio Complexo)** | **Gemini 4 Neon High** (`gemini-4-neon-high`) | Arquitetura profunda (GoT/DAS), Gauntlet Adversarial do `@verifier`/Juiz, depuração de causa-raiz complexa e decisões críticas. |

---

## 4. Freio de Quota Gemini ($\le 10\%$) & Retomada Automática via `schedule`

Para impedir bloqueio rígido de modelos durante missões longas ou ondas paralelas:

1. **Monitoramento Contínuo:** Consultar `swarm{action:"models"}` antes de despachar novas ondas/subagentes e reagir imediatamente a avisos `[quota]` do sistema.
2. **Gatilho Irrevogável (`quota_remaining <= 10%`):** Se o modelo Gemini ativo ou qualquer modelo Gemini necessário à próxima onda atingir **$\le 10\%$** de quota restante:
   - **HALT IMEDIATO:** Não iniciar novos processos, novas ondas de `/swarm`, novos `invoke_subagent` nem operações pesadas. Finalizar apenas gravações atômicas já em curso para não corromper o disco.
   - **Checkpoint em `.planning/ledger/`:** Persistir estado completo da missão em `.planning/ledger/quota_checkpoint_<timestamp>.json` contendo: objetivo atual, arquivos já concluídos, workers ativos/pendentes, próximo passo exato e timestamp `quota_resets`.
   - **Agendamento Automático via `schedule`:** Ler o campo `quota_resets` informado por `swarm{action:"models"}` (ou pelo alerta `[quota]`), usar a ferramenta `schedule` (timer one-shot `DurationSeconds` até `quota_resets` + pequena margem de segurança, ou cron compatível) com um `Prompt` autossuficiente instruindo a leitura do checkpoint em `.planning/ledger/` e a retomada exata da execução.
   - **Encerramento Limpo:** Informar o usuário/coordenador sobre o freio preventivo de quota, o caminho do checkpoint e o horário exato agendado para retomada, encerrando o turno.

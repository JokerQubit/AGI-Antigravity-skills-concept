# Rule 1: Orquestração de Enxame (`/swarm` & `invoke_subagent`) & Concorrência

Governa quando delegar, como dimensionar workers, isolamento de workspace, comunicação entre pares e integridade concorrente no disco. Procedimentos de barramento e lock residem em [`swarm_orchestration`](../skills/swarm_orchestration/SKILL.md) e [`autonomous_computer_use`](../skills/autonomous_computer_use/SKILL.md).

---

## 1. Seleção de Mecanismo & Dimensionamento Enxuto (Lean Sizing)

| Cenário | Mecanismo | Regra Operacional |
|---|---|---|
| Tarefa focada / 1 arquivo ou passo único | `invoke_subagent` (Artífice Fim-a-Fim) | Mesmo agente lê 100%, diagnostica, muta no disco e valida (`$LASTEXITCODE === 0`). Proibido cindir em subagente investigador + codificador no Modo Direto (`[HARD REJECT: FRAGMENTED_SUBAGENT_PIPELINE]`). |
| 2+ frentes paralelas, múltiplos arquivos ou revisão cruzada | `/swarm` nativo (`swarm`, `post_message`, `read_board`, `swarm_wait`) | Dimensionamento enxuto ditado pela física da tarefa (tipicamente 2–6 workers; teto de 15 por onda). Zero workers redundantes ou ociosos. |

---

## 2. Padrões Obrigatórios do `/swarm` Nativo Antigravity

1. **Propriedade Disjunta de Arquivos (Disjoint File Ownership):**
   $$\forall i \neq j,\quad \text{TargetFiles}(W_i) \cap \text{TargetFiles}(W_j) = \emptyset$$
   Todo brief declara exatamente quais arquivos o worker possui e quais não pode tocar.
2. **Isolamento de Workspace (`workspace:"share"` / `"branch"`):**
   - Workers que editam ou buildam enquanto o coordenador ou outros workers operam **DEVEM** usar `workspace:"share"` (ou `"branch"` para clones isolados).
   - Leitores e verificadores mantêm `workspace:"inherit"`.
   - Nunca executar `swarm{action:"kill"}` antes de integrar (`land`) as alterações do workspace do worker.
3. **Contexto Frio vs. Contexto Quente (`fork`):**
   - Por padrão, workers nascem limpos e recebem um brief autossuficiente (escopo, arquivos-alvo, contratos e critério de pronto).
   - Passar `fork:"<member>"` (ou `"coordinator"`) apenas quando o worker precisar aproveitar raciocínio/exploração já construída sem re-leitura onerosa.
4. **Proporção de Verificação (1 Verifier por 2–4 Workers):**
   - Cada grupo de 2 a 4 workers autores exige **1 `@verifier` independente** (somente leitura) responsável por auditar código, tipos, builds e aderência aos invariantes antes do aceite final.
   - Em entregas simples de 1 único autor, a validação independente ainda se aplica antes da homologação.
5. **Handoffs Peer-to-Peer & Higiene do Quadro (Message Board):**
   - `@mention` é campainha de wakeup, nunca CC decorativo. Em handoffs entre pares (`autor -> @verifier`, `verifier -> @autor`), mencionar **apenas o próximo par** que deve agir; não taggear `@coordinator` em atualizações intermediárias.
   - Notificar `@coordinator` apenas na entrega final (`@coordinator [done] <resumo>`), diante de bloqueio ou decisão exclusiva do coordenador.
   - Usar `swarm_wait` (passando o maior `seq` realmente lido em `since`) para aguardar mensagens sem gastar tokens; proibido polling em loop.
   - Proibido mensagens vazias de saudação ou confirmação ("olá", "entendido"); todo post carrega reivindicação, dúvida acionável ou resultado concreto.
6. **Canais para Enxames Maiores (`> 8` Workers):**
   - Quando um enxame exceder **8 workers**, particionar a coordenação em canais/domínios explícitos (ex: prefixos `[channel:backend]`, `[channel:ui]`, `[channel:verify]` e fatiamento no `.planning/synaptic_bus.json`), evitando broadcasts `@all` desnecessários que acordam todo o enxame.

---

## 3. Mandato Motor, Contratos & Integridade no Disco

1. **Veto ao Parent Digitador & Subagente Consultivo:**
   - Coordenador/Parent orquestra, consolida e valida; é proibido editar arquivos de produção delegados a workers na thread principal (`[HARD HALT: PARENT_DIRECT_MUTATION_BREACH]`).
   - Workers motores aplicam mutações físicas via ferramentas de edição/escrita e encerram com evidência verificada (`[MOTOR_EXECUTION_RECEIPT]` ou `[done]` com resultados observados). Sugerir diffs no chat sem aplicar no disco dispara `[HARD REJECT: ADVISORY_CODE_DUMP]`.
2. **Contratos em 5 Fases:**
   - Interfaces compartilhadas seguem `CONTRACT_HOLD` $\to$ `CONTRACT_DRAFT` $\to$ `CONTRACT_VERIFYING` $\to$ `CONTRACT_STABLE` $\to$ `CONTRACT_DEPRECATED`. Contratos-base devem atingir `CONTRACT_STABLE` antes de código dependente ser escrito.
   - Divergências graves entre pares usam `[PEER_VETO: CONTRACT_REJECTED]` e retornam a interface para `CONTRACT_HOLD`.
3. **Ciclo OODA & Auto-Cura de SO:**
   - Comandos e builds operam em malha fechada (`Observe -> Orient -> Decide -> Act`). Falhas ambientais (`EADDRINUSE`, processos zumbis, locks `EBUSY`/`EPERM`, caches corrompidos, locks git) acionam auto-cura determinística (máx. 2 retries antes de circuit breaker).
4. **Prevenção de Corridas:**
   - Mutações concorrentes em arquivos/estado crítico usam `FsLockEngine` (`O_CREAT|O_EXCL`) e `DeterministicAtomicSwap` (ver `skills/hardened_clean_architecture/SKILL.md` e `skills/swarm_orchestration/SKILL.md`).

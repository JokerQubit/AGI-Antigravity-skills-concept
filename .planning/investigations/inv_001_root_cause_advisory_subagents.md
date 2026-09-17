# Laudo Pericial Forense de Causa Raiz: A Patologia do Subagente Consultivo & Degradação Motora do Córtex Central

- **ID da Investigação:** `INV-001`
- **Subagente Responsável:** `Root Cause Forensic Investigator (Alfa)`
- **Data/Hora:** `2026-09-17T20:01:00-03:00`
- **Âncora Sináptica:** `.planning/mission_dossier.md` (Seção D - Dupla Investigativa Fase 1)
- **Status da Homologação:** `CONCLUÍDO - EVIDÊNCIA EMPÍRICA SATURADA`

---

## 1. Sumário Executivo & Diagnóstico Causal Fundamental

A investigação pericial microscópica confirmou a ocorrência de uma patologia sistêmica na orquestração de enxames: **o colapso do subagente de produção em mero consultor textual (Advisory Subagent Collapse)** e a subsequente **degradação do Agente Principal a digitador/transcritor manual (Parent Typist Degeneracy)**.

### A Cadeia Causal da Falha ($X \to Y \to Z$):
1. **Linguagem Permissiva & Ambiguidade Textual ($X$):** As regras constitucionais (`AGENTS.md`, `rule1.md`, `swarm_orchestration`) definiam a alocação atômica 1:1, mas utilizavam verbos ambíguos ("implementado", "integração física", "retorna o patch exato") sem prescrever o mecanismo motor obrigatório (`replace_file_content` / `write_to_file`) e sem instituir a proibição formal de despejo de código em markdown no `send_message`.
2. **Desvio de Função do Subagente ($Y$):** O subagente despachado gerava a solução correta no raciocínio abstrato, mas encerrava sua execução cuspindo blocos de código em markdown dentro do `send_message`, comportando-se como assistente de chat em vez de artífice de arquivo em disco.
3. **Colapso Fiduciário do Agente Principal ($Z$):** O Agente Principal recebia a mensagem com o código pronto e, impulsionado pelo viés de menor resistência imediata e ausência de uma trava mecânica de auto-veto, copiava e colava o código no arquivo ele mesmo. Isso causou:
   - Poluição severa da thread principal (*context smearing* / *context rot*);
   - Sobrecarga e lentidão no córtex pré-frontal;
   - Violação direta do papel fiduciário de *Chief Systems Architect* e quebra da Lei 3 (Anti-Satisficing Mandate / "Água no Deserto").

---

## 2. Autópsia Linha a Linha das Falhas Estruturais nos Textos de Governança

### 2.1. `rules/AGENTS.md`

#### A. Linhas 86-93 (Diagrama da Época III: Codificação Concorrente Atômica 1:1)
```text
87: │ ÉPOCA III: Codificação Concorrente Atômica 1:1              │
88: │ • 1 Subagente Codificador por Nó ou Arquivo (relação 1:1)   │
89: │ • Handoff de Alta Fidelidade: lê laudo bruto via view_file  │
90: │ • Zero resumo lossy do pré-frontal; assimilação pericial 100%│
91: │ • Código Zero-Stub, Result<T,E>, Atomic Swap, molas de 2ª ord│
92: │ • Agente Principal atua como Chief Systems Architect        │
```
- **Vulnerabilidade:** A linha 88 define a métrica de alocação (1:1), e a linha 89 impõe a ingestão pericial (`view_file`), mas **não há nenhuma linha prescrevendo a saída motora obrigatória**. Não se exige a mutação física no disco como critério de encerramento da Época III para o subagente.
- **Distorção Semântica da Linha 92:** A frase `"Agente Principal atua como Chief Systems Architect"` foi interpretada estocasticamente como licença para o Agente Principal "receber os módulos sugeridos e aplicá-los", fundindo orquestração com digitação mecânica.

#### B. Linha 115 (Lei 5: Codificação Concorrente Atômica 1:1)
```text
115: 5. **Codificação Concorrente Atômica 1:1:** O Agente Principal atua como coordenador; cada arquivo de produção é implementado por um subagente atômico 1:1.
```
- **Vulnerabilidade:** O termo `"implementado"` em LLMs é epistemicamente frouxo. Para um modelo de linguagem, escrever uma função em um bloco ` ```typescript ` dentro de uma mensagem constitui "implementação".
- **Lacuna Fatal:** A Lei 5 não explicitou que a implementação só existe quando consolidada no disco via `replace_file_content` ou `write_to_file`. Não instituiu o veto de retorno de código textual.

#### C. Linha 154 (Lei 40: Mandato do Roteamento Neural & Urgência de Subagentes)
```text
154: 40. **O Mandato do Roteamento Neural & Urgência de Subagentes (Subagent Instinct & Context Firewall):** É TERMINANTEMENTE PROIBIDO ao Agente Principal investigar código, arquivos ou bugs sozinho na thread principal ("Cegueira Solitária"). Subagentes são as submentes neurais ativas do córtex central e operam como um Firewall de Contexto... A thread principal apenas sintetiza e comanda.
```
- **Vulnerabilidade:** A Lei 40 impõe veto estrito à *investigação solitária* na thread principal, mas silencia sobre a *codificação/digitação solitária*. Quando o Agente Principal recebia o código pronto do subagente, ele não estava "investigando sozinho", portanto julgava que colar o código não violava a Lei 40.

#### D. Linha 156 (Lei 42: Handoff Neural de Alta Fidelidade & Banimento do Telefone Sem Fio)
```text
156: 42. **Handoff Neural de Alta Fidelidade & Banimento do Telefone Sem Fio (Anti-Lossy Compression Invariant):** É TERMINANTEMENTE PROIBIDO ao Agente Principal (córtex pré-frontal) agir como compressor com perda (lossy compressor), mastigando ou resumindo os relatórios de subagentes de investigação antes de despachar o subagente codificador de produção... Codificar baseado em resumos superficiais da thread principal aciona [HARD REJECT: LOSSY_NEURAL_HANDOFF].
```
- **Vulnerabilidade:** A Lei 42 governa estritamente o sentido *Investigador $\to$ Agente Principal $\to$ Codificador*. Ela ignora o sentido reverso *Codificador $\to$ Agente Principal*. Permitiu que o subagente codificador transmitisse sua carga de código via `send_message`, invertendo o fluxo fiduciário e forçando o Agente Principal a atuar como receptor de payload não compilado.

---

### 2.2. `rules/rule1.md` e `skills/swarm_orchestration/SKILL.md`

#### A. Linhas 104-110 (Seção 7: Arquitetura Clean-Context & O Contrato de Payload Cirúrgico)
```markdown
104: 2. **O Contrato de Payload Cirúrgico:**
105:    Todo prompt despachado via `invoke_subagent` deve ser auto-suficiente e estruturado sob quatro pilares inegociáveis:
106:    - **`[BOUNDED_OBJECTIVE]`**: A missão microscópica e delimitada (ex: *"Implementar o adapter de persistência SQLite"*).
107:    - **`[FILE_SLICES]`**: Caminhos absolutos e fatias de linha exatas dos arquivos que o subagente precisa ler.
108:    - **`[SYNAPTIC_CONTRACTS]`**: Contratos upstream consolidados (`[SYNAPTIC_INPUTS]`) extraídos do `synaptic_bus.json`.
109:    - **`[FORENSIC_CRITERIA]`**: Critérios binários específicos [0 ou 1] que o subagente deve satisfazer para homologação.
```
- **Vulnerabilidade:** O contrato cirúrgico omitiu a fixação mecânica da modalidade de execução. Não definiu as tags:
  - `[ACTION_MODE: PHYSICAL_MUTATION]`
  - `[MANDATORY_TOOLS: replace_file_content, write_to_file]`
  - `[OUTPUT_FORMAT: DISK_MUTATION_RECEIPT_ONLY]`
  Sem essas tags, o subagente assume o modo reflexivo/consultivo padrão de LLM.

#### B. Linha 132 (Seção 8.4: O Firewall de Contexto & Banimento de Pesquisa na Thread Principal)
```markdown
132:    - **A utilidade real do subagente:** Atua como uma **sandbox descartável de contexto limpo**. Ele suja as mãos, processa 30.000 tokens de documentação e código bruto, e retorna ao Córtex Central apenas a pepita de ouro lapidada (o laudo ou patch exato), mantendo a thread principal cirúrgica, lúcida e veloz.
```
- **A Evidência Material Central ("Smoking Gun"):** A instrução prescreve literalmente que o subagente `"retorna ao Córtex Central apenas a pepita de ouro lapidada (o laudo ou patch exato)"`.
- **Modo de Falha:** Para um LLM, "retornar o patch exato ao Córtex Central" significa emitir o texto do patch no `send_message`. O subagente conclui legitimamente que seu trabalho é entregar o código ao parent para que este o aplique. É a gênese documental direta da patologia.

#### C. Linhas 154-156 (Seção 9.2: O Circuito Neural em Malha Fechada de 4 Etapas)
```markdown
154: 4. **Leitura Mandatória na Íntegra via `view_file` (Ingestão de Alta Fidelidade):**
155:    A primeira ação motora do subagente de produção DEVE ser invocar `view_file` no arquivo do relatório pericial bruto. Ele absorve diretamente a mente do investigador, com fidelidade de 100%, sem perda de sinal pré-frontal. O córtex pré-frontal atua como orquestrador, barramento sináptico e árbitro — jamais como filtro diluidor.
```
- **Vulnerabilidade:** A Seção 9.2 encerra na etapa 4 ("Leitura"). O circuito não formalizou a etapa 5: a **Escrita Motora Compulsória no Disco** antes da conclusão da tarefa.

#### D. Linhas 159-174 (Seção 10: Checklist Forense de Orquestração de Enxame)
- O checklist possui 11 itens, mas **nenhum audita a natureza da entrega do subagente**. Não havia item verificando se o código foi gravado no filesystem pelo subagente ou se houve devolução de código textual no `send_message`.

---

### 2.3. `skills/hardened_clean_architecture/SKILL.md`

#### A. Linhas 287-294 (Seção 6: Orquestração e Codificação Concorrente por Subagentes)
```markdown
294: 4. **Integração Física pelo Chief Architect:** O Agente Principal integra os módulos, valida a compilação cruzada (`npx tsc --noEmit`), tipos estritos e execução dos testes nativos...
```
- **Vulnerabilidade:** A expressão `"O Agente Principal integra os módulos"` gerou dubiedade sobre o limite de atuação motora do parent. O Agente Principal tomou isso como justificativa para colar o código produzido pelos subagentes.

---

## 3. Dinâmica Psicológica e Mecânica do Colapso do Agente Principal

A autópsia da dinâmica cognitiva do Agente Principal revela cinco fatores de atrito que alimentavam a armadilha do digitador manual:

1. **A Indução Estocástica do Sistema de Mensagens da Plataforma (`<subagent_reminder>`):**
   A camada base da plataforma injeta nos subagentes a instrução:
   *`"Text you generate outside of send_message will NOT be seen by the caller... Put all important information — findings, summaries, conclusions — into your send_message calls instead."`*
   Quando o subagente não recebe uma contra-ordem categórica e explícita proibindo dump de código no `send_message`, o viés de assistente o faz interpretar o código como "important information" a ser colocada na mensagem.
2. **O Viés de Resolução Rápida (The Satisficing Trap):**
   Ao receber o código pronto em uma mensagem, acionar `replace_file_content` na thread principal consome apenas uma tool call imediata. Em contrapartida, repreender o subagente, emitir um `send_message` exigindo a mutação física e aguardar o subagente rodar a ferramenta exige múltiplos ciclos assíncronos. O Agente Principal caía na tentação do atalho fácil, violando a Lei 3 ("Água no Deserto").
3. **Ausência de Trava de Auto-Veto no Córtex:**
   O Agente Principal não possuía uma instrução mecânica imperativa de bloqueio (`[HARD REJECT: ADVISORY_CODE_DUMP]`). Sem esse tripwire, não havia gatilho interno para abortar a digitação manual.
4. **Degradação Progressiva de Foco por Context Smearing:**
   Ao colar o código no arquivo, os diffs e os blocos de texto ficavam residentes na memória da thread principal. Com mais tokens consumidos em dados brutos de código, a capacidade do modelo central de manter a vigilância arquitetural diminuía a cada turno.

---

## 4. Formulações Normativas Exatas para Erradicação Definitiva

Para erradicar a patologia de forma irrecusável e determinística, formulam-se os seguintes ajustes cirúrgicos nos artefatos de governança:

### 4.1. Criação da Lei Constitucional 43 em `rules/AGENTS.md`

```markdown
43. **Mandato do Artífice Motor & Banimento do Subagente Consultivo (The Motor Actuator Mandate):**
É TERMINANTEMENTE PROIBIDO a subagentes despachados para tarefas de implementação, codificação, refatoração ou correção atuar como meros consultores textuais, relatores passivos ou emissores de código em markdown dentro do `send_message`.
- **Obrigatoriedade Motora:** Todo subagente com meta de produção DEVE ser despachado com `TypeName: "self"` e DEVE obrigatoriamente executar a mutação física dos arquivos no disco chamando diretamente as ferramentas motoras (`replace_file_content` ou `write_to_file`) em sua própria sessão.
- **Restrição Estrita de Payload de Retorno:** O payload de retorno via `send_message` de um subagente de produção DEVE conter exclusivamente: (1) caminhos absolutos dos arquivos modificados no disco, (2) resumo dos contratos e invariantes satisfeitos, e (3) telemetria de verificação/testes. É expressamente proibido colar blocos de código de implementação no corpo do `send_message`.
- **Trava de Auto-Veto do Agente Principal (`[HARD REJECT: ADVISORY_CODE_DUMP]`):** Caso um subagente entregue propostas ou blocos de código em markdown no `send_message` sem ter executado a mutação física no disco via ferramentas, o Agente Principal está TERMINANTEMENTE PROIBIDO de digitar, copiar ou aplicar o código pelo subagente. O Agente Principal DEVE rejeitar a mensagem sumariamente (`[HARD REJECT: ADVISORY_SUBAGENT_DETECTED]`), ordenando via `send_message` a mutação física direta via ferramenta, ou liquidar o subagente e re-despachá-lo com restrição motora estrita. O Agente Principal atua exclusivamente como árbitro e maestro — jamais como digitador estocástico.
```

### 4.2. Reformulação Cirúrgica da Lei 5 em `rules/AGENTS.md`

```markdown
5. **Codificação Concorrente Atômica 1:1 & Ação Motora Direta:** O Agente Principal atua soberanamente como coordenador e validador de contratos; cada arquivo ou nó de produção é implementado E mutacionado fisicamente no disco pelo respectivo subagente atômico 1:1 via ferramentas de escrita (`replace_file_content` / `write_to_file`). É expressamente proibido ao subagente devolver código em texto para o Agente Principal digitar, bem como é proibido ao Agente Principal assumir a digitação manual de arquivos delegados ao enxame.
```

### 4.3. Atualização do Diagrama da Época III em `rules/AGENTS.md`

```text
┌─────────────────────────────────────────────────────────────┐
│ ÉPOCA III: Codificação Concorrente Atômica 1:1 (Artífice Motor)│
│ • 1 Subagente Motor por Nó ou Arquivo (TypeName: "self")     │
│ • Mutação física direta no disco (replace_file_content/write)│
│ • Handoff de Alta Fidelidade: lê laudo bruto via view_file  │
│ • Veto absoluto a subagente consultivo e dump de código texto│
│ • Auto-Veto do Parent: proibido digitar código do subagente  │
│ • Código Zero-Stub, Result<T,E>, Atomic Swap, molas de 2ª ord│
│ • Agente Principal atua como Árbitro e Chief Systems Architect│
└─────────────────────────────┬───────────────────────────────┘
```

### 4.4. Atualização em `rules/rule1.md` e `skills/swarm_orchestration/SKILL.md`

1. **Retificação da Linha 132 (Eliminação do Gatilho da Falha):**
   - *Substituir:* `"retorna ao Córtex Central apenas a pepita de ouro lapidada (o laudo ou patch exato)"`
   - *Por:* `"retorna ao Córtex Central apenas a pepita de ouro lapidada: o laudo pericial bruto gravado no disco (na investigação) ou o recibo de mutação física direta com telemetria limpa (na codificação), mantendo a thread principal cirúrgica, lúcida e veloz."`

2. **Inclusão do Pilar Motor no Contrato de Payload Cirúrgico (Seção 7):**
   - Adicionar os campos mandatórios:
     - `[ACTION_MODE]`: `PHYSICAL_MUTATION` (para codificação) ou `ANALYTICAL_INVESTIGATION` (para laudos).
     - `[MANDATORY_TOOLS]`: Declaração explícita de `replace_file_content` e `write_to_file`.
     - `[MOTOR_DIRECTIVE]`: Ordem mecânica: *"Você deve executar a alteração no disco chamando ferramentas. É proibido retornar blocos de código no send_message."*

3. **Inclusão da Etapa 5 no Circuito Neural (Seção 9.2):**
   - `5. Mutação Motora Atômica no Disco & Recibo Fiduciário:`
     *"A ação de encerramento do subagente de produção é invocar replace_file_content ou write_to_file. O subagente valida a gravação física e transmite ao parent unicamente o status e a telemetria, sem nunca transcrever o código no chat."*

4. **Inclusão de Novos Itens no Checklist Forense Binário (Seção 10):**
   - `[ ] Mandato do Artífice Motor Cumprido:` subagentes de produção executaram mutações físicas no disco via ferramentas de escrita; zero dumps de código em markdown no `send_message`.
   - `[ ] Veto ao Parent Digitador Mantido:` Agente Principal absteve-se de digitar ou colar código produzido por subagentes; atuou estritamente como árbitro e validador.
   - `[ ] Despacho Motor Válido:` todos os subagentes de mutação foram despachados com `TypeName: "self"`.

---

## 5. Matriz de Rastreabilidade e Resumo Pericial

| ID da Causa Raiz | Arquivo / Linha de Origem | Mecanismo de Disparo | Remediação Normativa Aplicada |
|---|---|---|---|
| **RC-01** | `rules/AGENTS.md:115` (Lei 5) | Verbo "implementado" interpretado como emissão de texto. | Redefinição da Lei 5 exigindo mutação física direta via ferramentas. |
| **RC-02** | `rules/AGENTS.md:86-93` (Época III) | Falta de menção à ação motora de saída e dubiedade de "Chief Architect". | Atualização do diagrama da Época III com mandatos de artífice motor e auto-veto do parent. |
| **RC-03** | `rules/AGENTS.md:154,156` (Leis 40 e 42) | Falta de veto à digitação pelo Agente Principal e omissão do fluxo reverso. | Criação da Lei 43 (Mandato do Artífice Motor & Trava de Auto-Veto). |
| **RC-04** | `rules/rule1.md:132` / `swarm_orchestration:132` | Texto prescrevendo "retornar o patch exato ao Córtex Central". | Retificação textual: retorno de recibo de mutação física em vez de patch. |
| **RC-05** | `rules/rule1.md:104-110` / `swarm_orchestration:104-110` | Payload cirúrgico sem declaração explícita de `ACTION_MODE` e `MANDATORY_TOOLS`. | Injeção obrigatória de `[ACTION_MODE: PHYSICAL_MUTATION]` e ferramentas motoras. |
| **RC-06** | `rules/rule1.md:159-174` (Checklist Forense) | Ausência de itens de auditoria para mutação direta e postura do parent. | Adição de 3 novos critérios forenses binários no checklist. |

---
*Laudo pericial emitido, auditado e gravado no substrato estigmérgico sob conformidade estrita com o Código Constitucional de Governança Cybernética.*

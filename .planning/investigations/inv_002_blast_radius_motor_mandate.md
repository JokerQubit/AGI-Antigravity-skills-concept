# Laudo Pericial Forense: Raio de Impacto Colateral (Downstream Blast Radius) & Requisitos de Ferramental do Mandato do Artífice Motor

**Identificação do Laudo:** `inv_002_blast_radius_motor_mandate.md`  
**Data/Hora:** `2026-09-17T20:15:00-03:00`  
**Subagente Auditor:** `Downstream Blast Radius & Tooling Auditor` (`TypeName: "self"`)  
**Âncora Sináptica:** `.planning/mission_dossier.md` (Seção D - Dupla Investigativa Fase 1)  
**Status Epistêmico:** `HOMOLOGATED_EMPIRICAL_AUDIT`  
**Veredito de Blast Radius:** `CRITICAL_DOWNSTREAM_RECONFIGURATION_REQUIRED`

---

## 1. Sumário Executivo & Topologia do Raio de Destruição (Blast Radius)

A imposição do **Mandato do Artífice Motor** — diretriz que obriga subagentes de produção na Época III a realizar mutações físicas diretamente no disco via `replace_file_content` e `write_to_file`, banindo a devolução de relatórios e propostas de código em texto via `send_message` — não é uma mera alteração estilística de prompt. Trata-se de uma **mudança ontológica na arquitetura motora do enxame cybernético**.

Ao transformar subagentes de "consultores passivos" em "artífices atuadores", o ecossistema descentraliza a escrita no sistema de arquivos. Essa transição gera impactos de primeira, segunda e terceira ordem em cinco domínios críticos:

```text
                            [MANDATO DO ARTÍFICE MOTOR]
                                         │
        ┌───────────────────┬────────────┴───────┬───────────────────┐
        ▼                   ▼                    ▼                   ▼
[Concorrência de FS]  [Ferramental]       [Contratos & Bus]   [Ecossistema Parceiro]
• Race conditions     • TypeName: "self"  • Synaptic Mutex    • MTA:SA rules.md
• File locks (Win32)  • Amputação de      • HOLD/GO estável   • Banimento do
• Corrupção de AST      "research"        • Disjoint sets       patch manual
• Atomic Swap         • send_message puro • Wave dispatch     • MTACodeCraftsman
```

Abaixo detalham-se os quatro eixos forenses obrigatórios desta auditoria pericial.

---

## 2. Critério 1: Dinâmica de Concorrência de FS & Mitigação Determinística de Race Conditions

### 2.1. Anatomia das Falhas de Escrita Concorrente no Windows/NTFS
Quando múltiplos subagentes são despachados concorrentemente em uma onda (até 15 subagentes simultâneos), a escrita no disco enfrenta três vetores de falha física caso o isolamento de alvos não seja matematicamente absoluto:

1. **Colisão de Locks no Windows (`EBUSY` / `EPERM` / Sharing Violation):**
   - O subsistema de I/O do Windows bloqueia descritores de arquivos abertos para escrita. Se o Subagente A estiver executando `replace_file_content` enquanto o Subagente B tenta abrir o mesmo arquivo, o kernel Win32 emite erro imediato de compartilhamento ou violação de acesso (`Error: EBUSY: resource busy or locked`).
2. **Invalidação Dinâmica de AST & Offset Drift em `replace_file_content`:**
   - A ferramenta `replace_file_content` opera com base em coordenadas discretas: `StartLine`, `EndLine` e `TargetContent`.
   - Se o Subagente A altera as linhas 30–45 de um arquivo compartilhado (acrescentando 10 novas linhas), todos os números de linha subsequente são deslocados em $+10$.
   - O Subagente B, que foi instruído com base no estado anterior a alterar as linhas 60–75, falhará catastroficamente: seu `TargetContent` não coincidirá mais com o intervalo `[StartLine, EndLine]`, ou pior, substituirá o trecho incorreto, corrompendo a sintaxe do arquivo.
3. **Anomalia de Atualização Perdida (*Lost Update Anomaly*) via `write_to_file`:**
   - Se dois subagentes utilizarem `write_to_file` com `Overwrite: true` sobre o mesmo arquivo, o último subagente a completar o I/O sobrescreverá integralmente o trabalho do anterior, destruindo as mutações do primeiro sem deixar rastro de erro no runtime.

### 2.2. A Blindagem Fiduciária: O Princípio dos Conjuntos Disjuntos (1:1 Subagente-por-Arquivo)
Para erradicar qualquer possibilidade de colisão de escrita concorrente, impõe-se a **Lei da Ortogonalidade Estrita de Alvos**:

$$\forall S_i, S_j \in \text{Onda } K, \quad i \neq j \implies \text{TargetFiles}(S_i) \cap \text{TargetFiles}(S_j) = \emptyset$$

- **Invariante:** É terminantemente proibido atribuir o mesmo arquivo físico de destino a mais de um subagente na mesma onda.
- **Granularidade Atômica:** Se uma funcionalidade exige alterações em múltiplos arquivos (ex: `src/core/ports/IStorage.ts`, `src/adapters/storage/SqliteAdapter.ts`, `src/use_cases/saveData.ts`), devem ser despachados 3 subagentes distintos, cada um com propriedade exclusiva e isolada sobre seu respectivo arquivo.

### 2.3. O Protocolo Synaptic Mutex (`CONTRACT_HOLD` / `CONTRACT_STABLE`)
A relação de dependência lógica entre arquivos (ex: o adaptador consome a interface definida na porta) é governada pelas travas de exclusão mútua no barramento sináptico (`.planning/synaptic_bus.json`):

1. **Fase de Definição de Contrato (Onda $K$):**
   - O subagente responsável pelo contrato (ex: `IStorage.ts`) é despachado na Onda $K$.
   - O contrato é sinalizado como `CONTRACT_HOLD` no `synaptic_bus.json`.
   - Nenhum subagente consumidor pode ser despachado enquanto o contrato estiver em `CONTRACT_HOLD`.
2. **Consolidação & Liberação (`CONTRACT_STABLE`):**
   - O subagente conclui a mutação física de `IStorage.ts`, executa `tsc --noEmit` para validar os tipos e relata sucesso.
   - O Agente Principal altera o sinal para `CONTRACT_STABLE` (GO) e consolida a interface sob `[SYNAPTIC_OUTPUTS]`.
3. **Fase de Implementação de Consumidores (Onda $K+1$):**
   - Na onda seguinte, o subagente do `SqliteAdapter.ts` é despachado recebendo o contrato já estável sob `[SYNAPTIC_INPUTS]`.
   - Essa segregação temporal em ondas sequenciais elimina qualquer corrida de contratos ou dependências circulares.

### 2.4. Resiliência por Atomic Swap (POSIX / Win32)
Conforme prescrito na skill `hardened_clean_architecture`, toda gravação de arquivos gerados integralmente via `write_to_file` ou scripts deve adotar o padrão de gravação em arquivo temporário único (`.tmp.<random>`) seguida de substituição atômica via `fs.renameSync`. Isso garante que processos leitores concorrentes nunca observem arquivos parcialmente truncados.

---

## 3. Critério 2: Auditoria de Ferramental (`TypeName: "self"` vs `TypeName: "research"`)

### 3.1. Matriz Anatômica de Ferramentas por Tipo de Subagente
A plataforma Antigravity expõe duas classes nativas de subagentes pré-configurados:

| Ferramenta / Capacidade | `TypeName: "research"` | `TypeName: "self"` | Impacto Operacional |
|---|---|---|---|
| `view_file` | Sim | Sim | Leitura de código e documentação. |
| `grep_search` / `find_by_name` | Sim | Sim | Localização de símbolos e arquivos. |
| `search_web` / `read_url_content` | Sim | Sim | Pesquisa externa (Firewall de Contexto). |
| `send_message` | Sim | Sim | Comunicação de retorno ao Agente Principal. |
| **`replace_file_content`** | **NÃO** | **SIM** | **Mutação cirúrgica de trechos de código.** |
| **`write_to_file`** | **NÃO** | **SIM** | **Criação e substituição atômica de arquivos.** |
| **`run_command`** | **NÃO** | **SIM** | **Compilação, testes (`tsc`, `npm test`, `luac`).** |

### 3.2. A Autópsia da Falha do Subagente "Consultor de Poltrona"
A investigação forense revela o mecanismo causal exato que induz a IA a reverter para o modo consultor:
1. **Amputação Instrumental Involuntária:** O Agente Principal despacha um subagente para implementar uma classe, mas utiliza inadvertidamente `TypeName: "research"`.
2. **Impotência Mecânica:** O subagente analisa o problema com perfeição, identifica a linha do bug, mas ao tentar acionar ferramentas de escrita, descobre que elas não existem em seu namespace.
3. **Recurso de Contingência (The Advisory Fallback):** Para não falhar silenciosamente perante a diretriz *"You MUST use send_message to communicate all results"*, o subagente formata o código em markdown e envia uma mensagem para o Agente Principal contendo: *"Aqui está o código corrigido. Por favor, aplique no arquivo X..."*.
4. **Contaminação em Cascata:** O Agente Principal recebe o payload em texto, é forçado a ler centenas de linhas na thread principal, abre os arquivos e gasta dezenas de milhares de tokens aplicando manualmente os diffs. A concorrência é aniquilada e a thread principal sofre degradação de contexto (*context rot*).

### 3.3. Cláusula Pétrea de Despacho & Trava Mecânica
Fica formalizada a seguinte regra inegociável:
- **Regra de Tipagem de Subagente:** Qualquer subagente despachado com objetivo que envolva criação de arquivo, refatoração, edição de código, correção de bug ou execução de comandos CLI DEVE ser despachado compulsoriamente com `TypeName: "self"`.
- **Despacho Inválido:** O despacho de `TypeName: "research"` para tarefas motoras constitui violação primária e deve ser rejeitado em pré-condição.
- **Higiene Fiduciária do `send_message`:** A mensagem final de um subagente com meta motora (`[ACTION_MODE: PHYSICAL_MUTATION]`) é restrita à **Telemetria de Fechamento**:
  1. Caminhos absolutos dos arquivos modificados no disco.
  2. Linhas alteradas e hash da modificação.
  3. Evidência de compilação ou execução de testes (`$LASTEXITCODE === 0`).
  4. Certificação explícita de Zero-Stub.
  *Veto Absoluto:* É proibido incluir blocos de código não aplicados no `send_message`. A presença de código não persistido no payload da mensagem sem mutação prévia no disco aciona rejeição sumária `[HARD REJECT: ADVISORY_ONLY_SUBAGENT]`.

---

## 4. Critério 3: Avaliação de Impacto e Harmonização no Repositório Parceiro (MTA:SA)

### 4.1. Diagnóstico do Repositório Parceiro
Auditoria pericial realizada sobre o arquivo de governança do Multi Theft Auto: San Andreas:
`D:\MTA San Andreas 1.6\server\mods\deathmatch\resources\.agents\rules\agents.md`

#### Pontos de Fricção Identificados:
1. **Ambiguidade no Papel de Sandbox (Seção 1.2, Linha 25):**
   O texto estabelece: *"O subagente retorna apenas a solução lapidada: 'O limite do engineRequestModel no MTA 1.6 é X; o erro na linha 42 do render.lua foi corrigido no patch Y.'"*
   *Análise Crítica:* A expressão *"o erro ... foi corrigido no patch Y"* é ambígua. Não deixa explícito se o patch foi gravado diretamente no arquivo `.lua` pelo subagente ou se o subagente devolveu o patch em texto para o Agente Principal aplicar.
2. **Gargalo Sequencial no Diagrama de Execução (Seção 5, Linhas 63–78):**
   O fluxograma prescreve que o subagente `MTAEngineScout` pesquisa, inspeciona e *"Grava laudo / patch limpo"*, desaguando em uma caixa subsequente chamada `[Aplicação do Patch & Teste]`.
   *Análise Crítica:* Se `MTAEngineScout` for puramente consultivo, o Agente Principal é quem terá que abrir o arquivo Lua e colar o código. Em servidores MTA:SA com dezenas de resources (`play`, `scoreboard`, `vehicles_shader`, `admin`), o Agente Principal gasta todo o seu orçamento de 2 leituras e satura a thread principal.

### 4.2. Plano de Harmonização para o MTA:SA
Para alinhar o repositório parceiro com a governança soberana v4.1, a diretriz do MTA:SA deve ser atualizada para incorporar o **Mandato do Artífice Motor**:
1. **Bifurcação Clara de Papéis de Subagentes no MTA:SA:**
   - **`MTAScout` (`TypeName: "research"`):** Exclusivo para varredura de documentação da wiki do MTA, busca de limites de memória de shaders e cruzamento exploratório de arquivos de configuração (`meta.xml`, `acl.xml`). Entrega laudo pericial.
   - **`MTACodeCraftsman` (`TypeName: "self"`):** Subagente com mandato motor obrigatório. Recebe a tarefa de alterar os scripts Lua (`client.lua`, `server.lua`, shaders `.fx`), executa a mutação física via `replace_file_content`, roda a checagem estática de sintaxe Lua (`luac -p <script.lua>` via `run_command`), valida que não há erros de sintaxe e somente então emite o aviso de que o recurso está pronto para `/restart <resource>`.
2. **Eliminação do Patch Manual pelo Parent:** O Agente Principal jamais abre arquivos de script para colar código gerado por subagente. Ele delega a mutação ao `MTACodeCraftsman` e apenas orienta o usuário no chat a testar in-game.

---

## 5. Critério 4: Mapeamento Exaustivo dos Pontos de Mutação Normativa no Ecossistema AGI-Research

A imposição do Mandato do Artífice Motor exige mutações coordenadas nos seguintes arquivos mestres:

| Arquivo Alvo | Trecho / Linha Atual | Mutação Prescrita | Justificativa de Causalidade |
|---|---|---|---|
| **`rules/AGENTS.md`** | **Lei 5** (Linhas 66–67): *"O Agente Principal atua como coordenador; cada arquivo de produção é implementado por um subagente atômico 1:1."* | Adicionar cláusula explícita do **Mandato do Artífice Motor**: O subagente codificador DEVE aplicar fisicamente a alteração no disco via ferramentas motoras de escrita. Proibido devolver código não aplicado em `send_message`. | Fecha a lacuna onde subagentes agiam como redatores de código em vez de operadores de filesystem. |
| **`rules/AGENTS.md`** | **Lei 40** (Linhas 94–96): *"Context Firewall & Urgência de Subagentes"* | Reforçar que subagentes de codificação operam como atuadores físicos no disco sob `TypeName: "self"`, preservando o Córtex Central 100% livre de digitação manual de código. | Erradica a sobrecarga do Agente Principal. |
| **`rules/AGENTS.md`** | **Criação da Lei 43** | Formalizar a **Lei 43: O Mandato do Artífice Motor & Veto ao Subagente Consultor**: Subagentes despachados em fases de produção ou correção que emitirem propostas discursivas sem prévia mutação física comprovada no disco serão sumariamente rejeitados via `[HARD REJECT: ADVISORY_ONLY_SUBAGENT]`. | Estabelece base constitucional inviolável. |
| **`rules/rule1.md`** & **`skills/swarm_orchestration/SKILL.md`** | **Seção 7 / 8** (Linhas 105–110 / 118–133): Contrato de Payload Cirúrgico | Inclusão mandatória da tag `[ACTION_MODE: PHYSICAL_MUTATION]` no payload de subagentes de produção, impondo `TypeName: "self"` e proibindo dumps de código no `send_message`. | Padroniza a sintaxe de despacho motor. |
| **`rules/rule1.md`** & **`skills/swarm_orchestration/SKILL.md`** | **Seção 10**: Checklist Forense | Adicionar dois novos itens binários de auditoria: `[ ] Mandato Motor Respeitado (arquivos alterados no disco via ferramentas de escrita)` e `[ ] TypeName: "self" verificado para subagentes de mutação`. | Permite ao Subagente Juiz reprovar entregas consultivas. |
| **`skills/hardened_clean_architecture/SKILL.md`** | **Seção 6** (Linhas 286–295): Subagent Craft | Blindar a instrução de que cada subagente codificador executa fisicamente a escrita do arquivo de porta, entidade ou adaptador no disco via `replace_file_content` / `write_to_file`, seguido de validação com `tsc --noEmit`. | Garante que Clean Architecture seja aplicada pelo subagente, não pelo parent. |
| **`skills/autonomous_computer_use/SKILL.md`** | **Seção 1** (Linhas 15–51): Ciclo OODA | Explicitar que o Ciclo OODA do subagente motor fecha obrigatoriamente no quadrante **ACT & VERIFY**, utilizando Nível 1 (Arquivo) e Nível 2 (CLI) para consumar a alteração no disco e validar a telemetria fria. | Fecha o circuito cibernético de ação motora autônoma. |
| **`skills/adaptive_token_governance/SKILL.md`** | **Tabela de Expedientes** (Linha 36): Expediente 4 | Confirmar que subagentes codificadores 1:1 rodam sob `TypeName: "self"` no modo Flash Medium ou High, com orçamento dimensionado para escrita e compilação. | Alinhamento fiduciário de tokens. |

---

## 6. Checklist Forense Binário de Homologação de Blast Radius (Lei 41)

> Auditado para autorizar a transição da Época I para a Época II.

- [x] **Risco de Concorrência de FS Mapeado:** Identificadas causas de `EBUSY`, corrupção por offset em `replace_file_content` e Lost Updates.
- [x] **Salvaguarda de Ortogonalidade Estabelecida:** Proibição formal de alocação concorrente do mesmo arquivo a múltiplos subagentes na mesma onda ($\text{FileSet}(S_i) \cap \text{FileSet}(S_j) = \emptyset$).
- [x] **Synaptic Mutex Validado:** Sequenciamento garantido entre definição de interfaces (`CONTRACT_HOLD` $\to$ `CONTRACT_STABLE`) na Onda $K$ e consumo na Onda $K+1$.
- [x] **Tooling Profile Dissecado:** Identificada a incapacidade mecânica de `TypeName: "research"` para escrita e estabelecida a obrigatoriedade de `TypeName: "self"` para subagentes motores.
- [x] **Higiene de `send_message` Definida:** Payload de retorno restrito à telemetria fria de arquivos alterados, linhas, hashes e status de testes; código solto banido.
- [x] **Impacto no MTA:SA Mapeado:** Proposta de bifurcação entre `MTAScout` (pesquisa) e `MTACodeCraftsman` (mutação direta em `.lua` e teste com `luac`).
- [x] **Mutações Normativas Mapeadas:** Linhas e cláusulas exatas mapeadas em `rules/AGENTS.md`, `rules/rule1.md`, `skills/swarm_orchestration/SKILL.md`, `skills/hardened_clean_architecture/SKILL.md` e `skills/autonomous_computer_use/SKILL.md`.

---
*Laudo pericial emitido, persistido e auditado pelo Subagente Auditor de Raio de Destruição e Ferramental.*

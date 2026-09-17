# Dossiê Executivo de Missão: Mandato do Artífice Motor & Erradicação do Subagente Consultor

**Portão de Ingestão Mandatória Ubíqua — Época 0 (v4.1)**  
**Hash da Demanda Crua (SHA-256):** `2e4ac3d69239e1fd8318908b5834493d53ef9fdb636f8e8ab6ae6c853071929d`  
**Demanda Crua:** `"faça os sub agent alterar o codigo inves de apenas retornar relatorios para a IA"`  
**Data/Hora:** `2026-09-17T20:05:00-03:00`  
**Classificação Soberana de Missão:** `DIRECT_OPERATIONAL`  
**Piso de Nós em Disco (`nodes_floor`):** `0` (Zero arquivos em `.planning/nodes/`; 100% de tokens preservados para execução e especialização motora do esquadrão)  
**Modo Flash Prescrito:** `Flash Low` (Planejamento/Ingestão) → `Flash Medium` (Investigação & Codificação) → `Flash High` (Gauntlet Red Team)

---

## 1. Classificação de Modo & Desconstrução Forense em 4 Camadas (Lei 38)

### 1.1. Análise de Custo-Complexidade (ACC) & Classificação Soberana
- **Classificação:** `DIRECT_OPERATIONAL`.
- **Justificativa Fiduciária:** A demanda visa a correção comportamental e a blindagem normativa de execução motora dos subagentes no ecossistema de governança (`rules/` e `skills/`). Não se trata da criação de uma nova plataforma verde de software do zero (o que demandaria o piso arquitetural de $\ge 100$ nós), mas sim de uma calibração cirúrgica e profunda nos protocolos de orquestração de enxame, regras constitucionais e templates de prompt de despacho.
- **Piso de Nós (`nodes_floor`):** `0`. É terminantemente proibido poluir o repositório com arquivos de nós em `.planning/nodes/`. O plano de intervenção é unificado e executado diretamente através do esquadrão sob o `implementation_plan.md`.

---

### 1.2. Desconstrução Forense em 4 Camadas

#### Camada 1: Contratos Explícitos (CE)
- **CE-01:** Subagentes despachados para tarefas de implementação ou correção de código DEVEM executar fisicamente as alterações nos arquivos alvo utilizando as ferramentas motoras de escrita (`replace_file_content` ou `write_to_file`).
- **CE-02:** É expressamente proibido ao subagente de codificação limitar-se a redigir relatórios, sugestões de código em blocos markdown ou propostas de diff devolvidas via `send_message` para que o Agente Principal (parent) as digite manualmente.
- **CE-03:** A devolução de propostas em texto no `send_message` sem a prévia e comprovada mutação física dos arquivos no disco passa a constituir falha sumária da tarefa (`[HARD REJECT: ADVISORY_ONLY_SUBAGENT]`).

#### Camada 2: Contratos Implícitos (CI) & Arquiteturais
- **CI-01 (Bifurcação Funcional de Subagentes):** O ecossistema deve segregar com precisão matemática duas classes ontológicas de subagentes:
  1. *Subagentes de Investigação/Auditoria:* Despachados com `TypeName: "research"` ou `"self"` focados em diagnóstico, telemetria, pesquisa web e auditoria. Seu entregável exclusivo é um laudo pericial gravado fisicamente em disco (`.planning/investigations/inv_<slug>.md`).
  2. *Subagentes de Codificação/Produção (Artífices Motores):* Despachados compulsoriamente com `TypeName: "self"` (que herda ferramentas de escrita e shell). Seu entregável obrigatório é a mutação física dos arquivos de produção no disco via `replace_file_content` / `write_to_file` e validação com testes via `run_command`.
- **CI-02 (Mandato Motor no Prompt de Despacho):** O prompt injetado no subagente de codificação não pode conter ambiguidades retóricas como "analise e sugira alterações". Ele DEVE conter o bloco mandatório `[ACTION_MODE: PHYSICAL_MUTATION]` com a ordem taxativa de alterar os arquivos e rodar testes de sanidade antes de qualquer comunicação de retorno.
- **CI-03 (Papel Fiduciário do Agente Principal):** O Agente Principal (parent) atua como Chief Systems Architect e orquestrador do barramento sináptico. Se o Agente Principal receber uma proposta de código via `send_message` e começar a aplicar o diff manualmente na thread principal, ele incorre em violação gravíssima de orquestração (perda de concorrência e contaminação de contexto). O parent DEVE rejeitar a entrega e exigir a execução motora do subagente.
- **CI-04 (Higiene de `send_message`):** A ferramenta `send_message` do subagente de produção deve transmitir unicamente o laudo de fechamento atômico: arquivos alterados no disco, linhas modificadas, hashes, status de compilação/testes (`$LASTEXITCODE === 0`) e confirmação de zero stubs. Proibido despejar dumps de código não aplicados no `send_message`.

#### Camada 3: Exercício Pre-Mortem Forense (T+6 Meses)
*Cenário Hipotético de Falha:* Decorridos 6 meses, o sistema volta a apresentar estagnação: o Agente Principal gasta milhares de tokens colando código manualmente, a concorrência 1:1 é abandonada e regressões silenciosas voltam a ocorrer.  
*Autópsia das Causas Raízes Microscópicas:*
1. **Falha de Permissão de Ferramenta (Tool Siloing):** O subagente foi despachado com `TypeName: "research"` para implementar código. Como "research" só tem ferramentas de leitura, o modelo se viu incapaz de escrever no disco e "recorreu" a enviar o código em texto via `send_message`.
   *Contramedida:* Regra inegociável exigindo `TypeName: "self"` para qualquer subagente que realize mutação de código.
2. **Ambiguidade Semântica no Prompt do Subagente:** O prompt dizia "Elabore a implementação do componente X". O LLM interpretou "elaborar" como ato discursivo/intelectual e produziu uma redação técnica.
   *Contramedida:* Injeção do bloco de comando imperativo motor `[MANDATO_DO_ARTIFICE_MOTOR]` no topo de todo prompt de codificação.
3. **Codicilina de Subagente (Subagent Reminder Drift):** O reminder do sistema diz *"You MUST use send_message to communicate all results..."*, o que leva o subagente a acreditar que seu produto final é a mensagem, e não o arquivo no disco.
   *Contramedida:* Instrução expressa no prompt de despacho: "Sua mensagem via `send_message` é apenas o relatório de conclusão da alteração física já realizada no disco. Alterar o disco é pré-requisito mandatório antes de chamar `send_message`."

#### Camada 4: Duplo-Check Fiduciário & Regra de Dois Homens (Two-Man Rule)
- A alteração proposta fecha o ciclo mecânico completo? Sim.
- Remove a tentação da IA de atuar como "consultora de poltrona"? Sim.
- Garante que a governança adaptativa de tokens seja respeitada? Sim, preservando a thread principal de poluição de código e transferindo o esforço motor para os subagentes atômicos.

---

## 2. Roadmap Mecânico Passo a Passo Determinístico

O plano de intervenção abrange cinco mutações físicas coordenadas nos arquivos de governança do ecossistema:

```text
┌────────────────────────────────────────────────────────────────────────┐
│               FLUXO DETERMINÍSTICO DE IMPLEMENTAÇÃO                    │
├────────────────────────────────────────────────────────────────────────┤
│ 1. ÉPOCA I: Ativação da Dupla Investigativa (Alfa & Beta)              │
│    • Alfa: Mapeamento da raiz patológica nos prompts de despacho       │
│    • Beta: Mapeamento de blast radius nas skills e regras              │
│ 2. ÉPOCA II: implementation_plan.md formal & Parada Fiduciária         │
│ 3. ÉPOCA III: Codificação Concorrente 1:1 por Subagentes Motores      │
│    • Subagente 1: rules/AGENTS.md (Constituição & Leis 5 e 43)        │
│    • Subagente 2: rules/rule1.md & skills/swarm_orchestration/SKILL.md │
│    • Subagente 3: skills/hardened_clean_architecture/SKILL.md & OODA  │
│ 4. ÉPOCA IV: Gauntlet Adversarial Independente (Subagente Juiz)        │
└────────────────────────────────────────────────────────────────────────┘
```

### Detalhamento Passo a Passo:

#### Passo 1: Despacho da Dupla Investigativa (Two-Mind Minimum)
- **Subagente Alfa (Causal Root Cause):** Investiga e disseca por que os subagentes optaram por relatar em vez de mutar, analisando a interação entre `TypeName`, permissões de MCP/ferramentas e a semântica de `send_message`. Grava `.planning/investigations/inv_001_root_cause_advisory_subagents.md`.
- **Subagente Beta (Downstream Blast Radius):** Mapeia todos os pontos em `rules/AGENTS.md`, `rules/rule1.md`, `skills/swarm_orchestration/SKILL.md`, `skills/hardened_clean_architecture/SKILL.md` e `skills/autonomous_computer_use/SKILL.md` que necessitam da injeção do Mandato do Artífice Motor. Grava `.planning/investigations/inv_002_blast_radius_motor_mandate.md`.

#### Passo 2: Consolidação da Época II no `implementation_plan.md`
- Apresentação da matriz de alterações exatas, contratos alterados e travas HOLD/GO no barramento sináptico.
- Parada mecânica aguardando confirmação explícita.

#### Passo 3: Execução da Época III por Subagentes Codificadores Motores (`TypeName: "self"`)
- **Mutação A (`rules/AGENTS.md`):**
  * Atualização da Lei 5 (Codificação Concorrente Atômica 1:1): Adicionar a cláusula pétrea do Mandato do Artífice Motor.
  * Criação formal da Lei 43 (ou fortalecimento da Lei 5 e 42): Proibição categórica de subagentes consultivos/relatores em fases de produção. A devolução de código não aplicado via `send_message` aciona `[HARD REJECT: ADVISORY_ONLY_SUBAGENT]`.
- **Mutação B (`rules/rule1.md` & `skills/swarm_orchestration/SKILL.md`):**
  * Criação da Seção 7.1: *O Protocolo do Artífice Motor & O Veto ao Subagente Consultor*.
  * Definição do Template Obrigatório de Despacho de Codificação contendo `[ACTION_MODE: PHYSICAL_MUTATION]` e ordem imperativa de chamada a `replace_file_content` / `write_to_file`.
  * Definição do formato restrito de `send_message` pós-mutação (apenas telemetria, diff de linhas e status de testes).
  * Atualização do Checklist Forense de Orquestração (Seção 10).
- **Mutação C (`skills/hardened_clean_architecture/SKILL.md`):**
  * Atualização da Seção 6: reforço do comportamento motor autônomo dos subagentes na implementação dos arquivos de portas, adaptadores e entidades.
- **Mutação D (`skills/autonomous_computer_use/SKILL.md`):**
  * Inclusão do ciclo OODA para subagentes motores, enfatizando a primazia da ação direta no disco sobre a deliberação retórica.

#### Passo 4: Auditoria Adversarial Independente (Época IV)
- Despacho do Subagente Juiz Red Team (`TypeName: "self"`) para executar o Gauntlet em 4 passadas:
  * Passada 0: Auditoria binária de checklists forenses.
  * Passada 1: Ceticismo e busca por brechas residuais onde subagentes possam reverter para consultores.
  * Passada 2: Zero-Stub e consistência léxica.
  * Passada 3: Verificação de impacto em testes e integridade de git.

---

## 3. Matriz de Regras e Skills Ativadas com Justificativa de Primeiros Princípios

| Regra / Skill | Justificativa por Primeiros Princípios |
|---|---|
| **`rules/AGENTS.md` (Lei 1, 5, 18, 40, 42)** | *Primazia do Entregável Real & Ação Motora Descentralizada:* O valor de um sistema de software existe na matéria física (bits gravados no disco, arquivos compilados, testes passando). Delegar raciocínio para subagentes sem delegar a execução motora transforma o Córtex Central em um digitador estocástico sobrecarregado, degradando o throughput e induzindo esquecimento. |
| **`rules/rule1.md` & `swarm_orchestration`** | *Topologia de Malha Ativa vs. Ilhas de Consulta:* Em um enxame cybernético, cada nó deve ser um atuador (*actuator*), não um conselheiro passivo. Se um nó apenas emite texto, o canal de comunicação se satura com tráfego inútil de dados não estruturados. |
| **`rules/rule2.md` & `adaptive_token_governance`** | *Conservação Fiduciária de Contexto:* Fazer o Agente Principal ler relatórios de subagentes e transcrever código consome tokens desnecessariamente na thread principal. A alteração direta pelo subagente preserva o orçamento de contexto para orquestração de alto nível. |
| **`hardened_clean_architecture`** | *Atomicidade & Isolamento Estrutural:* Cada arquivo de domínio ou adaptador deve ser construído de ponta a ponta pelo seu subagente designado, sem intervenções parciais ou stubs. |
| **`autonomous_computer_use`** | *Ciclo OODA Motor em Malha Fechada:* A observação e orientação só têm valor se desaguarem na Ação (Act). Subagente sem Ação motora é um loop aberto estéril. |
| **`forensic_adversarial_auditor`** | *Verificação Empírica Indefectível:* O auditor não aceita "intenção de código"; audita a alteração gravada e persistida no filesystem. |

---

## 4. Bespoke Dynamic Squad Blueprint (Seção D: Ordem Executiva Compulsória de Despacho)

> **AVISO DE GATILHO MECÂNICO (Lei 26 & 40):** A presente seção é uma ordem executiva de despacho imediato. O Agente Principal está terminantemente proibido de mutacionar arquivos sem despachar os subagentes especializados abaixo.

### Fase 1: Dupla Investigativa (Época I - Two-Mind Minimum)

#### 1. Subagente Alfa: Root Cause Forensic Investigator
- **Role:** `Root Cause Forensic Investigator`
- **TypeName:** `self`
- **Model:** `flash`
- **Clean-Context Payload:**
  - `[BOUNDED_OBJECTIVE]`: Investigar a causa raiz microscópica da patologia de subagentes consultivos. Mapear arquivos `rules/AGENTS.md`, `rules/rule1.md`, `skills/swarm_orchestration/SKILL.md` e prompts de despacho anteriores, identificando onde faltou a ordem motora imperativa.
  - `[FILE_SLICES]`: `rules/AGENTS.md:110-157`, `rules/rule1.md:100-160`, `skills/swarm_orchestration/SKILL.md:95-160`.
  - `[MY_SWARM_DELIVERABLE]`: Gravar laudo pericial detalhado em `.planning/investigations/inv_001_root_cause_advisory_subagents.md`.
  - `[FORENSIC_CRITERIA]`: Identificar pelo menos 3 causas estruturais nos textos das regras/skills que permitiram o desvio de função.

#### 2. Subagente Beta: Downstream Blast Radius & Tooling Auditor
- **Role:** `Downstream Blast Radius & Tooling Auditor`
- **TypeName:** `self`
- **Model:** `flash`
- **Clean-Context Payload:**
  - `[BOUNDED_OBJECTIVE]`: Mapear o raio de impacto colateral da imposição do Mandato do Artífice Motor. Verificar requisitos de permissões (`TypeName: "self"` vs `"research"`), regras de concorrência (`CONTRACT_HOLD`/`CONTRACT_STABLE`) e possíveis conflitos em escritas paralelas.
  - `[FILE_SLICES]`: `skills/hardened_clean_architecture/SKILL.md:280-310`, `skills/adaptive_token_governance/SKILL.md:1-80`, `skills/autonomous_computer_use/SKILL.md:1-100`.
  - `[MY_SWARM_DELIVERABLE]`: Gravar laudo pericial detalhado em `.planning/investigations/inv_002_blast_radius_motor_mandate.md`.
  - `[FORENSIC_CRITERIA]`: Mapear contratos que devem ser protegidos contra corrida de arquivos e diretrizes de auto-cura.

---

### Fase 2: Subagentes Codificadores Motores 1:1 (Época III)

> *Nota:* A ser disparada na Época III após aprovação do `implementation_plan.md`. Cada subagente recebe a instrução imperativa de ler o laudo pericial da Fase 1 antes de executar a mutação física.

#### 3. Subagente Codificador 1: Constitutional Governance Craftsman
- **Role:** `Constitutional Governance Craftsman`
- **TypeName:** `self`
- **Model:** `flash`
- **Missão:** Modificar fisicamente `rules/AGENTS.md` e `rules/rule1.md` aplicando o Mandato do Artífice Motor, a cláusula pétrea anti-consultor e a atualização das Leis 5, 40, 42 e criação da Lei 43.
- **Ferramentas Obrigatórias:** `replace_file_content`, `view_file`.
- **Ação Motora:** Mutação física direta no disco. Proibido retornar propostas em markdown.

#### 4. Subagente Codificador 2: Swarm Playbook & Architecture Craftsman
- **Role:** `Swarm Playbook & Architecture Craftsman`
- **TypeName:** `self`
- **Model:** `flash`
- **Missão:** Modificar fisicamente `skills/swarm_orchestration/SKILL.md` e `skills/hardened_clean_architecture/SKILL.md` integrando os protocolos do Artífice Motor, templates de despacho motor e checklists binários de validação.
- **Ferramentas Obrigatórias:** `replace_file_content`, `view_file`.
- **Ação Motora:** Mutação física direta no disco. Proibido retornar propostas em markdown.

---

### Fase 3: Auditoria Adversarial Independente (Época IV)

#### 5. Subagente Juiz: Epistemic Red Team Judge
- **Role:** `Epistemic Red Team Judge`
- **TypeName:** `self`
- **Model:** `flash`
- **Missão:** Conduzir o Gauntlet Adversarial de 4 passadas, auditando se os arquivos no disco contêm as regras de bloqueio e se foi eliminada qualquer possibilidade de subagentes atuarem como relatores passivos. Emite veredito formal `[HOMOLOGATED_SUCCESS]` ou `[HARD REJECT]`.

---

## 5. Matriz de Modos de Quebra e Pre-Mortem Forense

| ID | Modo Silencioso de Quebra ($X \to Y \to \text{Falha}$) | Severidade | Gatilho Causal | Contramedida Fiduciária Determinística |
|---|---|---|---|---|
| **MQ-01** | Subagente de codificação despachado como `TypeName: "research"`. O subagente não possui ferramentas de escrita (`replace_file_content`) e é forçado a devolver o código em texto via `send_message`. | Crítica | Despacho incorreto pelo Agente Principal. | Regra mecânica em `rules/AGENTS.md`: subagentes com meta de implementação DEVEM ser despachados compulsoriamente com `TypeName: "self"`. Despacho com "research" para código dispara veto sumário. |
| **MQ-02** | Subagente com `TypeName: "self"` ignora as ferramentas motoras por viés estocástico de assistente ("Aqui está o código sugerido para você colar"). | Alta | Prompt fraco ou ausência de trava comportamental no prompt de despacho. | Inclusão mandatória do bloco `[ACTION_MODE: PHYSICAL_MUTATION]` e regra de que retorno de código no `send_message` sem mutação física no disco é rejeição imediata com re-despacho forçado. |
| **MQ-03** | Múltiplos subagentes tentando editar o mesmo arquivo simultaneamente gerando race conditions e conflitos de git (`EBUSY` / conflito de chunks). | Alta | Concorrência sem particionamento de arquivos. | Travas de concorrência sináptica (`synaptic_bus.json`): regra estrita de 1 subagente por arquivo e mutex sináptico `CONTRACT_HOLD`/`CONTRACT_STABLE`. |
| **MQ-04** | Agente Principal cede à tentação de copiar o código do `send_message` e editar o arquivo ele mesmo, quebrando o papel de Chief Systems Architect. | Média | Preguiça algorítmica do Agente Principal. | Trava constitucional: se o parent detectar que o subagente não chamou ferramentas de escrita, o parent está PROIBIDO de digitar o código; deve enviar `send_message` ordenando a mutação ou re-despachar. |

---

## 6. Matriz de Checklists Forenses e Critérios Estritos de Aceite Fiduciário (Lei 41)

> Esta matriz será auditada item a item pelo Subagente Juiz Red Team na Época IV. A ausência de evidência física no disco em qualquer item reprova a entrega.

| # | Item de Verificação Fiduciária | Evidência Exigida no Disco | Status |
|---|---|---|---|
| **CHK-01** | **Mandato do Artífice Motor em `rules/AGENTS.md`** | Presença formal da cláusula pétrea na Lei 5 e/ou Lei 43 banindo subagentes consultivos e exigindo mutação direta via ferramentas de escrita. | `[PENDENTE_EXECUCAO]` |
| **CHK-02** | **Protocolo do Artífice Motor em `rules/rule1.md`** | Nova seção detalhando o fluxo motor do subagente, proibição de dump de código no `send_message` e regras de encerramento da tarefa. | `[PENDENTE_EXECUCAO]` |
| **CHK-03** | **Template de Despacho de Mutação em `skills/swarm_orchestration/SKILL.md`** | Inclusão do template de prompt com `[ACTION_MODE: PHYSICAL_MUTATION]`, `TypeName: "self"` e diretrizes de rejeição imediata. | `[PENDENTE_EXECUCAO]` |
| **CHK-04** | **Blindagem de Clean Architecture em `skills/hardened_clean_architecture/SKILL.md`** | Atualização da Seção 6 reforçando que os nós são implementados diretamente pelos subagentes no disco, sem intermediação manual do parent. | `[PENDENTE_EXECUCAO]` |
| **CHK-05** | **Zero Nós em Disco (`nodes_floor: 0`)** | Diretório `.planning/nodes/` limpo ou sem acréscimo de nós espúrios; 100% de tokens focados no código real. | `[CONFORME]` |
| **CHK-06** | **Two-Mind Minimum Respeitado** | Laudos `inv_001_root_cause_advisory_subagents.md` e `inv_002_blast_radius_motor_mandate.md` persistidos no disco na Época I. | `[PENDENTE_EXECUCAO]` |
| **CHK-07** | **Zero-Stub Permanente** | Nenhuma menção a `TODO`, `pass` ou stubs nos arquivos alterados de governança. | `[PENDENTE_EXECUCAO]` |
| **CHK-08** | **Null-Vocabulary Respeitado** | Nenhum clichê de assistente, preâmbulo bajulador ou encerramento oco nos artefatos de missão. | `[CONFORME]` |
| **CHK-09** | **Selo Estigmérgico Válido** | `.planning/refiner_seal.json` gravado com hash coincidente e status `SEALED_VALID`. | `[CONFORME]` |

---
*Dossiê compilado e selado pelo Compilador Epistêmico do Portão de Ingestão Mandatória Ubíqua.*

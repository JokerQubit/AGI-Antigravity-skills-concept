---
name: swarm_orchestration
description: "v4.0 — Universal Cognitive Parity — Orquestração Cybernética de Enxame & Governança Neural. Playbook operacional para gestão do Barramento Sináptico Neural (synaptic_bus.json), exclusão mútua sináptica (HOLD/GO), síntese dinâmica sob medida de esquadrões (Bespoke Dynamic Squads), identidade e autoconsciência de enxame, e veto técnico entre pares (Peer Veto)."
---

# Swarm Orchestration & Cybernetic Neural Mesh Playbook — v4.0

Playbook operacional de engenharia de coordenação de enxames de inteligência artificial de alta escala, governando a comunicação inter-agentes, barramento sináptico, exclusão mútua em contratos estruturais, auto-organização dinâmica sob medida e deliberação adversarial entre pares.

---

## 1. O Barramento Sináptico Neural (`synaptic_bus.json`)

Subagentes operando em enxame não são silos isolados, mas neurônios de uma malha viva. Toda decisão, contrato de dados ou primitiva gerada por um subagente deve ser propagada para a rede através do arquivo estigmérgico `.planning/synaptic_bus.json`:

```json
{
  "bus_version": "4.0.0",
  "active_expediente": 2,
  "synaptic_signals": {
    "CONTRACT_STATUS": {
      "src/core/ports/IStorage.ts": "CONTRACT_STABLE",
      "src/core/types/Order.ts": "CONTRACT_HOLD"
    }
  },
  "propagated_synapses": [
    {
      "origin_node": "node_001_domain_entity.md",
      "emitted_by": "DomainEntityArchitect",
      "synaptic_output": "export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };",
      "consumed_by": ["node_002_storage_adapter.md", "node_003_use_case.md"]
    }
  ]
}
```

### Protocolo de Propagação Feedforward:
1. **Onda $K$:** Subagentes emitem seus nós contendo explicitamente a tag `[SYNAPTIC_OUTPUTS]`.
2. **Consolidação:** O Agente Principal atua como *Chief Systems Architect*, lê as saídas, valida consistência e atualiza `synaptic_bus.json`.
3. **Injeção na Onda $K+1$:** Os subagentes da próxima onda recebem no prompt as sinapses consolidadas relevantes sob a tag `[SYNAPTIC_INPUTS]`. A onda subsequente constrói diretamente sobre a causalidade comprovada da onda anterior ($X \to Y \to Z$).

---

## 2. As Travas de Concorrência Sináptica & Protocolo HOLD/GO (Synaptic Mutex)

Subagentes que definem ou refatoram contratos estruturais, tipos compartilhados ou portas arquiteturais (`src/core/ports/`) operam sob **exclusão mútua (*Synaptic Mutex*)**:

- **Sinal `CONTRACT_HOLD`:** Enquanto o contrato estiver em elaboração pelo nó emissor, ele sinaliza `CONTRACT_HOLD` no barramento sináptico.
- **Veto a Código Especulativo:** Subagentes consumidores estão terminantemente proibidos de gerar código especulativo sobre interfaces instáveis, devendo suspender a execução ou aguardar o sinal determinístico `CONTRACT_STABLE (GO)`.
- **Eliminação de Colisões:** Este mecanismo previne refatorações concorrentes conflitantes, colisão de arquivos e retrabalho sob concorrência massiva.

---

## 3. Síntese Dinâmica de Esquadrões Sob Medida (Bespoke Dynamic Squads)

**Veto Absoluto a Templates Estáticos de Equipes:** Impor listas cegas pré-formatadas de papéis (ex: sempre despachar "1 pesquisador, 1 arquiteto, 1 testador") induz a máquina à preguiça estocástica e resumos repetitivos.

### Princípio da Síntese Pela Física do Problema:
O Agente Principal DEVE dissecar a topologia única e os modos silenciosos de falha daquela demanda específica e sintetizar especialidades extremas sob medida:
- Se envolver áudio: `DSP Buffer & Web Audio Thread Specialist`.
- Se envolver concorrência/storage: `Atomic Swap & File Descriptor Locks Engineer`.
- Se envolver animação: `GPU Compositor & Spring Physics Craftsman`.
- Se envolver transações: `Idempotent Webhook & Compensating Action Architect`.

Toda equipe nasce da física do problema e se dissolve com a entrega do artefato consolidado.

---

## 4. Identidade e Autoconsciência Estigmérgica de Enxame

Todo subagente despachado opera com consciência lúcida de seu papel no hipergrafo coletivo, registrando no topo de sua análise:
1. **Identidade Atômica:** `[MY_SWARM_ROLE]` (especialidade exata e escopo delimitado).
2. **Âncora Sináptica:** `[MY_SYNAPTIC_ANCHOR]` (quais contratos upstream consome).
3. **Entregável Estrito:** `[MY_SWARM_DELIVERABLE]` (arquivo e artefato exato que deve persistir no disco para destravar os pares).

**Veto ao Desvio de Função (*Role Drift*):** É proibido ao subagente invadir escopo alheio ou agir como entidade isolada sem propósito sistêmico.

---

## 5. Auditoria Cruzada & Veto Técnico Entre Pares (Peer Veto)

Subagentes adjacentes que compartilham fronteiras de dados ou concorrência possuem poder de revisão bilateral:
- Caso um nó de interface proponha um padrão que degrade a latência, viole o frame rate de 60fps ou imponha concorrência insegura sobre o armazenamento, o subagente de domínio impactado DEVE emitir um veto técnico formal (`[PEER_VETO: CONTRACT_REJECTED]`).
- Nenhuma primitiva contestada pode ser consolidada no `graph.json` ou transicionar para a Época II sem resolução e consentimento mútuo entre os pares.

---

## 6. Trava Epistêmica & Banimento da Teimosia (`[EPISTEMIC_HALT]`)

Diante de qualquer incerteza, ambiguidade ou lacuna documental ($\varepsilon > 0$), é proibido à IA avançar obstinadamente no palpite ou gerar stubs. O sistema deve acionar imediatamente a **Trava Epistêmica**:
1. Nomear formalmente a lacuna em seu raciocínio.
2. Despachar uma sonda de investigação empírica ou solicitar alinhamento de negócio ao usuário.
3. Somente após a liquidação definitiva da incerteza a esteira está autorizada a prosseguir.

---

## 7. Arquitetura Clean-Context & Higiene de Payloads (Anti-Context Smearing)

Subagentes operacionais e especialistas não devem ser sufocados com o histórico acumulado de conversas da thread principal. Toda invocação obedece à **Higiene Fiduciária de Payload**:

1. **Janela de Contexto Limpa (*Clean Window*):**
   - O subagente opera focado unicamente no seu entregável atômico.
   - É expressamente proibido transferir logs de conversas passadas, monólogos reflexivos da thread principal ou ruído de turnos anteriores para especialistas de implementação.
2. **O Contrato de Payload Cirúrgico:**
   Todo prompt despachado via `invoke_subagent` deve ser auto-suficiente e estruturado sob quatro pilares inegociáveis:
   - **`[BOUNDED_OBJECTIVE]`**: A missão microscópica e delimitada (ex: *"Implementar o adapter de persistência SQLite"*).
   - **`[FILE_SLICES]`**: Caminhos absolutos e fatias de linha exatas dos arquivos que o subagente precisa ler.
   - **`[SYNAPTIC_CONTRACTS]`**: Contratos upstream consolidados (`[SYNAPTIC_INPUTS]`) extraídos do `synaptic_bus.json`.
   - **`[FORENSIC_CRITERIA]`**: Critérios binários específicos [0 ou 1] que o subagente deve satisfazer para homologação.

---

## 8. O Mandato do Roteamento Neural & Urgência de Subagentes (The Subagent Instinct)

Subagentes não são utilitários opcionais nem ferramentas de apoio secundárias: são **submentes neurais ativas do próprio agente**, particionando a inteligência para atingir profundidade analítica inatingível por uma thread solitária.

### Invariantes de Urgência de Enxame:
1. **Veto à Investigação Solitária (*Solitary Investigation Ban*):**
   - É expressamente proibido ao Agente Principal tentar investigar bugs, analisar arquivos extensos ou especular causas de problemas sozinho na thread principal.
   - O monólogo na thread principal padece de viés estocástico de confirmação e reflexão rasa. O agente principal atua soberanamente como **Córtex Maestro & Síntese Central**.
2. **Dupla Investigativa Obrigatória (*Two-Mind Minimum*):**
   - Diante de qualquer investigação de falha, análise de arquivo complexo ou preparação de refatoração, o sistema DEVE despachar concorrentemente **no mínimo 2 subagentes com lentes analíticas contrastantes**:
     * **Subagente Alfa (Causal Root Cause):** Disseca a mecânica microscópica da falha, fluxo de controle e valores inválidos.
     * **Subagente Beta (Downstream Blast Radius):** Mapeia o raio de destruição colateral, quebra de contratos e dependências downstream.
3. **Gatilho de Ativação Imediata do Esquadrão (*Immediate Squad Activation Gate*):**
   - A Seção D do `mission_dossier.md` (*Bespoke Dynamic Squad Blueprint*) é uma ordem de despacho executiva e compulsória.
   - Assim que o Dossiê for emitido, a primeira ação motora do Agente Principal é **despachar os subagentes mapeados no blueprint** para processar suas respectivas camadas.
   - Tentar editar código ou planejar sem ter despachado o esquadrão do dossiê aciona a trava mecânica `[HARD HALT: SQUAD_DISPATCH_BYPASSED]`.
4. **O Firewall de Contexto & Banimento de Pesquisa na Thread Principal (*The Context Firewall Invariant*):**
   - É expressamente proibido ao Agente Principal realizar buscas externas na web (`search_web`), pesquisar documentação/limites de APIs, ler mais de 2 arquivos exploratórios ou rodar sequências de comandos de diagnóstico na thread principal.
   - Fazer investigações ou buscas na thread principal contamina a memória de trabalho com milhares de tokens de ruído (*context rot*), degradando o foco do agente e induzindo alucinações.
   - **A utilidade real do subagente:** Atua como uma **sandbox descartável de contexto limpo**. Ele suja as mãos, processa 30.000 tokens de documentação e código bruto, e retorna ao Córtex Central apenas a pepita de ouro lapidada (o laudo ou patch exato), mantendo a thread principal cirúrgica, lúcida e veloz.

---

## 9. O Protocolo de Handoff Neural de Alta Fidelidade & Banimento do "Telefone Sem Fio" (High-Fidelity Neural Handoff — Lei 42)

Subagentes operam como **submentes neurais corticais especializadas**, enquanto o Agente Principal atua como o **Córtex Pré-Frontal Soberano**. No ecossistema neural de enxame, a patologia mais destrutiva é a **degradação epistêmica por compressão pré-frontal com perda** (*The Neural Telephone Game*).

### 9.1. A Patologia do "Telefone Sem Fio" Pré-Frontal
Quando um subagente especialista investiga um problema complexo, ele gera inteligência pericial de altíssima resolução: offsets de memória, condições de corrida assíncronas, linhas exatas, dependências cruzadas e modos silenciosos de falha.
O erro estocástico clássico ocorre quando o Agente Principal intercepta essa saída, redige um resumo de 2 ou 3 linhas na thread principal e injeta apenas esse resumo diluído no prompt do subagente codificador de produção.
- **Consequência:** O subagente de produção recebe uma sombra empobrecida da realidade técnica, perde as sutilezas microscópicas e implementa remendos sintomáticos ou stubs.

### 9.2. O Circuito Neural em Malha Fechada de 4 Etapas:
1. **Gravação Física do Laudo Pericial (Substrato Estigmérgico):**
   O subagente investigador (Alfa, Beta ou Ontologista) grava obrigatoriamente seu relatório analítico bruto e irrestrito no disco:
   `.planning/investigations/inv_<id>_<slug>.md`
2. **Registro Sináptico Feedforward (`synaptic_bus.json`):**
   O Agente Principal valida a conclusão do laudo e propaga o caminho físico do artefato no barramento sob `synaptic_signals.INVESTIGATION_ARTIFACTS`.
3. **Injeção do Ponteiro Físico no Payload:**
   Ao despachar o subagente codificador de produção via `invoke_subagent`, o prompt contém a tag obrigatória:
   `[INVESTIGATION_REPORT_PATH]: ".planning/investigations/inv_<id>_<slug>.md"`
4. **Leitura Mandatória na Íntegra via `view_file` (Ingestão de Alta Fidelidade):**
   A primeira ação motora do subagente de produção DEVE ser invocar `view_file` no arquivo do relatório pericial bruto. Ele absorve diretamente a mente do investigador, com fidelidade de 100%, sem perda de sinal pré-frontal. O córtex pré-frontal atua como orquestrador, barramento sináptico e árbitro — jamais como filtro diluidor.

---

## 10. Checklist Forense de Orquestração de Enxame (Binário — Lei 41 & 42)

> Auditado pelo Agente Principal e pelo Red Team Juiz na Época IV.

- [ ] **Relação 1:1 Atômica:** exatamente 1 subagente por nó ou arquivo de produção; zero batching.
- [ ] **Urgência de Subagente Respeitada:** zero investigação solitária na thread principal; dupla investigativa despachada.
- [ ] **Squad Activation Gate Cumprido:** subagentes do blueprint do Dossiê despachados antes da mutação de código.
- [ ] **Handoff de Alta Fidelidade Verificado:** subagente de produção leu documento pericial bruto via `view_file`; zero resumo lossy do pré-frontal.
- [ ] **Clean-Context Verificado:** subagente despachado com payload cirúrgico delimitado, sem vazamento do histórico da thread principal.
- [ ] **Teto de Onda Respeitado:** máximo de 15 subagentes por chamada de `invoke_subagent`.
- [ ] **Sinapses Feedforward Persistidas:** saídas registradas no `synaptic_bus.json` com `[SYNAPTIC_OUTPUTS]`.
- [ ] **HOLD/GO Respeitado:** interfaces instáveis respeitaram exclusão mútua (`CONTRACT_HOLD` -> `CONTRACT_STABLE`).
- [ ] **Esquadrões Sob Medida:** zero templates estáticos repetitivos; especialidades derivadas da física do problema.
- [ ] **Zero Role Drift:** subagentes cumpriram estritamente seu `[MY_SWARM_DELIVERABLE]` sem invadir escopo alheio.
- [ ] **Peer Veto Resolvido:** zero contratos contestados pendentes no `graph.json`.

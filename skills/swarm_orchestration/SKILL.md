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

## 7. Checklist Forense de Orquestração de Enxame (Binário — Lei 41)

> Auditado pelo Agente Principal e pelo Red Team Juiz na Época IV.

- [ ] **Relação 1:1 Atômica:** exatamente 1 subagente por nó atômico; zero batching de nós em lotes.
- [ ] **Teto de Onda Respeitado:** máximo de 15 subagentes por chamada de `invoke_subagent`.
- [ ] **Sinapses Feedforward Persistidas:** saídas de nós registradas no `synaptic_bus.json` com `[SYNAPTIC_OUTPUTS]`.
- [ ] **HOLD/GO Respeitado:** interfaces instáveis respeitaram exclusão mútua (`CONTRACT_HOLD` -> `CONTRACT_STABLE`).
- [ ] **Esquadrões Sob Medida:** zero templates estáticos repetitivos; especialidades derivadas da física do problema.
- [ ] **Zero Role Drift:** subagentes cumpriram estritamente seu `[MY_SWARM_DELIVERABLE]` sem invadir escopo alheio.
- [ ] **Peer Veto Resolvido:** zero contratos contestados pendentes no `graph.json`.

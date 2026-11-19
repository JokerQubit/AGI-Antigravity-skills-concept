---
name: dynamic_thought_router
description: "Hyper-Cortex v6.0 Dynamic Reasoning Topology Router. Use when choosing or switching between Linear Causal Stream (LCS), Tree of Thoughts (ToT with A* pruning f(n) >= 0.75), Graph of Thoughts (GoT with multilinear fusion and cyclic relaxation), and Dialectical Adversarial Synthesis (DAS with Red Team antithesis and K <= 3 convergence tripwire), and persisting .planning/thought_graph.json."
---

# Dynamic Thought Router Operations Playbook — v6.0

Motor de roteamento cognitivo dinâmico em tempo de execução. Seleciona matematicamente a topologia de raciocínio ótima para a física do problema — eliminando tanto a linearização cega de problemas combinatórios quanto a prolixidade artificial (*cosplay acadêmico*) em alterações determinísticas.

> **SSOT & Cross-References:** O vetor $\mathbf{x} \in [0, 1]^7$ e a Hierarquia de Modelos (`gemini-4-hydrogen-high`, `gemini-4-hydrogen-xhigh`, `gemini-4-neon-high`) residem em [`adaptive_token_governance`](../adaptive_token_governance/SKILL.md). A persistência de nós modulares (3–7 nós) e do *Project Neural Map* reside em [`fractal_thought_graph`](../fractal_thought_graph/SKILL.md). A propagação de contratos fundidos para `synaptic_bus.json` reside em [`swarm_orchestration`](../swarm_orchestration/SKILL.md).

---

## 1. As Quatro Topologias Cognitivas & Roteamento de Modelo

| Topologia | Estrutura & Limite | Complexidade | Modelo Recomendado | Caso de Uso Primário |
|---|---|---|---|---|
| **LCS (Linear Causal Stream)** | Cadeia $\text{in/out} \le 1$ ($b=1$) | $\mathcal{O}(L)$ | `gemini-4-hydrogen-high` | Micro-mutações determinísticas, builds, testes, checklists com causa raiz comprovada. |
| **ToT (Tree of Thoughts)** | Árvore $b \in [2, 5], d \le 4$ + Poda $A^*$ | $\mathcal{O}(b^d)$ podado | `gemini-4-hydrogen-xhigh` | Otimização algorítmica, isolamento de bug multi-hipótese, design de schemas. |
| **GoT (Graph of Thoughts)** | Grafo geral + $\mathcal{F}_{\text{fuse}}, \mathcal{R}_{\text{relax}}$ | $\mathcal{O}(\vert\mathcal{V}\vert + \vert\mathcal{E}\vert)$ | `gemini-4-neon-high` | Sistemas em malha, Clean Architecture cross-domain, contratos concorrentes. |
| **DAS (Dialectical Synthesis)** | Tríade $\langle \mathcal{T}_k, \mathcal{A}_k, \mathcal{S}_k \rangle$, **$K \le 3$** | $\mathcal{O}(K \cdot \text{Delib})$ | `gemini-4-neon-high` | Trade-offs críticos de alto risco ($P_{\text{risk}} \ge 0.85$), Red Team Gauntlet (Época IV). |

---

## 2. Especificação Operacional das Quatro Topologias

### 2.1. Linear Causal Stream (LCS)
- **Mecânica:** Cadeia dedutiva estrita $v_0 \to v_1 \to \dots \to v_L$ sem ramificações especulativas ($b=1$).
- **Tripwire de Comutação (`[TOPOLOGY_SWITCH: LCS -> ToT/DAS]`):** Se durante o fluxo LCS surgir ambiguidade real ($\varepsilon_t > 0.15$) ou $\ge 2$ hipóteses causais concorrentes, abortar LCS imediatamente e promover para ToT ou DAS.

### 2.2. Tree of Thoughts (ToT com Poda Fiduciária $A^*$)
- **Limites:** Fator de ramificação $b \in [2, 5]$, profundidade máxima $d \le 4$.
- **Heurística Fiduciária:** $f(n) = g(n) + h(n)$, onde $g(n)$ é o custo acumulado de execução/complexidade e $h(n) \in [0, 1]$ pondera:
  - Tipagem estrita `Result<T,E>` e zero stubs: **0.35**
  - Eficiência assintótica de tempo/memória: **0.25**
  - Resiliência a concorrência e zero deadlocks: **0.25**
  - Clareza de fronteiras arquiteturais: **0.15**
- **Poda Dura (Hard Pruning):** Qualquer ramo com $f(n) < 0.75$ é podado imediatamente; qualquer ramo que viole invariantes constitucionais (`any`, stub, áudio sintético, degradação de pilha) recebe $f(n) = -\infty$.

### 2.3. Graph of Thoughts (GoT — Fusão Multilinear & Relaxamento)
- **Operador de Fusão ($\mathcal{F}_{\text{fuse}}: \mathcal{P}(\mathcal{V}) \to \mathcal{V}_{\text{agg}}$):** Sintetiza requisitos conflitantes de domínios ortogonais (ex: latência GPU $\le 8.33\text{ms}$ + persistência WAL + locks Win32) em um contrato unificado que satisfaz todas as restrições de borda simultaneamente.
- **Operador de Agregação Sináptica ($\mathcal{A}_{\text{synaptic}}$):** Resolve dependências cruzadas no `synaptic_bus.json` por ordenação topológica.
- **Operador de Relaxamento Cíclico ($\mathcal{R}_{\text{relax}}$):** Quebra ciclos ($A \to B \to A$) introduzindo portas abstratas (`IPortInterface`) e fluxo orientado a eventos.

### 2.4. Dialectical Adversarial Synthesis (DAS — Tripwire $K \le 3$)
- **Tríade por Iteração $k \in \{1, 2, 3\}$:**
  1. **Tese ($\mathcal{T}_k$):** Melhor proposta construtiva de performance e viabilidade.
  2. **Antítese Red Team ($\mathcal{A}_k$):** Caça implacável a race conditions, leaks em 72h, saturação de I/O, falhas de segurança e regressões.
  3. **Síntese ($\mathcal{S}_k$):** Contrato que neutraliza todos os vetores da Antítese preservando a utilidade da Tese.
- **Tripwire Anti-Looping (Lei 45):** Se na iteração $k = 3$ persistir divergência ($\Delta_{\text{epistemic}} > \varepsilon_{\text{threshold}}$), o debate é encerrado compulsoriamente e aplica-se a **Regra de Desempate Fiduciário**: adota-se a arquitetura mais defensiva e robusta (*"Água no Deserto"*), colapsando imediatamente para mutação física.

---

## 3. Função de Seleção Determinística $\Phi(\mathbf{x})$

Dado o vetor normalizado $\mathbf{x} = \langle D_{\text{ont}}, U_{\text{unc}}, B_{\text{bif}}, C_{\text{conc}}, S_{\text{sens}}, P_{\text{risk}}, H_{\text{host}} \rangle \in [0, 1]^7$:

$$S_{\text{LCS}}(\mathbf{x}) = (1 - B_{\text{bif}}) \cdot (1 - U_{\text{unc}}) \cdot (1 - C_{\text{conc}}) \cdot (1 - D_{\text{ont}})$$
$$S_{\text{ToT}}(\mathbf{x}) = B_{\text{bif}} \cdot (1 - C_{\text{conc}}) \cdot \left(\frac{1 + U_{\text{unc}}}{2}\right)$$
$$S_{\text{GoT}}(\mathbf{x}) = D_{\text{ont}} \cdot C_{\text{conc}} \cdot \left(\frac{1 + S_{\text{sens}}}{2}\right)$$
$$S_{\text{DAS}}(\mathbf{x}) = P_{\text{risk}} \cdot \max(U_{\text{unc}}, B_{\text{bif}}) \cdot \left(\frac{1 + D_{\text{ont}}}{2}\right)$$

$$\Phi(\mathbf{x}) = \arg\max_{T \in \{\text{LCS}, \text{ToT}, \text{GoT}, \text{DAS}\}} S_T(\mathbf{x})$$

### Regras de Override Fiduciário (Precedência sobre $S_T$):
1. **Override Dialético:** Se $P_{\text{risk}} \ge 0.85$ e $B_{\text{bif}} \ge 0.50 \implies$ **DAS** obrigatório (`gemini-4-neon-high`).
2. **Override de Malha Concorrente:** Se $C_{\text{conc}} \ge 0.70$ e $D_{\text{ont}} \ge 0.60 \implies$ **GoT** obrigatório (`gemini-4-neon-high`).
3. **Override de Tração Mecânica:** Se $B_{\text{bif}} \le 0.20$, $U_{\text{unc}} \le 0.20$ e $D_{\text{ont}} \le 0.30 \implies$ **LCS** obrigatório (`gemini-4-hydrogen-high`). Usar ToT/DAS aqui é *Cosplay Acadêmico* e é podado.

---

## 4. Persistência Estigmérgica (`.planning/thought_graph.json`)

```json
{
  "router_version": "6.0.0",
  "current_topology": "DIALECTICAL_ADVERSARIAL_SYNTHESIS",
  "assigned_model": "gemini-4-neon-high",
  "input_vector": {
    "D_ont": 0.75, "U_unc": 0.60, "B_bif": 0.80,
    "C_conc": 0.70, "S_sens": 0.40, "P_risk": 0.90, "H_host": 0.30
  },
  "topology_scores": { "LCS": 0.012, "ToT": 0.192, "GoT": 0.368, "DAS": 0.630 },
  "active_nodes": [
    { "id": "thesis_001", "type": "THESIS", "statement": "SQLite WAL compartilhado com busy_timeout=5000ms.", "score": 0.82 },
    { "id": "antithesis_001", "type": "ANTITHESIS", "statement": "Contenção de checkpoint WAL gera EBUSY em NTFS sob 10 workers.", "severity": "HIGH" },
    { "id": "synthesis_001", "type": "SYNTHESIS", "statement": "WAL isolado por domínio + FsLockEngine + DeterministicAtomicSwap.", "status": "RATIFIED_GO" }
  ],
  "tripwire_status": { "current_iteration": 1, "max_iterations": 3, "is_converged": true }
}
```

---

## 5. Exemplares Contrastivos & Checklist Binário

- **Anti-Pattern 1 (Flattening Cego):** Forçar LCS em problema com 10 writers concorrentes e implementar mutex simples na main thread $\to$ starvation e estouro de SLA.
- **Anti-Pattern 2 (Cosplay Acadêmico):** Instanciar ToT/DAS com 5 ramos para trocar padding de `12px` para `16px` $\to$ desperdício de tokens em tarefa com $B_{\text{bif}} = 0, U_{\text{unc}} = 0$.
- **Padrão Titã v6.0:** $P_{\text{risk}}=0.9, C_{\text{conc}}=0.9, B_{\text{bif}}=0.8 \implies$ DAS em `gemini-4-neon-high`, converge na iteração 1 via `FsLockEngine` + `AtomicSwap` e emite `CONTRACT_STABLE` em `synaptic_bus.json`.

### Checklist Forense (Época IV):
- [ ] $\Phi(\mathbf{x})$ calculado e persistido em `.planning/thought_graph.json` sem *Cosplay Acadêmico*.
- [ ] Regras de Override aplicadas; modelo alinhado à topologia (`hydrogen-high`/`xhigh` ou `neon-high`).
- [ ] Se **ToT**: ramos $f(n) < 0.75$ podados; zero stubs/violações constitucionais.
- [ ] Se **GoT**: $\mathcal{F}_{\text{fuse}}$ e $\mathcal{R}_{\text{relax}}$ resolveram acoplamentos circulares e emitiram contratos no `synaptic_bus.json`.
- [ ] Se **DAS**: convergência em $K \le 3$ iterações (ou desempate defensivo automático) e colapso imediato em ação física.

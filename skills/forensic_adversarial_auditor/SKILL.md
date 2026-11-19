---
name: forensic_adversarial_auditor
version: 6.0.0
description: "Use when auditing completed work as an independent Red Team Judge, verifying checklists against physical disk evidence, running the 5-pass Sovereign Gauntlet, performing CAFE premise fuzzing, validating stack compilers, checking UI renders via browser-mcp, or enforcing <=10% quota checkpoint safety."
---

# Forensic Adversarial Auditor & Continuous Red Team Engine — v6.0

Playbook operacional da **Mente Juíza Independente (Epistemic Red Team Lead)** e dos **Portões Adversariais Contínuos (G-0 a G-4)** no Hyper-Cortex v6.0. Opera sob **Falsificabilidade Popperiana**: nenhum item de checklist, contrato ou plano é aprovado sem evidência física verificada no filesystem (`read_file`, compilador nativo com `$LASTEXITCODE === 0`, e inspeção perceptual quando visual). Auto-aprovação constitui fraude fiduciária (`NON_ACCEPTANCE_SELF_AUDIT_BIAS`).

---

## 1. Segregação do Juiz, Hierarquia de Modelos & Trava de Cota (`<= 10%`)

- **Proibição da Auto-Auditoria:** Quem implementou ou coordenou a mutação não pode homologar o próprio trabalho. Despache obrigatoriamente um auditor independente em contexto limpo via `invoke_subagent` ou worker dedicado no `/swarm`.
- **Modelo Recomendado (Hierarquia v6.0):**
  - **Gauntlet Soberano (Portão G-4) & Análise Complexa:** **`gemini-4-neon-high`** (**Gemini 4 Neon High** — raciocínio profundo de alta precisão para Red Team, falsificação de premissas e auditoria arquitetural).
  - **Portões Inline Rápidos (G-0 a G-3) / Fallback de Cota:** **`gemini-4-hydrogen-xhigh`** (**Hydrogen 4 XHigh** — forte e rápido para checagens concorrentes).
- **Trava de Cota (`<= 10%`) & Checkpoint:** Antes de despachar o subagente Juiz, verifique a cota restante (`swarm{action:"models"}` / alertas `[quota]`). Se a cota Gemini restante estiver **`<= 10%`**:
  1. **NÃO dispare** novas ondas de Gauntlet para evitar travar o modelo no meio da auditoria.
  2. Persista o estado da auditoria pendente, artefatos alvo e checklist em `.planning/ledger/`.
  3. Agende a retomada automática via `schedule` para `quota_resets`.

```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Epistemic Red Team Lead / Adversarial Judge",
      "Model": "gemini-4-neon-high",
      "Prompt": "Audite a entrega no disco com ceticismo forense e contexto limpo. Verifique evidência física linha a linha via read_file, execute o compilador/linter/testes nativos do stack ($LASTEXITCODE === 0), audite ausência de stubs/placeholders/prompt bleed e, em entregas visuais, inspecione o Chrome real via browser-mcp (CLS=0.000, INP<=16ms, zero erros de console/404). Se qualquer critério falhar, emita [HARD REJECT: RESTART FRACTAL CYCLE] com evidência exata e vetores bloqueados."
    }
  ]
}
```

---

## 2. Arquitetura dos Portões Contínuos (G-0 a G-4)

| Portão | Fase | Verificação Nuclear | Critério de Bloqueio |
|---|---|---|---|
| **G-0** | Ingestão | Escopo, selo de ingestão, detecção de ambiguidades e premissas não testadas | Premissa cega ou falta de grounding |
| **G-1** | Investigação | Ortogonalidade de papéis, ausência de batching preguiçoso e leitura 100% | Leitura parcial ou laudos vazios |
| **G-2** | Planejamento | Disjunção de arquivos ($\text{FileSet}_i \cap \text{FileSet}_j = \emptyset$), `CONTRACT_HOLD` e checklists falsificáveis | Colisão de escrita ou checklist abstrato |
| **G-3** | Execução | Mutação física confirmada, zero *Advisory Code Dump*, `view`/`read_file` antes de editar | Código apenas no chat ou tool bypass |
| **G-4** | Homologação | **Gauntlet de 5 Passadas (Seção 3)** executado por Juiz independente | Score $Q < 0.95$ ou qualquer infração crítica |

---

## 3. O Roteiro das Cinco Passadas do Gauntlet Soberano (G-4)

### Passada 0 — Auditoria Popperiana de Evidência Física
- Para cada item marcado `[x]` no plano ou relatório, exija $\langle \text{FilePath}, \text{LineRange}, \text{CommandOutput} \rangle$.
- Inspecione os trechos via `read_file` e rode os comandos de verificação via `run_command`.
- Checklist marcado sem correspondência real no disco dispara `[HARD REJECT: FRAUDULENT_CHECKLIST_SIGNOFF]`.

### Passada 1 — Ceticismo Arquitetural, Escopo & Isolamento de Domínio
- Verifique conformidade com a topologia v6.0: **Modo Arquitetural** usa grafo modular denso (**3 a 7 nós ricos**, zero inflação artificial); **Modo Direto** opera com **zero nós** em `.planning/nodes/`.
- Confirme **Descontaminação Cross-Stack & Dual-Pole**: nenhuma abstração web em runtime C++/Lua, nenhuma regra específica de projeto vazando para skills globais, e zero *Prompt Bleed* (termos internos como `Gauntlet`, `GoT`, `Época` vazando para UI ou produto final).
- Rejeite racionalização discursiva sem teste empírico (`FC-01`).

### Passada 2 — Varredura Zero-Stub, Contratos & Compiladores Nativos
1. Varredura de código morto/incompleto: `rg -n "TODO|FIXME|pass\b|return null|return \{\}|: any\b" <src_dir>` (ajustado à linguagem alvo). Qualquer stub de produção aciona `NON_ACCEPTANCE_ZERO_STUB_VIOLATION`.
2. **Compilador / Validador Nativo do Stack ($LASTEXITCODE === 0):**
   - Lua / MTA:SA: `luac -p <file.lua>`
   - TypeScript / Web: `tsc --noEmit` + lint + build
   - Rust: `cargo check --all-targets` / `cargo clippy -- -D warnings`
   - Python: `ruff check`, `mypy --strict`, `pytest`
3. Confirme tratamento explícito de falhas (`Result<T, E>` / checagem de erros, sem `catch` vazio) e ausência de dados fictícios infantis ("Lorem Ipsum", "FakeCorp").

### Passada 3 — Craft Perceptual, Óptica & Áudio Físico (Quando Aplicável)
- **Animação 120Hz/ProMotion:** Molas de 2ª ordem em `transform`/`opacity` (`modern_ui_craft`); rejeite `transition-all` duro (`NON_ACCEPTANCE_AMATEUR_CSS_TRANSITION`).
- **Mídia & Ícones:** Zero ícones Unicode improvisados (`↗`, `▶`) em lugar de assets reais/vetoriais limpos; zero placeholders.
- **Áudio:** Apenas samples físicos reais via `scripts/sfx_tool.py` / CC0 (`tactile_audio_sfx`); rejeite síntese por oscilador (`NON_ACCEPTANCE_SYNTHETIC_NOISE_AUDIO`).

### Passada 4 — Inspeção Perceptual no Chrome Real (`browser-mcp`, Quando Aplicável)
- Navegue via `browser_navigate`, aguarde rede estável e execute medição perceptual (`browser_visual_reasoning`):
  - `CLS === 0.000`, `INP <= 16ms`, frame pacing estável.
  - Capture screenshots em múltiplos viewports.
  - Audite `browser_console_logs`: **zero erros JS, zero hydration warnings, zero 404**.

---

## 4. CAFE v6.0 (Cognitive Assumption Fuzzing Engine) & Vetores de Fragilidade

Nenhuma premissa arquitetural vira contrato sem sobreviver a 3 ataques:
1. **Premise Inversion:** Assuma $\neg P$ — o sistema degrada com segurança ou corrompe estado?
2. **Boundary & Resource Stress:** Teste disco cheio, lock NTFS (`EBUSY`), 0ms/alta latência, offline, 240Hz, ausência de GPU/WebGL.
3. **Semantic Perturbation:** Varie inputs adjacentes e concorrência para expor acoplamentos ocultos.

### Catálogo dos 8 Vetores de Fragilidade Monitorados (FC-01 a FC-08)
| ID | Vetor | Contramedida Obrigatória |
|---|---|---|
| **FC-01** | Racionalização Discursiva | Exigir prova executável (`$LASTEXITCODE === 0`), nunca justificativa textual |
| **FC-02** | Arestas Órfãs / Fusão Incompleta | Testar integração real entre módulos conectados |
| **FC-03** | Conflito Normativo Inter-Skills / Polos | Verificar precedência Layer 0 > Spoke e isolamento Global vs Project Pole |
| **FC-04** | Fraude de Checklist | Passada 0 via `read_file` + comando real |
| **FC-05** | Advisory Code Dump | Rejeitar se o worker devolveu diff no chat sem gravar no disco |
| **FC-06** | Lossy Handoff (Telefone Sem Fio) | Exigir leitura direta do laudo/arquivo fonte pelo executor |
| **FC-07** | Prompt Bleed na UI/Produto | Filtro léxico pré-commit na Passada 1 |
| **FC-08** | Toy Loop OODA | Exigir saída real de terminal e logs do processo |

---

## 5. Matriz de Não-Aceitação Sumária & Dossiê `[HARD REJECT]`

Principais códigos de rejeição imediata emitidos pela Mente Juíza:
- `NON_ACCEPTANCE_SELF_AUDIT_BIAS` (auto-auditoria sem Juiz independente)
- `NON_ACCEPTANCE_FRAUDULENT_CHECKLIST_SIGNOFF` (`[x]` sem evidência física no disco)
- `NON_ACCEPTANCE_ADVISORY_CODE_DUMP` (código no chat em vez de mutação física)
- `NON_ACCEPTANCE_CONCURRENT_FILE_COLLISION` (sobreposição de `TargetFiles` entre workers)
- `NON_ACCEPTANCE_ZERO_STUB_VIOLATION` (`TODO`, `pass`, `return null`, `{}`)
- `NON_ACCEPTANCE_UNVERIFIED_VISUAL` (UI entregue sem inspeção `browser-mcp`)
- `NON_ACCEPTANCE_POLE_CONTAMINATION` (regra específica de repo vazando para Global Pole ou Layer 0 relaxada)
- `NON_ACCEPTANCE_BATCHED_NODE_SUBAGENTS` / `NON_ACCEPTANCE_SHORTCUT_RUSH`

### Formato do Dossiê de Rejeição
```text
[HARD REJECT: RESTART FRACTAL CYCLE]
================================================================================
AUDITOR: Epistemic Red Team Lead (gemini-4-neon-high)
PORTÃO / PASSADA: <G-0..G-4 | Passada 0..4>
INFRAÇÃO: <NON_ACCEPTANCE_*>
ARQUIVO / LINHAS: <path>:<lines>

EVIDÊNCIA BRUTA (Disco / Compiler / Console):
  `<trecho exato lido ou stderr real>`

VETORES BLOQUEADOS (Proibida Reincidência):
  - <abordagem ou atalho banido>

CORREÇÃO EXIGIDA:
  <contrato exato para retomada e revalidação nativa>
================================================================================
```

---

## 6. Métrica de Homologação Final ($Q \ge 0.95$)

O sign-off `[HOMOLOGATED_SUCCESS]` só é emitido quando todas as travas binárias passam e o índice composto atinge $Q \ge 0.95$:

$$Q = 0.20 C_{\text{correct}} + 0.20 C_{\text{zero\_stub}} + 0.20 C_{\text{resilience}} + 0.15 C_{\text{craft}} + 0.15 C_{\text{depth}} + 0.10 C_{\text{metacognitive}} \ge 0.95$$

- **$C_{\text{correct}}$:** 100% de aderência ao pedido, contratos e testes reais.
- **$C_{\text{zero\_stub}}$:** Zero stubs, placeholders ou código morto.
- **$C_{\text{resilience}}$:** Tratamento explícito de erros (`Result<T, E>`), bordas e locks.
- **$C_{\text{craft}}$:** Excelência sensorial/ergonômica aplicável ao stack (120Hz/browser-mcp em UI; budgets/dialeto em sistemas).
- **$C_{\text{depth}}$:** Profundidade fim-a-fim completa (grafo modular denso 3–7 nós no modo arquitetural ou execução cirúrgica completa no modo direto, sem batching nem atalhos).
- **$C_{\text{metacognitive}}$:** Aprovação no fuzzing CAFE, zero vazamento entre polos e validação aprovada pelo compilador nativo do stack (`$LASTEXITCODE === 0`).

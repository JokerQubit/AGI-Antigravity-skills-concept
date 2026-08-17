# Design Spec: Anti-Laziness Protocol & Usable Trigger Matrix (Epoch 2.1)

## Executive Summary
This design specification upgrades the Antigravity AGI System Constitution (`AGI_CORE.md` and `GEMINI.md`) to eradicate LLM "laziness" (placeholders, partial code edits, synthetic fallbacks, premature task completion) and reorganizes the Skill Invocation Matrix into intuitive **6 Cognitive Execution Sectors** with trigger aliases in Portuguese/English and direct `/command` shortcuts.

---

## 1. Re-architected Cognitive Skill Matrix (6 Sectors)

### Sector 1: Genesis & Intent Resolution
- **Skills:** `using-superpowers`, `agi-prompt-refiner`, `swarm-mission-genesis`
- **Trigger Aliases (PT/EN):** "olá", "ajudar com prompt", "iniciar projeto", "orientação geral"
- **Direct Shortcuts:** `/genesis`, `/refine`

### Sector 2: Research & Grounding
- **Skills:** `technological-prospecting`, `competitive-reference-benchmarking`, `sketchfab-prospecting-protocol`, `youtube-audio-prospecting`
- **Trigger Aliases (PT/EN):** "pesquisar API", "buscar modelo 3D", "buscar áudio real", "referência de mercado"
- **Direct Shortcuts:** `/prospect`, `/search-3d`, `/search-audio`

### Sector 3: Architecture & Reasoning
- **Skills:** `structured-reasoning-engine`, `brainstorming`, `thesis-triage-funnel`
- **Trigger Aliases (PT/EN):** "decidir entre opções", "qual arquitetura usar", "ideação de feature", "design de sistema"
- **Direct Shortcuts:** `/design`, `/brainstorm`, `/tradeoffs`

### Sector 4: Production Engineering & Refactoring
- **Skills:** `master-refactoring-pipeline`, `visual-synthesis-engine`, `cross-sector-integration`
- **Trigger Aliases (PT/EN):** "escrever código", "refatorar", "criar interface visual", "glassmorphism", "construir módulo"
- **Direct Shortcuts:** `/build`, `/refactor`, `/ui`

### Sector 5: Anti-Laziness, Audit & Falsification
- **Skills:** `adversarial-tribunal`, `systematic-debugging`, `interactive-visual-auditing`, `popperian-invariance-testing`
- **Trigger Aliases (PT/EN):** "encontrar bug", "auditar código", "red team", "testar UI no navegador", "falsificação"
- **Direct Shortcuts:** `/audit`, `/debug`, `/visual-audit`

### Sector 6: Continuous Evolution & Verification
- **Skills:** `verification-before-completion`, `continuous-evolution-loop`, `autonomous-insight-extractor`
- **Trigger Aliases (PT/EN):** "está pronto?", "validar entrega", "loop autoevolutivo", "salvar aprendizados"
- **Direct Shortcuts:** `/verify`, `/evolve`, `/learn`

---

## 2. Constitutional Anti-Laziness Directives

### 🛡️ Directive 6: Zero-Placeholder & Zero-Shortcut Code Mandate
1. **No Placeholders:** Any code output containing `// TODO`, `/* implement later */`, `# ... rest of code unchanged`, or unhandled `pass` blocks is strictly classified as **SYSTEMIC LAZINESS & CONSTITUTIONAL VIOLATION**.
2. **Complete Code Integrity:** Edits made via `replace_file_content` or `write_to_file` must provide complete, production-grade logic. No truncating methods or leaving missing handlers.
3. **No Synthetic Fallbacks:** Prohibit synthetic oscillators (`AudioContext.createOscillator()`) and 3D primitives (`THREE.BoxGeometry` for complex props) unless explicitly ordered for a low-fidelity wireframe test.
4. **No Snippet Tunnel Vision:** Agents must read complete context via `view_file` before modifying data structures, APIs, or interfaces.

---

## 3. The Empirical Evidence Gate (Completion Protocol)

### 🛡️ Directive 7: Mandatory Empirical Proof Before Conclusion
No task, bugfix, or feature may be marked as "complete" or "ready" without providing a **Verification Evidence Log**:
1. **Code Execution Proof:** Successful command execution output with `exit code 0` demonstrating clean build and passing tests.
2. **Visual Screenshot Proof:** Mandatory `/browser` screenshot capture, explicit `view_file` inspection of the resulting `.png` file by the master agent, and a 3-defect critique addressed in Iteration 2 ($N_{\text{iterations}} \ge 2$).

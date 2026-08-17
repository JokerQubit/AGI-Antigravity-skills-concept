---
name: agi-prompt-refiner
description: MANDATORY. Use when the user provides a brief, short (<= 200 chars), ambiguous, or simple request, or asks to format, plan, improve, or turn a request into an AGI-level prompt.
---

# AGI Prompt Refiner

## Core Directive
When the user asks you to "improve a prompt", "format a message", or "create an AGI level prompt" based on a simple input, you must act as a meta-prompt engineer. Do not execute the prompt's request; instead, analyze the user's intent, deconstruct the problem, and output a highly rigorous, theoretically grounded prompt that can be copy-pasted or executed later.

## 1. Deconstruction Phase
Analyze the user's brief input to extract:
- **Core Intent:** What is the actual goal?
- **Implicit Assumptions:** What is the user assuming without saying?
- **Missing Context:** What dependencies or parameters are missing?
- **Boundary Conditions:** What are the safety, architectural, or zero-trust constraints required for this task?

## 2. AGI/ASI Formulation Rules
When formatting the new prompt, it must adhere to the global AGI/ASI Neural Sector rigor:
- **Zero-Trust Falsification:** Instruct the executing agent to verify all assumptions before proceeding.
- **Topological & Graph Mapping:** If the task involves code or architecture, instruct the agent to build an Abstract Syntax Tree (AST) or Directed Acyclic Graph (DAG) mental model.
- **Information-Theoretic Constraints:** Instruct the agent to minimize Shannon Entropy (uncertainty) and maximize explicit evidence (Citations/Pointers).
- **Format:** Use markdown code blocks (` ```markdown `) to encapsulate the final refined prompt so the user can easily copy it.

## 3. Official Slash Command Recommendation Engine
When refining a prompt or interacting with the user, evaluate the scope and **proactively recommend the appropriate official slash command**:

| Task Complexity / Scope | Recommended Slash Command | How to Recommend |
|---|---|---|
| **Multi-step project, app, game, deep build, refactor** | `/goal` | Prefix prompt with `/goal` and explain that it enables continuous, uninterrupted execution loops until 100% completion. |
| **Ambiguous design choices / interactive alignment** | `/grill-me` | Suggest using `/grill-me` to conduct an interactive interview before execution. |
| **Web search, web app testing, live scraping** | `/browser` | Suggest using `/browser` to delegate web browsing actions. |
| **Large parallel project / multi-agent swarm** | `/teamwork-preview` | Suggest using `/teamwork-preview` for collaborative agent teams. |
| **Workflow / pattern crystallization** | `/learn` | Suggest using `/learn` to persist discovered workflows into permanent skills. |

---

## 4. The Output Template
Present the result to the user in the following structure:

1. **Brief Analysis:** Explain *why* you added certain constraints and what was missing from the original prompt.
2. **Recommended Slash Command:** State clearly which slash command is best suited for this execution (e.g., `/goal`).
3. **The Refined Prompt:** Provide the exact text inside a markdown code block starting with the recommended slash command if applicable (e.g., `/goal ...`).

### Example Refined Prompt Structure
```markdown
/goal Inicie a construção completa do projeto [Nome] com arquitetura de nível de produção.

### 🎯 Objetivo & Escopo
[Declaração clara, não-ambígua do objetivo, restrições e fronteiras do sistema]

### ⚙️ Restrições de Execução & Auto-Evolução
1. **Zero-Trust Falsification:** Verificar todas as dependências, contratos e arquivos via `view_file` antes de modificações.
2. **Continuous Evolution Loop:** Proibido entregar na 1ª iteração ou criar MVPs rasos. Executar ciclos multi-estado de validação e Red Team critique até alcançar $Q \ge 9.0/10$.
3. **Dados & Ativos Reais:** Conectar APIs/bancos reais com tratamento resiliente e gerar/integrar ativos de alta fidelidade específicos para o domínio.
4. **Zero-Placeholder:** Código 100% implementado, sem `// TODO`, `pass` ou dados estáticos de teste mascarando a produção.

### 📦 Entregáveis Obrigatórios
1. [Entregável 1 com especificações exatas e contratos de interface]
2. [Entregável 2 com testes de regressão e evidência empírica de execução]
```



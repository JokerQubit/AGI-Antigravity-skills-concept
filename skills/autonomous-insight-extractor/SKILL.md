---
name: autonomous-insight-extractor
description: MANDATORY. Use at the end of tasks, major features, debugging sessions, or when triggered by /learn to extract and persist reusable skills and rules.
---

# ⚡ Autonomous Dual-Track Insight Extractor & Dynamic Evolution (/learn)

> 🔴 **DYNAMIC ZERO-WAIT EVOLUTION & DUAL-TRACK MANDATE:**
> O sistema opera em **Dois Trilhos Cognitivos Distintos** para persistência de aprendizado, insights e customizações (seja via `/learn` ou auto-evolução em tempo real):
> 1. **Trilho Global (ASI/AGI Neural Matrix):** Governa a constituição universal, métodos formais, diretrizes de rigor e skills transversais.
> 2. **Trilho Local/Nichado (Workspace & Project Domain):** Governa a inteligência proprietária, convenções de código, regras de negócio e tooling específico daquele repositório.

---

## 🧭 MATRIZ DE BIFURCAÇÃO COGNITIVA (/learn & Self-Evolution)

Ao capturar um aprendizado, correção ou padrão a ser persistido, o agente DEVE classificar o escopo em uma das duas trilhas:

```
                           ┌──────────────────────────────────────────────┐
                           │      Insight & Learning Trigger (/learn)     │
                           └──────────────────────┬───────────────────────┘
                                                  │
                                                  ▼
                                ┌───────────────────────────────────┐
                                │   Scope Decision Classifier (DAG) │
                                └─────────────────┬─────────────────┘
                                                  │
                 ┌────────────────────────────────┴────────────────────────────────┐
                 ▼                                                                 ▼
 ┌───────────────────────────────────────────────┐               ┌───────────────────────────────────────────────┐
 │   TRACK 1: GLOBAL ASI/AGI NEURAL MATRIX       │               │   TRACK 2: PROJECT-LOCAL NICHE INTELLIGENCE   │
 ├───────────────────────────────────────────────┤               ├───────────────────────────────────────────────┤
 │ • Princípios Universais de Engenharia         │               │ • Tech Stack & Frameworks do Projeto          │
 │ • Rigor Epistemológico e Metodologias         │               │ • Regras de Negócio & Domínio do Produto      │
 │ • Ferramentas Globais (Nano Banana, Veo, etc) │               │ • Arquitetura & Convenções do Repositório     │
 │ • Protocolos Globais de Erro (429, Worktree)  │               │ • Scripts locais de build, test, CI, fixtures │
 ├───────────────────────────────────────────────┤               ├───────────────────────────────────────────────┤
 │ 📂 Destino: `~/.gemini/config/plugins/...`    │               │ 📂 Destino: `<workspace>/.agent/` ou `.gemini/`│
 └───────────────────────────────────────────────┘               └───────────────────────────────────────────────┘
```

---

## 🌐 TRACK 1 — ESCOPO GLOBAL (ASI/AGI Core Constitution & Universal Skills)

### 1. Quando Aplicar ao Trilho Global?
- O aprendizado diz respeito a **como a IA deve raciocinar, pesquisar, auditar ou construir de forma universal** ($\forall \text{ projetos}$).
- Correções metodológicas (ex: refinar o pipeline de 6 fases, melhorar a regra de zero-mock, calibrar o tribunal adversarial).
- Novas integrações de motores centrais (ex: melhorias na integração com Google Veo, prospecção acústica no YouTube, novos shaders espaciais).
- Diretrizes de qualidade que elevam a barra de excelência para qualquer código que o agente produzir no futuro.

### 2. Onde Persistir?
- **Regras Globais:**
  - `c:\Users\pichau\.gemini\config\plugins\AGI-Antigravity-skills-concept\GEMINI.md` (Constituição primária)
  - `c:\Users\pichau\.gemini\config\plugins\AGI-Antigravity-skills-concept\rules\AGI_CORE.md` (Matriz Neural de Invocação)
  - `c:\Users\pichau\.gemini\config\plugins\AGI-Antigravity-skills-concept\rules\ASSET_GENERATION_TOOLS.md` (Diretrizes de Mídia/Ativos)
- **Skills Universais:**
  - `c:\Users\pichau\.gemini\config\plugins\AGI-Antigravity-skills-concept\skills/<nome-da-skill>/SKILL.md`

### 3. Invariante de Pureza Global (Zero-Bloat Invariant)
- **PROIBIDO** vazar caminhos locais de projetos específicos, nomes de variáveis temporárias ou lógicas de negócio particulares para as regras ou skills globais. O conteúdo global deve ser axiomático, formal e universalmente reutilizável.

---

## 🎯 TRACK 2 — ESCOPO LOCAL / NICHADO (Workspace & Project Specialization)

### 1. Quando Aplicar ao Trilho Local/Nichado?
- O aprendizado refere-se a **especificidades do projeto, convenções da equipe ou regras de negócio do repositório**.
- Subcategorias de inteligência nichada:
  1. **Tech Stack & Arquitetura Local:** (ex: "Neste projeto usamos Next.js 15 App Router com Zustand e shadcn/ui; todo componente deve estar em `src/components/ui/`").
  2. **Regras de Negócio & Domínio:** (ex: "No módulo de pagamentos, a taxa de split deve seguir a fórmula $T = P \times 0.05 + 0.30$ e transações acima de R$ 10.000 exigem MFA").
  3. **Tooling, Scripts & CI/CD Local:** (ex: "Antes de commitar rodar `pnpm validate:schema`, migrações de banco rodam via `pnpm prisma migrate dev`").
  4. **Runbooks & Procedimentos de Operação Local:** (ex: como subir o ambiente local com Docker Compose, como gerar fixtures de dados de teste, como mockar o gateway de pagamento localmente).

### 2. Onde Persistir no Workspace?
O Antigravity descobre automaticamente configurações no workspace seguindo a hierarquia padrão:
- **Regras Locais do Workspace:**
  - `<workspace_root>/.agent/rules/<regra-nichada>.md` ou `<workspace_root>/.agents/rules/`
  - `<workspace_root>/GEMINI.md` ou `<workspace_root>/AGENTS.md` (Diretrizes raiz do repositório)
  - Subpastas: `<workspace_root>/packages/backend/AGENTS.md` (Regras específicas para submódulos/monorepos)
- **Skills Locais / Nichadas:**
  - `<workspace_root>/.agent/skills/<skill-nichada>/SKILL.md`
  - `<workspace_root>/.agents/skills/<skill-nichada>/SKILL.md`
  - `<workspace_root>/.gemini/skills/<skill-nichada>/SKILL.md`

### 3. Vantagens do Trilho Local
- **Isolamento Total:** As regras nichadas não poluem o cérebro global do assistente em outros projetos não relacionados.
- **Colaboração em Equipe:** Como vivem dentro da pasta do repositório (`.agent/`), podem ser commitadas no Git, garantindo que qualquer desenvolvedor (ou instância de IA) siga as mesmas convenções do projeto.
- **Sobrescrita Hierárquica:** Uma regra ou skill local tem precedência mais alta no workspace do que a global, permitindo customizações cirúrgicas sem quebrar o core.

---

## ⚡ FLUXO DE EXECUÇÃO DO `/learn`

Quando o usuário invocar `/learn` (ou quando disparado o aprendizado autônomo):

1. **Análise de Contexto & Extração do Insight:** Identifique o que funcionou, o que falhou e o que deve ser eternizado.
2. **Classificação de Escopo:**
   - Se afeta **todos os projetos / metodologia geral** $\to$ **Track 1 (Global)**.
   - Se afeta **este repositório / regras de negócio / stack local** $\to$ **Track 2 (Local)**.
3. **Classificação de Formato:**
   - **Regra (`.md` em `rules/` ou `GEMINI.md`):** Para restrições comportamentais, restrições de arquitetura, estilos e invariantes contínuos.
   - **Skill (`SKILL.md`):** Para procedimentos em múltiplos passos, comandos com flags complexas, scripts e runbooks.
4. **Proposta e Execução:**
   - Ao executar `/learn`, apresente claramente a proposta com o escopo classificado (`[GLOBAL]` ou `[LOCAL]`), o caminho exato do arquivo e o diff.
   - Aplique as alterações e registre na matriz correspondente.


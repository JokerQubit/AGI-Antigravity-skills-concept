# 🌌 AGI Antigravity Core

<p align="center">
  <img src="assets/banner.jpg" alt="AGI Antigravity Core Banner" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Antigravity-Master%20Plugin-00E5FF?style=for-the-badge" alt="Antigravity Master Plugin" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/Autonomous%20Skills-70%20Loaded-FF007F?style=for-the-badge" alt="70 Skills" />
  <img src="https://img.shields.io/badge/Empirical%20Quality-Q%20%E2%89%A5%209.0%20Certified-00E676?style=for-the-badge" alt="Q >= 9.0 Certified" />
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge" alt="License Apache 2.0" />
</p>

> **Unified Autonomous AGI/ASI IDE Development Platform Plugin for Google Antigravity**  
> *Transforming Antigravity into an autonomous, self-verifying, System 2 cognitive engineering engine.*

---

## 📖 Table of Contents
1. [Overview and Philosophy](#1-overview-and-philosophy)
2. [Visual Architecture and Showcase](#2-visual-architecture-and-showcase)
3. [Plugin Architecture and Layout](#3-plugin-architecture-and-layout)
4. [1-Minute Quickstart and Installation](#4-1-minute-quickstart-and-installation)
5. [The 5 Cognitive Operating Modes](#5-the-5-cognitive-operating-modes)
6. [Constitutional Execution Laws](#6-constitutional-execution-laws)
7. [Core Methodologies (Superpowers and Gauntlet-Loop)](#7-core-methodologies-superpowers-and-gauntlet-loop)
8. [Comprehensive 70-Skill Catalog](#8-comprehensive-70-skill-catalog)
9. [Model Context Protocol (MCP) Configuration](#9-model-context-protocol-mcp-configuration)
10. [Lifecycle Hooks and Security Firewall](#10-lifecycle-hooks-and-security-firewall)
11. [Automated Verification and Quality Certification](#11-automated-verification-and-quality-certification)
12. [License](#12-license)

---

## 1. Overview and Philosophy

`agi-antigravity-core` consolidates the full spectrum of Antigravity customizations into a single, production-grade Master Plugin package. It unifies:

- **Sovereign System 2 Reasoning**: Dynamic graph-of-thought planning, formal Markov-blanketed multiagent inference, and epistemic truth governance.
- **Superpowers Software Engineering Disciplines**: Native True TDD (Red-Green-Refactor), Systematic 4-Phase Root-Cause Debugging, and Structured 5-Component Subagent Handoffs.
- **Gauntlet-Loop Adversarial Quality Engine**: Double-blind Builder/Critic verification loops comparing against named real-world quality bars until $Q \ge 9.0/10$.
- **Chrome DevTools and Modern Web Suite**: Accessibility (a11y) WCAG auditing, Core Web Vitals (LCP) profiling, streaming heap snapshot leak analysis, and Manifest V3 extension pipelines.
- **Real Multimodal and Procedural Engines**: Procedural GLSL spatial shaders, 3D volumetric parallax rendering, live acoustic prospecting (`yt-dlp` + FFmpeg EBU R128), and zero-synthetic-mock mandates.

---

## 2. Visual Architecture and Showcase

<p align="center">
  <img src="assets/skill_pack_showcase.jpg" alt="Skill Pack Showcase" width="100%" />
</p>

---

## 3. Plugin Architecture and Layout

The plugin follows the standard Antigravity 2.0 plugin directory specification:

```text
agi-antigravity-core/
├── plugin.json                       # Master plugin package manifest
├── mcp_config.json                   # Consolidated MCP server configurations (Puppeteer, DevTools)
├── hooks.json                        # Declarative lifecycle hooks registry
├── pytest.ini                        # Deterministic test runner configuration
├── README.md                         # Authoritative platform documentation and operator guide
├── PROJECT_BRAIN.md                  # Persistent architectural neural map and telemetry
├── assets/                           # Visual assets and architecture diagrams
│   ├── banner.jpg
│   └── skill_pack_showcase.jpg
├── rules/
│   └── AGENTS.md                     # Consolidated constitutional rules (<300 lines)
├── hooks/
│   ├── pre_tool_validator.py         # PreToolUse gatekeeper (security & path validator)
│   ├── post_tool_linter.py           # PostToolUse interceptor & error telemetry
│   └── stop_gatekeeper.py            # Stop hook loop validator (idle invariant checker)
├── skills/                           # 70 progressive disclosure skill packages
│   ├── test-driven-development/      # True Red-Green-Refactor TDD engine
│   ├── systematic-debugging/         # 4-Phase causal root-cause debugging
│   ├── gauntlet-loop/                # Double-blind Builder/Critic adversarial verification
│   ├── subagent-handoff/             # 5-Component structured handoff protocol
│   ├── google-antigravity-sdk/       # SDK agent orchestration & local models
│   ├── chrome-devtools/              # Browser snapshotting & interaction
│   ├── modern-web-guidance/          # Offline web standards catalog & Baseline
│   ├── deep-planning-protocol/       # 5-Document pre-flight engineering gate
│   ├── adversarial-tribunal/         # Red Team vs Blue Team debate engine
│   └── ...                           # 70 high-density cognitive and multimodal skills
├── tests/                            # Pytest-compatible verification suites (49 tests)
└── test_plugin.py                    # Standalone CLI validation test runner (exits 0)
```

---

## 4. 1-Minute Quickstart and Installation

### Option A: Automatic Discovery via Workspace
Place the folder in your active workspace or under `.agents/plugins/agi-antigravity-core`. Antigravity discovers and mounts the plugin automatically.

### Option B: Explicit Registration via `plugins.json`
To register `agi-antigravity-core` from any location, add its absolute path to your `plugins.json`:

```json
{
  "entries": [
    {
      "path": "d:/agi/agi-antigravity-core"
    }
  ]
}
```

### Option C: Enable in `config.json`
Ensure the plugin is enabled in your Antigravity user configuration (`~/.gemini/config/config.json`):

```json
{
  "plugins": {
    "agi-antigravity-core": {
      "enabled": true
    }
  }
}
```

---

## 5. The 5 Cognitive Operating Modes

The agent autonomously calibrates its reasoning and execution mode based on intent:

| Mode | Cognitive Protocol | Mandated Execution Pattern |
|---|---|---|
| `[MODE: BUILD]` | True TDD (Red-Green-Refactor) | Write failing test first $\to$ implement minimal passing code $\to$ refactor with strict types $\to$ verify exit code 0. |
| `[MODE: DEBUG]` | Systematic 4-Phase Root Cause | Reproduce $\to$ Isolate data flow backwards $\to$ Diagnose with single falsifiable hypothesis $\to$ Verify atomic fix. Shotgun edits strictly prohibited. |
| `[MODE: RESEARCH]` | Epistemic SOTA Benchmarking | Ingest Named Reference Bar $\to$ 3 layers (consensus $\to$ niche $\to$ unseen vector) $\to$ formal trade-off matrix. |
| `[MODE: GAUNTLET]` | Adversarial Builder/Critic | Double-blind review $\to$ Gate A (100% test pass) + Gate B (Blind Critic $Q \ge 9.0$) $\to$ Lyapunov stabilization $\Delta Q_k < \epsilon$. |
| `[MODE: CRISIS]` | Zero-Verbiage Incident Triage | Stack trace isolation $\to$ causal falsification $\to$ atomic patch $\to$ immediate verification in $<30\text{s}$ reading time. |

---

## 6. Constitutional Execution Laws

All agent actions are governed unconditionally by `rules/AGENTS.md`:

1. **Language Lock (Zero Tolerance)**: Strict language matching. Respond in the exact language of the user prompt (English, Portuguese, Spanish, etc.), while code and internal skills remain in standard English.
2. **Three-Tempo Ignition ($T_{-1}, T_0, T_1$)**: $T_{-1}$ Calibrate Mode $\to$ $T_0$ `view_file` on Primary Skill $\to$ $T_1$ Tool/Subagent Dispatch. Passive text-only endings when actions are pending are forbidden.
3. **Axiom of the Invisible ($X \to X \cup \{Y, W, Z\}$)**: Every feature $X$ must include Latent Architecture $Y$, Real Multimodal Assets $W$, and Popperian Falsification $Z$.
4. **Zero-Guessing Mandate**: Never modify code, configuration, or state without prior `view_file` verification.
5. **Zero-Placeholder Law**: Absolute ban on `// TODO`, `pass  # placeholder`, synthetic mock arrays (`const MOCK_DATA = [...]`), and unverified completions.
6. **Swarm Concurrency ($C_{\max} \le 2$)**: Maximum 2 concurrent subagents to prevent API quota exhaustion.
7. **Reactive Wakeup**: No busy loops polling `manage_task(status)`; agents wake via reactive background event notifications.
8. **Tri-Gate Completion Firewall**: Non-trivial deliverables must clear Gate 1 (Build exit 0), Gate 2 (Visual/Interactive artifact), and Gate 3 (Adversarial Critic approval $Q \ge 9.0$).

---

## 7. Core Methodologies (Superpowers and Gauntlet-Loop)

### True Red-Green-Refactor TDD
```
┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
│          1. RED           │ ───> │         2. GREEN          │ ───> │        3. REFACTOR        │
│   Write Failing Test      │      │   Minimal Passing Logic   │      │   Clean, Typed & Scalable │
└───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘
```

### 5-Component Structured Subagent Handoff
Every subagent transfer report (`handoff.md`) contains:
1. **Observation**: Exact file paths, line numbers, verbatim outputs, and tool logs.
2. **Logic Chain**: Deductive, step-by-step reasoning from observations to findings.
3. **Caveats**: Scope boundaries, external dependencies, and assumptions.
4. **Conclusion**: Direct, unambiguous, and actionable summary.
5. **Verification Method**: Independent reproduction command (e.g. `python test_plugin.py`) and invalidation conditions.

---

## 8. Comprehensive 70-Skill Catalog

The plugin includes **70 high-density autonomous skills** organized across 5 specialized cognitive sectors:

### Sector 1: System 2 Cognitive Reasoning, Planning and Epistemic Governance (28 Skills)

| Skill Name | Primary Capability and Trigger Directive |
|---|---|
| [`active-inference-theory-of-mind`](skills/active-inference-theory-of-mind/SKILL.md) | AGI/ASI protocol for Multiagent Theory of Mind. Enforces Markov Blankets around subagent state and dynamic belief inference to prevent swarm hallucination. |
| [`agi-prompt-refiner`](skills/agi-prompt-refiner/SKILL.md) | MANDATORY. Use when the user provides a brief, short (<= 200 chars), ambiguous, or simple request, or asks to format, plan, improve, or turn a request into an AGI-level prompt. |
| [`agy-customizations`](skills/agy-customizations/SKILL.md) | Comprehensive guide and reference for the Antigravity Customization System. Use to explain how customizations work, their loading priority, discovery mechanisms, and to guide the creation of skills, rules, plugins, hooks, and MCP servers. |
| [`antigravity-guide`](skills/antigravity-guide/SKILL.md) | Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy), Antigravity 2.0, Antigravity IDE, Python SDK, slash commands, keybindings, and customizations (skills, rules, MCP, sidecars). Activate this skill when the user asks questions about how to use, configure, or customize Antigravity, AGY, the agy CLI, the Antigravity IDE, or Antigravity 2.0. |
| [`autonomous-insight-extractor`](skills/autonomous-insight-extractor/SKILL.md) | MANDATORY. Use at the end of tasks, major features, debugging sessions, or when triggered by /learn to extract and persist reusable skills and rules. |
| [`cognitive-memory`](skills/cognitive-memory/SKILL.md) | Canonical Cognitive State Memory Architecture & Transactional Schema Engine. Governs structured JSON-Schema state serialization, atomic state transitions, multi-agent context synchronization, and persistent cognitive continuity. |
| [`competitive-reference-benchmarking`](skills/competitive-reference-benchmarking/SKILL.md) | MANDATORY. Use before starting design/architecture of a new domain, interface, or product. Forces the agent to search the web, find the state-of-the-art reference bar, and compare before building. |
| [`context-preservation`](skills/context-preservation/SKILL.md) | Adaptive Context Window Governance, Dynamic Load Profiling & Context Entropy Management. Dynamically tracks model-specific token budgets, enforces semantic distillation, prevents context degradation, and manages seamless state handoffs. |
| [`cross-sector-integration`](skills/cross-sector-integration/SKILL.md) | Unified AGI protocol for cross-sector topological boundary integration, Quarantine Specification drafting, type-theoretic contract enforcement, and Production Blueprint generation. |
| [`deep-planning-protocol`](skills/deep-planning-protocol/SKILL.md) | MANDATORY. Protocolo de planejamento profundo obrigatório para qualquer projeto não-trivial. Exige 5 documentos formais aprovados ANTES de qualquer linha de código. |
| [`domain-alpha-prospecting`](skills/domain-alpha-prospecting/SKILL.md) | MANDATORY. Use when entering complex, high-stakes domains (Distributed Systems, AI/ML, Scientific Computing, Quantitative Finance, Cryptography, 3D/Simulation, Embedded/Robotics). Conducts deep research into state-of-the-art algorithms, formal standards, and competitive Alpha before writing logic. |
| [`dynamic-constitutional-evolution`](skills/dynamic-constitutional-evolution/SKILL.md) | Meta-Constitutional Self-Evolution & Dynamic Capability Lifecycle Manager. Enforces formal logic constitutional compliance, dynamic skill synthesis, information-theoretic fitness evaluation, and unbounded hierarchical skill tree scaling. |
| [`epistemic-governance`](skills/epistemic-governance/SKILL.md) | Autonomous AGI/ASI Epistemic Calibration & Formal Truth Governance Protocol. Enforces formal logic boundaries, dynamic Bayesian belief updates, machine-verifiable DEC labeling, and information-theoretic epistemic entropy monitoring across all cognitive outputs. |
| [`epistemic-stop-and-think`](skills/epistemic-stop-and-think/SKILL.md) | MANDATORY. Intercepta o agente ANTES de qualquer ação quando ele enfrenta ignorância, incerteza ou complexidade opaca. Proíbe tentativas cegas (50/50). Força a sequência invariável: PARAR → INVESTIGAR → DOCUMENTAR → HIPÓTESE CAUSAL → PLANEJAR → SOMENTE ENTÃO AGIR. |
| [`google-antigravity-sdk`](skills/google-antigravity-sdk/SKILL.md) | Design, implement, and debug autonomous AI agents and multi-agent systems using the Google Antigravity (AGY) SDK. Activates when configuring LocalAgentConfig, CapabilitiesConfig, LiteRT/OpenAI local models, subagent recursion depth, budget limits, or safety policies. |
| [`grill-me-layered`](skills/grill-me-layered/SKILL.md) | MANDATORY. Protocolo de entrevista profunda em 12 tópicos organizados em 4 camadas progressivas (Escopo → Arquitetura → Debate → Contratos). Ativado pelo comando /grill-me ou quando o projeto exige alinhamento profundo antes de planejamento. |
| [`meta-skill-synthesis`](skills/meta-skill-synthesis/SKILL.md) | Protocolo AGI/ASI de Autoaprendizado de Máquina. Define como o agente deve extrair insights técnicos duradouros de uma sessão e sintetizá-los em novas skills definitivas no próprio disco. |
| [`multiversal-poly-skill-entanglement`](skills/multiversal-poly-skill-entanglement/SKILL.md) | MANDATORY. Master Multiversal Poly-Skill Entanglement & Hypergraph Expansion Engine. Eliminates cognitive myopia and single-skill silos. Enforces 1:N fan-out orchestration across 4-part skill vectors (Primary, Auxiliary, Multimodal, Falsification) and cascading wave swarms (C_max <= 2). |
| [`omni-holistic-planner`](skills/omni-holistic-planner/SKILL.md) | MANDATORY. Master AGI/ASI Autonomous Planning & Latent Context Expansion Engine (X -> X ∪ Y). Intercepts any project or feature request, expands unsaid context across 10 enterprise dimensions (Branding, Architecture, Security, Legal, Logistics, Multi-State UX, Competitor Benchmarking, Real Assets, SEO, and Empirical Verification), and generates a zero-laziness production blueprint before execution. |
| [`one-shot-ultra-loop-engine`](skills/one-shot-ultra-loop-engine/SKILL.md) | MANDATORY. Intercepts broad or short one-shot prompt requests (systems, web apps, distributed backends, AI models, 3D simulations, CLI engines) and enforces an autonomous, multi-subsystem, multi-iteration ultra-loop execution until Quality Score Q >= 9.0/10 without shallow MVPs or premature stops. |
| [`permissioned-github`](skills/permissioned-github/SKILL.md) | Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agent environment. |
| [`project-neural-map`](skills/project-neural-map/SKILL.md) | MANDATORY. Protocolo de memória recursiva de longo prazo para projetos complexos. Implementa PROJECT_BRAIN.md (índice global) + NODE.md por módulo com 4 status dinâmicos. DEVE ser lido como primeira ação de qualquer turno em projeto ativo. |
| [`recursive-dual-loop-optimizer`](skills/recursive-dual-loop-optimizer/SKILL.md) | AGI/ASI Autonomous Recursive Self-Improvement engine. Implements a Dual-Loop architecture to safely rewrite system prompts and skills without Model Collapse. |
| [`sprint-audit-session`](skills/sprint-audit-session/SKILL.md) | Autonomous session management and state serialization protocol enforcing continuous multi-agent repository auditing and zero-loss context persistence. |
| [`structured-reasoning-engine`](skills/structured-reasoning-engine/SKILL.md) | MANDATORY. Use when facing architectural choices with 2+ alternatives, complex trade-offs, formal mathematical proofs, or deep multi-branch reasoning (Graph-of-Thought). |
| [`technical-documentation-crafting`](skills/technical-documentation-crafting/SKILL.md) | Use when creating or refining open-source documentation, READMEs, and technical landing pages to maximize clarity, scientific credibility, and developer conversion. |
| [`technological-prospecting`](skills/technological-prospecting/SKILL.md) | MANDATORY. Use when researching external APIs, libraries, framework capabilities, MCP servers, or benchmarking third-party technologies. |
| [`thesis-triage-funnel`](skills/thesis-triage-funnel/SKILL.md) | Autonomous Multi-Agent Thesis Triage & Causal Falsification Engine. Blocks speculative, ungrounded ideas from entering production via a rigorous 5-phase causal and theoretical triage funnel. |

### Sector 2: Software Engineering, True TDD and Systematic Debugging (9 Skills)

| Skill Name | Primary Capability and Trigger Directive |
|---|---|
| [`autonomous-workspace-orchestration`](skills/autonomous-workspace-orchestration/SKILL.md) | Gerenciamento autônomo de Git Worktrees para isolamento de estado durante missões de refatoração ou testes invasivos. |
| [`causal-debugging-protocol`](skills/causal-debugging-protocol/SKILL.md) | Guides deep causal root-cause investigations using mathematical state tracing, invariant tree verification, and Popperian falsification. Maps failure paths backwards and enforces atomic bug isolation with zero guesswork. |
| [`deep-iceberg-autonomous-engine`](skills/deep-iceberg-autonomous-engine/SKILL.md) | MANDATORY. Master AGI/ASI Deep Iceberg Engine (100% Depth Mandate). Prohibits stopping at the 5% surface level (naive UI, happy-path, static mocks). Enforces the 7 Deep Layers of production engineering (Causal DAG, Chaos/Idempotency, Tactile Sonification, Zero-Latency Optimistic UI, Telemetric Observability HUD, Immutability/Event Sourcing, and Self-Healing Offline-First Resilience). |
| [`master-refactoring-pipeline`](skills/master-refactoring-pipeline/SKILL.md) | MANDATORY. Use when creating, editing, refactoring, restructuring, or rebuilding code, modules, or services. Enforces zero-hardcoding and 8-phase theoretical reconstruction. |
| [`proactive-domain-bootstrapper`](skills/proactive-domain-bootstrapper/SKILL.md) | MANDATORY. Use when starting a new project domain, sourcing multimodal assets, injecting industry standards (PBR, real physics, consensus algorithms, low-latency patterns), or bootstrapping applications. |
| [`scientific-research-contract`](skills/scientific-research-contract/SKILL.md) | MANDATORY. Use for scientific grounding, mathematical modeling, LaTeX derivation of algorithms, or formal theorem contracts before coding. |
| [`session-handoff-protocol`](skills/session-handoff-protocol/SKILL.md) | Manages transactional session state serialization, cryptographic SHA-256 state hashing, and atomic session handoffs across agent turns or context windows. Eliminates hallucinations and context drift during long-horizon tasks. |
| [`systematic-debugging`](skills/systematic-debugging/SKILL.md) | Executes a rigorous 4-phase root-cause debugging protocol (Reproduce, Isolate, Diagnose, Verify) for complex defects. Eliminates trial-and-error edits, enforces zero-guesswork instrumentation, and triggers escalation upon 3 consecutive failures. |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Enforces strict Test-Driven Development (TDD) workflows using the Red-Green-Refactor cycle. Guides agents to write failing unit or integration tests before production code, implement minimal passing logic, and refactor cleanly with zero regressions. |

### Sector 3: Adversarial Quality, Invariance Testing and Evolution (9 Skills)

| Skill Name | Primary Capability and Trigger Directive |
|---|---|
| [`adversarial-tribunal`](skills/adversarial-tribunal/SKILL.md) | MANDATORY. Use for post-milestone quality audits, Red Team vs Blue Team architectural review, zero-trust validation, or security/robustness checks. |
| [`audit-tier-classifier`](skills/audit-tier-classifier/SKILL.md) | AST complexity and entropy-driven classification engine establishing 3-tier audit depth allocation for codebase analysis. |
| [`continuous-evolution-loop`](skills/continuous-evolution-loop/SKILL.md) | MANDATORY. Use for ANY non-trivial project. Enforces an infinite self-improvement loop of testing and refinement until the Reference Bar is surpassed. |
| [`gauntlet-loop`](skills/gauntlet-loop/SKILL.md) | Orchestrates double-blind Builder and Critic adversarial verification loops against an explicit Named Reference Bar. Enforces Dual-Gate convergence (empirical test pass and blind qualitative score Q >= 9.0) with Lyapunov delta stabilization. |
| [`integration-consensus-gate`](skills/integration-consensus-gate/SKILL.md) | Protocolo de aprovação final para merge de branches e finalização de tarefas arquiteturais complexas. |
| [`point-w-evolutionary-engine`](skills/point-w-evolutionary-engine/SKILL.md) | MANDATORY. Mathematical & Empirical Governance of Point W Convergence. Enforces hyper-critical adversarial double-blind critique, eliminates self-congratulatory LLM bias, and governs multi-cycle recursive evolution until non-trivial world-class superiority (Point W) is mathematically and empirically achieved. |
| [`popperian-invariance-testing`](skills/popperian-invariance-testing/SKILL.md) | Master scientific validation protocol fusing Popperian falsificationism, metamorphic invariance testing across topological, scale, temporal, and regime dimensions, and automated hypothesis tracking. |
| [`pragmatic-quality-inspection`](skills/pragmatic-quality-inspection/SKILL.md) | Consolidated master quality framework enforcing Evidence-Before-Assertion (Anti-Hallucination), Prompt Dispatch Shielding, Worker Report Verification, and Safety-First Architectural SWOT Analysis. |
| [`zero-trust-scientific-review`](skills/zero-trust-scientific-review/SKILL.md) | AGI/ASI Scientific Review Protocol. Governs mandatory zero-trust adversarial review of architectural specifications. Dynamically stress-tests mathematical models, performance bounds, robustness contracts, and safety guarantees before blueprinting. |

### Sector 4: Browser Automation, Chrome DevTools and Modern Web Suite (8 Skills)

| Skill Name | Primary Capability and Trigger Directive |
|---|---|
| [`a11y-debugging`](skills/a11y-debugging/SKILL.md) | Uses Chrome DevTools MCP for accessibility (a11y) debugging and auditing based on web.dev guidelines. Use when testing semantic HTML, ARIA labels, focus states, keyboard navigation, tap targets, and color contrast. |
| [`chrome-devtools`](skills/chrome-devtools/SKILL.md) | Uses Chrome DevTools via MCP for efficient debugging, troubleshooting and browser automation. Use when debugging web pages, automating browser interactions, analyzing performance, or inspecting network requests. This skill does not apply to `--slim` mode (MCP configuration). |
| [`chrome-devtools-troubleshooting`](skills/chrome-devtools-troubleshooting/SKILL.md) | Uses Chrome DevTools MCP and documentation to troubleshoot connection and target issues. Trigger this skill when list_pages, new_page, or navigate_page fail, or when the server initialization fails. |
| [`chrome-extensions`](skills/chrome-extensions/SKILL.md) | Build and publish Chrome Extensions using Manifest V3 best practices. Use this skill whenever the user asks to create, modify, debug, or understand Chrome browser extensions, add-ons, or anything involving the Chrome Extensions API. Trigger on mentions of: 'Chrome extension', 'browser extension', 'manifest.json', 'content script', 'service worker' (in browser context), 'popup' (in browser extension context), 'side panel', 'chrome.* API', 'declarativeNetRequest', 'omnibox', 'context menu' (in extension context), or any request to build functionality that integrates with the Chrome browser UI. Also trigger for publishing to the Chrome Web Store: 'publish extension', preparing an extension for publishing, responding to a review rejection, writing permission justifications, or drafting a privacy policy. |
| [`debug-optimize-lcp`](skills/debug-optimize-lcp/SKILL.md) | Guides debugging and optimizing Largest Contentful Paint (LCP) using Chrome DevTools MCP tools. Use this skill whenever the user asks about LCP performance, slow page loads, Core Web Vitals optimization, or wants to understand why their page's main content takes too long to appear. Also use when the user mentions "largest contentful paint", "page load speed", "CWV", or wants to improve how fast their hero image or main content renders. |
| [`memory-leak-debugging`](skills/memory-leak-debugging/SKILL.md) | Diagnoses and resolves memory leaks in JavaScript/Node.js applications. Use when a user reports high memory usage, OOM errors, or wants to analyze heapsnapshots or run memory leak detection tools like memlab. |
| [`modern-web-guidance`](skills/modern-web-guidance/SKILL.md) | Search tool for modern web development best practices. MANDATORY: Execute FIRST for all HTML/CSS and clientside JS tasks. Do NOT skip — web APIs evolve rapidly and training weights contain obsolete patterns. Trigger immediately for: - UI/Layout: Modals, dialogs, popovers, Glassmorphism/backdrop-filters, anchor positioning, container queries, `:has()`, `:user-valid`. - Scroll/Motion: View Transitions, Scroll-driven animations, scroll parallax/reveals. - Performance: CWV (LCP, INP), content-visibility, Fetch Priority, image optimization. - System/APIs: Local filesystem access, WebUSB, WebSockets sync, WebAssembly widgets. - Frameworks: Adapting layout/styles in React, Vue, Angular. - General Frontend: Forms, autofill, advanced inputs, custom scrollbars, modern component states, etc. DO NOT trigger for: - Backend: Database SQL, ORMs, Express API routes. - Pipelines: CI/CD deployment, Docker, Actions. - Generic: Local scripts (Python/Go tools), ESLint, Git. |
| [`puppeteer-browser-automation`](skills/puppeteer-browser-automation/SKILL.md) | MANDATORY. Protocol for autonomous browser automation, web scraping, live UI testing, form interaction, and multi-state visual verification using the bundled Puppeteer MCP server. |

### Sector 5: Multimodal Assets, Procedural 3D/Spatial and Swarm Governance (16 Skills)

| Skill Name | Primary Capability and Trigger Directive |
|---|---|
| [`corporate-swarm-os`](skills/corporate-swarm-os/SKILL.md) | MANDATORY. Protocolo de modelo empresarial AGI/ASI. Define hierarquia formal CEO→C-Level→Times com BRIEF.md extenso por nível, SECTOR.md com KPIs, contratos de entrega e SLAs. Use ao iniciar qualquer projeto com 3+ arquivos ou múltiplos subagentes. |
| [`gemini-omni-video-generation`](skills/gemini-omni-video-generation/SKILL.md) | MANDATORY. Master Gemini Omni & Veo Video Generation Engine. Governs cinematic prompt crafting, camera optics, temporal physics coherence, frame interpolation, seamless looping, video poster synthesis, and Web/App high-performance integration. |
| [`interactive-kinetic-media-engine`](skills/interactive-kinetic-media-engine/SKILL.md) | MANDATORY. Use for scroll-driven video scrubbing, multi-layer parallax, scrollytelling sticky chapters, 3D cursor tilt, clip-path mask reveals, and bespoke 3D/glass icon asset synthesis with micro-interactions. |
| [`interactive-visual-auditing`](skills/interactive-visual-auditing/SKILL.md) | MANDATORY. Use after a UI component, frontend page, or game scene is built. Enforces live visual testing via the /browser slash command and auto-rejects 'generic' or 'basic' aesthetics. |
| [`massive-batch-orchestration`](skills/massive-batch-orchestration/SKILL.md) | MANDATORY. Use when processing, auditing, refactoring, or building large codebases (+10 files) or long-running projects via subagent swarms. Integrates with Corporate OS (BRIEF.md + PROJECT_BRAIN.md). |
| [`omni-experience-synthesis`](skills/omni-experience-synthesis/SKILL.md) | Universal AGI/ASI engine for orchestrating trans-domain, ultra-modern digital experiences (Awwwards/FWA tier). Integrates dynamic design archetypes, clean developer UI, liquid glassmorphism, monumental editorial typography, Gemini Veo/Omni video generation, multimodal asset synthesis, and zero-cliché interactive architectures across developer tools, enterprise SaaS, fintech, spatial, narrative, architectural, and creative domains. |
| [`omni-multimodal-spatial-engine`](skills/omni-multimodal-spatial-engine/SKILL.md) | MANDATORY. Use for Multimodal Spatial Reasoning, procedural 3D math & GLSL shader generation, 3D bounding box projection, raymarching, Interior Mapping & Window Parallax shaders, audio-reactive visual synthesis, and high-frequency Flash swarm subagent execution. |
| [`sketchfab-prospecting-protocol`](skills/sketchfab-prospecting-protocol/SKILL.md) | Universal protocol for autonomously researching, evaluating, visually inspecting via candidate catalogs, and integrating 3D models, CAD assets, scientific meshes, and spatial environments from Sketchfab and open 3D repositories. Use whenever a project requires 3D assets, meshes, props, or spatial data. |
| [`subagent-handoff`](skills/subagent-handoff/SKILL.md) | Standardizes structured multi-agent coordination and task transfer using the 5-component handoff protocol (Observation, Logic Chain, Caveats, Conclusion, Verification Method). Guarantees context-isolated execution boundaries and zero context loss. |
| [`swarm-frequency-governor`](skills/swarm-frequency-governor/SKILL.md) | Use before dispatching any batch of parallel Workers to enforce the 2-concurrent-subagent limit, prevent 429 RESOURCE_EXHAUSTED errors, and sequence large swarms safely. |
| [`swarm-legacy-archaeology`](skills/swarm-legacy-archaeology/SKILL.md) | Consolidated skill for multi-level parallel swarm auditing of legacy repositories. Handles directory mapping, tier classification, batch planning, handoff generation, dashboard progress tracking, gap analysis, and the coverage gate. |
| [`swarm-mission-genesis`](skills/swarm-mission-genesis/SKILL.md) | MANDATORY. Use at the start of any new complex project, major application, multi-file system, or massive mission pre-flight scoping. Integrates with Corporate OS (grill-me-layered, deep-planning-protocol, project-neural-map, corporate-swarm-os). |
| [`swarm-synthesis-protocol`](skills/swarm-synthesis-protocol/SKILL.md) | Unified skill governing the synthesis phase where all legacy audits under a specific Conceptual Key are merged, debated, and refined. Fuses the 4-level approval pipeline, quarantine specifications, zero-trust scientific review, and cross-sector integration. Replaces swarm-synthesis, synthesis workflow, and swarm-synthesis workflow. |
| [`swarm-topology-delegation`](skills/swarm-topology-delegation/SKILL.md) | Governs the multi-level parallel chat swarm, programmatic subagent teams, and execution mode decisions. Consolidates orchestration hierarchy, swarm map tracking, and worker role classification (CEO Direct, Manual Parallel Chat, Programmatic Subagent). |
| [`visual-synthesis-engine`](skills/visual-synthesis-engine/SKILL.md) | MANDATORY. Use for any visual asset generation, web app design, frontend UI panels, CSS styling, glassmorphism components, graphics, HTML layouts, or AAA WebGL environments (Bloom, Fog, PBR). |
| [`youtube-audio-prospecting`](skills/youtube-audio-prospecting/SKILL.md) | Universal protocol for researching, identifying, extracting, and synthesizing authentic audio assets, acoustic telemetry, and soundscapes from open multimedia sources (YouTube, Freesound, OpenAudio, NASA Audio). Use when a project requires real sound effects, ambient audio, telemetry sonification, or music. |

---

## 9. Model Context Protocol (MCP) Configuration

Configured in `mcp_config.json`:

```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"],
      "env": {
        "PUPPETEER_HEADLESS": "true",
        "PUPPETEER_DEFAULT_VIEWPORT_WIDTH": "1920",
        "PUPPETEER_DEFAULT_VIEWPORT_HEIGHT": "1080"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--autoConnect"],
      "env": {
        "CHROME_STARTUP_TIMEOUT": "20000"
      }
    }
  }
}
```

---

## 10. Lifecycle Hooks and Security Firewall

Declaratively registered in `hooks.json` to enforce execution safety and telemetry:

- **`PreToolUse` (`hooks/pre_tool_validator.py`)**:
  - Validates tool names against deprecated and phantom mappings.
  - Sanitizes filesystem path arguments against null-byte and directory traversal attacks.
  - Intercepts and blocks destructive commands, fork bombs, and unsafe operations.
- **`PostToolUse` (`hooks/post_tool_linter.py`)**:
  - Intercepts tool execution errors and logs structured telemetry.
  - Returns `{}` conforming strictly to the Antigravity protojson contract.
- **`Stop` (`hooks/stop_gatekeeper.py`)**:
  - Inspects `fullyIdle` and `terminationReason`.
  - Prevents premature loop termination if background asynchronous tasks or subagents are active.

---

## 11. Automated Verification and Quality Certification

To run the complete verification suite across all manifests, skills, markdown links, hook contracts, and tool bindings:

```bash
# Run standalone test runner
python test_plugin.py

# Or run via pytest
pytest
```

### Verification Test Matrix:
- ✅ **Manifest and Config Schema**: Validates `plugin.json`, `mcp_config.json`, and `hooks.json`.
- ✅ **Skills Frontmatter Integrity**: 100% compliant YAML headers with matching names and descriptions.
- ✅ **Markdown Link Resolution**: Zero broken relative links across documentation and skill files.
- ✅ **Zero-Placeholder Law**: Zero `TODO`, `pass`, or synthetic mocks in production logic.
- ✅ **Tool Registry Bindings**: 100% verified tool references matching Antigravity native and MCP registries.
- ✅ **Lifecycle Hooks Contract**: Verified stdin/stdout JSON protocol conformance.
- ✅ **Autonomous 5-Phase Cycle**: End-to-end simulated execution clearing Quality Score $Q \ge 9.0/10$.

---

## 12. License

Apache-2.0 © 2026 AGI Core Architecture Team

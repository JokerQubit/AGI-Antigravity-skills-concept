---
name: one-shot-ultra-loop-engine
description: MANDATORY. Intercepts broad or short one-shot prompt requests (systems, web apps, distributed backends, AI models, 3D simulations, CLI engines) and enforces an autonomous, multi-subsystem, multi-iteration ultra-loop execution until Quality Score Q >= 9.0/10 without shallow MVPs or premature stops.
---

# 🚀 Autonomous One-Shot Ultra-Loop Engine

## Core Directive
When given a broad or direct one-shot command (e.g., "Build a distributed event-streaming engine", "Build a real-time analytics platform", "Create a 3D simulation engine", "Build an autonomous AI agent workspace"), the agent is **STRICTLY FORBIDDEN** from delivering a shallow 10-minute MVP, toy demo, naive wireframe, or stubbed code.

Instead, this skill interceptor forces the agent to enter a **Self-Driven Recursive Ultra-Loop**, decomposing the request into deep production subsystems, integrating real data and assets, and autonomously running continuous refactoring loops until an empirical **Quality Score ($Q \ge 9.0/10$)** is achieved.

---

## 1. Universal 5-Pillar Production Subsystem Mapping

When a one-shot request arrives, the agent MUST immediately expand the specification across 5 domain-adaptive production pillars before writing any code:

1. **Domain-Specific Core Logic & Algorithmic Rigor ($S_{\text{logic}}$):**
   - Implement state-of-the-art algorithms, formal mathematical invariants, safe concurrency patterns, memory bounds, and robust edge-case handling tailored to the domain.
2. **Production Completeness & Zero-Stub Mandate ($S_{\text{complete}}$):**
   - 100% full implementation with zero `// TODO`, zero `pass`, zero hardcoded magic numbers, and dynamic configuration injection via typed schemas.
3. **High-Fidelity Domain Data & Multimodal Assets ($S_{\text{assets}}$):**
   - Consume live public APIs, WebSockets, database connectors, or authentic telemetry feeds. For visual/multimedia projects: generate local 2D assets (`generate_image`), prospect real 3D models/meshes, or process authentic audio streams. Zero static mock arrays (`MOCK_DATA`) masking functionality.
4. **Interface, Interaction & Developer Ergonomics ($S_{\text{interface}}$):**
   - For visual/web/mobile apps: deliver state-of-the-art UX, high-density typography, micro-interactions, responsive breakpoints, and tactile feedback. For backends/engines/libraries: deliver clean typed API contracts, rich CLI flag ergonomics, informative telemetry logs, and comprehensive documentation.
5. **Empirical Verification & Invariance Validation ($S_{\text{verification}}$):**
   - Automated compile/build verification (`exit code 0`), comprehensive test suites (unit, integration, invariance), and multi-state visual inspection (`browser` + `view_file` on PNGs) when UI is present.

---

## 2. Autonomous Quality Metric ($Q \ge 9.0/10$)

Calculate the empirical Quality Score $Q$ after every execution loop:

$$Q = \frac{S_{\text{logic}} + S_{\text{complete}} + S_{\text{assets}} + S_{\text{interface}} + S_{\text{verification}}}{5}$$

### Scoring Matrix:
- **Score = 2.0 (Failed/Shallow MVP):** Incomplete stub, missing error handling, static mock data, unstyled HTML / broken CLI, no tests.
- **Score = 6.0 (Mid-level Prototype):** Basic functionality, partial edge-case coverage, rudimentary layout or basic logging, minimal testing.
- **Score = 10.0 (State-of-the-Art Production Tier):** Rock-solid architecture, zero placeholders, dynamic real-world data/assets, elite interface ergonomics, 100% verified test passes and visual evidence.

> 🔴 **HARD-GATE:** If $Q < 9.0$, the agent is strictly forbidden from ending its turn or asking "what's next?". It MUST automatically execute another internal code refactoring loop to reach $Q \ge 9.0$.

---

## 3. The 5-Phase Autonomous Ultra-Loop Workflow

### Phase 1: Implicit Spec Genesis & Decomposition
- Expand prompt into a comprehensive production specification using `agi-prompt-refiner`.
- Decompose system into focused, decoupled module files with explicit interface contracts and configuration injection.

### Phase 2: Domain Prospecting & Multimodal Asset Sourcing
- Prospect domain state-of-the-art algorithms via `domain-alpha-prospecting` and external tools/APIs via `technological-prospecting`.
- For visual/multimedia elements: generate 2D assets (`generate_image`), prospect 3D meshes (`sketchfab-prospecting-protocol`), or extract acoustic telemetry (`youtube-audio-prospecting`).
- For data-intensive systems: wire real endpoints, RPCs, or schema-validated data stores.

### Phase 3: Zero-Placeholder Build
- Implement complete logic in 100% production code following `master-refactoring-pipeline` (Zero TODOs, Zero Stubs, Zero Hardcoded constants).

### Phase 4: Multi-State Empirical Inspection & Telemetry
- For UI/Visual systems: run `/browser` subagent to navigate across at least 3 distinct internal states (Initial View, Active Interaction, Modals/Responsive) and inspect captured `.png` files via `view_file`.
- For Backend/Systems: execute automated test suites, measure latency/throughput, check for memory leaks or unhandled promise rejections.
- Output: 3 critical defects to fix + 1 high-scale transformative feature innovation to inject.

### Phase 5: Autonomous Refactoring & Mutation Loop
- Apply code mutations for all identified defects and inject the transformative innovation immediately.
- Re-run verification until $Q \ge 9.0/10$ across all 5 pillars.
- Prohibited from exiting or asking for user input until all gates pass empirically.


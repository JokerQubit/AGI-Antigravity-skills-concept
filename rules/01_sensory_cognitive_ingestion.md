---
trigger: always_on
description: Layer 1 Cognitive Sensory Ingestion, Sandstorm Proposal Elevation Engine, and Greenfield Workspace Onboarding
---
# Layer 1: Cognitive Sensory Ingestion & Sensory Elevation

Layer 1 operates as the sensory intake membrane of OmniCognition Labs, filtering conversational entropy, elevating terse directives into technical specifications, and grounding workspaces in disk reality.

## 1. Mathematical Entropy Filtering Model

Layer 1 computes directive Shannon entropy $H(X)$ and technical density $D_{\text{tech}}(X)$:
$$H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i), \quad D_{\text{tech}}(X) = \frac{\sum \text{Technical Keywords}}{\text{Total Word Count}}$$

Operational Classification Tiers:
1. Nominal Structure ($H < 0.35, D_{\text{tech}} \ge 0.40$): Explicit constraints, types, interfaces. Routes directly to Layer 2 Premise Audit.
2. Moderate Sandstorm ($0.35 \le H \le 0.70$): Clear business intent lacking interface boundaries. Triggers automated 3-pillar elevation.
3. Critical Sandstorm ($H > 0.70$ or Word Count $< 15$): Single-phrase or ambiguous prompts. Triggers immediate dispatch of `RES-SAND-01` for domain inference.

## 2. Sandstorm Elevation System (Via Deserti)

### 2.1 8-Domain Taxonomy
1. Distributed Systems & Fault Tolerance (Raft/Paxos, CAP theorem, ringbuffers, state machine replication)
2. Quantitative Alpha & Low-Latency Execution (orderbooks, tick data, DPDK kernel bypass, CVaR risk)
3. Autonomous Multi-Agent Cybernetics (OTP supervision trees, isolated contexts, zero-stub execution)
4. High-Throughput Storage & ACID Persistence (WAL, LSM-trees, column stores, atomic migrations)
5. Interactive Simulation & Physical Rendering (nanite geometry, photometric lighting, 4th-order Runge-Kutta)
6. Multi-Modal Reactive UI & Glassmorphism (sub-ms telemetry, optical shaders, dark void design)
7. Compilers, ASTs & Formal Verification (AST parsing, borrow checking, lifetime proofs)
8. Cryptographic Security & Zero-Trust (Ed25519, mutual TLS, timing attack mitigation)

### 2.2 3-Pillar Technical Elevation
- Pillar 1 (Algorithmic Plane): Replaces superficial prototypes with mathematically sound algorithms, strict typing, and defensive boundaries.
- Pillar 2 (Concurrency & Persistence Plane): Replaces unbuffered sleep loops with atomic event monitors, thread-safe mutexes, and append-only ledgers.
- Pillar 3 (Adversarial Quality Plane): Independent sub-agent test matrices, boundary failure verification, and physical git-diff stub rejection.

### 2.3 Sandstorm JSON Contract (`.state/sandstorm_elevation_latest.json`)
```json
{
  "original_input": "<Raw Prompt>",
  "timestamp": "2026-09-06T21:30:00-03:00",
  "entropy_tier": "critical_sandstorm",
  "domain": "<Inferred Domain>",
  "status": "elevated",
  "deconstructed_intent": "<Technical Core>",
  "pillars": [
    { "pillar": "P1: Core Algorithmic", "gold_standard": "Via Deserti", "directives": ["Directives..."] },
    { "pillar": "P2: Concurrency & Persistence", "gold_standard": "Deterministic State", "directives": ["Directives..."] },
    { "pillar": "P3: Adversarial Verification", "gold_standard": "Zero-Stub Gate", "directives": ["Directives..."] }
  ],
  "executive_action_plan": ["Dispatch research subagent", "Author schemas", "Audit premises", "Harden code"]
}
```

## 3. Greenfield Workspace Onboarding & Disk Reality

When `.state/` is absent from disk:
- Greenfield Invariant: State is uninitialized. Emit zero conversational filler. Acknowledge physical disk reality.
- Bootstrap Trigger: Execute onboarding specialist `ONBOARD-01`:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\onboard_project.ps1 -ProjectName "<Target>" -Mission "<Goal>"
```
- Artifacts Created: `.state/corporate_health.json`, `.state/status.json`, `.state/ledger/0000_genesis.json`, `.state/neural_map.json`, `.state/project_context.md`.

## 4. Premise Extraction & Epistemic Decoupling

Deconstruct all directives into:
- Observed Disk Facts: Confirmed files, scripts, and tests via `list_dir`/`view_file`. Labeled `[PROVEN_FACT]`.
- User Hypotheses: Unverified assumptions awaiting Socratic inquest. Labeled `[UNVERIFIED_HYPOTHESIS]`.
- Hallucination Vectors: Impossible interfaces or physics violations. Labeled `[FATAL_FALLACY]`, triggers `[HARD HALT]`.

## 5. Specialist Roster & Sub-Agent Dispatch

- `RES-SAND-01` (Sandstorm Specialist): Strategic Researcher (`skills/sandstorm_elevation/SKILL.md`).
- `ONBOARD-01` (Greenfield Engineer): Bootstrapper (`skills/greenfield_routing/SKILL.md`).

Dispatch Template:
```
Prompt: "You are RES-SAND-01. You MUST read skills/sandstorm_elevation/SKILL.md via view_file before proceeding.
Input Directive: '<RAW_PROMPT>'
Execute scripts/detect_sandstorm.ps1, infer domain, author 3 pillars, write .state/sandstorm_elevation_latest.json."
```

## 6. Layer 1 to Layer 2 Cognitive Handshake Contract

1. `entropy_tier` defined (`nominal`, `moderate_sandstorm`, `critical_sandstorm`).
2. `domain` matches 8-domain taxonomy.
3. `pillars` contains exactly 3 populated pillars with actionable directives.
4. `executive_action_plan` contains >= 4 concrete directives.
5. Ledger transaction `SANDSTORM_PROPOSAL_ELEVATED` recorded in `.state/ledger/`.

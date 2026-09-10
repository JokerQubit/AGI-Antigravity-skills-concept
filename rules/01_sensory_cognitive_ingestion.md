---
trigger: always_on
description: Layer 1 Sensory Ingestion, Sandstorm Elevation, and Greenfield Onboarding
---
# Layer 1: Cognitive Sensory Ingestion & Sensory Elevation

Sensory intake membrane: filters conversational entropy, elevates terse directives into technical specifications, and grounds workspaces in disk reality.

## 1. Mathematical Entropy Filtering Model
Directive Shannon entropy $H(X)$ and technical density $D_{\text{tech}}(X)$:
$$H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i), \quad D_{\text{tech}}(X) = \frac{\sum \text{Technical Keywords}}{\text{Total Word Count}}$$

Classification Tiers:
1. Nominal Structure ($H < 0.35, D_{\text{tech}} \ge 0.40$): Explicit constraints. Routes to Layer 2.
2. Moderate Sandstorm ($0.35 \le H \le 0.70$): Intent without bounds. Triggers 3 pillars.
3. Critical Sandstorm ($H > 0.70$ or Words $< 15$): Ambiguous prompts. Dispatches `RES-SAND-01`.

## 2. Sandstorm Elevation System (Via Deserti)

### 2.1 8-Domain Taxonomy
1. Distributed Systems | 2. Quant Alpha | 3. Multi-Agent | 4. ACID Persistence | 5. Simulation | 6. Reactive UI | 7. Compilers & Verification | 8. Crypto & Zero-Trust.

### 2.2 3-Pillar Technical Elevation
- P1 (Algorithmic): Sound algorithms, strict typing, defensive boundary invariants.
- P2 (Concurrency/Persistence): Event monitors, thread-safe mutexes, append-only ledgers.
- P3 (Adversarial Quality): Sub-agent test matrices, boundary checks, zero-stub rejection.

### 2.3 Sandstorm JSON Contract (`.state/sandstorm_elevation_latest.json`)
```json
{
  "original_input": "<Raw>", "timestamp": "2026-09-06T21:30:00-03:00",
  "entropy_tier": "critical_sandstorm", "domain": "<Domain>", "status": "elevated",
  "pillars": [
    { "pillar": "P1: Algorithmic", "gold_standard": "Via Deserti", "directives": ["..."] },
    { "pillar": "P2: Concurrency", "gold_standard": "Deterministic State", "directives": ["..."] },
    { "pillar": "P3: Adversarial", "gold_standard": "Zero-Stub Gate", "directives": ["..."] }
  ],
  "executive_action_plan": ["Dispatch subagent", "Author schemas", "Audit premises", "Harden code"]
}
```

## 3. Greenfield Dynamic Niche Onboarding & Context Rules
Static boilerplate is banned. The AI dynamically synthesizes project constitution, methodology, and domain playbooks into `.agents/rules/*.md` tailored 100% to the specific niche.
Bootstrap: `powershell -ExecutionPolicy Bypass -File .\scripts\onboard_project.ps1 -ProjectName "<Target>"`
Active Context Rules: Materialize `.agents/rules/<index>_<niche>.md` and root `AGENTS.md` with `trigger: always_on`. Methodology and playbooks enter AI context as active rules, never inert `docs/`.
Artifacts: `.state/corporate_health.json`, `status.json`, `ledger/0000_genesis.json`.

## 4. Premise Extraction, Specialists & Handshake
Directives: `[PROVEN_FACT]` (disk verified), `[UNVERIFIED_HYPOTHESIS]` (awaiting drill), `[FATAL_FALLACY]` (triggers `[HARD HALT]`).
Specialists: `RES-SAND-01` (`skills/sandstorm_elevation/SKILL.md`), `ONBOARD-01` (`skills/greenfield_routing/SKILL.md`).
Dispatch: Read skill, run `scripts/detect_sandstorm.ps1`, infer domain, author 3 pillars, write `.state/sandstorm_elevation_latest.json`.

Layer 1 to Layer 2 Handshake Contract:
- [ ] `entropy_tier` defined; `domain` matches 8-domain taxonomy; exactly 3 pillars populated.
- [ ] Niche context rules populated in `.agents/rules/*.md` and `AGENTS.md` with `trigger: always_on`.
- [ ] `executive_action_plan` contains >= 4 directives; transaction `SANDSTORM_PROPOSAL_ELEVATED` recorded in ledger.

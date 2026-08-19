---
name: technological-prospecting
description: MANDATORY. Use when researching external APIs, libraries, framework capabilities, MCP servers, or benchmarking third-party technologies.
---

# SKILL: Technological Prospecting (Autonomous API & MCP Integration Engine)

> *"An AGI system must dynamically sense its capability limits, discover external tools or protocols, benchmark them in isolated sandboxes, and synthesize seamless runtime bindings."*

---

## 1. Scope & Autonomous Triggering

This skill governs how the system autonomously discovers, evaluates, and integrates external data APIs, remote compute endpoints, and Model Context Protocol (MCP) servers.

---

## 2. Autonomous 4-Phase Prospecting Hunt

```
┌──────────────────────────┐
│  Phase 1: Sensing        │ System identifies capability gap & resource constraints
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Phase 2: Discovery      │ Queries registries, package indexes, OpenAPI/MCP specs
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Phase 3: Sandbox Matrix │ Evaluates security, latency, rate limits & protocol safety
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Phase 4: Synthesis      │ Generates sandbox verification & dynamic config binding
└──────────────────────────┘
```

### Phase 1: Capability Gap Sensing & Constraint Formulation
Identify core requirement dimensions:
- **Target Category:** External Web API, Local Stdio MCP Server, Remote SSE/HTTP MCP Server, or Native Subprocess Tool.
- **Functional Requirements:** Data schema, streaming vs. RPC, batch processing vs. real-time sub-millisecond execution.
- **Security & System Constraints:** Auth protocol (OAuth2, mTLS, API Key), sandbox isolation level, network policy, port availability.

### Phase 2: Autonomous Multi-Source Discovery
You MUST invoke the `research` subagent (`invoke_subagent` with `TypeName: "research"`, `Role: "API & Protocol Prospector"`) or use `search_web` to formulate targeted queries across package repositories, GitHub, OpenAPI indexes, and academic literature:
```json
{
  "TypeName": "research",
  "Role": "API & Protocol Prospector",
  "Prompt": "TECH PROSPECTING: Pesquise especificações oficiais, schemas OpenAPI, repositórios GitHub e documentação técnica para [TECNOLOGIA/API]. Extraia endpoints, rate limits, autenticação e contratos."
}
```
- **For APIs:** Parse OpenAPI 3.0 / Swagger / GraphQL schemas, rate limit tiers, SLA guarantees, and authentication schemes.
- **For MCP Servers:** Extract server manifest, tool definitions, resource schemas, prompt templates, and runtime dependencies (npm/pip/docker).

### Phase 3: Zero-Trust Security & Operational Matrix
Synthesize discovery findings into an actionable comparative matrix:

| Provider / Server | Security Profile | Rate Limits / SLA | Schema Standard | Sandbox Feasibility | Limitations / Risks |
|---|---|---|---|---|---|
| Provider Alpha | OAuth2 / Isolated | 10k req/min | OpenAPI 3.1 | High (Containerized) | Proprietary rate spikes |
| MCP Server Beta | Stdio Sandbox | Unlimited (Local) | MCP v1.0 | High (No network needed) | High memory footprint |

### Phase 4: Dynamic Sandbox Verification & Automated Binding
Instead of manual copy-paste instructions:
1. **Sandbox Validation (REAL PROBE MANDATORY):** Execute a real isolated probe command against the live endpoint to verify endpoint reachability, auth handshake, and schema compliance. **STRICTLY FORBIDDEN:** Using mock schema invocations, synthetic stubs, or local simulations in place of a real network probe. If the endpoint is unreachable, log the failure explicitly — do NOT substitute a mock and claim PASSED.
2. **Environment-Agnostic Binding Generation:** Output dynamic system config updates using relative workspace configuration variables (avoiding hardcoded user paths or static local ports).
3. **Automated Tool Registration:** Emit structural tool definition allowing agents to consume the newly integrated API/MCP immediately.

---

## 3. Output Artifact Schema

Generate the report artifact at `docs/prospecting/[capability_domain]_report.md`:

```markdown
# TECHNOLOGICAL PROSPECTING REPORT: [Capability Domain]

**Target Category:** [API / MCP Server / Native Module]  
**Capability Gap Solved:** [Description]  
**Date:** [ISO 8601]

## 1. Capability Matrix
[Comparative Table]

## 2. Sandbox Verification Log
- **Probe Endpoint / Manifest:** `...`
- **Authentication Scheme:** `...`
- **Schema Validation Status:** [PASSED | FAILED]
- **Latency / Memory Benchmark:** `...`

## 3. Dynamic Integration Snippet
```json
{
  "mcpServers": {
    "[server_name]": {
      "command": "[binary_or_npx]",
      "args": ["..."],
      "env": { ... }
    }
  }
}
```

## 4. Integration Verdict & Fallback Strategy
- **Recommended Provider:** [Name]
- **Primary Justification:** [Security, performance, schema quality]
- **Autonomous Fallback Path:** [Alternative provider if primary fails or hits rate limits]
```

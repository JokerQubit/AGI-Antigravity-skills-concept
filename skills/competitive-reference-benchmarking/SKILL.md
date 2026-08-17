---
name: competitive-reference-benchmarking
description: "MANDATORY. Use before starting design/architecture of a new domain, interface, or product. Forces the agent to search the web, find the state-of-the-art reference bar, and compare before building."
---

# Competitive Reference Benchmarking Protocol ("Bater de Frente")

> **ZERO-BLIND-BUILDING MANDATE:** You are strictly prohibited from building interfaces, mechanics, or architectures from scratch without first defining a "Reference Bar" based on the current state-of-the-art in the real world.

## 1. The Core Philosophy
The objective is to "bater de frente" (compete directly) with the absolute best in the industry or academia. 
- If building a distributed stream engine, benchmark against Kafka, Redpanda, or Flink.
- If building a high-throughput matching engine, benchmark against LMAX Disruptor or Nasdaq ITCH/OUCH protocols.
- If building an ML inference engine, benchmark against vLLM, TensorRT-LLM, or FlashAttention.
- If building a payment or fintech interface, benchmark against Stripe or Wise.
- If building an analytical dashboard, benchmark against Linear, Grafana, or TradingView.
- If building a 3D simulation or rendering engine, benchmark against Unreal Engine 5 or WebGPU benchmarks.
- If building an operating system module or runtime, benchmark against Linux kernel/Tokio/eBPF.

You must not generate generic, basic, or "MVP" quality deliverables when the system requires a state-of-the-art result.

## 2. The 4-Step Benchmarking Loop

### Phase A: Market & Academic Research (MANDATORY — Browser Subagent + `search_web`)
1. **Multi-Source Sourcing:** Invoke the `browser` subagent (`invoke_subagent` with `TypeName: browser`) or `search_web` to inspect real competitor architectures, design systems, academic papers, live systems, and GitHub benchmarks.
2. Determine the target domain and identify the top 3 industry or academic leaders.
3. Extract their key differentiators (e.g., "Zero-copy ring buffer memory model", "Sub-10ms P99 latency", "High-density editorial typography with fluid micro-interactions").

### Phase B: Define the Reference Bar
Create an explicit **Reference Bar** definition:
- **Reference Standard:** (e.g., Stripe API / Linear Interface / Redis Cache Coherence / UE5 PBR)
- **Key Architectural / Functional Traits:** (e.g., Idempotency tokens, sub-millisecond serialization, responsive state machine transitions)
- **Performance / SLA Metrics:** (e.g., P99 latency < 5ms, 60 FPS under 100k entities)

### Phase C: Gap Analysis & Target Setting
Before writing code, explicitly state how your proposed implementation will match or surpass the Reference Bar on at least 3 critical metrics (Robustness, Ergonomics/DX, Performance).

### Phase D: Rigorous Enforcement
If your proposed architecture relies on naive shortcuts, un-benchmarked abstractions, or unstyled generic defaults without thought for modern ergonomics, **REJECT IT**. Refactor to match or surpass the state-of-the-art reference bar.


## 3. Tool Utilization
- **`search_web`**: Use immediately to find recent articles, design teardowns, or documentation of the reference companies.
- **`technological-prospecting`**: If the reference uses a specific library (e.g., Three.js, Framer Motion), prospect it.
- **`generate_image`**: Generate a visual mockup of what the *surpassed* reference bar looks like before coding it.

## 4. Output Mandate
When invoking this skill, output the following block:
```markdown
> 🏆 **COMPETITIVE BENCHMARKING ACTIVE**
> **Target Domain:** [Domain]
> **Reference Bar:** [Company/Product 1], [Company/Product 2]
> **Mission:** Match or exceed the visual and technical quality of the reference bar.
```

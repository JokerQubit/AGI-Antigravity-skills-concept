---
name: domain-alpha-prospecting
description: "MANDATORY. Use when entering complex, high-stakes domains (Distributed Systems, AI/ML, Scientific Computing, Quantitative Finance, Cryptography, 3D/Simulation, Embedded/Robotics). Conducts deep research into state-of-the-art algorithms, formal standards, and competitive Alpha before writing logic."
---

# Domain Alpha Prospecting Protocol

> **NO-NAIVE-IMPLEMENTATION MANDATE:** When dealing with specialized or high-stakes domains, you are strictly forbidden from guessing algorithms, hallucinating mathematical formulas, or using naive "textbook" implementations without researching the current "Alpha" (state-of-the-art industry and academic edge).

## 1. Universal Domain Activation & Scope

### A. Distributed Systems, Concurrency & Infrastructure
- **Search Target:** Consensus protocols (Raft, Paxos, Multi-Paxos), lock-free data structures, zero-copy networking, asynchronous runtimes, eBPF, distributed cache coherency, event sourcing/CQRS.
- **Goal:** Extract zero-allocation, lock-free, fault-tolerant patterns. Eliminate naive global mutex locks and blocking I/O loops.

### B. AI, Deep Learning & LLM Systems
- **Search Target:** FlashAttention, KV-caching architectures, continuous batching, quantization kernels (AWQ, GPTQ), LoRA/QLoRA mechanics, speculative decoding, vector search indexing (HNSW, IVF-PQ).
- **Goal:** Implement high-throughput, memory-efficient ML infrastructure grounded in modern research papers.

### C. Scientific Computing, Physics & Bioinformatics
- **Search Target:** ArXiv/Nature papers, optimized NumPy/CUDA/SciPy kernels, differential equation solvers (Runge-Kutta, Symplectic Integrators), molecular dynamics algorithms, IEEE standards.
- **Goal:** Ground implementations in verified mathematics and physics invariants. Never hallucinate physics laws or statistical distributions.

### D. Quantitative Finance, Trading & Low-Latency Engines
- **Search Target:** LMAX Disruptor, ring buffers, limit order book matching engines (price-time priority), FIX protocol, tick data streaming, sub-microsecond serialization.
- **Goal:** Achieve ultra-low latency, deterministic memory layout, and event-driven architecture. Eliminate `setInterval` loops and unvalidated float math.

### E. AAA Graphics, Spatial Computing & Simulation
- **Search Target:** PBR specifications, WebGPU/GLSL shader whitepapers, GDC vault presentations, signed distance fields (SDF), BVH acceleration structures, rigid-body physics integrators.
- **Goal:** Implement cinematic lighting, smooth interpolation (quaternions), particle emitters, and spatial bounding rigor.

### F. Cybersecurity, Cryptography & Zero-Trust
- **Search Target:** NIST Post-Quantum standards, zero-knowledge proofs (zk-SNARKs/STARKs), constant-time cryptographic primitives, formal verification specs (TLA+, Coq), memory safety audits.
- **Goal:** Eliminate side-channel timing attacks, unsafe pointer arithmetic, and unverified crypto primitives.

### G. Modern Reactive Interfaces & User Experience
- **Search Target:** High-density typography standards, state machines (XState patterns), WebAssembly bridges, WebRTC data channels, sub-16ms render pipelines.
- **Goal:** Deliver fluid, tactile, accessible interfaces that match international benchmark products.

---

## 2. The Prospecting Pipeline

1. **MANDATORY Multi-Source Research:** Invoke the `research` subagent (`invoke_subagent` with `TypeName: "research"`, `Role: "Domain Alpha Prospector"`) or `search_web` to inspect academic papers (ArXiv, ACM, IEEE), official technical specifications, GitHub reference architectures, and benchmark leaderboards:
   ```json
   {
     "TypeName": "research",
     "Role": "Domain Alpha Prospector",
     "Prompt": "ALPHA PROSPECTING: Prospecte os algoritmos e padrões de engenharia State-of-the-Art para [DOMÍNIO]. Identifique: 1) Invariantes formais, 2) Otimizações de baixo nível/complexidade computacional, 3) Edge-cases e armadilhas comuns. Retorne o Alpha destilado."
   }
   ```
2. **Synthesize the Alpha:** Distill findings into 3 core architectural invariants that the implementation MUST enforce.
3. **Architectural Correction:** Compare the initial plan or user prompt with the discovered Alpha, upgrading any naive approach to the state-of-the-art standard.

---

## 3. Output Mandate
When invoking this skill, output the following block:
```markdown
> 🔬 **DOMAIN ALPHA PROSPECTING ACTIVE**
> **Domain Sector:** [Distributed Systems / AI / Science / Finance / Graphics / Security / UI]
> **Key Alpha Discovered:** [Summarize the cutting-edge technique/algorithm found]
> **Architectural Shift:** [How this elevates the system beyond naive implementations]
```


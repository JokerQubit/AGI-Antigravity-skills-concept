# Reference Guide: Polyglot Tech Stack & Free Global API Selection (`TECH-SELECT-01`)

## 1. Programming Language Selection Matrix

Never default to a single language out of habit. Match runtime characteristics to the technical domain:

| Domain / Workload | Optimal Language | Rationale & Architectural Fit |
| :--- | :--- | :--- |
| **High Concurrency & Systems Engine** | **Rust** | Zero-cost abstractions, memory safety without garbage collection, thread-safety invariants, SIMD vectorization. |
| **Distributed Microservices & Cloud Networking** | **Go (Golang)** | Lightweight goroutines, high-throughput network I/O, minimal binary footprint, simple maintainability. |
| **Interactive Modern UI & Web Frontends** | **TypeScript (React / Svelte / Next.js)** | Strict typing, massive ecosystem, rich component primitives, reactive DOM hydration. |
| **Machine Learning, Scientific & AGI Pipelines** | **Python 3.12+ (PyTorch, Polars, JAX)** | Unrivaled tensor processing ecosystem, rapid mathematical synthesis, GPU acceleration. |
| **Local Platform Automation & IDE Tooling** | **PowerShell 7+ / Bash** | Native OS pipeline integration, structured JSON object streams, robust error trapping. |

---

## 2. High-Assurance Free Global APIs Catalog

Actively evaluate and integrate these authoritative, high-uptime free global APIs:

1. **Environmental & Meteorological**:
   - *Open-Meteo API*: Free, open-source weather and climate API with zero API key requirement, hourly forecasts, and historical datasets.
2. **Code & Version Control Intelligence**:
   - *GitHub REST & GraphQL API*: Free rate-limited access for repository metrics, issue automation, and workflow dispatch.
3. **Machine Learning & Inference**:
   - *Hugging Face Inference API*: Free tier access to open-source transformer models, embeddings, and NLP pipelines.
4. **Geospatial & Planetary Data**:
   - *OpenStreetMap / Nominatim*: Free geographic coordinate lookups and reverse geocoding.
5. **Public Economic & Financial Data**:
   - *World Bank & US Federal Reserve (FRED) APIs*: Authoritative macroeconomic datasets and financial statistics.

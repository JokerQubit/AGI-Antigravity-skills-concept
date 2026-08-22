# Google Antigravity SDK Architecture

The Google Antigravity SDK architecture is designed around three foundational abstractions: `Agent`, `Conversation`, and `Connection`.

## Core Abstractions

### 1. Agent (`google.antigravity.Agent`)
The `Agent` is the primary high-level orchestrator. It manages the agent's lifecycle, loads configurations (`LocalAgentConfig`), initializes tools, attaches lifecycle hooks, and establishes connections to model backends.

An `Agent` is instantiated as an asynchronous context manager:
```python
from google.antigravity import Agent, LocalAgentConfig

config = LocalAgentConfig(
    system_instructions="You are an autonomous systems engineer."
)

async with Agent(config) as agent:
    response = await agent.chat("Analyze repository status.")
    async for chunk in response:
        print(chunk, end="", flush=True)
```

### 2. Conversation (`google.antigravity.Conversation`)
The `Conversation` maintains the stateful dialogue history, token budgets, scratchpad artifacts, and context window compaction. Each turn consists of user inputs, model reasoning ("thoughts"), structured tool calls, tool results, and final text output chunks.

### 3. Connection (`google.antigravity.Connection`)
The `Connection` layer abstracts communication with the underlying model provider:
- **Cloud Endpoints**: Gemini Developer API (`GeminiAPIEndpoint`) or Gemini Enterprise / Vertex AI (`VertexEndpoint`).
- **On-Device Runtimes**: LiteRT-LM (`LiteRTAgentConfig`) for hardware-accelerated local execution.
- **Local Server Adapters**: OpenAI-compatible loopback servers (`LocalOpenAIAgentConfig`) for Ollama or LM Studio.

## Execution Flow

```
[User Prompt]
      │
      ▼
[Pre-Turn Hooks & Policies]
      │
      ▼
[Model Inference / Thought Generation]
      │
      ├─► Tool Call Request ──► [Pre-Tool Hooks / Policy Check] ──► [Tool Execution] ──► [Post-Tool Hooks]
      │                                                                                         │
      │◄────────────────────────────────────────────────────────────────────────────────────────┘
      │
      ▼
[Streamed Chunks / Final Response]
      │
      ▼
[Post-Turn Hooks & Metrics Logging]
```

## Concurrency & Cancellation
- The SDK manages turns asynchronously with native Python `asyncio`.
- Active generation can be cleanly cancelled at any point via `await response.cancel()`, which raises `AntigravityCancelledError` and terminates active tool executions while keeping conversation history intact.

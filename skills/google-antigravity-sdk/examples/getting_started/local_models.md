# Local Model Execution (LiteRT & Ollama)

This example demonstrates running offline models locally using LiteRT-LM (Gemma) or an OpenAI-compatible local server.

## 1. LiteRT-LM Local Agent

```python
import asyncio
from google.antigravity import Agent, LiteRTAgentConfig

async def run_litert():
    config = LiteRTAgentConfig(
        model_path="d:/models/gemma-2b-it-gpu.litertlm",
        backend="gpu",
        max_context_tokens=4096,
    )

    async with Agent(config) as agent:
        response = await agent.chat("Explain the difference between process and thread.")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(run_litert())
```

## 2. Local OpenAI-Compatible Server (Ollama / LM Studio)

```python
import asyncio
from google.antigravity import Agent, LocalOpenAIAgentConfig

async def run_ollama():
    config = LocalOpenAIAgentConfig(
        base_url="http://127.0.0.1:11434/v1",
        model="llama3.2:latest",
        api_key="ollama",
    )

    async with Agent(config) as agent:
        response = await agent.chat("What are the key benefits of immutable data structures?")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()
```

# Hello World & Thought Streaming

This example demonstrates how to create a basic Google Antigravity agent and stream both reasoning thoughts and response chunks.

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig

async def main():
    config = LocalAgentConfig(
        system_instructions="You are a clear and concise programming assistant.",
    )

    async with Agent(config) as agent:
        response = await agent.chat("Explain why asynchronous I/O is beneficial for network bound services.")

        print("--- Response Stream ---")
        async for chunk in response:
            # Check for thinking/reasoning blocks
            if hasattr(chunk, "thought") and chunk.thought:
                print(f"[Thinking] {chunk.thought}", flush=True)
            else:
                print(chunk, end="", flush=True)
        print("\n-----------------------")

if __name__ == "__main__":
    asyncio.run(main())
```

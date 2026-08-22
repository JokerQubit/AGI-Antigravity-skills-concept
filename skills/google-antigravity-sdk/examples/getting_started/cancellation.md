# Programmatic Turn Cancellation

This example demonstrates how to cleanly abort an in-progress generation stream while preserving prior conversation history.

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig
from google.antigravity.errors import AntigravityCancelledError

async def main():
    config = LocalAgentConfig(
        system_instructions="You are an autonomous computational researcher.",
    )

    async with Agent(config) as agent:
        response = await agent.chat("Compute detailed simulation traces for 100 iterations.")

        async def cancel_after_delay():
            await asyncio.sleep(1.5)
            print("\n[Timer] Cancelling generation stream...")
            await response.cancel()

        cancel_task = asyncio.create_task(cancel_after_delay())

        try:
            async for chunk in response:
                print(chunk, end="", flush=True)
        except AntigravityCancelledError:
            print("\n[Notice] Stream successfully aborted by cancellation request.")
        finally:
            await cancel_task

        # Conversation history remains intact; follow-up turns work immediately
        followup = await agent.chat("Please summarize what was calculated so far.")
        async for chunk in followup:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```

# Session Persistence & History Restore

This example demonstrates saving conversation state and reloading it in subsequent sessions.

```python
import asyncio
from pathlib import Path
from google.antigravity import Agent, LocalAgentConfig

save_file = Path("d:/sessions/project_session.json")

async def run_session_turn(prompt: str):
    config = LocalAgentConfig(
        system_instructions="You are a stateful assistant remembering past sessions.",
    )

    async with Agent(config) as agent:
        # Restore prior conversation if saved
        if save_file.exists():
            await agent.load_session(str(save_file))
            print(f"[Storage] Loaded session state from {save_file}")

        response = await agent.chat(prompt)
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

        # Save updated conversation state
        save_file.parent.mkdir(parents=True, exist_ok=True)
        await agent.save_session(str(save_file))
        print(f"[Storage] Saved updated session to {save_file}")

async def main():
    await run_session_turn("Set project milestone goal to 'Production Launch by Q4'.")
    await run_session_turn("What was the milestone goal we agreed on?")

if __name__ == "__main__":
    asyncio.run(main())
```

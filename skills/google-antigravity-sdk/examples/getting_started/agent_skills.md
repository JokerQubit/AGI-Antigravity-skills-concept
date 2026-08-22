# Agent Skills Dynamic Discovery

This example demonstrates discovering and loading filesystem skills containing `SKILL.md` into the Antigravity Python SDK.

```python
import asyncio
from pathlib import Path
from google.antigravity import Agent, LocalAgentConfig

async def main():
    # Provide directories containing skill packages
    skills_directory = Path("d:/agi/agi-antigravity-core/skills").resolve()

    config = LocalAgentConfig(
        skills_paths=[str(skills_directory)],
        system_instructions="You are an autonomous engineer equipped with specialized skills.",
    )

    async with Agent(config) as agent:
        # Inspect registered skills
        print("Registered Skills:")
        for skill_name in agent.list_skills():
            print(f" - {skill_name}")

        response = await agent.chat("Run a test-driven development workflow to implement a token bucket rate limiter.")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```

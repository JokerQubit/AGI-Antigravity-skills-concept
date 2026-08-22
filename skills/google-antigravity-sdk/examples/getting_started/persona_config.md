# Persona Shaping & Dynamic System Instructions

This example demonstrates crafting focused domain personas and dynamically adjusting system instructions based on runtime requirements.

```python
import asyncio
from google.antigravity import Agent, LocalAgentConfig

def build_compiler_engineer_instructions() -> str:
    return (
        "You are a Principal Compiler Engineer specialized in LLVM intermediate representation, "
        "dead-code elimination, and register allocation. Respond with exact technical proofs, "
        "concrete benchmark comparisons, and zero superficial generalities."
    )

async def main():
    config = LocalAgentConfig(
        system_instructions=build_compiler_engineer_instructions(),
        model="gemini-3.7-flash",
    )

    async with Agent(config) as agent:
        response = await agent.chat("Explain the SSA phi-node elimination phase during register allocation.")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```

# Multimodal Inputs & Media Generation

This example demonstrates passing images, documents, and media prompts to the Google Antigravity SDK.

```python
import asyncio
from pathlib import Path
from google.antigravity import Agent, LocalAgentConfig, types

async def main():
    config = LocalAgentConfig(
        system_instructions="You are a multimodal technical documentation assistant.",
    )

    image_path = Path("d:/assets/architecture_diagram.png")

    async with Agent(config) as agent:
        # Pass image file alongside user prompt
        message = types.UserContent(
            parts=[
                types.TextPart("Explain the topology depicted in this system diagram:"),
                types.FilePart.from_uri(str(image_path), mime_type="image/png"),
            ]
        )

        response = await agent.chat(message)
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
```

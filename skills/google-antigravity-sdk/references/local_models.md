# Local Models & On-Device Inference

The Google Antigravity SDK supports 100% offline, on-device agent execution using LiteRT-LM or OpenAI-compatible local servers without API keys.

## 1. LiteRT-LM (`LiteRTAgentConfig`)

Runs quantized Gemma models (`.litertlm`) on local hardware (CPU, GPU, NPU):

```python
from google.antigravity import Agent, LiteRTAgentConfig

config = LiteRTAgentConfig(
    model_path="d:/models/gemma-2b-it-gpu.litertlm",
    backend="gpu",  # "gpu", "cpu", or "npu"
    max_context_tokens=8192,
    enable_speculative_decoding=True,
)

async with Agent(config) as agent:
    response = await agent.chat("Summarize local directory structure.")
    async for chunk in response:
        print(chunk, end="", flush=True)
```

### Requirements & Hardware Acceleration
- Python package: `litert-lm>=0.15.0`
- Windows GPU: Requires DirectX 12 / Dawn shader compiler.
- Linux GPU: Requires Vulkan or OpenCL drivers.
- macOS: Metal backend enabled automatically.
- Model paths must be absolute paths without unexpanded tildes (`~`).

## 2. OpenAI-Compatible Server (`LocalOpenAIAgentConfig`)

Connects to local inference servers such as Ollama, LM Studio, or vLLM:

```python
from google.antigravity import Agent, LocalOpenAIAgentConfig

config = LocalOpenAIAgentConfig(
    base_url="http://127.0.0.1:11434/v1",
    model="llama3.2:latest",
    api_key="ollama",  # Placeholder key for local endpoint
)

async with Agent(config) as agent:
    response = await agent.chat("Run local static analysis.")
    async for chunk in response:
        print(chunk, end="", flush=True)
```

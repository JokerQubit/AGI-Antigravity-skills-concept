# Error Handling & Lifecycle Recovery

The Google Antigravity SDK provides structured exception hierarchies and lifecycle hooks for error diagnosis and automated recovery.

## Exception Hierarchy

```
BaseException
 └── asyncio.CancelledError
      └── AntigravityCancelledError  # Raised when response.cancel() aborts generation
Exception
 └── AntigravityError
      ├── AntigravityValidationError  # Malformed config, relative paths in app_data_dir
      ├── AntigravityConnectionError  # Network drops or unreachable endpoint
      ├── AntigravityBudgetExceededError # Token or call budget limits breached
      └── AntigravityToolError       # Unhandled tool runtime exception
```

> **Cancellation Note**: `AntigravityCancelledError` inherits directly from `asyncio.CancelledError` (`BaseException`), preventing accidental suppression by generic `except Exception:` blocks.

## Automated Error Recovery with Hooks

You can intercept tool errors and provide structured guidance or synthetic fallback data back into the agent conversation loop using `@hooks.on_tool_error`:

```python
from google.antigravity import Agent, LocalAgentConfig, Hooks, HookResult

hooks = Hooks()

@hooks.on_tool_error
async def handle_tool_error(tool_name: str, args: dict, error: Exception) -> str | None:
    """Intercept tool failures to guide agent self-correction."""
    if tool_name == "view_file" and isinstance(error, FileNotFoundError):
        return f"File '{args.get('AbsolutePath')}' not found. Try find_by_name to locate the correct path."
    # Return None to propagate the error normally
    return None

config = LocalAgentConfig(
    hooks=hooks,
)
```

# Built-in Tools Reference

In `LocalAgentConfig`, all standard Cortex tools are registered and available. The `run_command` tool is governed by safety policies (`confirm_run_command()`), while read-only filesystem tools are allowed by default.

## Approved Tool Registry

| Tool Name | Purpose | Default Policy |
| :--- | :--- | :--- |
| `list_dir` | Lists directory contents and file metadata | Allowed |
| `grep_search` | Searches file contents using regex pattern matching | Allowed |
| `find_by_name` | Locates files matching glob patterns | Allowed |
| `view_file` | Reads contents of text and binary files | Allowed |
| `write_to_file` | Creates or overwrites files on disk | Allowed |
| `replace_file_content` | Performs contiguous surgical edits on existing files | Allowed |
| `run_command` | Executes shell commands in the local environment | Ask User / Confirmation |
| `finish` | Concludes task execution and returns summary | Allowed |
| `schedule` | Schedules one-shot timers or cron jobs | Allowed |
| `manage_task` | Inspects, sends input to, or cancels background tasks | Allowed |
| `send_message` | Sends messages to subagents or peer agents | Allowed |
| `generate_image` | Generates or edits visual media assets | Allowed |
| `read_url_content` | Fetches web page content converted to markdown | Allowed |
| `search_web` | Queries web search engine for current information | Allowed |
| `ask_question` | Prompts user for interactive input or clarification | Allowed in INTERACTIVE mode |

## Overriding Built-in Tools

Any built-in tool can be overridden by supplying a custom Python callable with the exact matching name to `LocalAgentConfig(tools=[...])`.

```python
from google.antigravity import Agent, LocalAgentConfig

def view_file(AbsolutePath: str) -> str:
    """Custom view_file implementation with audit logging."""
    print(f"[AUDIT] Reading file: {AbsolutePath}")
    with open(AbsolutePath, "r", encoding="utf-8") as f:
        return f.read()

config = LocalAgentConfig(
    tools=[view_file],
)
```

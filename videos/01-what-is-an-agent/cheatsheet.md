# Video 01 - Cheatsheet

## The one idea
**LLM = function: text in, text out.** A chatbot talks. An agent talks **and acts**, in a loop, until the goal is reached.

## Connect (once per notebook)
```python
from databricks.sdk import WorkspaceClient

client = WorkspaceClient().serving_endpoints.get_open_ai_client()
MODEL = "databricks-meta-llama-3-3-70b-instruct"
```

## Ask a question
```python
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Your question here"}],
)
print(response.choices[0].message.content)   # <- the reply text lives here
```

## Useful one-liners

| I want to... | Do this |
| --- | --- |
| Use another model | Change `MODEL`, e.g. `"databricks-claude-haiku-4-5"` |
| See which models I have | Left sidebar, **Serving** |
| Check where requests go | `print(client.base_url)` - your workspace, not OpenAI |
| See tokens used | `print(response.usage)` |

## Agent anatomy (the picture for the whole series)

| Part | Metaphor | Video |
| --- | --- | --- |
| LLM | Brain | 01-03 |
| Memory | Notebook | 04 |
| Tools | Hands | 06-07 |
| Loop | Persistence | 08 |
| Guardrails | Seatbelt | 09 |

## Remember
* An LLM can be **confidently wrong** (hallucination). Tools fix that.
* "OpenAI-compatible" is a **format**, not a company.
* You pay per **token** (about 3/4 of a word). A Hello World call costs a tiny fraction of a cent.

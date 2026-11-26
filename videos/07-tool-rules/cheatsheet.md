# Video 07 - Cheatsheet

## The one idea
Tool messages have strict rules. Some models enforce them, some don't - **write to the strictest**. And design tools that return small, exact results.

## The four golden rules

| # | Rule | In code |
| --- | --- | --- |
| 1 | Request before result | `messages.append(msg.model_dump(exclude_none=True))` first |
| 2 | Match the id | `"tool_call_id": call.id` |
| 3 | Results are strings | `"content": json.dumps(result)` (if not already a str) |
| 4 | Answer every call | `for call in msg.tool_calls:` - one `tool` message each |

## One helper that follows all four
```python
def add_tool_results(messages, msg, functions):
    messages.append(msg.model_dump(exclude_none=True))                  # rule 1
    for call in msg.tool_calls:                                          # rule 4
        args = json.loads(call.function.arguments or "{}")
        result = functions[call.function.name](**args)
        content = result if isinstance(result, str) else json.dumps(result)   # rule 3
        messages.append({"role": "tool", "tool_call_id": call.id, "content": content})  # rule 2
```

## Strict vs lenient (our tests)

| Broken rule | Llama 3.3 | Claude Haiku |
| --- | --- | --- |
| 1 - no request | accepted silently | ERROR |
| 2 - wrong id | accepted silently | ERROR |
| 3 - dict content | ERROR | ERROR |
| 4 - unanswered call | can't happen (one call per reply) | ERROR |

## Context engineering
The **context window** holds everything the model sees: system prompt + tool menu + history + tool results.
* Do filtering, joining and maths **in code**; return the answer, not the raw data.
* Return only the fields the model needs.
* Big tool results cost tokens on every later call - and can make answers *worse*.

## Remember
* "It works on my model" is not proof your code is right.
* The Databricks Llama endpoint returns one tool call per reply; Claude can return several.

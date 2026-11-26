# Video 08 - Cheatsheet

## The one idea
**An agent = LLM + tools + loop + memory.** Keep going until the model returns no tool calls.

## The loop (~40 lines)
```python
def run_agent(question, max_steps=5, verbose=True):
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use tools when you need facts or maths."},
        {"role": "user", "content": question},
    ]
    for step in range(1, max_steps + 1):
        response = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOL_SPECS)
        msg = response.choices[0].message

        if not msg.tool_calls:                         # done
            return msg.content

        add_tool_results(messages, msg, TOOLS)         # Video 07 helper: all 4 rules
        # (or inline: append request, run each call, append tool results)

    return "Stopped: reached max_steps without a final answer."
```

## Multi-tool routing
```python
TOOLS = {
    "get_order_total": get_order_total,
    "calculator": calculator,
    "get_today": get_today,
}
# inside the loop:
func = TOOLS.get(call.function.name)
result = func(**args) if func else f"error: unknown tool {call.function.name}"
```

## Design choices

| Prefer | Over | Why |
| --- | --- | --- |
| `for step in range(max_steps)` | `while True:` | Step limit = first guardrail |
| `if not msg.tool_calls` | `finish_reason == "tool_calls"` | Checks what was returned |
| `TOOLS[name](**args)` | Hard-coding one tool | Model can pick any tool |

## Remember
* One round is not enough - Llama may ask for one tool at a time.
* Each loop iteration = **one model call** (agents multiply cost by chain length).
* Reuse Video 07's golden rules inside the loop (`add_tool_results`).
* `max_steps` stops runaway loops; Video 09 adds more guardrails.

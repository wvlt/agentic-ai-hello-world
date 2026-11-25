# Video 06 - Cheatsheet

## The one idea
**The model never runs your code.** It returns a `tool_call` (structured output: function + arguments). You run it and send the result back.

## 1. A normal function
```python
def multiply(a: float, b: float) -> float:
    return a * b
```

## 2. Describe it (the menu)
```python
MULTIPLY_TOOL = {
    "type": "function",
    "function": {
        "name": "multiply",
        "description": "Multiply two numbers exactly. Use this for any multiplication.",
        "parameters": {
            "type": "object",
            "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            "required": ["a", "b"],
        },
    },
}
```

## 3-5. One full round
```python
messages = [{"role": "user", "content": "What is 48729 * 3817?"}]

# 3. the model asks
msg = client.chat.completions.create(model=MODEL, messages=messages, tools=[MULTIPLY_TOOL]).choices[0].message
call = msg.tool_calls[0]                       # finish_reason == "tool_calls", content is None

# 4. you run it
args = json.loads(call.function.arguments)     # arguments arrive as a JSON STRING
result = multiply(**args)

# 5. send the result back, then ask again
messages.append(msg.model_dump(exclude_none=True))                                   # the model's request
messages.append({"role": "tool", "tool_call_id": call.id, "content": str(result)})   # your result
final = client.chat.completions.create(model=MODEL, messages=messages, tools=[MULTIPLY_TOOL])
print(final.choices[0].message.content)
```

## Who writes what

| # | Role | Written by |
| --- | --- | --- |
| 1 | `user` | The user |
| 2 | `assistant` + `tool_calls` | The model |
| 3 | `tool` + `tool_call_id` | **Your code** |
| 4 | `assistant` | The model |

## Remember
* The model decides **whether** to use a tool - tools are options, not orders.
* The **name and description** are the model's only clue. Vague descriptions = wrong tool.
* Tool descriptions are sent with **every** call (they cost tokens), and one round = **two** model calls.
* The model trusts your tool's result completely - a buggy tool means a confidently wrong answer.
* Message order and `tool_call_id` rules: Video 07.

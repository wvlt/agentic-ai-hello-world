# Video 03 - Cheatsheet

## The one idea
The reply is more than text. **`finish_reason` tells you whether to trust it**; `usage` tells you what it cost.

## Where everything lives

| I want... | Read this |
| --- | --- |
| The reply text | `response.choices[0].message.content` |
| Why it stopped | `response.choices[0].finish_reason` |
| Tools it wants (Video 06) | `response.choices[0].message.tool_calls` |
| Tokens I sent | `response.usage.prompt_tokens` |
| Tokens it wrote | `response.usage.completion_tokens` |
| The whole thing | `print(response.model_dump_json(indent=2))` |

## finish_reason

| Value | Meaning | Your code should |
| --- | --- | --- |
| `stop` | Finished naturally | Use the answer |
| `length` | Hit `max_tokens` - cut off | Warn, raise `max_tokens`, or ask for shorter |
| `tool_calls` | Wants a tool run | Run it, send the result back (Video 06) |

## Useful parameters
```python
response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    max_tokens=200,    # cap on OUTPUT tokens: limits length AND cost
    temperature=0,     # 0 = predictable, ~1 = balanced, 1.5 = creative
    n=1,               # number of answers (n > 1 not supported by every model)
)
```

## A safe way to read replies
```python
def get_reply(response):
    choice = response.choices[0]
    if choice.finish_reason == "length":
        print("WARNING: answer was cut off by max_tokens")
    return choice.message.content
```

## Rules of thumb
* 1 token is roughly 3/4 of a word (100 words is about 130 tokens).
* Output tokens usually cost more than input tokens.
* Temperature 0 is **mostly** repeatable - never assume an LLM is deterministic.
* Low temperature for facts, extraction and agents; high for brainstorming.

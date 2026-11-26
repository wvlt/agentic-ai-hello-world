# Video 09 - Cheatsheet

## The one idea
**A working loop still needs seatbelts.** Caps, errors-as-results, truncation checks, allow-lists, repeat detection, read vs write.

## Errors as results
```python
try:
    result = func(**args)
except Exception as e:
    result = f"error: {e}"
content = result if isinstance(result, str) else json.dumps(result)
```

## Truncation
```python
if response.choices[0].finish_reason == "length":
    return "Stopped: reply was truncated (finish_reason=length)."
```

## Repeat detector
```python
seen = {}
fp = f"{name}:{arguments}"
seen[fp] = seen.get(fp, 0) + 1
if seen[fp] > 2:
    return "Stopped: repeated the same tool call."
```

## Allow-list + write gate
```python
if name not in TOOLS:
    result = f"error: unknown tool {name}"
elif name in WRITE_TOOLS and not allow_writes:
    result = "error: write requires approval"
else:
    result = TOOLS[name](**args)
```

## Budgets
```python
for step in range(1, max_steps + 1):
    response = client.chat.completions.create(...)
    tokens_used += response.usage.total_tokens
    if tokens_used > max_tokens_total:
        return "Stopped: token budget exceeded."
```

## Seatbelt checklist

| Guardrail | Stops |
| --- | --- |
| `max_steps` | Infinite tool loops |
| `max_tokens_total` / time | Runaway cost |
| `finish_reason == "length"` | Half-answers treated as done |
| try/except on tools | Notebook crashes |
| Allow-list | Unknown / invented tools |
| Repeat fingerprint | Sticky same call |
| Write approval | Accidental side effects |

## Remember
* Prompting helps; **code** guardrails are what you trust.
* Retry 429s a few times - never forever.
* Video 10: tracing so you can *see* which seatbelt fired.

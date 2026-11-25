# Video 05 - Cheatsheet

## The one idea
People read text. **Code reads JSON.** Use a JSON schema so the model must match your shape - then check the values in code.

## JSON text to Python dict
```python
import json
data = json.loads('{"sentiment": "negative", "confidence": 0.9}')
data["sentiment"]   # 'negative'
```

## Clean up code fences (Way 2)
```python
def parse_json(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`").removeprefix("json").strip()
    return json.loads(text)
```

## JSON schema (Way 3 - recommended)
```python
sentiment_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "sentiment",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "sentiment": {"type": "string", "enum": ["positive", "negative", "neutral"]},
                "confidence": {"type": "number"},
            },
            "required": ["sentiment", "confidence"],
            "additionalProperties": False,
        },
    },
}
response = client.chat.completions.create(model=MODEL, messages=messages, response_format=sentiment_format)
data = json.loads(response.choices[0].message.content)
```

## Schema building blocks

| I want... | Schema |
| --- | --- |
| Text | `{"type": "string"}` |
| A whole number | `{"type": "integer"}` |
| A decimal | `{"type": "number"}` |
| One of a fixed list | `{"type": "string", "enum": ["a", "b"]}` |
| Allowed to be missing | `{"type": ["string", "null"]}` |

## Always check the values
```python
PLACEHOLDERS = {"", "null", "none", "<unknown>", "unknown", "n/a"}

def clean(d):
    return {k: None if isinstance(v, str) and v.strip().lower() in PLACEHOLDERS else v for k, v in d.items()}
```

## Remember
* Asking nicely for JSON is a **request**, not a guarantee (code fences, extra words).
* A schema guarantees the **shape**, not that the **values** are true.
* JSON answers are short - usually far fewer output tokens than prose.
* Tool calling (Video 06) is structured output where the structure is "function + arguments".

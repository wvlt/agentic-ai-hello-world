# Video 02 - Cheatsheet

## The one idea
Every message has a **role** (who is speaking) and **content** (what they said). A conversation is a **list** of messages. You steer the model by choosing what goes in each role.

## The roles

| Role | Written by | Use it for |
| --- | --- | --- |
| `system` (or `developer`) | You, the developer | Rules, personality, goals |
| `user` | The app's user | Questions, instructions |
| `assistant` | The model - or you, for examples | Replies, few-shot examples |
| `tool` | Your code | Coming in Video 06 |

## A system prompt
```python
messages = [
    {"role": "system", "content": "You are a patient Python tutor. Answer in 2 sentences."},
    {"role": "user", "content": "What is a Python list?"},
]
response = client.chat.completions.create(model=MODEL, messages=messages)
print(response.choices[0].message.content)
```

## The ask() helper
```python
def ask(question, system="You are a helpful assistant."):
    messages = [{"role": "system", "content": system}, {"role": "user", "content": question}]
    return client.chat.completions.create(model=MODEL, messages=messages).choices[0].message.content
```

## Few-shot: show, don't tell
```python
messages = [
    {"role": "system", "content": "Turn feedback into a one-line ticket."},
    {"role": "user", "content": "the login page takes forever"},              # example input
    {"role": "assistant", "content": "[PERF] Login page slow | priority: medium"},  # example answer YOU wrote
    {"role": "user", "content": "export button broken on mobile"},          # the real request
]
```

## Remember
* The system prompt is sent with **every** call - keep it short (you pay for it each time).
* A system prompt is a **suggestion, not a lock**. Users can try "ignore all previous instructions" (prompt injection). Enforce important rules in code (Video 09).
* Order matters: the list is read top to bottom, newest last.

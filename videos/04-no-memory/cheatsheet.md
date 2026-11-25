# Video 04 - Cheatsheet

## The one idea
The model is **stateless**. **Memory is the list you send.** What's in the list can be remembered; what you leave out is gone.

## A chat that remembers
```python
class Chat:
    def __init__(self, system="You are a friendly, concise assistant.", max_history=None):
        self.system = {"role": "system", "content": system}
        self.history = []              # <- this list IS the memory
        self.max_history = max_history  # None = keep everything

    def send(self, text):
        self.history.append({"role": "user", "content": text})                 # 1. remember the user
        recent = self.history if self.max_history is None else self.history[-self.max_history:]
        response = client.chat.completions.create(model=MODEL, messages=[self.system] + recent)
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})          # 2. remember the reply
        return reply
```

## Memory strategies

| Strategy | How | Good | Watch out |
| --- | --- | --- | --- |
| Full history | Send everything | Remembers all | Grows forever; cost and context-window limits |
| Trim | Send last N messages | Cheap, simple | Silently forgets old facts |
| Pin | Key facts in the system prompt | Cheap and keeps what matters | You decide what's important |
| Summarise | LLM condenses old messages | Keeps the gist | Summaries can lose details |

## Remember
* You pay for the history on **every** call - long chats get expensive fast.
* The **context window** is the model's maximum input; exceed it and the call fails.
* The history is just data: you can print it, save it (`json.dump`), load it, even edit it.
* For agents, choosing what goes in the list is called **context engineering** (Video 07).

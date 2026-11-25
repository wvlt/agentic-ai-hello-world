# Video 05 - Quiz

Five questions. Answer first, then click to reveal.

---

**1. Why do agents need JSON answers instead of free text?**

<details><summary>Answer</summary>

Agents are **code**: they make decisions with `if` statements and function calls. Free text is hard to parse reliably; JSON turns into a Python `dict` with one line (`json.loads`), so code can act on it.
</details>

---

**2. You asked "Reply ONLY with JSON" and `json.loads` fails on a reply that starts with ```` ```json ````. What happened?**

<details><summary>Answer</summary>

The model wrapped its JSON in a markdown **code fence**. Asking nicely is a request, not a guarantee (in our test Claude Haiku did this 3 times out of 3). Strip the fences, or better, use a JSON schema.
</details>

---

**3. What does `response_format` with a JSON schema do?**

<details><summary>Answer</summary>

It **constrains** the model to return JSON with exactly the fields and types you define (e.g. `sentiment` must be one of three words, `confidence` must be a number). It's the most reliable way to get structured output.
</details>

---

**4. The model returns `{"time": "null"}`. Why is that dangerous?**

<details><summary>Answer</summary>

`"null"` is a **non-empty string**, not Python's `None`. `if booking["time"]:` is `True`, so your code thinks it has a time. Valid JSON is not the same as correct values - check values in code (e.g. a `clean()` function).
</details>

---

**5. How is structured output related to tool calling?**

<details><summary>Answer</summary>

Tool calling **is** structured output: the model returns JSON that names a function and its arguments, and your code runs it. You'll see this in Video 06.
</details>

---

**Score 4-5:** ready for Video 06. **Score 0-3:** rewatch 1:45-6:30 (the three ways to get JSON).

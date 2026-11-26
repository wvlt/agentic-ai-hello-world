# Video 07 - Quiz

Five questions. Answer first, then click to reveal.

---

**1. Name the four golden rules of tool messages.**

<details><summary>Answer</summary>

1. Request before result (assistant `tool_calls` message first).
2. Match the `tool_call_id`.
3. Results are strings (`json.dumps` dicts and lists).
4. Answer every call (one `tool` message per call).
</details>

---

**2. Your code sends a tool result with the wrong `tool_call_id`. On Llama it works. Is your code fine?**

<details><summary>Answer</summary>

**No.** Llama 3.3 quietly accepted it in our tests, but Claude Haiku returned a 400 error. Lenient models hide bugs - write to the strictest rules so your code works on every model.
</details>

---

**3. Your tool returns `{"sky": "rainy", "temp": 12}`. What must you do before sending it back?**

<details><summary>Answer</summary>

Turn it into a string: `json.dumps(result)`. In our tests both Llama and Claude rejected a dict as `content`.
</details>

---

**4. What is "context engineering"?**

<details><summary>Answer</summary>

Deciding what goes into the model's **context window** - system prompt, tool menu, history and tool results - so it has exactly what it needs, and nothing that wastes tokens or confuses it.
</details>

---

**5. `get_all_orders()` vs `get_order_total(customer, month)`: which is better, and why?**

<details><summary>Answer</summary>

**`get_order_total`.** It does the filtering and adding in Python and returns one small result. In our tests it used ~824 input tokens vs ~31,000, and was correct on both models every time - while the big dump gave wrong totals on Llama every time and on Claude one time in two. Do the work in code; give the model only what it needs.
</details>

---

**Score 4-5:** ready for Video 08. **Score 0-3:** rewatch 0:45-6:15 (the rules).

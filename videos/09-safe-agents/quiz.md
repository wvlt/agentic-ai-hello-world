# Video 09 - Quiz

Five questions. Answer first, then click to reveal.

---

**1. What is a guardrail, in one sentence?**

<details><summary>Answer</summary>

A **limit or check** that keeps the agent safe - e.g. step caps, token budgets, allow-lists, treating truncated replies as incomplete, or requiring approval for writes.
</details>

---

**2. A tool raises `ValueError`. What should the loop do?**

<details><summary>Answer</summary>

**Catch it** and send the error back as the tool message content (e.g. `"error: unknown customer"`). Do not let the exception kill the notebook. The model can then answer from the error.
</details>

---

**3. Why is `finish_reason == "length"` dangerous if you only check `if not msg.tool_calls`?**

<details><summary>Answer</summary>

A truncated reply has no tool calls, so your loop thinks it's **done** and returns a cut-off sentence. Treat `length` as incomplete - stop with a warning or retry with a higher `max_tokens`.
</details>

---

**4. Name three stop conditions beyond "no more tool calls".**

<details><summary>Answer</summary>

Any three of: **max_steps**, **max_tokens_total** (budget), **repeated identical tool calls**, **truncated reply**, **time limit**, **disallowed / unknown tool** (after telling the model).
</details>

---

**5. Why separate read tools from write tools?**

<details><summary>Answer</summary>

Reads (lookup, calculate) are usually safe to auto-run. Writes (cancel, update, send) can change the world - so require **human approval** (or an explicit `allow_writes` flag) before running them.
</details>

---

**Score 4-5:** ready for Video 10. **Score 0-3:** rewatch 2:30-8:30 (errors, truncation, caps).

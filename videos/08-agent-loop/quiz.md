# Video 08 - Quiz

Five questions. Answer first, then click to reveal.

---

**1. In one sentence: what is an AI agent?**

<details><summary>Answer</summary>

An **LLM + tools + a loop + memory**: keep asking the model, running any tools it requests, and feeding results back until it returns a final answer.
</details>

---

**2. Why is one hand-written tool round not enough?**

<details><summary>Answer</summary>

The model may need **several** tool rounds for one question (e.g. Llama asking for Perth, then Tokyo). After one round you can still get another `tool_call` instead of a final answer. A loop keeps going until `tool_calls` is empty.
</details>

---

**3. Why use `for step in range(max_steps)` instead of `while True:`?**

<details><summary>Answer</summary>

A confused model can request tools forever. A **step limit** is a guardrail against infinite loops and runaway cost. If you hit the limit without a final answer, stop with a clear message.
</details>

---

**4. Why check `if not msg.tool_calls` instead of `finish_reason == "tool_calls"`?**

<details><summary>Answer</summary>

It checks what the model **actually returned**. A reply cut off with `finish_reason == "length"` has no tool calls and is not a finished answer - treating `finish_reason` alone can mis-classify truncated replies.
</details>

---

**5. "What's 15% of customer 42's order total?" typically needs how many model calls, and why?**

<details><summary>Answer</summary>

About **3**: one to request `get_order_total`, one to request `calculator`, one to write the final answer. Each loop iteration is one model call - so longer tool chains cost more.
</details>

---

**Score 4-5:** ready for Video 09. **Score 0-3:** rewatch 0:45-5:00 (the loop itself).

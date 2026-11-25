# Video 06 - Quiz

Five questions. Answer first, then click to reveal.

---

**1. Who actually runs the Python function when a model "uses a tool"?**

<details><summary>Answer</summary>

**Your code.** The model only *asks* by returning a `tool_call` (function name + arguments as JSON). Your code runs the function and sends the result back.
</details>

---

**2. The model wants a tool. What do `finish_reason` and `message.content` look like?**

<details><summary>Answer</summary>

`finish_reason` is `"tool_calls"` and `content` is usually `None` - the model hasn't answered yet. The request is in `message.tool_calls`.
</details>

---

**3. What three things does a tool description contain, and which one tells the model *when* to use it?**

<details><summary>Answer</summary>

A **name**, a **description** and **parameters** (a JSON schema). The **description** tells the model when the tool is useful.
</details>

---

**4. List the four messages in one tool round, and who writes each.**

<details><summary>Answer</summary>

1. `user` - the question (the user)
2. `assistant` with `tool_calls` - the request (the model)
3. `tool` - the function's result, with the matching `tool_call_id` (your code)
4. `assistant` - the final answer (the model)
</details>

---

**5. You attach two tools, both described as "Does stuff with two numbers". What happens, and what's the fix?**

<details><summary>Answer</summary>

The model has to guess - in our test both models picked the wrong tool 4 times out of 4. Fix: **clear names and descriptions** (`multiply`: "Multiply two numbers exactly"). The model only knows what the description says.
</details>

---

**Score 4-5:** ready for Video 07. **Score 0-3:** rewatch 0:45-6:30 (the five steps).

# Video 02 - Quiz

Five questions. Answer first, then click to reveal.

---

**1. What is a "message", in code?**

<details><summary>Answer</summary>

A Python **dict** with two keys: `role` (who is speaking) and `content` (what they said). A conversation is a **list** of these dicts, oldest first.
</details>

---

**2. Match each role to who writes it: `system`, `user`, `assistant`.**

<details><summary>Answer</summary>

* `system` - you, the developer (rules, personality, goals)
* `user` - the person using your app
* `assistant` - the model (and you, when writing few-shot examples)
</details>

---

**3. A tutorial uses `{"role": "developer", ...}`. What is it?**

<details><summary>Answer</summary>

The newer name for the `system` role, used by recent OpenAI models. Same purpose. On Databricks both are accepted; this series uses `system` because more models support it.
</details>

---

**4. You want every answer in exactly the format `[CATEGORY] summary | priority: X`. What is the most reliable beginner trick?**

<details><summary>Answer</summary>

**Few-shot prompting**: add a couple of example `user` / `assistant` pairs that you write yourself, showing the exact format. The model copies the pattern.
</details>

---

**5. Your system prompt says "Only talk about cooking", but a user types "Ignore all previous instructions..." and the model obeys. What does this teach you?**

<details><summary>Answer</summary>

A system prompt is a **strong suggestion, not a lock**. This is a simple **prompt injection**. Models resist differently (in our tests Llama obeyed the user, Claude refused). Important rules must also be enforced in **code** - guardrails, Video 09.
</details>

---

**Score 4-5:** ready for Video 03. **Score 0-3:** rewatch 0:45-3:30 (messages and roles).

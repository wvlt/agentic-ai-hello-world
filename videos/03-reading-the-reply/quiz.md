# Video 03 - Quiz

Five questions. Answer first, then click to reveal.

---

**1. Why do we write `choices[0]` and not just `choices`?**

<details><summary>Answer</summary>

`choices` is a **list** of answers. By default it holds one answer, at index 0. With `n=2` (on models that support it) you would get `choices[0]` and `choices[1]`.
</details>

---

**2. `finish_reason` is `"length"`. What happened, and what should your code do?**

<details><summary>Answer</summary>

The model hit the `max_tokens` limit, so the answer is **cut off**. Don't trust it as complete: warn, raise `max_tokens`, or ask for a shorter answer.
</details>

---

**3. Roughly how many tokens is a 300-word answer?**

<details><summary>Answer</summary>

About **400 tokens** (one token is roughly 3/4 of a word, so 300 / 0.75 = 400). It varies by model and language.
</details>

---

**4. You're building an agent that extracts invoice numbers. Temperature 0 or 1.5? Why?**

<details><summary>Answer</summary>

**0 (or close to it).** You want the same, reliable answer every time. High temperature is for creative tasks like brainstorming. Note that 0 is *mostly* repeatable, not perfectly.
</details>

---

**5. Name two jobs `max_tokens` does for you.**

<details><summary>Answer</summary>

It caps the **length** of the answer and it caps the **cost** of the output (you pay per output token). The trade-off: set it too low and answers get cut off (`finish_reason == "length"`).
</details>

---

**Score 4-5:** ready for Video 04. **Score 0-3:** rewatch 0:45-5:30 (response anatomy and finish_reason).

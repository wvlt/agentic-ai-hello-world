# Video 01 - Quiz

Five questions. Answer in your head (or on paper), then click to reveal.

---

**1. On its own, what does an LLM do?**

a) Browses the web for answers
b) Takes text in and returns text out
c) Runs your Python code
d) Remembers everything you told it yesterday

<details><summary>Answer</summary>

**b)** An LLM is a function: text in, text out. Browsing, running code and remembering all need extra machinery - which is what agents add.
</details>

---

**2. In one sentence, what is the difference between a chatbot and an agent?**

<details><summary>Answer</summary>

A chatbot only **talks** (one message in, one out); an agent **talks and acts** - it uses tools in a loop until the goal is reached.
</details>

---

**3. The notebook uses an `openai.OpenAI` client. Are your prompts sent to OpenAI?**

<details><summary>Answer</summary>

**No.** "OpenAI-compatible" is a message format. The client's `base_url` points at your Databricks workspace (`/serving-endpoints/`), which sends the request to a model Databricks hosts, such as Llama 3.3. No OpenAI account or key is involved.
</details>

---

**4. You want to try Claude instead of Llama. What do you change?**

<details><summary>Answer</summary>

One line: the model name, e.g. `MODEL = "databricks-claude-haiku-4-5"`. Everything else stays the same.
</details>

---

**5. You ask "What is 48729 * 3817?" and the model confidently gives a wrong number. What is this called, and how will agents fix it?**

<details><summary>Answer</summary>

A **hallucination** - stating something false with confidence. An LLM predicts text; it does not calculate. Agents fix it with **tools**: the model asks your code to run a function (e.g. a `calculator`) that returns the exact answer. You'll build this in Videos 06-08.
</details>

---

**Score 4-5:** you're ready for Video 02. **Score 0-3:** rewatch 1:00-4:00 (the three diagrams) - that's the bit everything else builds on.

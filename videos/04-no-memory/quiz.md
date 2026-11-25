# Video 04 - Quiz

Five questions. Answer first, then click to reveal.

---

**1. What does "stateless" mean for an LLM?**

<details><summary>Answer</summary>

It keeps **nothing** between calls. Each call starts from zero; the model only knows what is in the messages you send in that call.
</details>

---

**2. So how does a chatbot "remember" what you said earlier?**

<details><summary>Answer</summary>

The app keeps a **list of all messages** (user and assistant) and sends the **whole list** with every call. That list is the memory.
</details>

---

**3. Turn 1 of a chat used 60 input tokens. Turn 10 used 400. Why?**

<details><summary>Answer</summary>

Every call resends the **entire history**, so input grows with every turn. You also pay for the early messages again on every turn, so the conversation's total cost grows even faster.
</details>

---

**4. You trim the history to the last 4 messages, and the bot forgets the user's name. What are two fixes?**

<details><summary>Answer</summary>

* **Pin** key facts (name, city, preferences) in the system prompt, which is always sent.
* **Summarise** old messages into a short note and keep that instead of dropping them.
</details>

---

**5. What is the "context window"?**

<details><summary>Answer</summary>

The **maximum** number of tokens a model can take in one call (system prompt + history + new message + room for the reply). If your message list is bigger, the call fails - another reason to trim.
</details>

---

**Score 4-5:** ready for Video 05. **Score 0-3:** rewatch 0:45-3:15 (stateless and the fix).

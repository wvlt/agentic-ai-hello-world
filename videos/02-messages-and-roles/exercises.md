# Video 02 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/02-messages-and-roles`, below the last cell. **Predict first** every time.

Solutions: `notebooks/02-messages-and-roles-solutions` (try first!).

---

## Exercise 1 - Design a persona (4 min)
Write a system prompt for a **"Databricks study buddy"** that:
* explains things using everyday analogies,
* always ends with one short quiz question,
* never uses more than 80 words.

Ask it 2 questions with your `ask()` helper.

**Predict first:** will it stick to 80 words? Count them with `len(answer.split())`.

## Exercise 2 - Yes or no only (3 min)
Write a system prompt that makes the model answer **only** `yes` or `no` (lowercase, nothing else). Test it on 5 questions, including a tricky one like *"Can you explain why the sky is blue?"*.

**Then:** check in code that every answer is exactly `"yes"` or `"no"`. How many passed?

## Exercise 3 - Few-shot translator (5 min)
Use few-shot examples (user/assistant pairs that **you** write) to turn plain-English requests into SQL-style one-liners, for example:
* user: `count customers in Perth` -> assistant: `SELECT COUNT(*) FROM customers WHERE city = 'Perth'`

Write 2 examples, then test with 3 new requests.

**Predict first:** will the model copy your exact style (uppercase keywords, single quotes)?

## Bonus - Defend the system prompt (3 min)
Go back to the *Ignore all previous instructions* cell. Try to make the cooking assistant resist the attack **using only the system prompt**. Test on Llama 3 times.

**Then think:** even if it works today, would you trust it with something important? (Hint: Video 09.)

# Video 04 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/04-no-memory`, below the last cell. **Predict first** every time.

Solutions: `notebooks/04-no-memory-solutions` (try first!).

---

## Exercise 1 - Edit the memory (3 min)
Have a 3-turn conversation with `Chat`, telling it your favourite colour in turn 1. Then **change** that message directly in `chat.history` (e.g. swap "blue" for "green") and ask *"What is my favourite colour?"*.

**Predict first:** which colour will it say?

**Then think:** what does this tell you about who controls an LLM's "memory"?

## Exercise 2 - Count the real cost (5 min)
Add a `total_input_tokens` counter to `Chat` that adds up `prompt_tokens` on every call. Run a 10-turn conversation with full history, then the same 10 turns with `max_history=4`.

**Predict first:** how many times more input tokens will the full history use in total?

## Exercise 3 - Save and resume (4 min)
Save `chat.history` to a JSON file with `json.dump`. Create a **brand new** `Chat`, load the history back in, and ask a question about something from the old conversation.

**Then think:** this is the simplest form of long-term memory. What would you need to do this for 1,000 users?

## Bonus - Summarise instead of drop (3 min)
Instead of throwing old messages away, ask the model to **summarise** them in 2 sentences, and put the summary in the system prompt. Test it with the name-and-city conversation.

**Then think:** what might a summary lose that a pinned fact would not?

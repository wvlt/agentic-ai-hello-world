# Video 03 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/03-reading-the-reply`, below the last cell. **Predict first** every time.

Solutions: `notebooks/03-reading-the-reply-solutions` (try first!).

---

## Exercise 1 - Find the cut-off point (4 min)
Ask *"List 10 tips for learning Python, one per line."* with `max_tokens` set to 20, 60, 120 and 400.

For each, print `finish_reason` and the number of lines in the answer.

**Predict first:** at which value does `finish_reason` change from `length` to `stop`?

## Exercise 2 - Your own token rule (4 min)
Ask for paragraphs of 50, 100 and 200 words. For each, compare the real word count (`len(text.split())`) with `usage.completion_tokens`.

**Then:** work out your own "words per token" number. Is it close to 0.75?

## Exercise 3 - Pick the right temperature (5 min)
For each task, choose a temperature (0, 0.7 or 1.5), run it 3 times and check you were right:
1. Extract the city from *"I live in Perth and work in Fremantle"*. (One word.)
2. Suggest a name for a hiking club.
3. Answer *"What is 2 + 2?"*.

**Then:** which tasks need the same answer every time? Which benefit from variety?

## Bonus - Make get_reply() stricter (2 min)
Change the `get_reply()` helper so that when `finish_reason == "length"` it **raises an error** instead of just warning.

**Think:** when would you prefer an error over a warning? (Hint: an agent deciding what to do next.)

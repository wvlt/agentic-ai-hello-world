# Video 06 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/06-first-tool`, below the last cell. **Predict first** every time.

Solutions: `notebooks/06-first-tool-solutions` (try first!).

---

## Exercise 1 - A weather tool (5 min)
Write `get_weather(city)` that returns fake weather from a dict (e.g. Perth: "sunny, 31C"). Describe it as a tool and do one full round by hand for *"Should I bring an umbrella in London today?"*.

**Predict first:** what arguments will the model send?

## Exercise 2 - Two cities, one question (4 min)
Ask *"What's the weather in Perth and in Tokyo?"* with your weather tool.

**Predict first:** how many items will be in `message.tool_calls`?

**Then:** run every requested call, add one `tool` message per call (each with its own `tool_call_id`), and call the model again. Is the second reply a final answer - or **another** tool call? Try it on both Llama and Claude.

*(Spoiler from our tests: Claude asks for both cities at once; Llama asks for one city per round. One round isn't always enough - that's why Video 08 adds a loop.)*

## Exercise 3 - A tool for something the model cannot know (3 min)
Write `get_today()` that returns `date.today().isoformat()`. Ask *"How many days until Christmas?"* with the tool attached.

**Then think:** the model still has to do the subtraction itself. Is that safe? What extra tool would make it safer?

## Bonus - A buggy tool (3 min)
Change `multiply` to return `a * b + 1000` (a bug). Do the full round again.

**Predict first:** will the model notice the answer is wrong?

**Then think:** who is responsible for a tool's result being correct - the model or you?

# Video 03 Script - Reading the reply: choices, finish_reason, tokens and temperature

**Format:** voice-over on screen recording | **Target length:** 10 minutes | **Notebook:** `notebooks/03-reading-the-reply`

Conventions: **[SCREEN]** = what is on screen, **[DO]** = action to perform, plain text = narration.

---

## 0:00 - Hook (30 s)
**[SCREEN]** A reply that reads: *"1. Start with the basics... 2. Choose a good resource: Select a reputable online"* - and stops.

I asked for ten tips. I got one and a half. And here's the scary part: nothing crashed. No error. If your code only reads the text, it would happily show this to a user. Today: how to read **everything** the model sends back - so this never fools you.

## 0:30 - You are here (15 s)
**[SCREEN]** `you-are-here.svg`

Video 01: we called a model. Video 02: we learned what we send. Video 03: what comes back.

## 0:45 - Anatomy of a response (2 min)
**[SCREEN]** `diagrams/01-anatomy-of-a-response.svg`
**[DO]** Run *Connect*, then *See the whole response*.

Here's the full response, printed as JSON. Let's walk through it.

`choices` is a **list**. Usually it has one item - one answer - which is why we always write `choices[0]`.

Inside `choices[0]` there's the `message`. Its `role` is always `assistant`, and its `content` is the text. There's also a `tool_calls` slot - empty for now; that's how agents ask to use tools, in Video 06.

Next to the message is `finish_reason` - **why** the model stopped. Keep your eye on that one.

And outside `choices` there's `usage` - the tokens you sent, the tokens the model wrote, and the total. That's your bill.

So: `response.choices[0].message.content`. Now every dot in that line makes sense.

## 2:45 - Why choices is a list (45 s)
**[DO]** Run *Ask for two answers at once*.

You can ask for several answers in one call with `n`. Here, `n=2` gives us two different fruits in one go - `choices[0]` and `choices[1]`.

One catch: not every model supports this. Claude rejects `n` greater than 1 - you'll see the error in the next cell. That's fine; most of the time we want just one answer.

## 3:30 - finish_reason (2 min)
**[SCREEN]** `diagrams/02-finish-reason.svg`

Three values you need to know.

`stop` - the model finished naturally. Use the answer.

`length` - it hit your `max_tokens` limit. The answer is **cut off**. Don't trust it.

`tool_calls` - it paused because it wants your code to run a tool. That's Video 06, and it's the heart of every agent.

**[DO]** Run *stop vs length*.

Same request, twice. Without a limit: `stop`, ten full tips. With `max_tokens=40`: `length`, and the list ends mid-sentence.

## 5:30 - Tokens (75 s)
**[DO]** Run *Words vs tokens*.

Models don't read words, they read **tokens** - chunks of text. A rough rule: one token is about three quarters of a word. We asked for 100 words; the model wrote about 95 words using about 120 tokens. Close to the rule.

Why care? Because tokens are what you pay for, and what `max_tokens` counts.

## 6:45 - Temperature (90 s)
**[SCREEN]** `diagrams/03-temperature-dial.svg`

Temperature is the creativity dial. Low means predictable; high means varied.

**[DO]** Run *Temperature experiment*.

Same question five times: "give me one unusual hobby". At temperature 0 we get the same answer every time - sand sculpting. At 1.5 we get five different ones - knife throwing, extreme ironing...

Use low temperature for facts, data extraction and agents - you want them reliable. Use high for brainstorming and names.

One honest note: temperature 0 is *mostly* repeatable, not perfectly. In our tests a different prompt still gave two different answers at zero. Never assume an LLM is deterministic.

## 8:15 - Cost meter (30 s)
**[DO]** Run *Cost meter*.

Output tokens usually cost more than input tokens. And `max_tokens` is a hard ceiling on output - so it's also a **cost cap**. Here's the same request with and without the cap.

## 8:45 - What could go wrong? (45 s)
**[DO]** Run *A safe way to read replies*.

Back to the hook: a cut-off answer looks completely normal if you only read `.content`. So here's a tiny helper, `get_reply`, that checks `finish_reason` first and warns you when the answer was cut off.

Remember this. In Video 08 our agent loop will make decisions based on `finish_reason` - an agent that ignores it acts on half answers.

## 9:30 - Recap and next (30 s)
**[SCREEN]** `you-are-here.svg`

Today: `choices` is a list of answers; the text is in `message.content`; `finish_reason` tells you whether to trust it; `usage` tells you what it cost; `max_tokens` caps length and cost; `temperature` sets predictable versus creative.

Next time: a surprise. Ask the model your name right after you told it - and it won't know. LLMs have **no memory**. We'll fix that.

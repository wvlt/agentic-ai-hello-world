# Video 08 Script - The agent loop

**Format:** voice-over on screen recording | **Target length:** 10 minutes | **Notebook:** `notebooks/08-agent-loop`

Conventions: **[SCREEN]** = what is on screen, **[DO]** = action to perform, plain text = narration.

---

## 0:00 - Hook (30 s)
**[SCREEN]** Video 06 leftover: Llama asked for Perth, then you answered, and the next reply is *another* tool call for Tokyo - not a final answer.

One tool round. Almost an answer. But the model still wants another tool. You could copy-paste another round by hand. Or you could put it in a loop. Today: that loop - and your first real agent.

## 0:30 - You are here (15 s)
**[SCREEN]** `you-are-here.svg`, then `../assets/agent-anatomy.svg` with **the LOOP** highlighted.

Brain, memory, tools - all lit. Today we connect them: persistence. Keep going until the job is done.

## 0:45 - The one big idea (60 s)
**[SCREEN]** `diagrams/01-the-agent-loop.svg`

An agent is not a special model. It is four ordinary things working together:

```
ask the model
if it wants tools -> run them, save results, ask again
else              -> return its answer
```

That's it. Frameworks are this loop with extras. By the end of this notebook you'll have written it in about 40 lines.

## 1:45 - Why one round isn't enough (60 s)
**[SCREEN]** `diagrams/02-one-round-vs-loop.svg`
**[DO]** Run *Connect*, then *One round is not enough*.

Same weather tool as Video 06. Ask about Perth and Tokyo. Do **one** round. Llama asks for Perth. You answer. Call again - it asks for Tokyo. Still not done. Claude often batches both cities in one reply - but either way, "exactly one round" is a fragile assumption. The agent loop removes that assumption: keep going until `tool_calls` is empty.

## 2:45 - The tools (45 s)
**[DO]** Run *Define the tools*, then *Describe them*.

Three plain Python functions: look up an order total, run a calculator, get today's date. Plus a small helper that turns each function into a tool menu entry. Nothing AI about these - same idea as Videos 06 and 07.

## 3:30 - Write the loop (90 s)
**[DO]** Run *The agent loop*.

Here it is. A `for` loop with a step limit. Each step: call the model. If there are no tool calls, return the text - we're done. If there are, use `add_tool_results` from Video 07 (all four golden rules), then loop again. If we hit `max_steps` without a final answer, stop with a clear message.

**[SCREEN]** Highlight: `if not msg.tool_calls` and `for step in range(1, max_steps + 1)`.

Two deliberate choices. We check `tool_calls`, not `finish_reason` - because a reply cut off with `finish_reason == "length"` is not a finished answer. And we use a step limit, not `while True` - so a confused model cannot run forever.

## 5:00 - Run it (75 s)
**[DO]** Run *Your first real agent*.

Predict first: "What's 15% of the order total for customer 42?" Which tools, in what order?

Watch the steps print. Look up the total. Calculator for 15%. Final answer. Multiple tools, one question - that's an agent.

**[DO]** Run *More questions*.

Today's date. Compare two customers. Unknown customer. A fun fact that needs no tool. The model decides when to use tools and when to just answer.

## 6:15 - Design choices (60 s)
**[SCREEN]** `diagrams/03-design-choices.svg`
**[DO]** Run *Design choices* (markdown).

Same loop you'll see in tutorials, with two safer defaults: step limit, and check what the model actually returned. Video 09 adds more guardrails. Today you already have the essential one.

## 7:15 - Cost meter (45 s)
**[DO]** Run *Cost meter*.

Count the model calls. Each loop iteration is one call. Three steps means three calls - plus all the tool descriptions and history on every call. Agents multiply cost by the length of the chain. Prefer narrow tools (Video 07) so each step stays small.

## 8:00 - What could go wrong? (60 s)
**[DO]** Run *What could go wrong? max_steps=1*.

Set `max_steps=1` and rerun the 15% question. It stops mid-job - looked up the total, never reached the calculator. Without any limit, the opposite failure: a model that keeps calling tools forever burns tokens until you kill the notebook. The step limit is the seatbelt. Video 09 puts on the rest of the harness.

## 9:00 - Recap and next (60 s)
**[SCREEN]** `you-are-here.svg`

Today: an agent is LLM + tools + loop + memory. One round is not enough - keep going until there are no tool calls. About 40 lines. A step limit from day one.

Next time: keeping agents safe - more guardrails, errors as results, retries, and stops that go beyond a step counter.

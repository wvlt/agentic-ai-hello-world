# Video 09 Script - Keeping agents safe

**Format:** voice-over on screen recording | **Target length:** 11 minutes | **Notebook:** `notebooks/09-safe-agents`

Conventions: **[SCREEN]** = what is on screen, **[DO]** = action to perform, plain text = narration.

---

## 0:00 - Hook (30 s)
**[SCREEN]** An agent mid-run. Python traceback. Cell dead. Or: five identical tool calls, bill climbing.

Last video you built a loop that works. Today: make sure it can't run away - or take your notebook down with it.

## 0:30 - You are here (15 s)
**[SCREEN]** `you-are-here.svg`, then `../assets/agent-anatomy.svg` with **Guardrails** lit.

Brain, memory, tools, loop - all on. The seatbelt goes around everything.

## 0:45 - The one big idea (60 s)
**[SCREEN]** `diagrams/01-the-seatbelt.svg`

Guardrails are not one feature. They are a set of stops and checks: step limit, token budget, "don't trust truncated replies", "errors become tool results", "only allow-listed tools", "stop if the same call repeats", and for writes - ask a human first.

You already have one: `max_steps`. Today we add the rest, in plain Python.

## 1:45 - Recap the unsafe loop (45 s)
**[DO]** Run *Connect*, then *Video 08 agent (baseline)*.

Same agent as last time. It works on happy paths. Now we break it on purpose.

## 2:30 - Errors as results (90 s)
**[SCREEN]** `diagrams/02-errors-as-results.svg`
**[DO]** Run *A tool that crashes*, then *Errors as results*.

Make `get_order_total` raise for an unknown customer. Without a try/except, the loop dies. Wrap the call: catch the exception, send `error: ...` back as the tool content. The model reads it and answers politely. The notebook stays alive.

Rule: **tools return results, including failures.** Exceptions are for your code - not for the model's conversation.

## 4:00 - Truncated replies (60 s)
**[DO]** Run *Don't trust finish_reason length*.

Force a tiny `max_tokens`. `finish_reason` is `length` - the text is cut off. If you only check `if not tool_calls`, you might return a half-sentence as "done". Guardrail: if `finish_reason == "length"`, stop with a clear message (or raise max_tokens and retry once). Never treat a truncated reply as a finished answer.

## 5:00 - Repeated tool calls (75 s)
**[DO]** Run *Stop repeated tool calls*.

Sometimes the model asks for the same tool with the same arguments again and again. Cap it: fingerprint each call; if you've seen it twice already, stop. In our demo that cut a runaway from five model calls down to two.

## 6:15 - Allow-lists and read vs write (75 s)
**[DO]** Run *Allow-list + read vs write*.

Only run tools that appear in your `TOOLS` dict - and be explicit about **read** vs **write**. Lookups and calculators are fine. Something like `cancel_order` should need approval. Pattern: if the tool is in `WRITE_TOOLS`, print the request and skip (or wait) until a human says yes. Beginner version: refuse writes unless `allow_writes=True`.

## 7:30 - Budget cap + cost meter (60 s)
**[SCREEN]** `diagrams/03-stop-conditions.svg`
**[DO]** Run *Token budget*, then *Cost meter*.

Add `max_tokens_total`. Sum `usage.total_tokens` each step; if you cross the budget, stop. Cost meter: show calls, tokens, and example dollars. Guardrails protect correctness *and* the bill.

## 8:30 - The safe agent (60 s)
**[DO]** Run *Safe agent: all seatbelts*.

One function that combines: step limit, truncation check, errors as results, allow-list, repeat detector, token budget. Same questions as Video 08 - plus the failure cases. It recovers or stops cleanly. It does not crash.

## 9:30 - What could go wrong? (45 s)
Retries on rate limits: wait and try again a few times - then give up. Infinite retries are just another runaway. And prompting "think step by step before calling tools" helps a little; **code guardrails** are what you trust.

## 10:15 - Recap and next (45 s)
**[SCREEN]** `you-are-here.svg`

Today: seatbelts - caps, errors as results, truncation, repeats, allow-lists, read vs write. An agent that cannot quietly run away.

Next time: seeing inside - MLflow tracing, so you can debug every decision.

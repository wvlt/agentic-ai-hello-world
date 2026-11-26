# Video 07 Script - The golden rules of tools

**Format:** voice-over on screen recording | **Target length:** 10 minutes | **Notebook:** `notebooks/07-tool-rules`

Conventions: **[SCREEN]** = what is on screen, **[DO]** = action to perform, plain text = narration.

---

## 0:00 - Hook (30 s)
**[SCREEN]** The same cell run twice. Llama: a friendly answer. Claude: `Error code: 400 - BAD_REQUEST`.

Same code. Same question. On one model it works perfectly. On the other, it crashes. The bug was there all along - one model just didn't tell us. Today: the rules that make tool code work on every model.

## 0:30 - You are here (15 s)
**[SCREEN]** `you-are-here.svg`

Last video you did one tool round by hand. Today we make it bulletproof - the last step before the agent loop.

## 0:45 - The four golden rules (90 s)
**[SCREEN]** `diagrams/01-four-golden-rules.svg`

Four rules. **One: request before result.** The assistant message with the tool call goes into the list *before* your tool result. **Two: match the id.** Every tool message carries the id of the call it answers. **Three: results are strings.** If your function returns a dict, `json.dumps` it. **Four: answer every call.** If the model asks for two tools, send back two tool messages.

That's it. Four rules. Let's break each one on purpose.

## 2:15 - Break the rules (2 min 30 s)
**[DO]** Run *Connect*, then *Get a real tool request*.

First we get a genuine tool request from each model, for "should I bring an umbrella in London".

**[DO]** Run *Break rules 1 to 3*.

**[SCREEN]** `diagrams/02-strict-vs-lenient.svg`

Now we send back five versions: one correct, three with a rule broken, and one with rule three fixed.

Look at Llama. Missing the assistant request? Accepted. Wrong id? Accepted. It just answers. Now Claude: error, error, error. Both reject a dict as content - and both are happy once we `json.dumps` it.

## 4:45 - What could go wrong? (45 s)

This is the scariest kind of bug: the silent one. If you'd only ever tested on Llama, your code would pass every test - and crash the day someone switches the model to Claude. Lenient isn't safe. **Write to the strictest rules.**

## 5:30 - Rule four (45 s)
**[DO]** Run *Break rule 4*.

Rule four needs a model that asks for two tools at once - Claude does. Ask about Perth and Tokyo, answer only the first call - error. By the way, this explains last video's mystery: the Databricks Llama endpoint only allows **one** tool call per reply. That's why it asked for Perth, then Tokyo.

## 6:15 - One safe helper (45 s)
**[DO]** Run *A helper that follows all four rules*.

So we write the rules down once, in code. `add_tool_results` appends the request, runs every call, turns every result into a string, and uses the right id. From now on, we never build these messages by hand.

## 7:00 - Context engineering (90 s)
**[SCREEN]** `diagrams/03-context-budget.svg`
**[DO]** Run *400 orders*, *Two ways to design the tool*, then *Big dump vs narrow tool*.

Everything the model sees lives in one place: the **context window** - system prompt, tool menu, history, and tool results. Tool results can be the biggest part.

Two tool designs for the same question - "how much did customer 42 spend in March?" Design one: `get_all_orders`, dump all 400 orders. Design two: `get_order_total`, which does the filtering and adding in Python and returns one number.

The big dump: over 31,000 input tokens. And look at the answers. Llama: wrong - it missed orders. In our tests Llama was wrong every time, and even Claude got it wrong one time in two. The narrow tool: about 800 tokens, and both models correct, every time.

This is **context engineering**: deciding what goes into the window. Do the work in code; give the model only what it needs.

## 8:30 - Cost meter (30 s)
**[DO]** Run *Cost meter*.

At our example prices, the big dump costs about 38 times more per question. Across ten thousand questions, that's real money - for a worse answer.

## 9:00 - Recap and next (60 s)
**[SCREEN]** `you-are-here.svg`

Today: four golden rules - request before result, match the id, results are strings, answer every call. Lenient models hide broken code, so write to the strictest rules. And design tools that return small, exact results.

Next time, the moment we've been building to: we put all of this in a loop - and you'll have your first real agent.

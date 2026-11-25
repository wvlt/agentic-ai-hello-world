# Video 06 Script - Giving the model hands: your first tool

**Format:** voice-over on screen recording | **Target length:** 10 minutes | **Notebook:** `notebooks/06-first-tool`

Conventions: **[SCREEN]** = what is on screen, **[DO]** = action to perform, plain text = narration.

---

## 0:00 - Hook (30 s)
**[SCREEN]** Video 01's cell: three different wrong answers to `48729 * 3817`. Then today's final cell: *"The answer is 185,998,593"* - correct.

In Video 01, the model got this multiplication wrong three times in a row. Today it gets it right - every time. Not because it got smarter. Because we gave it **hands**.

## 0:30 - You are here (15 s)
**[SCREEN]** `you-are-here.svg`, then `../assets/agent-anatomy.svg` with **Tools** lit up.

Foundations are done. Welcome to the Tools phase. Today the agent gets its hands.

## 0:45 - The one big idea (60 s)
**[SCREEN]** `diagrams/01-the-tool-call-dance.svg`

Here's the most important sentence in this whole series: **the model never runs your code.**

It can't. It's text in, text out. So instead, we give it a menu of functions it may ask for. When it wants one, it replies with a request: "please call multiply with a equals 48729 and b equals 3817". **Your** code runs the function, sends back the result, and the model writes the final answer.

And that request? It's JSON - exactly what you learned in Video 05. A tool call is just structured output where the structure is "which function, which arguments".

## 1:45 - Step 1: a normal function (30 s)
**[DO]** Run *Connect*, *Without a tool*, then *Step 1 - a normal Python function*.

First, proof of the problem: without a tool, the answer is wrong. Then a completely ordinary Python function. Nothing AI about it.

## 2:15 - Step 2: describe it (75 s)
**[SCREEN]** `diagrams/02-function-to-schema.svg`
**[DO]** Run *Step 2 - describe the tool*.

The model can't see our code, so we describe the function: a **name**, a **description** that says *when* to use it, and the **parameters** - which is a JSON schema, just like Video 05. Think of it as the menu. The model can only order what's on the menu, and it only knows what the menu says.

## 3:30 - Step 3: the model asks (75 s)
**[DO]** Run *Step 3 - the model asks for the tool*.

We send the question plus the menu. Look at the reply. The text `content` is **empty** - the model isn't answering yet. `finish_reason` is `tool_calls` - remember that from Video 03? And here's the request: function `multiply`, arguments `a: 48729, b: 3817`.

Notice the arguments arrive as a JSON **string**. We'll need `json.loads`.

## 4:45 - Step 4: we run it (30 s)
**[DO]** Run *Step 4 - we run the tool*.

Parse the arguments, call our function. Python gives the exact answer.

## 5:15 - Step 5: send the result back (75 s)
**[DO]** Run *Step 5 - send the result back*.

Now we add two messages to the conversation: the model's request, and our result with the role `tool` - and the same `tool_call_id`, so the model knows which request this answers. Then we call the model again.

"The answer is 185,998,593." Correct.

**[DO]** Run *Trace the conversation*.

Here's the whole dance as a list: user question, assistant tool call, tool result, assistant answer. Four messages. Who wrote each one? The user, the model, **your code**, the model.

There are some strict rules about these messages - what happens if you get the order or the id wrong. That's next video.

## 6:30 - The model decides (45 s)
**[DO]** Run *The model decides when to use a tool*.

The tool is just an option. Ask "what's the capital of France?" with the same tool attached, and both models simply answer - no tool call. The model decides.

## 7:15 - Cost meter (45 s)
**[DO]** Run *Cost meter*.

Tools aren't free. Their descriptions are sent with every call - and models wrap them in extra instructions. Just saying "Hi" went from about 36 input tokens to about 720 with one small tool on Llama. And one tool round needs **two** model calls: one to ask, one to answer. Only give the model the tools it needs.

## 8:00 - What could go wrong? (75 s)
**[SCREEN]** `diagrams/03-descriptions-matter.svg`
**[DO]** Run *Vague tool descriptions*.

The model only knows your tools by their names and descriptions. Here are two tools, `tool_a` and `tool_b`, both described as "does stuff with two numbers". Secretly, `tool_a` adds and `tool_b` multiplies. Which does the model pick for a multiplication? `tool_a`. In our tests, both models did this four times out of four. The adder returns 52,546 - and look what happens next: the model notices that can't be right, gives up on the tool, and guesses the product in its head. Wrong again - we're back to Video 01.

**[DO]** Run *Clear names and descriptions*.

Same functions, honest names and descriptions: `add` and `multiply`. Correct every time. Writing good tool descriptions matters more than any clever prompt.

## 9:15 - Recap and next (45 s)
**[SCREEN]** `you-are-here.svg`

Today: the model never runs your code - it asks. You describe tools with a name, a description and parameters. One round is: ask, run, send back, answer. And the description is the model's only clue.

Next time: the golden rules of tool messages - and why code that works on one model can crash on another.

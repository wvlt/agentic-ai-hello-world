# Video 04 Script - LLMs have no memory

**Format:** voice-over on screen recording | **Target length:** 10 minutes | **Notebook:** `notebooks/04-no-memory`

Conventions: **[SCREEN]** = what is on screen, **[DO]** = action to perform, plain text = narration.

---

## 0:00 - Hook (30 s)
**[SCREEN]** Two cells. Cell 1: "Hi, my name is Sam." Cell 2: "What is my name?" - reply: *"I don't know your name."*

I told it my name. One second later, it has no idea. This isn't a bug - this is how every LLM works. And once you understand why, you'll understand how every chatbot and agent in the world really "remembers".

## 0:30 - You are here (15 s)
**[SCREEN]** `you-are-here.svg`, then `../assets/agent-anatomy.svg` with **Memory** lit up.

Videos 1 to 3 were all about the brain. Today we add the second part of our agent: memory - the notebook.

## 0:45 - Proof: the model forgets (60 s)
**[DO]** Run *Connect*, then *Proof that the model forgets*.

Two separate calls. In the first, I introduce myself. In the second, I ask my name. It doesn't know.

**[SCREEN]** `diagrams/01-stateless.svg` - left side

Each call starts from zero. The model is **stateless**: nothing carries over from one call to the next. It's like phoning a call centre and getting a new person every time.

## 1:45 - The fix: send the history (90 s)
**[SCREEN]** `diagrams/01-stateless.svg` - right side

So how do chatbots remember? Simple: **you** keep a list of everything that's been said, and send the **whole list** every time.

**[DO]** Run *The same question, with history*.

Same question - "What is my name?" - but this time the list contains my introduction and the model's reply. Now it knows.

Remember Video 02: a conversation is a list of messages. That list **is** the memory. There's nothing else.

## 3:15 - A chat class that remembers (2 min)
**[DO]** Run *A chat that remembers*.

Let's wrap that in a small class. `Chat` keeps a list. `send()` does three things: add the user's message, call the model with the whole list, and add the model's reply. That's it - a chatbot with memory, in about fifteen lines.

**[DO]** Run *Have a conversation*.

Six turns. I tell it my name and city, chat about a weekend plan, and at the end ask "what is my name and where do I live?" It remembers.

**[DO]** Run *Look inside the memory*.

And here's the memory itself - just a Python list. You can read it, print it, save it to a file, even edit it.

## 5:15 - Cost meter: memory isn't free (90 s)
**[SCREEN]** `diagrams/02-memory-is-a-list.svg`
**[DO]** Run *Cost meter - tokens per turn*.

Look at the input tokens on each turn. Turn 1: about 60. Turn 6: about 200. Because every call resends the **whole** history.

And look at the total. You don't pay for turn 6's history once - you paid for the early messages on **every** turn since. Long conversations get expensive fast. Every model also has a maximum - the **context window** - and if the list gets bigger than that, the call fails.

## 6:45 - Trimming (60 s)
**[DO]** Run *Trim the history*.

The simplest fix: only send the last few messages. Here our `Chat` keeps just the last four. Fewer tokens per call - about half.

But watch the last answer...

## 7:45 - What could go wrong? (60 s)
**[SCREEN]** `diagrams/03-trimming-and-pinning.svg` - row 2

"I don't have that information." My name was in the very first message - and trimming threw it away. Trimming silently forgets things. The model doesn't warn you; it just doesn't know.

**[DO]** Run *Pin the important facts*.

**[SCREEN]** Row 3

The fix: **pin** important facts in the system prompt, which is always sent. Now we trim the chat to four messages **and** it still knows I'm Sam from Perth. Cheap and correct.

In real systems, you might also ask the LLM to **summarise** old messages into a few lines. Same idea: decide what's worth keeping.

## 8:45 - Why agents care (30 s)

This matters for agents more than chatbots. An agent's memory holds its plan, every tool result, every decision. What you keep in that list - and what you drop - decides how smart it can be. People call this **context engineering**, and we'll come back to it in Video 07.

## 9:15 - Recap and next (45 s)
**[SCREEN]** `you-are-here.svg`

Today: LLMs are stateless - they forget everything between calls. Memory is the list you send. Memory makes every call bigger and pricier. Trimming saves tokens but can forget; pin what matters.

Next time: answers your **code** can use. Instead of free text, we'll get the model to reply in clean JSON - the last step before we give it tools.

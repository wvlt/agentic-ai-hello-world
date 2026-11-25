# Video 01 Script - What is an AI agent? + your first LLM call

**Format:** voice-over on screen recording | **Target length:** 10 minutes | **Notebook:** `notebooks/01-hello-llm`

Conventions: **[SCREEN]** = what is on screen, **[DO]** = action to perform, plain text = narration.

---

## 0:00 - Hook (45 s)
**[SCREEN]** A finished agent (from Video 08) answering: *"What's 15% of the order total for customer 42?"* The output shows it looking up the order, calculating, and answering *$37.50*.

This is an AI agent. I asked it a question it couldn't possibly know the answer to. So it looked up the order, did the maths, and answered. Nobody told it which steps to take - it decided.

By the end of this series you'll build this yourself, in about 40 lines of plain Python. No frameworks, no magic. And today we take the very first step.

## 0:45 - You are here (15 s)
**[SCREEN]** `you-are-here.svg`

Thirteen short videos, one idea each. We're at number one: what is an agent, and how do we talk to the brain inside it.

## 1:00 - An LLM is a function (90 s)
**[SCREEN]** `diagrams/01-llm-is-a-function.svg`

At the heart of every AI agent is an LLM - a large language model. Llama, Claude, GPT - they're all LLMs.

If you know Python, here's the best way to think about an LLM: it's a function. Text goes in, text comes out. That's it.

**[SCREEN]** Highlight `def llm(text: str) -> str`

It's an incredibly good function - it can explain, summarise, write code, translate. But notice what's missing. On its own, an LLM can't browse the web. It can't run code. It can't even do exact maths. And it doesn't remember you between calls.

Keep that list in mind. Fixing every item on it is what the rest of this series is about.

## 2:30 - Chatbot vs agent (90 s)
**[SCREEN]** `diagrams/02-chatbot-vs-agent.svg` - left panel first

Wrap an LLM in a chat window and you get a chatbot. You ask, it answers. One message in, one message out. Ask it "what's 15% of my last order?" and the best it can do is say sorry - it can't see your orders.

**[SCREEN]** Reveal right panel

An agent is different. It has the same brain - the LLM - but now it can use **tools**: normal Python functions, like "look up an order" or "calculate". The LLM decides which tool to use, your code runs it, the result goes back to the LLM, and it decides again. It repeats until the job is done.

**[SCREEN]** `../assets/agent-anatomy.svg`, LLM highlighted

So here's the picture we'll build up over the series. The **brain** is the LLM. The **hands** are tools. The **notebook** is memory - what the brain can see. The **loop** keeps it going. And around everything, **guardrails** - the seatbelt.

One sentence to remember: **a chatbot talks; an agent talks and acts, in a loop, until the goal is reached.**

Today we light up just one part - the brain.

## 4:00 - Where the request goes (60 s)
**[SCREEN]** `diagrams/03-where-the-request-goes.svg`

One thing that confuses almost everyone. In the code you'll see the word "OpenAI". But we're not using OpenAI.

"OpenAI-compatible" is a message format that became the industry standard. Databricks speaks that format. So we use the popular `openai` Python library, but it's pointed at **your Databricks workspace**. Your workspace sends the request to a model it hosts - here, Llama 3.3 from Meta.

No API keys, no OpenAI account. And to switch models, you change one line.

## 5:00 - Live coding: connect and Hello World (2 min 30 s)
**[SCREEN]** Notebook `01-hello-llm`
**[DO]** Run the *Connect* cell.

Three lines. We import the Databricks SDK, ask it for an OpenAI-style client that's already logged in as us, and pick the model by name.

**[DO]** Run the *Hello World* cell.

And here's our first call. We send a message - "In one sentence, what is an AI agent?" - and print the reply.

**[SCREEN]** The reply appears.

That's it. You've just called an LLM. Text in, text out.

The reply lives at `response.choices[0].message.content`. That looks like a mouthful - we'll unpack every piece in Video 03. For now: that's where the text is.

**[DO]** Run the *Prove it* cell.

And here's proof of what I said earlier: the client is a normal OpenAI client, but it's sending requests to our Databricks workspace.

## 7:30 - Experiment: change the question, swap the model (90 s)
**[DO]** Edit `question`, re-run.

Change the question to anything you like. Run it again.

**[DO]** Run the *Swap the model* cell.

Now the same question, but to a different model - Claude Haiku. One line changed. Notice the answers differ in style and length. Models are like people: same question, different answers.

## 8:15 - Cost meter (30 s)
**[DO]** Run the *Cost meter* cell.

Every video we'll check the cost. Models read and write **tokens** - chunks of text, roughly three quarters of a word. You pay per token. Our last call used a few hundred tokens - a tiny fraction of a cent, or thousands of calls per dollar even at the example prices. So experiment freely.

## 8:45 - What could go wrong? (45 s)
**[DO]** Run the *Confidently wrong* cell.

Here's something every LLM struggles with: maths. We ask it to multiply 48,729 by 3,817 - three times - and compare with Python.

**[SCREEN]** Three model answers vs Python's answer.

Wrong. Confidently wrong. And a *different* wrong answer each time. An LLM predicts text that *looks* like the right answer - it doesn't calculate. Stating something false with confidence is called a **hallucination**.

This is exactly why agents need tools. Soon we'll give the model a calculator tool - and it'll get it right every time.

## 9:30 - Recap and next (30 s)
**[SCREEN]** `you-are-here.svg`

Today you learned: an LLM is a function - text in, text out. A chatbot talks; an agent talks and acts in a loop. And you made your first LLM call on Databricks.

Try the three exercises - about fifteen minutes - and the five-question quiz.

Next time: how to give the model instructions and a personality, using **messages and roles**. See you there.

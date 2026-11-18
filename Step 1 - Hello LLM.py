# Databricks notebook source
# DBTITLE 1,Welcome and Big Picture
# MAGIC %md
# MAGIC # Step 1 - Hello, LLM
# MAGIC
# MAGIC **Course:** Agentic AI Hello World (Steps 1-6)
# MAGIC
# MAGIC ## Step 0: what is an agent? (read first)
# MAGIC * An **LLM** is a function: text in, text out. On its own it cannot *do* anything.
# MAGIC * An **agent** is an LLM in a **loop**: it looks at the situation, decides on an action, calls a **tool**, sees the result, and repeats until done.
# MAGIC * Mental model: **LLM = brain**, **tools = hands**, **loop = persistence**, **memory = notebook**.
# MAGIC
# MAGIC By Step 5 you will have built a real agent in plain Python. Today: just talk to a model.
# MAGIC
# MAGIC ## Goal of this notebook
# MAGIC Send one message to an LLM hosted on Databricks and print the reply.
# MAGIC
# MAGIC **Done when:** you get a reply, can explain the four message roles (`system`/`developer`, `user`, `assistant`, `tool`), and know what `choices` and `finish_reason` mean.

# COMMAND ----------

# DBTITLE 1,Connect to a Databricks-hosted model
# Databricks hosts many models behind an OpenAI-compatible API.
# The SDK gives us a ready-authenticated client - no API keys needed.
from databricks.sdk import WorkspaceClient

client = WorkspaceClient().serving_endpoints.get_open_ai_client()

# The name of the model (a "serving endpoint") we will talk to
MODEL = "databricks-meta-llama-3-3-70b-instruct"
print("Client ready. Model:", MODEL)

# COMMAND ----------

# DBTITLE 1,Wait - OpenAI client, but a Llama model?
# MAGIC %md
# MAGIC ## Wait - an OpenAI client, but a Llama model?
# MAGIC
# MAGIC We are **not** calling OpenAI the company. **"OpenAI-compatible" is a format, not a vendor.**
# MAGIC
# MAGIC * OpenAI's *Chat Completions* API became the industry-standard way to talk to LLMs: send a list of `{"role", "content"}` messages, get back `choices[0].message`.
# MAGIC * Many providers accept that same format: Databricks, Azure, vLLM, Ollama, ...
# MAGIC * The `openai` Python package is just an **HTTP client** that speaks this format. It sends requests to whatever server you point it at.
# MAGIC
# MAGIC ### Where our requests actually go
# MAGIC * `get_open_ai_client()` returns a normal `openai.OpenAI` client, but with its `base_url` set to **your Databricks workspace** (`https://<workspace>/serving-endpoints/`) and authenticated with your Databricks login.
# MAGIC * `MODEL = "databricks-meta-llama-3-3-70b-instruct"` is the name of a **serving endpoint** in your workspace. Databricks routes the request to Meta's Llama 3.3 70B, hosted by Databricks.
# MAGIC * No OpenAI API key is involved, and your prompts stay inside Databricks.
# MAGIC
# MAGIC **Analogy:** the `openai` library is a web browser and "OpenAI-compatible" is HTTP. A browser can open any website that speaks HTTP - here the "website" is your Databricks endpoint, and Llama is the model behind it.
# MAGIC
# MAGIC ### Why this matters
# MAGIC You can swap models by changing **one line** (`MODEL`), e.g. `databricks-claude-sonnet-4-5`, `databricks-gpt-oss-120b`. Messages, JSON schemas, tool calls and the agent loop all stay the same.
# MAGIC
# MAGIC **Caveat:** models differ in quality. Small models (e.g. `llama-3-1-8b`) are less reliable at tool calling and strict JSON, which matters in Steps 4-5.
# MAGIC
# MAGIC Run the next cell to see it for yourself.

# COMMAND ----------

# DBTITLE 1,Prove it - where is the client pointing?
# The client is a standard OpenAI client...
print("Client type:", type(client))
# ...but it points at YOUR Databricks workspace, not api.openai.com
print("Sends requests to:", client.base_url)
print("Model / endpoint :", MODEL)

# COMMAND ----------

# DBTITLE 1,Hello World
# Hello World: one message in, one reply out
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Say hello to a new AI student in one sentence."}],
)

print(response.choices[0].message.content)

# COMMAND ----------

# DBTITLE 1,Explain the response object
# MAGIC %md
# MAGIC ## What just happened?
# MAGIC * `messages` is a **list of dicts**. Each dict has a `role` and `content`.
# MAGIC * The model returns a `response` object. The text lives in `response.choices[0].message.content`.
# MAGIC
# MAGIC ### Why `choices` is a list
# MAGIC * By default the model generates **one** answer, so it sits at index 0: `response.choices[0]`.
# MAGIC * If you ask for several variations at once with the `n` parameter, you get `choices[0]`, `choices[1]`, ... (not every model supports `n > 1` - Claude endpoints reject it).
# MAGIC
# MAGIC ### What's inside `choices[0]`
# MAGIC * `.message.role` - always `"assistant"` (it's the model speaking).
# MAGIC * `.message.content` - the text reply (can be `None` when the model wants a tool instead).
# MAGIC * `.message.tool_calls` - functions the model wants **your Python code** to run (Step 4).
# MAGIC * `.finish_reason` - **why** the model stopped:
# MAGIC
# MAGIC | `finish_reason` | Meaning |
# MAGIC | --- | --- |
# MAGIC | `stop` | Finished naturally |
# MAGIC | `length` | Hit your `max_tokens` limit - the answer is cut off |
# MAGIC | `tool_calls` | Paused because it wants you to run a tool |
# MAGIC
# MAGIC Run the next two cells to see these for yourself.

# COMMAND ----------

# DBTITLE 1,Inspect the full response
print("Role of reply :", response.choices[0].message.role)
print("Finish reason :", response.choices[0].finish_reason)
print("Tokens used   :", response.usage)

# COMMAND ----------

# DBTITLE 1,choices and finish_reason in action
# 1. Several answers at once with n=2 -> choices has 2 entries
multi = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Name a fruit. One word."}],
    n=2,
    temperature=1.0,
)
print("Number of choices:", len(multi.choices))
for i, choice in enumerate(multi.choices):
    print(f"  choices[{i}] -> {choice.message.content}")

# 2. finish_reason == "length": we cut the model off with a tiny max_tokens
cut = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Count from 1 to 50."}],
    max_tokens=10,
)
print("\nTruncated reply:", cut.choices[0].message.content)
print("finish_reason  :", cut.choices[0].finish_reason)   # 'length' - the answer is incomplete!

# COMMAND ----------

# DBTITLE 1,The four message roles
# MAGIC %md
# MAGIC ## The four message roles
# MAGIC Every message has a `role` that tells the model **who is speaking**.
# MAGIC
# MAGIC | Role | Who writes it | Purpose | First used |
# MAGIC | --- | --- | --- | --- |
# MAGIC | `system` (or `developer`) | You, the developer | Rules, personality and goals | This step |
# MAGIC | `user` | The end user | The question or instruction | This step |
# MAGIC | `assistant` | The model | Its replies. You send past replies back so it "remembers" | Step 2 |
# MAGIC | `tool` | Your Python code | The result of a function the model asked you to run | Step 4 |
# MAGIC
# MAGIC **`system` vs `developer`:** newer OpenAI models call this role `developer`; `system` is the older name and still works. On the Databricks endpoints used here (Llama, Claude) both are accepted - we use `system` because it's the most widely supported.
# MAGIC
# MAGIC ### Why this matters for agents
# MAGIC An agent is just a Python `while` loop around this message list:
# MAGIC 1. Start with `system` + `user` messages.
# MAGIC 2. The model replies with `tool_calls` (`finish_reason == "tool_calls"`).
# MAGIC 3. Your code runs the function and appends the result as a `tool` message.
# MAGIC 4. Send the list back. Repeat until the model answers with no tool calls (`finish_reason == "stop"`).
# MAGIC
# MAGIC You'll build exactly this in Step 5. For now, let's add a `system` message and see how it changes behaviour.

# COMMAND ----------

# DBTITLE 1,System prompt changes behaviour
def ask(question, system_prompt="You are a helpful assistant.", temperature=0.7):
    """Small helper: send one question with a system prompt, return the reply text."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content

question = "What is a Python list?"
print("--- Normal ---")
print(ask(question))
print("\n--- Pirate ---")
print(ask(question, system_prompt="You are a pirate. Answer in one short sentence, in pirate speak."))

# COMMAND ----------

# DBTITLE 1,Temperature experiment
# temperature controls randomness: 0 = predictable, higher = more creative/varied
q = "Give me a name for a pet robot. Reply with the name only."
print("temperature=0  :", [ask(q, temperature=0) for _ in range(3)])
print("temperature=1.2:", [ask(q, temperature=1.2) for _ in range(3)])

# COMMAND ----------

# DBTITLE 1,Exercises
# MAGIC %md
# MAGIC ## Exercises
# MAGIC 1. **Predict first:** before running, guess what the pirate answer will look like. Were you right?
# MAGIC 2. Write a system prompt that makes the model answer **only** with yes or no.
# MAGIC 3. Swap `MODEL` to another endpoint, e.g. `databricks-claude-haiku-4-5`, and compare answers.
# MAGIC 4. Replace `"system"` with `"developer"` in the `ask` helper. Does anything change?
# MAGIC 5. Set `max_tokens=5` on a long question. What is the `finish_reason`, and what would an agent need to do about it?
# MAGIC
# MAGIC **Key takeaway:** an LLM call is just a function call: `messages in -> message out`. Everything in agentic AI is built on this one call.
# MAGIC
# MAGIC Next: **Step 2 - Conversation and Memory**

# COMMAND ----------


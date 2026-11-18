# Databricks notebook source
# DBTITLE 1,Intro
# MAGIC %md
# MAGIC # Step 2 - Conversation and Memory
# MAGIC
# MAGIC **Big idea:** LLMs are **stateless**. They forget everything between calls.
# MAGIC A "conversation" is just you sending the **whole message history** every time.
# MAGIC
# MAGIC **Done when:** the model remembers your name from turn 1 when asked in turn 3.

# COMMAND ----------

# DBTITLE 1,Setup
from databricks.sdk import WorkspaceClient

client = WorkspaceClient().serving_endpoints.get_open_ai_client()
MODEL = "databricks-meta-llama-3-3-70b-instruct"

# COMMAND ----------

# DBTITLE 1,Proof that the model forgets
# Two SEPARATE calls - nothing connects them
r1 = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": "Hi, my name is Sam."}])
print("Call 1:", r1.choices[0].message.content)

r2 = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": "What is my name?"}])
print("Call 2:", r2.choices[0].message.content)

# COMMAND ----------

# DBTITLE 1,Explain memory
# MAGIC %md
# MAGIC ## The fix: keep a list and keep appending
# MAGIC We store every message (ours **and** the model's) in a Python list, and send the full list each time.
# MAGIC This list is the agent's **short-term memory**.

# COMMAND ----------

# DBTITLE 1,Chat class with memory
class Chat:
    def __init__(self, system_prompt="You are a friendly, concise assistant."):
        self.messages = [{"role": "system", "content": system_prompt}]

    def send(self, text):
        self.messages.append({"role": "user", "content": text})          # 1. remember what the user said
        response = client.chat.completions.create(model=MODEL, messages=self.messages)
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})    # 2. remember what the model said
        return reply

chat = Chat()
print("Turn 1:", chat.send("Hi, my name is Sam and I love Python."))
print("Turn 2:", chat.send("Suggest one fun beginner project."))
print("Turn 3:", chat.send("What is my name and what language do I like?"))

# COMMAND ----------

# DBTITLE 1,Look inside the memory
# This list is exactly what the model saw on turn 3
for i, m in enumerate(chat.messages):
    print(f"{i}. [{m['role']}] {m['content'][:80]}")

# COMMAND ----------

# DBTITLE 1,Exercises
# MAGIC %md
# MAGIC ## Exercises
# MAGIC 1. Delete message index 1 from `chat.messages` and ask the name again. What happens?
# MAGIC 2. Memory costs money: every turn resends the history. Add a `max_history` limit that keeps the system prompt + last N messages.
# MAGIC 3. **Think:** what would happen to a very long conversation if we never trimmed it?
# MAGIC
# MAGIC **Key takeaway:** memory is just a list you manage in Python. The model has none of its own.
# MAGIC
# MAGIC Next: **Step 3 - Structured Output**

# COMMAND ----------


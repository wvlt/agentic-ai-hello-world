# Databricks notebook source
# DBTITLE 1,Intro
# MAGIC %md
# MAGIC # Step 4 - Your First Tool (by hand)
# MAGIC
# MAGIC **Big idea:** the model **never runs your code**. It only *asks* you to run a tool, by returning a `tool_call`.
# MAGIC You run the Python function, send the result back, and the model writes the final answer.
# MAGIC
# MAGIC ```
# MAGIC user question -> model: "please call add(a=1234, b=5678)" -> YOU run add() -> result 6912 -> model: "The answer is 6912"
# MAGIC ```
# MAGIC
# MAGIC **Done when:** you can trace all 4 messages (user, tool_call, tool result, answer) and say who produced each one.

# COMMAND ----------

# DBTITLE 1,Setup
import json
from databricks.sdk import WorkspaceClient

client = WorkspaceClient().serving_endpoints.get_open_ai_client()
MODEL = "databricks-meta-llama-3-3-70b-instruct"

# COMMAND ----------

# DBTITLE 1,1 - A normal Python function
# 1. A completely normal Python function. Nothing AI about it.
def get_weather(city: str) -> str:
    fake_weather = {"perth": "sunny, 31C", "london": "rainy, 12C", "tokyo": "cloudy, 18C"}
    return fake_weather.get(city.lower(), "unknown city")

print(get_weather("Perth"))

# COMMAND ----------

# DBTITLE 1,2 - Describe the tool to the model
# 2. Describe the function to the model: name, what it does, what arguments it takes.
#    The model only sees this description - never your code.
weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "City name, e.g. Perth"}},
            "required": ["city"],
        },
    },
}

# COMMAND ----------

# DBTITLE 1,3 - The model asks for the tool
# 3. Ask a question and offer the tool
messages = [{"role": "user", "content": "Should I bring an umbrella in London today?"}]

response = client.chat.completions.create(model=MODEL, messages=messages, tools=[weather_tool])
msg = response.choices[0].message

print("Text content :", msg.content)        # usually None - the model isn't answering yet!
print("Tool calls   :", msg.tool_calls)     # it is asking US to run a function
tool_call = msg.tool_calls[0]
print("\nModel wants  :", tool_call.function.name, "with", tool_call.function.arguments)

# COMMAND ----------

# DBTITLE 1,4 - We run the tool
# 4. WE run the function, using the arguments the model chose
args = json.loads(tool_call.function.arguments)   # arguments arrive as a JSON string
result = get_weather(**args)
print("We ran get_weather ->", result)

# COMMAND ----------

# DBTITLE 1,5 - Send the result back
# 5. Add the model's tool request AND our result to the history, then call the model again
messages.append(msg.model_dump(exclude_none=True))       # the assistant's tool_call message
messages.append({
    "role": "tool",
    "tool_call_id": tool_call.id,    # links our result to the request
    "content": result,
})

final = client.chat.completions.create(model=MODEL, messages=messages, tools=[weather_tool])
print("Final answer:", final.choices[0].message.content)

# COMMAND ----------

# DBTITLE 1,Trace the conversation
# Who said what? This is the whole tool-calling dance.
messages.append({"role": "assistant", "content": final.choices[0].message.content})
for i, m in enumerate(messages, 1):
    detail = m.get("content") or f"tool_calls={[tc['function']['name'] for tc in m['tool_calls']]}"
    print(f"{i}. [{m['role']:9}] {str(detail)[:90]}")

# COMMAND ----------

# DBTITLE 1,Three golden rules of tool messages
# MAGIC %md
# MAGIC ## The three golden rules of tool messages
# MAGIC 1. **Never skip the assistant message.** A `tool` message must come *after* the `assistant` message whose `tool_calls` requested it.
# MAGIC 2. **Match the `tool_call_id`.** Every `tool` message must carry the exact `id` of the tool call it answers - that's how the model links question and answer (essential when it calls several tools at once).
# MAGIC 3. **`content` must be a string.** If your function returns a dict or list, convert it with `json.dumps()`.
# MAGIC
# MAGIC **Surprise:** different models enforce these rules differently. In our tests Llama quietly *ignored* rule 1 and 2 violations, while Claude rejected them with an error. Code that "works" on a lenient model can break the moment you swap models - so always follow the strictest rules.
# MAGIC
# MAGIC Run the next cell to break each rule on purpose and see what happens.

# COMMAND ----------

# DBTITLE 1,Break the rules on purpose
# Rebuild a fresh tool request so we can tamper with it
base = [{"role": "user", "content": "Should I bring an umbrella in London today?"}]
req = client.chat.completions.create(model=MODEL, messages=base, tools=[weather_tool]).choices[0].message
call = req.tool_calls[0]
assistant_msg = req.model_dump(exclude_none=True)

experiments = {
    "Correct (all rules followed)": base + [assistant_msg, {"role": "tool", "tool_call_id": call.id, "content": "rainy, 12C"}],
    "Rule 1 broken: no assistant msg": base + [{"role": "tool", "tool_call_id": call.id, "content": "rainy, 12C"}],
    "Rule 2 broken: wrong id": base + [assistant_msg, {"role": "tool", "tool_call_id": "call_wrong", "content": "rainy, 12C"}],
    "Rule 3 broken: dict content": base + [assistant_msg, {"role": "tool", "tool_call_id": call.id, "content": {"temp": 12}}],
    "Rule 3 fixed: json.dumps": base + [assistant_msg, {"role": "tool", "tool_call_id": call.id, "content": json.dumps({"temp": 12, "sky": "rainy"})}],
}

for model in [MODEL, "databricks-claude-haiku-4-5"]:
    print(f"\n=== {model} ===")
    for name, msgs in experiments.items():
        try:
            r = client.chat.completions.create(model=model, messages=msgs, tools=[weather_tool])
            print(f"  OK    {name:34} -> {str(r.choices[0].message.content)[:50]}")
        except Exception as e:
            print(f"  ERROR {name:34} -> {str(e)[:70]}")

# COMMAND ----------

# DBTITLE 1,Exercises
# MAGIC %md
# MAGIC ## Exercises
# MAGIC 1. Ask "What's the capital of France?" with the tool attached. Does the model call it? Why not?
# MAGIC 2. Change the tool `description` to something vague ("does stuff"). Does the model still use it correctly?
# MAGIC 3. Ask about **two** cities in one question. How many `tool_calls` come back?
# MAGIC
# MAGIC **Key takeaway:** tool calling = structured output (Step 3) where the structure is "which function + which arguments".
# MAGIC You did one round by hand. In Step 5 we automate it with a loop - and that loop **is** the agent.
# MAGIC
# MAGIC Next: **Step 5 - The Agent Loop**

# COMMAND ----------


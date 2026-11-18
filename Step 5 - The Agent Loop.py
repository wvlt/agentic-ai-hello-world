# Databricks notebook source
# DBTITLE 1,Intro
# MAGIC %md
# MAGIC # Step 5 - The Agent Loop (Hello World of Agentic AI)
# MAGIC
# MAGIC **Big idea:** take Step 4 and put it in a `while` loop:
# MAGIC
# MAGIC ```
# MAGIC while True:
# MAGIC     ask the model
# MAGIC     if it wants tools -> run them, add results to memory, loop again
# MAGIC     else              -> it's done, return its answer
# MAGIC ```
# MAGIC
# MAGIC That's it. That's an agent. Frameworks (LangGraph, OpenAI Agents SDK, ...) are this loop with extra features.
# MAGIC
# MAGIC **Done when:** your ~40-line agent chains multiple tools to answer one question.

# COMMAND ----------

# DBTITLE 1,Setup
import json
from datetime import date
from databricks.sdk import WorkspaceClient

client = WorkspaceClient().serving_endpoints.get_open_ai_client()
MODEL = "databricks-meta-llama-3-3-70b-instruct"

# COMMAND ----------

# DBTITLE 1,Define the tools (plain Python)
# --- Tools: ordinary Python functions ---
ORDERS = {42: {"customer": "Alice", "total": 250.0}, 7: {"customer": "Bob", "total": 80.0}}

def get_order_total(customer_id: int):
    order = ORDERS.get(int(customer_id))
    return order["total"] if order else "customer not found"

def calculator(expression: str):
    # Safety: only allow digits and arithmetic symbols, never arbitrary code
    if not set(expression) <= set("0123456789+-*/(). "):
        return "error: only basic arithmetic is allowed"
    return eval(expression, {"__builtins__": {}})

def get_today():
    return date.today().isoformat()

# Name -> function lookup, so the loop can run whatever the model asks for
TOOLS = {"get_order_total": get_order_total, "calculator": calculator, "get_today": get_today}

# COMMAND ----------

# DBTITLE 1,Describe the tools to the model
def tool_spec(name, description, properties=None, required=None):
    """Small helper so tool descriptions are less verbose."""
    return {"type": "function", "function": {
        "name": name, "description": description,
        "parameters": {"type": "object", "properties": properties or {}, "required": required or []}}}

TOOL_SPECS = [
    tool_spec("get_order_total", "Look up the order total in dollars for a customer id.",
              {"customer_id": {"type": "integer"}}, ["customer_id"]),
    tool_spec("calculator", "Evaluate a basic arithmetic expression, e.g. '250 * 0.15'.",
              {"expression": {"type": "string"}}, ["expression"]),
    tool_spec("get_today", "Get today's date in ISO format."),
]

# COMMAND ----------

# DBTITLE 1,The agent loop
def run_agent(question, max_steps=5, verbose=True):
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use the tools when you need facts or maths."},
        {"role": "user", "content": question},
    ]
    for step in range(1, max_steps + 1):                       # safety: never loop forever
        response = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOL_SPECS)
        msg = response.choices[0].message

        if not msg.tool_calls:                                 # no tools requested -> final answer
            return msg.content

        messages.append(msg.model_dump(exclude_none=True))     # rule 1: save the assistant's request first
        for tc in msg.tool_calls:                              # run every requested tool
            args = json.loads(tc.function.arguments or "{}")
            func = TOOLS.get(tc.function.name)
            result = func(**args) if func else f"error: unknown tool {tc.function.name}"
            if verbose:
                print(f"  step {step}: {tc.function.name}({args}) -> {result}")
            content = result if isinstance(result, str) else json.dumps(result)   # rule 3: content must be a string
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": content})  # rule 2: matching id

    return "Stopped: reached max_steps without a final answer."

# COMMAND ----------

# DBTITLE 1,Run the agent
# Predict first: which tools, in what order?
print(run_agent("What's 15% of the order total for customer 42?"))

# COMMAND ----------

# DBTITLE 1,More questions
questions = [
    "What is today's date?",
    "How much more did customer 42 spend than customer 7?",
    "What is the order total for customer 999?",   # tool returns 'not found' - how does the agent cope?
    "Tell me a fun fact about Python.",            # no tool needed
]
for q in questions:
    print("Q:", q)
    print("A:", run_agent(q), "\n")

# COMMAND ----------

# DBTITLE 1,Design choices in our loop
# MAGIC %md
# MAGIC ## Design choices: why our loop looks the way it does
# MAGIC Many tutorials write the loop as `while True:` and check `if finish_reason == "tool_calls"`. Ours makes a few deliberate changes:
# MAGIC
# MAGIC | Tutorial style | Our style | Why |
# MAGIC | --- | --- | --- |
# MAGIC | `while True:` | `for step in range(max_steps):` | A confused model can request tools forever. A step limit is your **guardrail** against infinite loops (and runaway cost). |
# MAGIC | `if finish_reason == "tool_calls"` | `if not msg.tool_calls` | Checks what the model *actually returned*. Also, a reply cut off with `finish_reason == "length"` would wrongly be treated as a final answer in the tutorial version. |
# MAGIC | `result = get_weather(city=args["city"])` | `TOOLS[tc.function.name](**args)` | **Multi-tool routing**: look up whichever function the model picked by name, instead of hard-coding one. |
# MAGIC | `"content": result` | `json.dumps(result)` if not a string | Golden rule 3 from Step 4. |
# MAGIC
# MAGIC Everything else - append the assistant message, run each tool, append `tool` messages with matching ids, call again - is identical. Same loop, a bit safer.

# COMMAND ----------

# DBTITLE 1,Exercises
# MAGIC %md
# MAGIC ## Exercises
# MAGIC 1. Add a new tool `apply_discount(total, percent)` and ask a question that needs it.
# MAGIC 2. Set `max_steps=1` and rerun the first question. What happens and why?
# MAGIC 3. Make a tool raise an exception. Wrap the tool call in `try/except` and send the error text back to the model - watch it recover.
# MAGIC 4. Count how many LLM calls one question cost. (Hint: one per loop iteration.)
# MAGIC 5. Make a tool return a dict, e.g. `{"customer": "Alice", "total": 250.0}`. Confirm the `json.dumps` line handles it.
# MAGIC 6. Rewrite the loop in the tutorial style (`while True` + `finish_reason`). Then call it with `max_tokens=5`. What goes wrong?
# MAGIC
# MAGIC **Key takeaway:** you just wrote an agent from scratch: **LLM + tools + loop + memory**.
# MAGIC
# MAGIC Next: **Step 6 - Tracing with MLflow** (seeing inside the agent's head).

# COMMAND ----------


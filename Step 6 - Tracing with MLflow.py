# Databricks notebook source
# DBTITLE 1,Intro
# MAGIC %md
# MAGIC # Step 6 - Seeing Inside with MLflow Tracing
# MAGIC
# MAGIC **Big idea:** agents make many hidden decisions. **Tracing** records every LLM call and tool call (inputs, outputs, timing) so you can debug them.
# MAGIC
# MAGIC **Done when:** you can open a trace and point to where the agent made each decision.

# COMMAND ----------

# DBTITLE 1,Setup and turn on tracing
import json
import mlflow
from databricks.sdk import WorkspaceClient

client = WorkspaceClient().serving_endpoints.get_open_ai_client()
MODEL = "databricks-meta-llama-3-3-70b-instruct"

# One line: automatically trace every OpenAI-client call
mlflow.openai.autolog()

# COMMAND ----------

# DBTITLE 1,Tools, decorated for tracing
# Same tools as Step 5. @mlflow.trace makes each tool call show up as a span in the trace.
ORDERS = {42: {"customer": "Alice", "total": 250.0}, 7: {"customer": "Bob", "total": 80.0}}

@mlflow.trace(span_type="TOOL")
def get_order_total(customer_id: int):
    order = ORDERS.get(int(customer_id))
    return order["total"] if order else "customer not found"

@mlflow.trace(span_type="TOOL")
def calculator(expression: str):
    if not set(expression) <= set("0123456789+-*/(). "):
        return "error: only basic arithmetic is allowed"
    return eval(expression, {"__builtins__": {}})

TOOLS = {"get_order_total": get_order_total, "calculator": calculator}

def tool_spec(name, description, properties=None, required=None):
    return {"type": "function", "function": {
        "name": name, "description": description,
        "parameters": {"type": "object", "properties": properties or {}, "required": required or []}}}

TOOL_SPECS = [
    tool_spec("get_order_total", "Look up the order total in dollars for a customer id.",
              {"customer_id": {"type": "integer"}}, ["customer_id"]),
    tool_spec("calculator", "Evaluate a basic arithmetic expression, e.g. '250 * 0.15'.",
              {"expression": {"type": "string"}}, ["expression"]),
]

# COMMAND ----------

# DBTITLE 1,Traced agent loop
# The whole agent run becomes one parent span (type AGENT) containing LLM + TOOL child spans
@mlflow.trace(span_type="AGENT")
def run_agent(question, max_steps=5):
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use the tools when you need facts or maths."},
        {"role": "user", "content": question},
    ]
    for _ in range(max_steps):
        msg = client.chat.completions.create(model=MODEL, messages=messages, tools=TOOL_SPECS).choices[0].message
        if not msg.tool_calls:
            return msg.content
        messages.append(msg.model_dump(exclude_none=True))
        for tc in msg.tool_calls:
            func = TOOLS.get(tc.function.name)
            args = json.loads(tc.function.arguments or "{}")
            result = func(**args) if func else f"error: unknown tool {tc.function.name}"
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})
    return "Stopped: reached max_steps."

# Run it - a trace viewer appears under the cell output. Click through the spans!
run_agent("What's 15% of the order total for customer 42?")

# COMMAND ----------

# DBTITLE 1,Read the trace in code
# Traces are data too - you can inspect them programmatically
trace = mlflow.get_trace(mlflow.get_last_active_trace_id())
for span in trace.data.spans:
    print(f"{span.span_type:10} {span.name:25} {(span.end_time_ns - span.start_time_ns)/1e9:.2f}s")

# COMMAND ----------

# DBTITLE 1,Exercises and what's next
# MAGIC %md
# MAGIC ## Exercises
# MAGIC 1. In the trace viewer, click the first LLM span. Find the exact `tool_calls` the model produced.
# MAGIC 2. Which step took the longest: LLM calls or tool calls?
# MAGIC 3. Break a tool on purpose (e.g. return the wrong number). Use the trace to find where the answer went wrong.
# MAGIC
# MAGIC **Key takeaway:** you can't improve what you can't see. Always trace agents.
# MAGIC
# MAGIC ## Where to go next
# MAGIC * **Step 7 - Real data:** swap fake tools for SQL over Unity Catalog tables or UC functions as tools (read-only first!).
# MAGIC * **Step 8 - Production:** rebuild with a framework (LangGraph / OpenAI Agents SDK), evaluate with MLflow, deploy with Mosaic AI Agent Framework.

# COMMAND ----------


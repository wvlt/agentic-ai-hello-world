# Databricks notebook source
# DBTITLE 1,Intro
# MAGIC %md
# MAGIC # Step 3 - Structured Output
# MAGIC
# MAGIC **Big idea:** agents are code. Code can't easily read free-form prose, but it *can* read **JSON**.
# MAGIC Before a model can drive tools, we need it to answer in a format Python can parse.
# MAGIC
# MAGIC **Done when:** you reliably get a Python `dict` back, e.g. `{"sentiment": "positive", "confidence": 0.9}`.

# COMMAND ----------

# DBTITLE 1,Setup
import json
from databricks.sdk import WorkspaceClient

client = WorkspaceClient().serving_endpoints.get_open_ai_client()
MODEL = "databricks-meta-llama-3-3-70b-instruct"

# COMMAND ----------

# DBTITLE 1,Approach 1 - just ask for JSON
# Approach 1: politely ask for JSON in the prompt
prompt = (
    "Classify the sentiment of this review: 'The battery died after one day.'\n"
    'Reply ONLY with JSON like {"sentiment": "positive|negative|neutral", "confidence": 0.0-1.0}'
)
raw = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": prompt}], temperature=0)
text = raw.choices[0].message.content
print("Raw text:", text)

try:
    data = json.loads(text)
    print("Parsed dict:", data, "| sentiment =", data["sentiment"])
except json.JSONDecodeError:
    print("Could not parse! The model added extra text. This is why Approach 2 exists.")

# COMMAND ----------

# DBTITLE 1,Why approach 1 is fragile
# MAGIC %md
# MAGIC ## Why Approach 1 is fragile
# MAGIC Sometimes the model wraps JSON in ` ```json ` fences or adds "Sure! Here you go:". Your `json.loads` then crashes.
# MAGIC
# MAGIC ## Approach 2: a JSON schema (recommended)
# MAGIC We pass `response_format` with a **schema**. The model is *constrained* to output JSON that matches it.

# COMMAND ----------

# DBTITLE 1,Approach 2 - JSON schema
sentiment_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "sentiment",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "sentiment": {"type": "string", "enum": ["positive", "negative", "neutral"]},
                "confidence": {"type": "number"},
            },
            "required": ["sentiment", "confidence"],
        },
    },
}

def classify(review):
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": f"Classify the sentiment of this review: {review}"}],
        response_format=sentiment_schema,
        temperature=0,
    )
    return json.loads(r.choices[0].message.content)

for review in ["I love it!", "Broke on day one.", "It arrived on Tuesday."]:
    result = classify(review)
    print(f"{review:25} -> {result}  (type: {type(result).__name__})")

# COMMAND ----------

# DBTITLE 1,Using the dict in code
# Now the model's answer can drive normal Python logic
result = classify("Terrible support, I want a refund.")
if result["sentiment"] == "negative" and result["confidence"] > 0.7:
    print("Escalating to a human support agent!")
else:
    print("No action needed.")

# COMMAND ----------

# DBTITLE 1,Exercises
# MAGIC %md
# MAGIC ## Exercises
# MAGIC 1. Add a `"topic"` field (enum: `battery`, `delivery`, `price`, `other`) to the schema.
# MAGIC 2. Build an "intent detector": given `"Book me a table for 2 at 7pm"`, return `{"intent": ..., "people": ..., "time": ...}`.
# MAGIC 3. **Think:** exercise 2 is basically the model *deciding which action to take*. That's what tool calling is - see Step 4.
# MAGIC
# MAGIC **Key takeaway:** structured output turns an LLM from a chatbot into a component your code can trust.
# MAGIC
# MAGIC Next: **Step 4 - Your First Tool**

# COMMAND ----------


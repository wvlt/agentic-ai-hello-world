# Agentic AI Hello World

A beginner-friendly, step-by-step course on building AI agents from scratch in plain Python, using Databricks notebooks and Databricks-hosted models.

**Audience:** anyone comfortable with Python who has never built anything with an LLM.

**Approach:** one new idea per step, no frameworks until the very end. By Step 5 you will have written a working agent in about 40 lines of Python, so you understand exactly what agent frameworks do under the hood.

## Curriculum

| Step | Notebook | New idea | Done when |
| --- | --- | --- | --- |
| 0 | (intro in Step 1) | What is an agent? LLM = brain, tools = hands, loop = persistence, memory = notebook | You can explain chatbot vs agent in one sentence |
| 1 | Step 1 - Hello LLM | First model call, the four message roles, `choices`, `finish_reason`, temperature | You get a reply and can explain each role |
| 2 | Step 2 - Conversation and Memory | LLMs are stateless; memory is a list you manage | The model remembers your name on turn 3 |
| 3 | Step 3 - Structured Output | JSON and JSON-schema responses | You reliably get a Python dict back |
| 4 | Step 4 - Your First Tool | Tool calling by hand, the three golden rules of tool messages | You can trace user -> tool_call -> tool result -> answer |
| 5 | Step 5 - The Agent Loop | The agent loop: LLM + tools + loop + memory, with a step limit | Your agent chains multiple tools to answer one question |
| 6 | Step 6 - Tracing with MLflow | Seeing inside the agent with MLflow tracing | You can point to each decision in a trace |

Coming next: **Step 7** (tools over real Unity Catalog data) and **Step 8** (frameworks, evaluation and deployment with Mosaic AI Agent Framework).

## Requirements

* A Databricks workspace with Foundation Model APIs (the notebooks use `databricks-meta-llama-3-3-70b-instruct`; swap the `MODEL` variable to try others).
* Serverless or a cluster with `openai`, `mlflow` and `databricks-sdk` available (included in recent Databricks runtimes).
* No external API keys: the OpenAI-compatible client is authenticated with your Databricks login and sends requests to your workspace, not to OpenAI.

## How to use

1. Clone this repo into your workspace as a Git folder.
2. Work through the notebooks in order, running each cell.
3. Before running a cell, predict what the model will do. Then check.
4. Finish the exercises at the end of each notebook before moving on.

## Video series (new)

A beginner video series - 13 short videos, one idea each - lives in [`videos/`](videos/README.md). Each video has its own folder with the notebook, solutions, script, SVG diagrams, a "you are here" map, exercises, quiz and cheatsheet.

* Start here: [videos/README.md](videos/README.md)
* The full plan and topic coverage: [videos/course-map.md](videos/course-map.md)
* Video 01: [What is an AI agent? + your first LLM call](videos/01-what-is-an-agent/README.md)

The Step 1-6 notebooks above remain as the compact reference version of the course.

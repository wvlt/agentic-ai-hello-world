# Glossary

Every term used in the series, in plain English, and the video that introduces it. New terms are added as each video is released.

| Term | Plain-English meaning | Video |
| --- | --- | --- |
| **LLM** (Large Language Model) | A program that takes text in and predicts text out. On its own it cannot browse, run code or remember anything. | 01 |
| **Prompt** | The text you send to an LLM. | 01 |
| **Model** | A specific trained LLM, e.g. Llama 3.3 70B or Claude Haiku. Different models differ in quality, speed and cost. | 01 |
| **Serving endpoint** | A named URL in your Databricks workspace that hosts a model, e.g. `databricks-meta-llama-3-3-70b-instruct`. | 01 |
| **OpenAI-compatible API** | A common *format* for talking to LLMs, made popular by OpenAI. Many providers, including Databricks, accept it. Using it does **not** mean you are using OpenAI. | 01 |
| **Client** | The Python object that sends your request to the endpoint and gives you the reply. | 01 |
| **Token** | A chunk of text (roughly 3/4 of a word) that models read and write. You pay per token. | 01 (cost meter), 03 |
| **Hallucination** | When a model states something false with confidence. | 01 |
| **Chatbot** | An LLM that answers one message at a time. It talks but cannot act. | 01 |
| **AI agent** | An LLM in a loop that can decide on actions, use tools, see the results and keep going until a goal is reached. | 01 |
| **Tool** | A normal function (e.g. look up an order, run a query) the agent may ask your code to run. | 01 (concept), 06 |
| **Agent loop** | The repeat cycle: think, act, observe, until done. | 01 (concept), 08 |

## Coming in later videos
`message`, `role`, `system prompt` (02) | `choices`, `finish_reason`, `temperature` (03) | `context window`, `memory` (04) | `structured output`, `JSON schema` (05) | `tool call`, `tool_call_id` (06-07) | `termination`, `guardrail` (08-09) | `trace`, `span` (10) | `retrieval` (11) | `evaluation`, `judge` (12)

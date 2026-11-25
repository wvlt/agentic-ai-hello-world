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
| **Message** | A Python dict with a `role` and `content`. A conversation is a list of messages, oldest first. | 02 |
| **Role** | Who is speaking in a message: `system`, `user`, `assistant` (and `tool`, Video 06). | 02 |
| **System prompt** | The `system` message written by the developer: rules, personality, goals. Sent with every call. | 02 |
| **developer role** | Newer OpenAI name for the `system` role. Databricks endpoints accept both. | 02 |
| **Few-shot prompting** | Teaching a format by including example `user`/`assistant` pairs that you write yourself. | 02 |
| **Prompt injection** | A user (or text) trying to override your instructions, e.g. "ignore all previous instructions". | 02, 09 |
| **Response** | Everything the model sends back: `choices`, `usage` and metadata (`id`, `model`, `created`). | 03 |
| **choices** | A list of answers in the response - usually one, at `choices[0]`. `n` asks for more (not every model supports it). | 03 |
| **finish_reason** | Why the model stopped: `stop` (done), `length` (cut off by `max_tokens`), `tool_calls` (wants a tool). | 03 |
| **usage** | Token counts for a call: `prompt_tokens` (input), `completion_tokens` (output), `total_tokens`. | 03 |
| **max_tokens** | A cap on output tokens. Limits answer length and cost; too low cuts answers off. | 03 |
| **Temperature** | How much randomness in word choice. Low (0) = predictable, high (1.5) = varied. | 03 |
| **Stateless** | Keeping nothing between calls. LLMs are stateless: each call starts from zero. | 04 |
| **Memory (short-term)** | The message list your code keeps and resends every call. The model only "remembers" what is in it. | 04 |
| **Context window** | The maximum number of tokens a model accepts in one call. Exceed it and the call fails. | 04 |
| **Trimming** | Sending only the last N messages to save tokens. Can silently drop important facts. | 04 |
| **Pinning** | Keeping key facts in the system prompt so they survive trimming. | 04 |
| **Context engineering** | Deciding what goes into the message list (and what stays out) so the model has what it needs. | 04, 07 |
| **JSON** | A text format of keys and values, like a Python dict. `json.loads` turns it into a `dict`. | 05 |
| **Structured output** | A model answer in a fixed, machine-readable shape (usually JSON) instead of free text. | 05 |
| **JSON schema** | A description of the exact fields, types and allowed values an answer must have. | 05 |
| **response_format** | The API parameter that passes a JSON schema to the model, constraining its answer. | 05 |
| **Code fence** | Markdown's ```` ``` ```` wrapper around code. Some models add it around JSON, which breaks `json.loads`. | 05 |
| **enum** | A schema rule that a value must be one of a fixed list, e.g. positive / negative / neutral. | 05 |

## Coming in later videos
`tool call`, `tool_call_id` (06-07) | `termination`, `guardrail` (08-09) | `trace`, `span` (10) | `retrieval` (11) | `evaluation`, `judge` (12)

# Video 01 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/01-hello-llm`, below the last cell. Every exercise starts with **predict first**: write your guess down *before* running the code. Being wrong is how you learn what models really do.

Solutions: `notebooks/01-hello-llm-solutions` (try first!).

---

## Exercise 1 - Explain it like I'm 10 (3 min)
Ask the model: *"Explain what an AI agent is to a 10-year-old, in 2 sentences."*

**Predict first:** Will it use an analogy? Will it stick to 2 sentences?

**Then:** run it 3 times. Is the answer the same each time? (Why that happens is in Video 03.)

## Exercise 2 - Make it reusable (5 min)
Write a Python function:

```python
def ask(question: str, model: str = MODEL) -> str:
    ...
```

It should send `question` to `model` and **return** the reply text (not print it). Use it to ask 3 different questions in a loop.

**Why:** from Video 02 onwards you'll wrap every LLM call in a small function like this.

## Exercise 3 - Model taste test (5 min)
Ask the same question to three models:
* `databricks-meta-llama-3-3-70b-instruct`
* `databricks-claude-haiku-4-5`
* `databricks-meta-llama-3-1-8b-instruct` (a much smaller model)

For each, print the answer, the total tokens (`response.usage.total_tokens`) and how long it took (use `time.time()`).

**Predict first:** which will be fastest? Which will give the best answer?

**Then answer:** which would you choose for a quick, cheap task, and which for a hard one?

*If a model is not available in your workspace, pick any other chat model listed under **Serving**.*

## Bonus - Find the limits (2 min)
Ask the model 3 things it **cannot** know, for example:
* "What is my name?"
* "What's the weather in Perth right now?"
* "How many files are in my Databricks home folder?"

Write down what it does: does it guess, refuse, or hallucinate? Each one is a job for a **tool** - keep the list, you'll fix them later in the series.

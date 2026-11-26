# Video 09 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/09-safe-agents`, below the last cell. **Predict first** every time.

Solutions: `notebooks/09-safe-agents-solutions` (try first!).

---

## Exercise 1 - Time budget (4 min)
Add `max_seconds` to `run_safe_agent`. If wall-clock time exceeds it, stop with a clear message.

**Predict first:** with `max_seconds=0.01`, does the agent finish the 15% question or stop early?

## Exercise 2 - Validate calculator input (4 min)
Before calling `calculator`, reject expressions longer than 40 characters or containing letters. Return an error string as the tool result.

**Predict first:** if the model sends `os.system("ls")`, what does the agent do?

## Exercise 3 - Soft retry once on truncation (4 min)
When `finish_reason == "length"`, retry the same step once with a higher `max_tokens` (e.g. 256 → 512). If still truncated, stop.

**Predict first:** does the retry usually recover a short answer?

## Bonus - Human approval stub (3 min)
Add a write tool `cancel_order(order_id)`. In the loop, if that tool is requested and `allow_writes` is False, return `"error: write requires approval"` as the tool result (do not run it).

**Then think:** when would you set `allow_writes=True` in a real product?

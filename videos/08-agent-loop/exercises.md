# Video 08 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/08-agent-loop`, below the last cell. **Predict first** every time.

Solutions: `notebooks/08-agent-loop-solutions` (try first!).

---

## Exercise 1 - A new tool (5 min)
Add `apply_discount(total, percent)` that returns `total * (1 - percent / 100)`. Describe it, put it in `TOOLS` and `TOOL_SPECS`, and ask:

> "What's customer 42's order total after a 20% discount?"

**Predict first:** which tools will run, and in what order?

## Exercise 2 - max_steps too low (3 min)
Call `run_agent(..., max_steps=1)` on the 15% question.

**Predict first:** what does the function return, and why?

**Then think:** what would happen with `while True:` and no step limit if the model kept requesting tools?

## Exercise 3 - Count the calls (3 min)
Change `run_agent` to return `(answer, n_calls)` - how many model calls that question used.

**Predict first:** for "What is today's date?", how many calls? For the 15% question?

## Bonus - Errors as results (4 min)
Make `get_order_total` raise `ValueError("unknown customer")` for missing ids. Wrap the tool call in `try/except` and send the error text back as the tool result.

Ask about customer 999.

**Predict first:** does the agent crash, or answer politely?

*(Video 09 builds on this pattern - errors as results, not exceptions that kill the loop.)*

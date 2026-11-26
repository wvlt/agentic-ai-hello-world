# Video 07 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/07-tool-rules`, below the last cell. **Predict first** every time.

Solutions: `notebooks/07-tool-rules-solutions` (try first!).

---

## Exercise 1 - A rule checker (5 min)
Write `check_tool_messages(messages)` that returns a list of rule violations in a message list:
* a `tool` message whose `tool_call_id` doesn't match any earlier request (rules 1 and 2),
* a `tool` message whose `content` isn't a string (rule 3),
* a request whose call ids are never answered (rule 4).

Test it on a correct list and on each broken list from the notebook.

**Why:** a checker like this catches bugs *before* a strict model does.

## Exercise 2 - Two ways to answer "which customer spent most?" (5 min)
Add a tool `get_top_customers(month, n)` that returns only the top `n` customers and their totals for a month.

**Predict first:** how many input tokens will the second call use, compared with `get_all_orders`?

**Then:** check the answer against a pandas calculation.

## Exercise 3 - Trim a tool result (3 min)
Keep `get_all_orders`, but make it return only `order_id`, `customer_id`, `date`, `status` and `total` (drop the address and notes).

**Predict first:** how much do the input tokens drop? Does Llama's answer improve?

## Bonus - Errors as results (2 min)
Make `get_order_total` return `{"error": "unknown customer"}` for an unknown id, and ask about customer 12345.

**Then think:** why is returning the error *as a string result* better than letting Python crash? (Video 09 builds on this.)

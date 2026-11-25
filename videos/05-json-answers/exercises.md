# Video 05 - Exercises (about 15 minutes)

Do these in your copy of `notebooks/05-json-answers`, below the last cell. **Predict first** every time.

Solutions: `notebooks/05-json-answers-solutions` (try first!).

---

## Exercise 1 - Add a field (3 min)
Add a `"topic"` field to the sentiment schema, limited to `battery`, `delivery`, `price`, `support` or `other` (use `enum`). Classify 4 reviews of your choice.

**Predict first:** what topic will *"Arrived late and the box was crushed"* get?

## Exercise 2 - Intent detector (5 min)
Build a schema that turns a request into an action:
* `intent`: one of `book_table`, `cancel_booking`, `ask_question`
* `people`: integer or null
* `time`: string or null

Test with: *"Book me a table for 2 at 7pm"*, *"Cancel my booking please"*, *"Do you have vegan options?"*.

**Then notice:** this is the model *choosing an action and its arguments*. That's exactly what tool calling is (Video 06).

## Exercise 3 - Break the schema on purpose (4 min)
Ask the model to classify a review, but give it a schema where `confidence` must be an **integer from 0 to 100** instead of a decimal. Check the type of the value you get back.

**Then:** write a `check_sentiment(d)` function that returns a list of problems (wrong type, out of range, unexpected label). Run it on every result.

## Bonus - Make clean() smarter (3 min)
Extend `clean()` so it also treats `"N/A"`, `"none"`, `"unknown"` (any capitalisation) and strings of only spaces as missing.

**Then think:** why is it safer to treat a suspicious value as *missing* (and ask) than to use it?

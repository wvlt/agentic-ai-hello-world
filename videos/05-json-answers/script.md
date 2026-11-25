# Video 05 Script - Answers code can use: structured JSON output

**Format:** voice-over on screen recording | **Target length:** 10 minutes | **Notebook:** `notebooks/05-json-answers`

Conventions: **[SCREEN]** = what is on screen, **[DO]** = action to perform, plain text = narration.

---

## 0:00 - Hook (30 s)
**[SCREEN]** A model reply: *"The review is clearly negative - I'd say I'm about 90% sure."* Next to it, a Python `if` statement with question marks.

A person can read this answer in a second. Your code can't. Is it negative? How sure? Where's the number? Today we teach the model to answer in a format code can use - and that's the last step before we give it tools.

## 0:30 - You are here (15 s)
**[SCREEN]** `you-are-here.svg`

Video five - the last of the Foundations. After this, the model gets hands.

## 0:45 - People read text, code reads JSON (60 s)
**[SCREEN]** `diagrams/01-text-vs-json.svg`

An agent is code. It has to *decide* things based on what the model says: escalate this ticket or not, call this tool or not. Free text is great for people and terrible for `if` statements.

JSON is the fix. It's text, but it's text in a strict shape: keys and values - exactly like a Python dictionary. One line of code - `json.loads` - turns it into a dict.

## 1:45 - Way 1: ask nicely (2 min)
**[DO]** Run *Connect*, then *Free text*.

Here's the free-text answer. Nice for us, useless for code.

**[DO]** Run *Way 1 - ask nicely for JSON*.

Now we ask: "Reply ONLY with JSON like this." We try three models, and parse each reply with `json.loads`.

**[SCREEN]** `diagrams/02-three-ways-to-get-json.svg` - card 1

Llama: works. But look at Claude. It wrapped the JSON in a markdown code fence - three backticks and the word json. To a person that looks helpful. To `json.loads` it's an error. In our tests that happened three times out of three.

That's the problem with asking nicely: it's a request, not a guarantee.

## 3:45 - Way 2: clean up (45 s)
**[DO]** Run *Way 2 - clean up the reply*.

We can patch it: strip the code fences, then parse. Now Claude's answer works too. Better - but we're guessing at every way the model might decorate its answer.

## 4:30 - Way 3: a JSON schema (2 min)
**[SCREEN]** Card 3
**[DO]** Run *Way 3 - JSON schema*.

The proper way: describe the exact shape you want - a **JSON schema** - and pass it as `response_format`. Here: a `sentiment` that must be one of positive, negative or neutral, and a `confidence` that must be a number. Both required, nothing else allowed.

The model is now *constrained* to that shape. Same three models - all clean JSON, no fences, every time.

**[DO]** Run *Use the answer in code*.

And now the payoff: a real `if` statement. Negative and confident? Escalate to a human. That's a model making a decision your code can act on.

## 6:30 - Extracting data from messy text (75 s)
**[DO]** Run *Extract bookings*.

The same trick pulls structured data out of messy messages. Three booking requests, written three different ways - out come name, number of people, date and time, as a table.

## 7:45 - Cost meter (30 s)
**[DO]** Run *Cost meter*.

Bonus: JSON is short. Same question, prose answer: about 76 output tokens. JSON answer: about 16. Nearly five times cheaper on output.

## 8:15 - What could go wrong? (60 s)
**[SCREEN]** `diagrams/03-valid-is-not-correct.svg`
**[DO]** Run *Valid is not correct*.

Look at the third booking: no time given. The schema says `time` must be filled in, so the model filled it in... with the *word* "null" in quotes. Claude writes "UNKNOWN" in angle brackets. Both are perfectly valid JSON. And both pass `if booking["time"]` - so your code thinks it has a time.

Allowing a real `null` in the schema helped Llama but not Claude. So the real fix is in **your code**:

**[DO]** Run *Clean the values*.

A tiny `clean()` function turns those placeholder strings into a real `None`, and then we know to ask the user for the time. Valid JSON is not the same as correct JSON. Always check the values.

## 9:15 - Recap and next (45 s)
**[SCREEN]** `you-are-here.svg`

Today: code needs JSON, not prose. Asking nicely is fragile; a JSON schema is reliable; and your code still checks the values.

Here's the secret for next time: when a model "calls a tool", it's doing exactly what you saw today - returning structured output. The structure is just: which function, and which arguments. Next video, we give the model hands.

# Day 3 — strings and lists

60 minutes. Coursera skim: **Python Data Structures**, Chapter 6 (Strings) and Chapter 8 (Lists).

## Strings

A Python string is close to `string` in C#. Both are immutable. `len(text)` is `text.Length`. `text.lower()` is `text.ToLower()`. `text.strip()` is `text.Trim()`. `text.split(" ")` is `text.Split(' ')`.

Indexes start at 0 in both languages. A slice takes a piece without a `Substring` call.

```python
email = "dev@contoso.com"
at = email.find("@")          # IndexOf
name = email[:at]             # Substring(0, at)
domain = email[at + 1 :]      # Substring(at + 1)
```

`email[:at]` means "from the start up to, but not including, `at`". `email[at + 1 :]` means "from the next character through the end".

## Lists

A list is `List<string>` with no separate class to construct.

```python
days = []
days.append("Mon")            # Add
days.append("Tue")
first = days[0]               # indexer
print(len(days))              # Count
```

`for day in days:` is `foreach (var day in days)`. `sorted(days)` returns a new sorted list and leaves `days` unchanged, like `OrderBy` into a new list rather than `Sort()` on the same list.

`"Mon Tue".split()` with no argument splits on any whitespace and drops empty pieces. That is the usual way to take the first word of a line: `line.split()[0]`.

## Practice

`exercise.py` has a log and an email address. Build a list of weekdays from the log, and take the mailbox name from the email. The samples above use different text, so you still write the loop yourself.

Expected printout:

```text
azeem
['Mon', 'Tue', 'Mon']
```

# Day 2 — functions, loops, and try/except

60 minutes. About 20 minutes on this page, about 35 minutes in `exercise.py`, 5 minutes in `notes.md`.

Coursera skim: **Programming for Everybody**, Module 6 (Functions) and Module 7 (Loops and Iteration). You already know methods, `foreach`, and `try/catch`. Watch for indentation and `except`.

## What changes from C#

A Python function is a method that is not inside a class.

```python
def double(n):
    return n * 2
```

The lines that belong to `double` are indented. There are no `{ }` braces. Four spaces is the usual indent.

`for` walks a collection the way `foreach` does. This loop adds numbers. It is a different problem from today's exercise.

```python
def total(numbers):
    running = 0
    for n in numbers:
        running = running + n
    return running
```

`try/except` is `try/catch`. `float("10")` is `double.Parse("10")`. Bad text raises `ValueError`.

```python
raw = "10"
try:
    hours = float(raw)
except ValueError:
    hours = 0
```

`return` hands a value back. Printing inside the function is optional, and today's function should return the pay so the loop can print it.

## Practice

Open `exercise.py`. The comments there describe overtime pay and a second `try` around `input()`. The snippets on this page are not the answer to that file.

Expected lines once TODO 1 is done, before you type extra hours:

```text
40 400
45 475
```

If extra hours is `abc`, the script prints `Enter a number for hours.`

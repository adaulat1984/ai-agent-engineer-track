# Day 4 — dictionaries

60 minutes. Coursera skim: **Python Data Structures**, Chapter 9 (Dictionaries).

A dictionary is `Dictionary<TKey, TValue>`. The usual agent pattern is a count: how many times each word, status, or tool name appears.

```python
counts = {}
word = "python"
counts[word] = counts.get(word, 0) + 1
```

`counts.get(word, 0)` is `TryGetValue`: if `word` is missing, use `0` instead of throwing. `counts[word]` alone raises `KeyError` when the key is missing, the same way a C# indexer throws when the key is absent.

Loop both sides with `items()`, which is like enumerating `KeyValuePair`.

```python
for word, count in counts.items():
    print(word, count)
```

`counts.keys()` is the keys. `counts.values()` is the values. `"python" in counts` is `ContainsKey`.

Build the count in a loop. Do not type the totals by hand. For a line `Mon 09:01 user1 login`, the key you want today is the first word, the same word you stored in a list yesterday.

## Practice

`exercise.py` uses a slightly longer log than Day 3. Count the weekdays.

Expected lines, in any order:

```text
Mon 2
Tue 1
Wed 1
```

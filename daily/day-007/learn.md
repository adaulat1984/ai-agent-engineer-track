# Day 7 — checkpoint

60 minutes. No new Coursera module. This repeats files and dictionaries on a new text, which is the combination you will use when an agent reads a document and counts what is in it.

## Shape of the script

1. Take a block of text that lives in the program.
2. Write it to `notes.txt`.
3. Read `notes.txt` back, so the counts come from the file and not from the constant by accident.
4. Split each line into words. Lowercase each word before counting, so `Python` and `python` are the same key.
5. Track the word with the largest count while you loop the dictionary, the same idea as "find the max in a foreach".
6. Write `summary.json` with three fields: the winning word, its count, and how many distinct words you saw.

`len(counts)` is the number of keys, which is the number of distinct words.

A max loop looks like this for a different dictionary:

```python
winner = None
best = -1
for name, score in scores.items():
    if score > best:
        best = score
        winner = name
```

Use that pattern. Do not call a library helper that hides the loop. The point is to see the loop you already know from C#.

## Practice

Words in the file, after lowercasing:

- python appears 3 times
- agent appears 2 times
- csharp appears 1 time

Expected console lines:

```text
python 3
3
```

The second number is how many distinct words there are. `summary.json` should contain the same facts: top word `python`, count `3`, unique `3`.

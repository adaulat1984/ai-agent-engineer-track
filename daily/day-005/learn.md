# Day 5 — files

60 minutes. Coursera skim: **Python Data Structures**, Chapter 7 (Files).

`open` plus `with` is a `using` block. The file closes when the block ends, including when an exception is thrown.

```python
with open("hours.txt", "w", encoding="utf-8") as handle:
    handle.write("40\n")
```

`"w"` overwrites the file. `"a"` appends. `"r"` reads. `encoding="utf-8"` matches the usual .NET UTF-8 write.

Read the lines back:

```python
with open("hours.txt", encoding="utf-8") as handle:
    for line in handle:
        print(line.strip())
```

`line.strip()` removes the newline, like `Trim()` on the row you just read. `int("40")` is `int.Parse("40")`.

Write a result the same way you wrote the input file: open with `"w"`, and include a newline if you want one line of text.

Paths are relative to the folder where you run `python`, not to the folder where the editor is open. Run this script from `daily/day-005` so `hours.txt` and `total.txt` appear beside `exercise.py`.

## Practice

The script should create `hours.txt` with three hour values, read that file, add the numbers, print the total, and store the total in `total.txt`.

Expected console line:

```text
123
```

`total.txt` should contain `123`.

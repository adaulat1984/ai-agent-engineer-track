# Day 6 — JSON

60 minutes. Coursera skim: **Using Python to Access Web Data**, the JSON and REST section. You only need the shape of JSON today. Sockets and HTML can wait.

`json` is in the standard library. It fills the role of `System.Text.Json`.

A JSON object becomes a dictionary. A JSON array becomes a list. Strings stay strings. Numbers become `int` or `float`. `true` / `false` / `null` become `True` / `False` / `None`.

```python
import json

raw = '{"tool": "clock", "ok": true}'
payload = json.loads(raw)
print(payload["tool"])
```

`json.loads` reads text. `json.dumps` writes text. That pair is `JsonSerializer.Deserialize` and `JsonSerializer.Serialize`.

```python
text = json.dumps({"done": 2, "open": 1})
```

A list of objects is a list of dictionaries:

```python
tasks = json.loads('[{"status": "done"}, {"status": "open"}]')
for task in tasks:
    print(task["status"])
```

Counting those statuses is the dictionary skill from Day 4. `task["status"]` is the key.

## Practice

`exercise.py` holds a JSON array of three tasks. Parse it, count each status, print the counts, and write them to `counts.json`.

Expected console lines, in any order:

```text
done 2
open 1
```

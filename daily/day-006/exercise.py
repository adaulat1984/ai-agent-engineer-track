# Day 6 practice. Parse JSON, count a field, write JSON back out.
# C#: JsonSerializer.Deserialize<List<Task>> and Serialize.

import json

raw = """[
  {"title": "login", "status": "done"},
  {"title": "pay", "status": "open"},
  {"title": "report", "status": "done"}
]"""

# TODO 1: parse `raw` into a Python list with json.loads.

# TODO 2: count how many tasks have each status.
# "done" appears twice. "open" appears once.

# TODO 3: print each status and its count.
# Expected: done 2, and open 1, in any order.

# TODO 4: write the counts to counts.json with json.dumps.
# Open the file with "w" and encoding="utf-8", the same pattern as Day 5.

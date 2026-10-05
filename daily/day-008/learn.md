# Day 8 — the body of an HTTP response

60 minutes. Coursera skim: **Using Python to Access Web Data**, Chapter 12 (HTTP) and the JSON section you used on Day 6. One pass is enough. You already know HTTP from ASP.NET.

An agent calls a tool, gets a status code, and reads a body. In C# that is `HttpClient.GetAsync`, then `response.Content.ReadAsStringAsync()`, then deserialize. In the standard library the same steps are `urllib.request.urlopen` and `json.loads`.

```python
import json
import urllib.request

with urllib.request.urlopen("https://httpbin.org/json") as response:
    status = response.status
    body = response.read().decode("utf-8")

if status == 200:
    payload = json.loads(body)
```

`response.status` is the HTTP status code. `read()` returns bytes, so `decode("utf-8")` is `Encoding.UTF8.GetString`. `json.loads` is the Day 6 parser.

Bad JSON raises `json.JSONDecodeError`. That is the exception to catch, not `ValueError`, when the failure is the body rather than `float()`.

Today's exercise does not call the network. It hands you the body as a string, which is the step that usually breaks after the request succeeds. The live `urlopen` call is written in comments at the bottom of `exercise.py` if you finish early and want to see a real status code.

## Practice

`read_status` should pull the `status` field out of a JSON object. A body that is not JSON should print `bad response` instead of crashing.

Expected lines:

```text
ok
bad response
```

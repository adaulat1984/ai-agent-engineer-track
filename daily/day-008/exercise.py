# Day 8 practice. Read a field from a response body.
# C#: ReadAsStringAsync, then JsonSerializer.Deserialize, catch a bad body.

import json

def read_status(response_text):
    # TODO: parse response_text and return the "status" field.
    # {"status": "ok", "tool": "clock"} -> "ok"
    # This function can let JSONDecodeError escape. The caller catches it.
    return None


sample = '{"status": "ok", "tool": "clock"}'
bad = "not-json"

# TODO: print read_status(sample). Expected: ok
# Wrap the bad body in try/except json.JSONDecodeError and print: bad response


# Optional after the expected lines work. Needs a network connection.
# import urllib.request
# with urllib.request.urlopen("https://httpbin.org/json") as response:
#     print(response.status)
#     print(response.read().decode("utf-8")[:80])

# Day 4 practice. Count weekdays with a dictionary.
# C#: Dictionary<string, int> and TryGetValue.

log = """Mon 09:01 user1 login
Tue 10:15 user2 login
Mon 11:00 user3 login
Wed 12:45 user1 login
"""

counts = {}

# TODO: for each non-empty line, read the first word.
# Add 1 to that word's count in `counts`.
# Use .get so a missing key starts at 0.
# Then print each day and its count on its own line.
# Expected counts: Mon 2, Tue 1, Wed 1.
# Order of the lines may follow insertion order.

print(counts)

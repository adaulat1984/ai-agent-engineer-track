# Day 3 practice. Finish both TODOs.
# C#: Substring / Split, and List<string> with Add.

email = "azeem@example.com"
log = """Mon 09:01 user1 login
Tue 10:15 user2 login
Mon 11:00 user3 login
"""

# TODO 1: print only the mailbox name, the text before @.
# Expected: azeem
# C#: email.Substring(0, email.IndexOf('@'))
# Python tools from learn.md: find, or split, and a slice.

print(email.split('@')[0])
print(email.split('@')[1])  # Using split to get the domain name
 
# TODO 2: for each non-empty line, take the first word and append it to days.
# Print days when the loop finishes.
# Expected: ['Mon', 'Tue', 'Mon']
# Skip a blank line. "Mon 09:01 user1 login".split()[0] is "Mon".

days = []
# days.append('Monday')
# days.append('Tuesday')
# days.append('Wednesday')
# days.append('Thursday')
# days.append('Friday')
# days.append('Saturday')
# days.append('Sunday')
for line in log.strip().split('\n'):
    if line:  # Skip blank lines
        days.append(line.split()[0])
print(days)

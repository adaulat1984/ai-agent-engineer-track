# Day 1 starter. Fill the three TODOs, then run this file.
# C# picture: a tiny console app with ReadLine, a null/empty check, and WriteLine.

name = input("Your name: ")

# TODO 1: if name is blank or only spaces, use "developer".
# C#: string.IsNullOrWhiteSpace(name) ? "developer" : name.Trim()
if name.isspace() or name == "":
    name = "developer"
else:
    name = name.strip()
display = name

# TODO 2: build a greeting that includes display.
# C#: $"Hello, {display}. Day 1 of 180 starts here."
greeting = f"Hello, {display}. Day 1 of 180 starts here."
# TODO 3: print greeting.
print(greeting)

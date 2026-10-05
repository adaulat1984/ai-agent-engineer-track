# Day 2 starter. Fill the two TODOs, then run this file.
# C# picture: a Pay method, a foreach over shifts, and try/catch around Parse.

def overtime_pay(hours, rate):
    # TODO 1: return the pay as a number. Do not print inside this function.
    #
    # This is a C# method: decimal OvertimePay(double hours, double rate)
    # There are no braces. The lines you add under this comment must be indented.
    #
    # Rule:
    # - 40 hours or fewer: pay = hours * rate
    # - more than 40: the first 40 hours use rate, and only the extra hours use rate * 1.5
    #
    # Check your math before you code it:
    # - 40 hours at 10 -> 40 * 10 = 400
    # - 45 hours at 10 -> (40 * 10) + (5 * 10 * 1.5) = 400 + 75 = 475
    #
    # Replace the line below with: return <your pay>
    return None


shifts = [(40, 10.0), (45, 10.0)]

for hours, rate in shifts:
    print(hours, overtime_pay(hours, rate))

raw = input("Extra hours: ")
try:
    # TODO 2: raw is text, like Console.ReadLine(). The except below is the catch.
    #
    # 1. Turn raw into a number. float(raw) is double.Parse(raw).
    #    "10" becomes 10.0. "abc" raises ValueError, and the except prints the message.
    # 2. Call overtime_pay with that number and rate 15.
    # 3. Print the number it returns.
    #
    # Delete the print("TODO", raw) line once your own print is in place.
    print("TODO", raw)
except ValueError:
    print("Enter a number for hours.")

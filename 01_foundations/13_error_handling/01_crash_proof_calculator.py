while True:
    try:
        first = input("Number: ")
        if first.lower() == "q":
            print("Calculator closed. Goodbye!")
            break
        num1 = float(first)
    except ValueError:
        print("That's not a number, try again.")
        continue

    try:
        second = input("Number: ")
        if second.lower() == "q":
            print("Calculator closed. Goodbye!")
            break
        num2 = float(second)
    except ValueError:
        print("That's not a number, try again.")
        continue
    operator = input("Operator (+, -, *, /) or q to quit: ")
    if operator.lower() == "q":
        print("Calculator closed. Goodbye!")
        break
    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator! Use +, -, *, or /.")
        continue
    if operator == "/" and num2 == 0:
        print("Cannot divide by zero! Try again.")
        continue
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    else:
        result = num1 / num2

    print("Result:", result)
    
"""Crash-Proof Calculator
try/except and retry loops
Build a calculator that never crashes. The user enters two numbers and an operator (+, -, *, /). Handle:
• non-numeric input (ask again)
• division by zero (show a friendly message)
• an invalid operator

Keep looping until the user provides valid input (or chooses to quit).

Example:

Number: abc   -> That's not a number, try again.
Number: 10
Number: 0
Operator: /   -> Cannot divide by zero!
"""
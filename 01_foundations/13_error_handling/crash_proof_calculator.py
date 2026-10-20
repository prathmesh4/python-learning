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
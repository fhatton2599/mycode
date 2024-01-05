#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
while calc1 != "q":
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1_input = input()
    if calc1_input.lower() == "q":
        break

    try:
        calc1 = float(calc1_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2_input = input()
    if calc2_input.lower() == "q":
        break

    try:
        calc2 = float(calc2_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\nNot a valid entry. Restarting...")


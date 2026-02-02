def calculator():

    operation = input("Enter an input (+,-,*,/)")

    first_number = float(input("Enter first number:"))

    second_number = float(input("Enter your second number:"))

    if operation == "+":

        print(f"The result is: {first_number + second_number}")

    elif operation == "-":
        print(f"The result is: {first_number - second_number}")

    elif operation == "*":
        print(f"The result is: {first_number * second_number}")

    elif operation == "/":
        if second_number != 0:
            print(f"The result is: {first_number / second_number}")

    else:
        print("Error: Division by zero")

calculator()
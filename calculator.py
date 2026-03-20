while True:
    try:
        x_str = input("Enter the first number: ")
        x = float(x_str)

        y_str = input("Enter the second number: ")
        y = float(y_str)

        op = input("Enter an operator (+, -, *, /): ")

        if op == "+":
            result = x + y
        elif op == "-":
            result = x - y
        elif op == "*":
            result = x * y
        elif op == "/":
            result = x / y
        else:
            print("Operator must be one of: +, -, *, /. Please try again.\n")
            continue

        print(f"{x} {op} {y} = {result}")
        break

    except ValueError:
        print("Input must be a valid number. Please try again.\n")
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a non-zero second number.\n")
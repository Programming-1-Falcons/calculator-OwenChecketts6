def calculate(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero not allowed"
    elif operation == '^':
        return num1 ** num2
    else:
        return "Invalid operation"

while True:
    # Get user inputs
    operation = input("Enter the operation (+, -, *, /, ^) or 'q' to quit: ")
    
    if operation.lower() == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    # Calculate result
    result = calculate(operation, num1, num2)

    # Output the formula and the result
    if isinstance(result, str):  # Check if the result is an error message
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result}")

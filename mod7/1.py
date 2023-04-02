import logging

logging.basicConfig(filename='calculator.log', level=logging.DEBUG)


def calculator(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
        logging.info(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        logging.info(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        logging.info(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            logging.error("Cannot divide by zero")
            return "Error: Cannot divide by zero"
        else:
            result = num1 / num2
            logging.info(f"{num1} / {num2} = {result}")
    else:
        logging.error(f"Invalid operator: {operation}")
        return "Error: Invalid operator"

    return result



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = calculator(num1, num2, operation)
print("Result: ", result)
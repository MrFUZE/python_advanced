import logging
import sys

def configure_logging():
    formatter = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[handler])


configure_logging()


def calculator(num1, num2, operation):
    logger = logging.getLogger(__name__)
    logger.info(f"Performing operation {num1} {operation} {num2}")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            logger.error("Cannot divide by zero")
            return "Error: Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        logger.error(f"Invalid operator: {operation}")
        return "Error: Invalid operator"

    logger.info(f"Result: {result}")
    return result


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = calculator(num1, num2, operation)
print("Result: ", result)

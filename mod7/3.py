import logging
import sys

def configure_logging():
    # Create formatter with desired format
    formatter = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')

    # Create handler to output logs to stdout
    handler_stdout = logging.StreamHandler(sys.stdout)
    handler_stdout.setLevel(logging.DEBUG)
    handler_stdout.setFormatter(formatter)

    # Create handler to write debug level logs to calc_debug.log file
    handler_debug = logging.FileHandler('calc_debug.log')
    handler_debug.setLevel(logging.DEBUG)
    handler_debug.setFormatter(formatter)

    # Create handler to write error level logs to calc_error.log file
    handler_error = logging.FileHandler('calc_error.log')
    handler_error.setLevel(logging.ERROR)
    handler_error.setFormatter(formatter)

    # Configure root logger with handlers
    logging.basicConfig(level=logging.DEBUG, handlers=[handler_stdout, handler_debug, handler_error])

configure_logging()

def arithmetic_operation(num1, num2, operation):
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

result = arithmetic_operation(num1, num2, operation)
print("Result: ", result)

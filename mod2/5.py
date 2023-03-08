from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    # Split the numbers string by the slash /
    numbers_list = numbers.split('/')
    try:
        numbers = [int(number) for number in numbers_list]
        max_num = max(numbers)
        return f"Максимальное число: {max_num}"
    except ValueError:
        return "Неверный ввод: не все значения являются числами"


if __name__ == '__main__':
    app.run(debug=True)

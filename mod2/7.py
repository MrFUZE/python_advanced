from flask import Flask
from collections import defaultdict
from typing import Dict

app = Flask(__name__)

expenses: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))


@app.route('/add/<date>/<int:amount>')
def add_expense(date: str, amount: int):
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    expenses[year][month] += amount
    return {'success': True}, 200


@app.route('/calculate/<int:year>')
def calculate_year(year: int):
    total = sum(expenses[year].values())
    return {'total': total}, 200


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year: int, month: int):
    total = expenses[year][month]
    return {'total': total}, 200


if __name__ == '__main__':
    app.run(debug=True)

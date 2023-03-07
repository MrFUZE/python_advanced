import random
from datetime import datetime, timedelta

from flask import Flask


app = Flask(__name__)

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cat_breeds = ['Cornish Rex', 'Russian Blue', 'Scottish Lop', 'Maine Coon', 'Munchkin']

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def get_cars():
    return ', '.join(cars)

@app.route('/cats')
def get_cat_breed():
    breed = random.choice(cat_breeds)
    return f"Случайная порода кошек: {breed}"

@app.route('/get_time/now')
def get_current_time():
    current_time = datetime.now()
    return f"Точное время: {current_time}"

@app.route('/get_time/future')
def get_time_in_one_hour():
    current_time = datetime.now()
    time_in_one_hour = current_time + timedelta(hours=1)
    return f"Точное время через час будет {time_in_one_hour}"

if __name__ == '__main__':
    app.run(debug=True)

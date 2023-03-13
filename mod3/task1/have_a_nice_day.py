from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/hello-world/<name>')
def hello_world(name):
    weekdays = ['понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья']
    weekday = weekdays[datetime.today().weekday()]
    if weekday in ['среды', 'пятницы', 'субботы']:
        return f'Привет, {name}. Хорошей {weekday}!'
    else:
        return f'Привет, {name}. Хорошего {weekday}!'


if __name__ == '__main__':
    app.run(debug=True)

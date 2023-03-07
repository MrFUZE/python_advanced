from datetime import datetime, timedelta
from flask import Flask

app = Flask(__name__)

@app.route('/time_in_one_hour')
def get_time_in_one_hour():
    current_time = datetime.now()
    time_in_one_hour = current_time + timedelta(hours=1)
    return f"Точное время через час будет {time_in_one_hour}"

if __name__ == '__main__':
    app.run(debug=True)

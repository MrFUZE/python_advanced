import datetime
import os
import re
from flask import Flask, render_template, send_from_directory
import random


root_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(root_dir, "templates")
js_dir = os.path.join(template_folder, 'js')

app = Flask(__name__, template_folder=template_folder)



@app.route('/')
def days_until_new_year():
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    days_left = (new_year - today).days
    return render_template('index.html', days_until_new_year=days_left)


@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory(js_dir, path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

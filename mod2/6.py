import os
from flask import Flask

app = Flask(__name__)


@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size, relative_path):
    abs_path = os.path.abspath(relative_path)

    with open(abs_path, 'r') as file:
        result_text = file.read(size)

    result_size = len(result_text)

    response = f"<b>{abs_path}</b> {result_size}<br>{result_text}"

    return response


if __name__ == '__main__':
    app.run(debug=True)


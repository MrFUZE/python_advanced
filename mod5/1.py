from flask import Flask
import subprocess
import shlex

app = Flask(__name__)


def start_server(port: int):
    command = shlex.split(f'lsof -ti:{port}')
    res = subprocess.run(command, capture_output=True, text=True)
    if res.stdout.strip() != '':
        pid = res.stdout.strip()
        command = shlex.split(f'kill {pid}')
        subprocess.run(command)
    app.run(port=port)


if __name__ == '__main__':
    start_server(5000)

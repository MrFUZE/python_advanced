import shlex
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/ps')
def ps_command():
    args = request.args.getlist('arg')
    quoted_args = [shlex.quote(arg) for arg in args]
    command = ['ps'] + quoted_args
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return f'<pre>{output.decode()}</pre>'


if __name__ == '__main__':
    app.run(debug=True)

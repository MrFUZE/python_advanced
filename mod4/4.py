from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/uptime')
def uptime():
    uptime = subprocess.check_output(['uptime']).decode('utf-8')
    return f"Current uptime is {uptime}"

if __name__ == '__main__':
    app.run(debug=True)

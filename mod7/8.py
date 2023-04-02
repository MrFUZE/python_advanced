import logging
import json
import urllib.request
from logging.handlers import HTTPHandler
from flask import Flask, request, jsonify

app = Flask(__name__)

class FlaskHTTPHandler(HTTPHandler):
    def emit(self, record):
        try:
            data = json.dumps(self.mapLogRecord(record)).encode('utf-8')
            req = urllib.request.Request(self.host, data=data, headers={'Content-Type': 'application/json'}, method='POST')
            urllib.request.urlopen(req)
        except Exception:
            self.handleError(record)

logging.basicConfig(level=logging.INFO)
handler = FlaskHTTPHandler('localhost:5000', '/logs')
logging.getLogger().addHandler(handler)

@app.route('/logs', methods=['POST'])
def receive_logs():
    log_data = request.json
    # process the log data as needed
    return jsonify({'message': 'Logs received successfully'})

@app.route('/logs', methods=['GET'])
def get_logs():
    # retrieve logs from the centralized logging system
    logs = []
    # process logs as needed
    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(debug=True)

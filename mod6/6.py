from flask import Flask, request

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return 'Hello, world!'


@app.errorhandler(404)
def not_found_error(error):
    reply = f'Seems like the page you want to go does not exist :( <br><br>List of all available pages:<br>'
    for rule in app.url_map.iter_rules():
        if str(rule) != '/':
            reply += f'<a href="{request.host_url}{rule}">{rule}</a><br>'
    return reply


if __name__ == '__main__':
    app.run(debug=True)

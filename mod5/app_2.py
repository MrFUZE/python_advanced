import subprocess
from flask import Flask, request, Response
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class CodeForm(FlaskForm):
    code = StringField('code', validators=[DataRequired()])
    timeout = IntegerField('timeout', validators=[DataRequired(), NumberRange(min=1, max=30)])

@app.route('/execute', methods=['POST'])
def execute_code():
    form = CodeForm(request.form)
    if form.validate():
        code = form.code.data
        timeout = form.timeout.data

        if "shell=True" in code:
            return Response('Insecure code entered.', status=400)

        try:
            process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate(timeout=timeout)

            if error:
                result = error.decode('utf-8')
            else:
                result = output.decode('utf-8')

            return Response(result, status=200, mimetype='text/plain')
        except subprocess.TimeoutExpired:
            process.kill()
            return Response('Code execution did not meet the given time limit.', status=400, mimetype='text/plain')
    else:
        errors = '\n'.join([f'{field}: {", ".join(error)}' for field, error in form.errors.items()])
        return Response(errors, status=400, mimetype='text/plain')


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)

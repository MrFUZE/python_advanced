from flask import Flask, request
from wtforms import Form, StringField, IntegerField, validators

app = Flask(__name__)

class RegistrationForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    phone = IntegerField('Phone', [validators.DataRequired(), validators.NumberRange(min=1000000000, max=9999999999)])
    name = StringField('Name', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])
    index = IntegerField('Index', [validators.DataRequired(), validators.NumberRange(min=0)])
    comment = StringField('Comment')

@app.route('/registration', methods=['POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate():

        return "Registration successful"
    else:
        return str(form.errors), 400


if __name__ == '__main__':
    app.run(debug=True)

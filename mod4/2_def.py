from wtforms.validators import InputRequired, ValidationError
from flask_wtf import FlaskForm
from wtforms import IntegerField

def number_length(min_len: int, max_len: int, message: str = None):
    def _number_length(form: FlaskForm, field: IntegerField):
        if not min_len <= len(str(field.data)) <= max_len:
            if message is None:
                message = f'Number should be between {min_len} and {max_len} digits long.'
            raise ValidationError(message)
    return _number_length

number = IntegerField(validators=[InputRequired(), number_length(10, 10)])

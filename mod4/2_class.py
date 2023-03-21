from wtforms.validators import InputRequired, ValidationError
from flask_wtf import FlaskForm
from wtforms import IntegerField

class NumberLength:
    def __init__(self, min_len: int, max_len: int, message: str = None):
        self.min_len = min_len
        self.max_len = max_len
        self.message = message

    def __call__(self, form: FlaskForm, field: IntegerField):
        if not self.min_len <= len(str(field.data)) <= self.max_len:
            if self.message is None:
                self.message = f'Number should be between {self.min_len} and {self.max_len} digits long.'
            raise ValidationError(self.message)

number = IntegerField(validators=[InputRequired(), NumberLength(10, 10)])

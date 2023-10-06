from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import IntegerField

class PDFCountForm(FlaskForm):
    pdf_count = IntegerField(
        'PDF Count',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=10, message='Please enter a number between 1 and 10.')
        ]
    )

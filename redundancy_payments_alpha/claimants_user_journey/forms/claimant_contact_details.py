from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class ClaimantContactDetails(Form):
    forenames = TextField('Forename(s)', validators=[DataRequired()])
    surname = TextField('Surname', validators=[DataRequired()])

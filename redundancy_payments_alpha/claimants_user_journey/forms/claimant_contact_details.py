from flask_wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import DataRequired, Optional, NoneOf, AnyOf, Length


class ClaimantContactDetails(Form):
    forenames = TextField('Forename(s)', validators=[DataRequired(), Length(max=60)])
    surname = TextField('Surname', validators=[DataRequired(), Length(max=60)])
    title = SelectField('Title',
                        choices=[
                            (1, 'Mr'),
                            (2, 'Mrs'),
                            (3, 'Miss'),
                            (4, 'Ms'),
                            (5, 'Other'),
                            (6, '')
                        ],
                        default=6,
                        validators=[Optional()])
    other = TextField('Other', validators=[Optional()])
    building_number = TextField('Building Number', validators=[DataRequired()])
    street = TextField('Street', validators=[DataRequired()])
    district = TextField('District', validators=[DataRequired()])
    town_or_city = TextField('Town or City', validators=[DataRequired()])
    county = TextField('County', validators=[DataRequired()])
    postcode = TextField('Post Code', validators=[DataRequired()])
    email = TextField('Email Address', validators=[DataRequired()])
    telephone_number = TextField('Telephone Number', validators=[DataRequired()])



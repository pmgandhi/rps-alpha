from flask_wtf import Form
from wtforms import TextField, SelectField, StringField
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import DataRequired, Optional, Length, Email


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
    building_number = StringField('Building Number', validators=[DataRequired(), Length(max=30)])
    street = TextField('Street', validators=[DataRequired(), Length(max=30)])
    district = TextField('District', validators=[DataRequired(), Length(max=30)])
    town_or_city = TextField('Town or City', validators=[DataRequired(), Length(max=30)])
    county = TextField('County', validators=[DataRequired(), Length(max=30)])
    postcode = TextField('Post Code', validators=[DataRequired(), Length(max=10)])
    email = EmailField('Email Address', validators=[DataRequired(), Length(max=320), Email()])
    telephone_number = TelField('Telephone Number', validators=[DataRequired()])

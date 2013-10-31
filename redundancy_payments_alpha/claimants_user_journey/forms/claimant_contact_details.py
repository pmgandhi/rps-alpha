from flask_wtf import Form
from wtforms import TextField, SelectField, StringField, ValidationError
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import DataRequired, Optional, Length, Email, AnyOf


class ClaimantContactDetails(Form):
    forenames = TextField('Forename(s)', validators=[DataRequired(), Length(max=60)])
    surname = TextField('Surname', validators=[DataRequired(), Length(max=60)])
    title = SelectField('Title',
                        choices=[
                            ('Mr', 'Mr'),
                            ('Mrs', 'Mrs'),
                            ('Miss', 'Miss'),
                            ('Ms', 'Ms'),
                            ('Other', 'Other'),
                            ('', '')
                        ],
                        default='',
                        validators=[AnyOf(values=[
                            'Mr',
                            'Mrs',
                            'Miss',
                            'Ms',
                            'Other'
                        ])])
    other = TextField('Other')

    def validate_other(form, field):
        claimants_title = form._fields.get('title')
        if claimants_title.data == 'Other' and not field.data:
            raise ValidationError("Field is required if 'Other' is selected.")

    building_number = StringField('Building Number', validators=[DataRequired(), Length(max=30)])
    street = TextField('Street', validators=[DataRequired(), Length(max=30)])
    district = TextField('District', validators=[DataRequired(), Length(max=30)])
    town_or_city = TextField('Town or City', validators=[DataRequired(), Length(max=30)])
    county = TextField('County', validators=[DataRequired(), Length(max=30)])
    postcode = TextField('Post Code', validators=[DataRequired(), Length(max=10)])
    email = EmailField('Email Address', validators=[DataRequired(), Length(max=320), Email()])
    telephone_number = TelField('Telephone Number', validators=[DataRequired()])

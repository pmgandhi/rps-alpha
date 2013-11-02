import re
from datetime import date
from flask_wtf import Form
from wtforms import TextField, SelectField, StringField, ValidationError
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import DataRequired, Length, Email, AnyOf, Regexp


def convert_string_to_date(date_string):
    split_string = date_string.split('/')
    if type(split_string) != list or len(split_string) != 3:
        raise SyntaxError('Was expecting dd/MM/yyyy.')
    return date(int(split_string[2]), int(split_string[1]), int(split_string[0]))


class ClaimantContactDetails(Form):
    forenames = TextField('First name(s)', validators=[DataRequired(), Length(max=60)])
    surname = TextField('Last name', validators=[DataRequired(), Length(max=60)])
    title = SelectField('Title',
                        choices=[
                            ('Mr', 'Mr'),
                            ('Mrs', 'Mrs'),
                            ('Miss', 'Miss'),
                            ('Ms', 'Ms'),
                            ('Dr', 'Dr'),
                            ('Other', 'Other'),
                            ('', '')
                        ],
                        default='',
                        validators=[AnyOf(values=[
                            'Mr',
                            'Mrs',
                            'Miss',
                            'Ms',
                            'Dr',
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
    nino = TextField('National Insurance Number',
                     validators=[DataRequired(),
                                 Regexp(regex=re.compile('^[A-Z]{2}[0-9]{6}[A-Z]{1}$'),
                                        message="National Insurance Number must be two letters followed by six digits and a further letter (e.g. 'AB123456C').")])
    date_of_birth = TextField('Date Of Birth',
                              validators=[DataRequired(),
                                          Regexp(regex=re.compile('^[0-9]{2}[/][0-9]{2}[/][0-9]{4}$'),
                                                 message="Date Of Birth must be in the format dd/mm/yyyy.") ])

    def validate_date_of_birth(form, field):
        date_of_birth = form._fields.get('date_of_birth')
        try:
            parsed_date = convert_string_to_date(date_of_birth.data)
        except SyntaxError:
            raise ValidationError('Date Of Birth must be greater than or equal to 1900 and not in the future.')
        if parsed_date.year < 1900 or parsed_date >= date.today():
            raise ValidationError('Date Of Birth must be greater than or equal to 1900 and not in the future.')

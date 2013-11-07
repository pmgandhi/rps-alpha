import re
from flask_wtf import Form
from wtforms import TextField, SelectField, StringField, ValidationError
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import DataRequired, Length, Email, AnyOf, Regexp
from validators.Validators import DateOfBirthValidator


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
    other = TextField('Other', validators=[Length(max=15)])

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
                              validators=[DataRequired(), DateOfBirthValidator(format_message="Date Of Birth must be in the format dd/mm/yyyy.")])


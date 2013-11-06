import time
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, ValidationError, Length

class EmployerDetailsForm(Form):
    company_name  = TextField('Company Name', validators=[DataRequired(), Length(max=60)])
    company_number  = TextField('Company Number', validators=[Length(max=10)])
    nature_of_business  = TextField('Nature of Business', validators=[DataRequired(), Length(max=60)])
    date_of_insolvency  = TextField('Date of Insolvency', validators=[DataRequired()])
    type_of_insolvency  = TextField('Type of Insolvency', validators=[DataRequired()])
    insolvency_practitioner_name  = TextField('Insolvency Practitioner Name', validators=[DataRequired(), Length(max=30)])
    insolvency_practitioner_registration  = TextField('Insolvency Practitioner Registration', validators=[DataRequired(), Length(max=15)])
    insolvency_practitioner_firm  = TextField('Insolvency Practitioner Firm', validators=[DataRequired(), Length(max=30)])
    address_line_1  = TextField('Address Line 1', validators=[DataRequired(), Length(max=7)])
    address_line_2  = TextField('Address Line 2', validators=[DataRequired(), Length(max=22)])
    address_line_3  = TextField('Address Line 3', validators=[Length(max=30)])
    town_or_city  = TextField('Town or City', validators=[DataRequired(), Length(max=30)])
    postcode  = TextField('Postcode', validators=[DataRequired(), Length(max=8)])
    country  = TextField('Country', validators=[DataRequired(), Length(max=30)])
    email_address  = TextField('Email Address', validators=[DataRequired(), Length(max=60)])
    telephone_number  = TextField('Telephone Number', validators=[DataRequired(), Length(max=14)])

    def validate_date_of_insolvency(self, field):
        try:
            time.strptime(field.data, "%d/%m/%Y")
        except ValueError as e:
            raise ValidationError('Date must be in the format dd/mm/yyyy.')

    def validate_company_number(self, field):
        if field.data:
            try:
                int(field.data)
            except ValueError as e:
                raise ValueError('Company number must be a number.')

    def validate_insolvency_practitioner_registration(self, field):
        if field.data:
            try:
                int(field.data)
            except ValueError as e:
                raise ValueError('Insolvency Practitioner Registration must be a number.')


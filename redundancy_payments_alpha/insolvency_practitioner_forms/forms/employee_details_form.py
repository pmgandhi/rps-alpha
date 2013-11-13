import re

from flask_wtf import Form
from wtforms import TextField, SelectField, DecimalField
from wtforms.validators import ValidationError, Length, AnyOf, DataRequired

from validators.validators import parses_to_date


class EmployeeDetailsForm(Form):
    employer_name = TextField('Employer Name', validators=[Length(max=60), DataRequired()])
    employee_title = SelectField(
        label='Title',
        default = '',
        choices = [
            ('Mr', 'Mr'),
            ('Mrs', 'Mrs'),
            ('Miss', 'Miss'),
            ('Ms', 'Ms'),
            ('Other', 'Other'),
            ('', '')
        ],
        validators=[AnyOf(['Mr', 'Mrs', 'Miss', 'Ms', 'Other'])]
    )
    employee_title_other = TextField('Title if other', validators=[Length(max=15)])

    def validate_employee_title_other(self, field):
        if not field.data and self.employee_title.data == 'Other':
            raise ValidationError('A title must be provided if other is selected.')

    employee_forenames = TextField('Forenames', validators=[Length(max=40), DataRequired()])
    employee_surname = TextField('Surname', validators=[Length(max=60), DataRequired()])
    employee_national_insurance_class = TextField('National insurance class')

    def validate_employee_national_insurance_class(self, field):
        if field.data and not re.match("^[A-Za-z]{1}$", field.data):
            raise ValidationError('National insurance class must be a single letter.')

    employee_national_insurance_number = TextField('National insurance number', validators=[DataRequired()])

    def validate_employee_national_insurance_number(self, field):
        if field.data and not re.match('^[A-Za-z]{2}[0-9]{6}[A-Za-z]{0,1}$', field.data):
            raise ValidationError('National insurance number should be two letters followed by six numbers and an optional letter')

    employee_date_of_birth = TextField('Date of birth', validators=[DataRequired(), parses_to_date])
    employee_start_date = TextField('Employment Start date', validators=[DataRequired(), parses_to_date])
    employee_date_of_notice = TextField('Date notice was given', validators=[DataRequired(), parses_to_date])
    employee_end_date = TextField('Employment End date', validators=[DataRequired(), parses_to_date])
    employee_basic_weekly_pay = DecimalField('Basic weekly pay', validators=[DataRequired()])
    employee_weekly_pay_day = SelectField(
        'If paid weekly on which day of week?',
        default='',
        choices = [
            ('', ''),
            ('sunday', 'Sunday'),
            ('monday', 'Monday'),
            ('tuesday', 'Tuesday'),
            ('wednesday', 'Wednesday'),
            ('thursday', 'Thursday'),
            ('friday', 'Friday'),
            ('saturday', 'Saturday')
        ]
    )
    employee_owed_wages_from = TextField('Period 1 From', validators=[DataRequired()])
    employee_owed_wages_to = TextField('Period 1 To', validators=[DataRequired()])
    employee_owed_wages_in_arrears = TextField('Arrears of pay amount', validators=[DataRequired()])
    employee_owed_wages_in_arrears_type = SelectField(
        'Arrears of pay type',
        default = '',
        choices = [
            ('',''),
            ('attatchment_of_earnings','attachment of earnings'),
            ('wages','wages'),
            ('overtime','overtime'),
            ('unpaid_checque','unpaid cheque'),
            ('commission','commission')
        ]
    )
    employee_holiday_year_start_date = TextField('Holiday year start date', validators=[DataRequired(), parses_to_date])
    employee_holiday_owed = DecimalField('Total number of days holiday owed', validators=[DataRequired()])
    employee_unpaid_holiday_from = TextField('Unpaid holiday from', validators=[parses_to_date])
    employee_unpaid_holiday_to = TextField('Unpaid holiday to', validators=[parses_to_date])


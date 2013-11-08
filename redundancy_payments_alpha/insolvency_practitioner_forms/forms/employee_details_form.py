import re

from flask_wtf import Form
from wtforms import TextField, SelectField, DecimalField
from wtforms.validators import ValidationError, Length, AnyOf, DataRequired

from validators.validators import parses_to_date


class EmployeeDetailsForm(Form):
    employer_name = TextField('Employer Name', validators=[Length(max=60), DataRequired()])
    employee_title = SelectField(
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

    employee_forenames = TextField('Employee forenames', validators=[Length(max=40), DataRequired()])
    employee_surname = TextField('Employee surname', validators=[Length(max=60), DataRequired()])
    employee_national_insurance_class = TextField('National insurance class')

    def validate_employee_national_insurance_class(self, field):
        if field.data and not re.match("^[A-Za-z]{1}$", field.data):
            raise ValidationError('National insurance class must be a single letter.')

    employee_national_insurance_number = TextField('National insurance number', validators=[DataRequired()])
    employee_date_of_birth = TextField('Date of birth', validators=[DataRequired(), parses_to_date])
    employee_start_date = TextField('Start date', validators=[DataRequired(), parses_to_date])
    employee_date_of_notice = TextField('Date notice was given', validators=[DataRequired(), parses_to_date])
    employee_end_date = TextField('End date', validators=[DataRequired(), parses_to_date])
    employee_basic_weekly_pay = DecimalField('Basic weekly pay', validators=[DataRequired()])
    employee_weekly_pay_day = SelectField(
        'If paid weekly on which day of week?',
        default='',
        choices = [
            ('not_paid_weekly', 'Not paid weekly'),
            ('sunday', 'Sunday'),
            ('monday', 'Monday'),
            ('tuesday', 'Tuesday'),
            ('wednesday', 'Wednesday'),
            ('thursday', 'Thursday'),
            ('friday', 'Friday'),
            ('saturday', 'Saturday')
        ]
    )
    employee_owed_wages_from = TextField('Employee owed wages from', validators=[DataRequired()])
    employee_owed_wages_to = TextField('Employee owed wages to', validators=[DataRequired()])
    employee_owed_wages_in_arrears = TextField('Owed wages in arrears', validators=[DataRequired()])
    employee_owed_wages_in_arrears_type = SelectField(
        'Owed wages in arrears type',
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
    employee_holiday_owed = DecimalField('Number of days holiday owed', validators=[DataRequired()])
    employee_unpaid_holiday_from = TextField('Unpaid holiday from')
    employee_unpaid_holiday_to = TextField('Unpaid holiday to')


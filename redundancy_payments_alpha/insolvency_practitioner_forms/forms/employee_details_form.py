from flask_wtf import Form
from wtforms import TextField, SelectField, DecimalField

class EmployeeDetailsForm(Form):
    employer_name = TextField('Employer Name')
    employee_title = SelectField(
        default = '',
        choices = [
            ('Mr', 'Mr'),
            ('Mrs', 'Mrs'),
            ('Miss', 'Miss'),
            ('Ms', 'Ms'),
            ('Other', 'Other'),
            ('', '')
        ]
    )
    employee_title_other = TextField('Title if other')
    employee_forenames = TextField('Employee forenames')
    employee_surname = TextField('Employee surname')
    employee_national_insurance_class = TextField('National insurance class')
    employee_national_insurance_number = TextField('National insurance number')
    employee_date_of_birth = TextField('Date of birth')
    employee_start_date = TextField('Start date')
    employee_date_of_notice = TextField('Date notice was given')
    employee_end_date = TextField('End date')
    employee_basic_weekly_pay = DecimalField('Basic weekly pay')
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
    employee_owed_wages_from = TextField('Employee owed wages from')
    employee_owed_wages_to = TextField('Employee owed wages to')
    employee_owed_wages_in_arrears = TextField('Owed wages in arrears')
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
    employee_holiday_year_start_date = TextField('Holiday year start date')
    employee_holiday_owed = DecimalField('Number of days holiday owed')
    employee_unpaid_holiday_from = TextField('Unpaid holiday from')
    employee_unpaid_holiday_to = TextField('Unpaid holiday to')


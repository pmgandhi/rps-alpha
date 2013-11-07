from flask_wtf import Form
from wtforms import TextField, RadioField
from wtforms.validators import DataRequired, AnyOf, StopValidation
from employment_details import FutureDateValidator

class RequiredIfFieldHasValue(DataRequired):
    # a validator which makes a field required if
    # another field is set and has a truthy value
    def __init__(self, other_field_name, other_field_value, *args, **kwargs):
        self.other_field_name = other_field_name
        self.other_field_value = other_field_value
        super(RequiredIfFieldHasValue, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        if other_field.data == self.other_field_value:
            super(RequiredIfFieldHasValue, self).__call__(form, field)
        else:
            #If it gets this far then the field is optional
            field.errors[:] = []
            raise StopValidation()


class HolidayPay(Form):
    holiday_owed = RadioField('Are you owed any holiday pay?',choices=[
                                         ('Yes', 'Yes'),
                                         ('No', 'No')
                                     ],
                                     validators=[DataRequired(), AnyOf(values=[
                                         'Yes',
                                         'No'
                                     ])])
    holiday_start_date = TextField('What was the start date of your holiday year?',
                                   validators=[
                                       RequiredIfFieldHasValue(other_field_name='holiday_owed', other_field_value='Yes',
                                                               message='Holiday Year Start Date has not been completed.'),
                                       FutureDateValidator(format_message="Start date must be in the format dd/mm/yyyy.",
                                                           future_message='Start date cannot be in the future.')])
    number_of_holiday_days_entitled = TextField('How many days holiday per year (including bank holidays) were you entitled to?',
                                                validators=[RequiredIfFieldHasValue(other_field_name='holiday_owed', other_field_value='Yes',
                                                               message='Holiday entitlement has not been completed.')])
    days_carried_over = TextField('If you were allowed to carry forward untaken holiday entitlement from your previous holiday year, how many days did you carry forward this year?',
                                                validators=[RequiredIfFieldHasValue(other_field_name='holiday_owed', other_field_value='Yes',
                                                               message='Days carried over has not been completed.')])
    days_taken = TextField('How many days have you taken this year (including bank holidays)?',
                                                validators=[RequiredIfFieldHasValue(other_field_name='holiday_owed', other_field_value='Yes',
                                                               message='Days taken mandatory fields has not been completed.')])
    days_owed = TextField('How many days are you still owed (including bank holidays) up to your termination date?',
                                                validators=[RequiredIfFieldHasValue(other_field_name='holiday_owed', other_field_value='Yes',
                                                               message='Days owed mandatory fields has not been completed.')])
    holiday_taken_from = TextField('From')
    holiday_taken_to = TextField('To')
    number_of_days_pay_owed = TextField('Number of days for which pay is owed')

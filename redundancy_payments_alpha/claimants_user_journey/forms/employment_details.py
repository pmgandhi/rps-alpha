import re
from datetime import date
from flask_wtf import Form
from wtforms import TextField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, AnyOf, Regexp
from claimant_contact_details import convert_string_to_date


class FutureDateValidator(Regexp):
    def __init__(self, format_message, future_message):
        self.future_message = future_message
        super(FutureDateValidator, self).__init__(r'^[0-9]{2}[/][0-9]{2}[/][0-9]{4}$', re.IGNORECASE, format_message)

    def __call__(self, form, field):
        message = self.message
        super(FutureDateValidator, self).__call__(form, field, message)
        extracted_date = convert_string_to_date(field.data)
        if self.future_message is None:
            self.future_message = 'Date cannot be in the future'

        if extracted_date > date.today():
            raise ValidationError(self.future_message)


class EmploymentDetails(Form):
    job_title = TextField('Job Title', validators=[DataRequired(), Length(max=30)])
    category_of_worker = SelectField('Category of Worker',
                                     choices=[
                                         ('Employed', 'Employed'),
                                         ('Labour-only Sub-contractor', 'Labour-only Sub-contractor'),
                                         ('Agency Worker', 'Agency Worker'),
									     ('Fixed-term contracts worker', 'Fixed-term contracts worker'),
                                         ('Director or Shareholder', 'Director or Shareholder'),
                                         ('Freelance worker', 'Freelance worker'),
                                         ('Casual worker', 'Casual worker'),
                                         ('Home worker', 'Home worker'),
                                         ('', '')
                                     ],
                                     default='',
                                     validators=[AnyOf(values=[
                                         'Employed',
                                         'Labour-only Sub-contractor',
                                         'Agency Worker',
                                         'Fixed-term contracts work',
                                         'Director or Shareholder',
                                         'Freelance worker',
                                         'Casual worker',
                                         'Home worker',
                                     ])])
    start_date = TextField('When did you start working for this employer?',
                           validators=[DataRequired(),
                                       FutureDateValidator(format_message="Start date must be in the format dd/mm/yyyy.",
                                                           future_message='Start date cannot be in the future.')])
    end_date = TextField('When did your employment end?',
                           validators=[DataRequired(),
                                       FutureDateValidator(format_message="End date must be in the format dd/mm/yyyy.",
                                                           future_message='End date cannot be in the future.')])


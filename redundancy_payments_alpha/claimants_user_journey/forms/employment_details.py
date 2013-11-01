import re
from flask_wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import DataRequired, Length, AnyOf, Regexp


class EmploymentDetails(Form):
    job_title = TextField('Job Title', validators=[DataRequired(), Length(max=30)])
    category_of_worker = SelectField('Category of Worker',
                                     choices=[
                                         ('Employed', 'Employed'),
                                         ('Labour-only', 'Labour-only'),
                                         ('Sub-contractor', 'Sub-contractor'),
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
                                         'Labour-only',
                                         'Sub-contractor',
                                         'Agency Worker',
                                         'Fixed-term contracts work',
                                         'Director or Shareholder',
                                         'Freelance worker',
                                         'Casual worker',
                                         'Home worker',
                                     ])])
    start_date = TextField('When did you start working for this employer?',
                           validators=[DataRequired(),
                                       Regexp(regex=re.compile('^[0-9]{2}[/][0-9]{2}[/][0-9]{4}$'),
                                        message="Date must be in the format dd/mm/yyyy.")])
    end_date = TextField('When did your employment end?',
                           validators=[DataRequired(),
                                       Regexp(regex=re.compile('^[0-9]{2}[/][0-9]{2}[/][0-9]{4}$'),
                                        message="Date must be in the format dd/mm/yyyy.")])



import re
from datetime import datetime, date
from flask_wtf import Form
from wtforms import TextField, SelectField, StringField, ValidationError, DateField
from wtforms.fields.html5 import TelField, EmailField, DateField
from wtforms.validators import DataRequired, Optional, Length, Email, AnyOf, Regexp

class ClaimantWageDetails(Form):
    FrequencyOfPayment = TextField('How often do you get paid?')
    GrossRateOfPay = TextField('Gross rate of pay (before Tax and NI)')
    every = TextField('every')
    NumberHoursWorked = TextField('Number of hours you normally work')
    BonusOrCommission = TextField('Did your pay include any bonus or commission ?')
    Overtime = TextField('Did you work overtime as a part of your contract ?')
    NormalDaysofWork = TextField('How many days you normally work each week')


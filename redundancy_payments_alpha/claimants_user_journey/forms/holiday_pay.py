from flask_wtf import Form
from wtforms import TextField


class HolidayPay(Form):
    holiday_owed = TextField('Are you owed any holiday pay?')
    holiday_start_date = TextField('What was the start date of your holiday year?')
    number_of_holiday_days_entitled = TextField('How many days holiday per year (including bank holidays) were you entitled to?')
    days_carried_over = TextField('If you were allowed to carry forward untaken holiday entitlement from your previous holiday year, how many days did you carry forward this year?')
    days_taken = TextField('How many days have you taken this year (including bank holidays)?')
    days_owed = TextField('How many days are you still owed (including bank holidays) up to your termination date?')
    holiday_taken_from = TextField('From')
    holiday_taken_to = TextField('To')
    number_of_days_pay_owed = TextField('Number of days for which pay is owed')
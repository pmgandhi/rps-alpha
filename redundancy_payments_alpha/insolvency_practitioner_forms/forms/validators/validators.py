import time
from wtforms.validators import ValidationError

def parses_to_date(form, field):
    try:
        time.strptime(field.data, "%d/%m/%Y")
    except ValueError as e:
        raise ValidationError('Date must be in the format dd/mm/yyyy.')


from insolvency_practitioner_forms.mapper import mapper
from hamcrest import *
from decimal import *

def test_that_all_values_are_coerced_to_string():
    """ We don't need the decimal values from the form to be decimals in the rest of the app, at least at the moment.
    Also decimal types will not serialise, therefore we coerce everything to a string for now.
    """
    # given
    decimal = Decimal(10)
    KEYNAME = "whatever"
    dict = { KEYNAME : decimal }
    # when
    result = mapper(dict)
    # then
    assert_that(isinstance(result[KEYNAME], str))

def test_all_dates_are_given_in_iso_utc_format():
    """ We want the representation of the date in the form to be decoupled from datastore representation.
    """
    # given

    # when
    # then
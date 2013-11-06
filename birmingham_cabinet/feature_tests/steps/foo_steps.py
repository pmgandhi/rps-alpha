from hamcrest import assert_that, is_

from birmingham_cabinet.api import add_rp1_form, add_rp14_form
from birmingham_cabinet.models import Claimant, Employer
from birmingham_cabinet.base import make_session

@when('we add a dictionary containing sample rp1 details')
def step(context):
    form = {
        'forenames': 'Donald',
        'surname': 'Duck',
        'title': 'Mr',
        'other': '',
        'address_line_1': '5 street name',
        'address_line_2': 'district name',
        'address_line_3': "", # FIXME: None instead of ""
        'town_or_city': 'Duckburg',
        'postcode': 'A1 2BC',
        'email': 'donald.duck@duckburg.com',
        'telephone_number': '12345 123456',
        'nino': 'AA112233B',
        'date_of_birth': '01/01/1900'
    }
    add_rp1_form(form)
    
@then('the data store should contain a claimant')
def step(context):
    session = make_session()
    try:
        assert_that(session.query(Claimant).count(), is_(1))
    finally:
        session.close()
        
@when("we add a dictionary containing sample rp14 details")
def step(context):
    form = {
        "employer_name": "Mickey Mouse Enterprises",
        "company_number": "010101",
        "date_of_insolvency": "01/01/1900",
        "telephone_number": "12345 123456"
    }
    add_rp14_form(form)

@then("the data store should contain an employer")
def step(context):
    session = make_session()
    try:
        assert_that(session.query(Employer).count(), is_(1))
    finally:
        session.close()
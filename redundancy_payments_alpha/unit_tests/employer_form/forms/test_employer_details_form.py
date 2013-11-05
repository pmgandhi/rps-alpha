import unittest
from hamcrest import assert_that, is_, has_entry
from wtforms import Form, TextField


class EmployerDetailsForm(Form):
    company_name  = TextField('Company Name')
    company_number  = TextField('Company Number')
    nature_of_business  = TextField('Nature of Business')
    date_of_insolvency  = TextField('Date of Insolvency')
    type_of_insolvency  = TextField('Type of Insolvency')
    insolvency_practitioner_name  = TextField('Insolvency Practitioner Name')
    insolvency_practitioner_registration  = TextField('Insolvency Practitioner Registration')
    insolvency_practitioner_firm  = TextField('Insolvency Practitioner Firm')
    address_line_1  = TextField('Address Line 1')
    address_line_2  = TextField('Address Line 2')
    address_line_3  = TextField('Address Line 3')
    town_or_city  = TextField('Town or City')
    postcode  = TextField('Postcode')
    country  = TextField('Country')
    email_address  = TextField('Email Address')
    telephone_number  = TextField('Telephone Number')


class TestEmployerDetailsForm(unittest.TestCase):
    def test_form_takes_employer_data(self):
        form_data = {
            'company_name': 'Self Pres 12#',
            'company_number': '98998987',
            'nature_of_business': 'Stealing gold from Italian banks',
            'date_of_insolvency': '01/05/2013',
            'type_of_insolvency': 'Compulsory Liquidation (WUO)',
            'insolvency_practitioner_name': 'Tywin Lannster',
            'insolvency_practitioner_registration': '9888',
            'insolvency_practitioner_firm':'House Lannister of Caterley Rock',
            'address_line_1':'269a',
            'address_line_2':'Winterfell',
            'address_line_3':'Summerhasdied St',
            'town_or_city':'Birmingham',
            'postcode':'B4 6FD',
            'country':'England',
            'email_address':'tywin.lannister@hotmail.co.uk',
            'telephone_number':'07537345763'
        }

        form = EmployerDetailsForm(**form_data)
        assert_that(form.data, has_entry('company_name', 'Self Pres 12#'))
        assert_that(form.data, has_entry('company_number', '98998987'))
        assert_that(form.data, has_entry('nature_of_business', 'Stealing gold from Italian banks'))
        assert_that(form.data, has_entry('date_of_insolvency', '01/05/2013'))
        assert_that(form.data, has_entry('type_of_insolvency', 'Compulsory Liquidation (WUO)'))
        assert_that(form.data, has_entry('insolvency_practitioner_name', 'Tywin Lannster'))
        assert_that(form.data, has_entry('insolvency_practitioner_registration', '9888'))
        assert_that(form.data, has_entry('insolvency_practitioner_firm', 'House Lannister of Caterley Rock'))
        assert_that(form.data, has_entry('address_line_1', '269a'))
        assert_that(form.data, has_entry('address_line_2', 'Winterfell'))
        assert_that(form.data, has_entry('address_line_3', 'Summerhasdied St'))
        assert_that(form.data, has_entry('town_or_city', 'Birmingham'))
        assert_that(form.data, has_entry('postcode', 'B4 6FD'))
        assert_that(form.data, has_entry('country', 'England'))
        assert_that(form.data, has_entry('email_address', 'tywin.lannister@hotmail.co.uk'))
        assert_that(form.data, has_entry('telephone_number', '07537345763'))

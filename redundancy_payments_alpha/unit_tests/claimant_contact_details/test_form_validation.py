import unittest
from hamcrest import *
from redundancy_payments_alpha.claimants_user_journey.forms.claimant_contact_details \
    import ClaimantContactDetails
from redundancy_payments_alpha.claimants_user_journey.routes import app

test_client = app.test_client()


def complete_form(data):
    with app.test_request_context('/claimant-contact-details'):
        form = ClaimantContactDetails(**data)
        return form


def complete_form_data():
    form = {
        'forenames': 'Donald',
        'surname': 'Duck',
        'title': 'Mr',
        'other': '',
        'building_number': 5,
        'street': 'street name',
        'district': 'district name',
        'town_or_city': 'Duckburg',
        'county': 'county name',
        'postcode': 'A1 2BC',
        'email': 'donald.duck@duckburg.com',
        'telephone_number': '12345 123456'
    }
    return form


class TestFormValidation(unittest.TestCase):
    def test_form_is_invalid_without_forenames(self):
        # given
        entered_data = complete_form_data()
        del entered_data['forenames']
        # when
        form = complete_form(entered_data)
        # then
        assert_that(form.validate(), is_(False))


class TestForenamesValidation(unittest.TestCase):
    def test_forenames_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.forenames.errors, has_length(0))

    def test_forenames_field_can_be_no_longer_than_60_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['forenames'] = 'a' * 61
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.forenames.errors, has_item('Field cannot be longer than 60 characters.'))


class TestSurnameValidation(unittest.TestCase):
    def test_surname_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that((form.surname.errors, has_length(0)))

    def test_surname_field_can_be_no_longer_than_60_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['surname'] = 'a' * 61
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.surname.errors, has_item('Field cannot be longer than 60 characters.'))

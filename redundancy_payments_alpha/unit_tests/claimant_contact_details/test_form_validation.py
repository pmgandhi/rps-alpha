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
        'building_number': '5',
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


class TestBuildingNumberValidation(unittest.TestCase):
    def test_building_number_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.building_number.errors, has_length(0))

    def test_building_number_field_can_be_no_longer_than_30_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['building_number'] = 'a' * 31
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.building_number.errors, has_item('Field cannot be longer than 30 characters.'))

class TestStreetValidation(unittest.TestCase):
    def test_street_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.street.errors, has_length(0))

    def test_street_field_can_be_no_longer_than_30_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['street'] = 'a' * 31
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.street.errors, has_item('Field cannot be longer than 30 characters.'))

class TestDistrictValidation(unittest.TestCase):
    def test_district_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.district.errors, has_length(0))

    def test_district_field_can_be_no_longer_than_30_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['district'] = 'a' * 31
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.district.errors, has_item('Field cannot be longer than 30 characters.'))

class TestTownOrCityValidation(unittest.TestCase):
    def test_town_or_city_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.town_or_city.errors, has_length(0))

    def test_town_or_city_field_can_be_no_longer_than_30_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['town_or_city'] = 'a' * 31
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.town_or_city.errors, has_item('Field cannot be longer than 30 characters.'))

class TestCountyValidation(unittest.TestCase):
    def test_county_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.county.errors, has_length(0))

    def test_county_field_can_be_no_longer_than_30_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['county'] = 'a' * 31
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.county.errors, has_item('Field cannot be longer than 30 characters.'))

class TestPostCodeValidation(unittest.TestCase):
    def test_post_code_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.postcode.errors, has_length(0))

    def test_post_code_field_can_be_no_longer_than_10_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['postcode'] = 'a' * 11
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.postcode.errors, has_item('Field cannot be longer than 10 characters.'))

class TestEmailValidation(unittest.TestCase):
    def test_email_field_allows_email_addresses(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.email.errors, has_length(0))

    def test_email_field_can_be_no_longer_than_320_characters(self):
        # given
        entered_data = complete_form_data()
        entered_data['email'] = 'a' * 321
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.email.errors, has_item('Field cannot be longer than 320 characters.'))

    def test_email_field_only_allows_correctly_formatted_email_addresses(self):
        # given
        entered_data = complete_form_data()
        entered_data['email'] = 'not an email address'
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.email.errors, has_item('Invalid email address.'))


class TestTelephoneNumberValidation(unittest.TestCase):
    def test_telephone_number_field_allows_strings(self):
        # given
        entered_data = complete_form_data()
        # when
        form = complete_form(entered_data)
        form.validate()
        # then
        assert_that(form.telephone_number.errors, has_length(0))

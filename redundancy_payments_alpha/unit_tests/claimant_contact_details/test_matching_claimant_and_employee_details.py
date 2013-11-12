import unittest
from redundancy_payments_alpha.claimants_user_journey import routes
from hamcrest import *
from BeautifulSoup import BeautifulSoup

class TestMatchingClaimantAndEmployeeDetails(unittest.TestCase):
    def test_claimant_is_sent_to_nino_not_found_page(self):
        test_app = routes.app.test_client()
        response = test_app.get('/claim-redundancy-payment/employee-records/?nino=AB999999C')
        assert_that(response.status_code, is_(200))
        page = BeautifulSoup(response.data)
        assert_that(page.find('h1').text, contains_string('No Employee Record Found'))

    def test_claimant_is_shown_employee_record_for_nino(self):
        test_app = routes.app.test_client()
        response = test_app.get('/claim-redundancy-payment/employee-records/?nino=AB111111C')
        assert_that(response.status_code, is_(200))
        page = BeautifulSoup(response.data)
        assert_that(page.find('h1').text, contains_string('Your Employee Record'))
        assert_that(page.find('pre').text, contains_string('John'))

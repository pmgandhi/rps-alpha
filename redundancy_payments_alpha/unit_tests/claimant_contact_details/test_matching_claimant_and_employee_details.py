import unittest
from redundancy_payments_alpha.claimants_user_journey import routes
from hamcrest import *


class TestMatchingClaimantAndEmployeeDetails(unittest.TestCase):
    def test_claimant_is_sent_to_nino_not_found_page(self):
        test_app = routes.app.test_client()
        response = test_app.get('/claim-redundancy-payment/employee-records/?nino=Ab999999C')
        assert_that(response.status_code, is_(200))
        assert_that(response.data, contains_string('Employee record not found'))

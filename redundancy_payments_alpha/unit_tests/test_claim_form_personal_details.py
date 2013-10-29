import unittest
import sys
import os
from claimants_user_journey import routes

sys.path.insert(0, os.path.join('..', 'claimants_user_journey'))

test_client = routes.app.test_client()


#class TestStatus(unittest.TestCase):
#    def test_first_name_field_is_shown(self):
#        response = test_client.get('/_not_status')
#        self.assertEqual(response.data, 'everything is ok')

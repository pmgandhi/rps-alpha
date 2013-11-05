from ...employer_form import routes
import unittest

test_client = routes.app.test_client()

class TestEmployerForm(unittest.TestCase):
    def test_employer_form(self):
        response = test_client.get('/create-insolvency-case/employer-details/')
        self.assertEqual(response.status_code, 200)

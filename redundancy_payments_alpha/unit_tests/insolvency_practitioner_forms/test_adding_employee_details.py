from hamcrest import *

from ...insolvency_practitioner_forms import routes
import form_test


class TestAddingEmployeeDetails(form_test.FormTest):
    def setUp(self):
        self.app = routes.app.test_client()

    def employee_data(self, **kwargs):
        employee_data = {
            'employer_name': 'Widgets Co.',
            'employee_title': 'Other',
            'employee_title_other': 'Doctor',
            'employee_forenames': 'J',
            'employee_surnames': 'Smith',
            'employee_weekly_pay_day': 'monday' 
        }
        employee_data.update(kwargs)
        return employee_data

    def test_posting_complete_employee_details_redirects_to_employee_added_page(self):
        response = self.submit_form(
            self.app,
            '/create-employee-record/employee-details/',
            self.employee_data()
        )
        assert_that(response.status_code, is_(302))
        assert_that(response.headers, has_entry('Location', contains_string('/create-employee-record/employee-added/')))

    def test_posting_empty_employee_details_keeps_submitter_on_form_page(self):
        response = self.submit_form(
            self.app,
            '/create-employee-record/employee-details/',
            {}
        )
        assert_that(response.status_code, is_(200))


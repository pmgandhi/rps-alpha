from behave import *
from ..employer_form import routes


@given('the employer information')
def step(context):
    employer_information = {}
    for field_name, value in context.table:
        employer_information[field_name] = value
    context.employer_information = employer_information

@when('the insolvency practitioner submits the employer information')
def step(context):
    other_test_client = routes.app.test_client()
    print test_client.get('/_status/').data, '<---------------------'
    csrf_token = None
    context.employer_information['csrf_token'] = csrf_token
    response = test_client.post(
        '/create-insolvency-case/employer-details/',
        data=context.employer_information
    )
    assert_that(response.status_code, is_(200))


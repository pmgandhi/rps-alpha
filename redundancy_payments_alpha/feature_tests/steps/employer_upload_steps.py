from behave import *
from ..employer_form import routes

test_client = routes.app.test_client()

@given('the employer information')
def step(context):
    employer_information = {}
    for field_name, value in context.table:
        employer_information[field_name] = value
    context.employer_information = employer_information

@when('the insolvency practitioner submits the employer information')
def step(context):
    test_client.get('/create-insolvency-case/employer-details')
    # some code to get csrf token
    csrf_token = None
    context.employer_information['csrf_token'] = csrf_token
    test_client.post(
        '/create-insolvency-case/employer-details',
        data=context.employer_information
    )


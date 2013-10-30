from behave import *
from hamcrest import *
from claimants_user_journey import routes
from BeautifulSoup import BeautifulSoup

test_client = routes.app.test_client()


def parse_csrf_token(response):
    # in order to post form data back to the app
    # we need to also send back the csrf token
    page = BeautifulSoup(response.data)
    csrf_token = page.find('input', id='csrf_token')['value']
    return csrf_token


@given('a claimant with the personal details')
def step(context):
    context.form_data = {}
    for row in context.table:
        context.form_data[row['DETAILS']] = row['VALUE']


@when('the claimant goes to /claimant-contact-details')
def step(context):
    personal_details_form = test_client.get('/claimant-contact-details')
    context.form_data['csrf_token'] = parse_csrf_token(personal_details_form)


@when('enters their details')
def step(context):
    context.response_from_posting_data = test_client.post(
        '/claimant-contact-details',
        data=context.form_data
    )


@then('the claimant should be sent to the /done page')
def step(context):
    assert_that(context.response_from_posting_data.status, is_('302 FOUND'))
    headers = context.response_from_posting_data.headers
    redirect_path = headers['Location'].split('/')[-1]
    assert_that(redirect_path, is_('done'))


@then('the claimant should stay on the /claimant-contact-details page')
def step(context):
    page = BeautifulSoup(context.response_from_posting_data.data)
    title = page.find('title').text
    assert_that(title, is_('Claimant Contact Details'))

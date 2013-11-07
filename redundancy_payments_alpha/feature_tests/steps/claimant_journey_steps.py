from hamcrest import *
from BeautifulSoup import BeautifulSoup

@then('the claimant should stay on {url} with title "{expected_title}"')
def step(context, url, expected_title):
    page = BeautifulSoup(context.response_from_posting_data.data)
    title = page.find('title').text
    assert_that(title, is_(expected_title))

@then('the claimant should be redirected')
def step(context):
    assert_that(context.response_from_posting_data.status, is_('302 FOUND'))

@then('the form should display error message "{message}"')
def step(context, message):
    assert_that(context.response_from_posting_data.data, contains_string(message))

@when('the claimant goes to {url}')
def step(context, url):
    form = test_client.get(url)
    context.form_data['csrf_token'] = parse_csrf_token(form)


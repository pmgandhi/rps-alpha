from behave import *
from hamcrest import *
from ..claimants_user_journey import routes

@given('the app is running')
def step(context):
    context.client = routes.app.test_client()

@when('we visit the {url} page')
def step(context, url):
    context.response = context.client.get(url)

@then('the page should include "{content}"')
def step(context, content):
    assert_that(context.response.data, contains_string(content))

@then('the page should have title "{expected_title}"')
def step(context, expected_title):
    assert_that(context.response.data,
                contains_string('<title>%s</title>' % expected_title))

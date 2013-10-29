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
    assert_that(context.response.data, is_(content))

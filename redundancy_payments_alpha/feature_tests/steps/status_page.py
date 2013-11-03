from behave import *
from hamcrest import *

@given('the app is running')
def step(context):
    assert_that(context.app.is_running())

@when('we visit {url}')
def step(context, url):
    context.browser.visit(context.app.root + url)

@then('the page should include "{content}"')
def step(context, content):
    assert_that(context.browser.is_text_present(content))

@then('the page should have title "{expected_title}"')
def step(context, expected_title):
    assert_that(context.browser.title, is_(expected_title))

@then('the page should have an input field called "{input_name}" labeled "{label_name}"')
def step(context, input_name, label_name):
    #TODO: better testing for HTML elements
    assert_that(context.response.data, contains_string('name="%s"' % input_name))
    assert_that(context.response.data, contains_string('%s</label>' % label_name))

from behave import *
from hamcrest import *
from claimants_user_journey import routes
from test_support.pages import ClaimantsDetailsForm


@given('a claimant with the personal details')
def step(context):
    context.form_data = {}
    for row in context.table:
        context.form_data[row['DETAILS']] = row['VALUE']


@when('the claimant goes to {url}')
def step(context, url):
    context.browser.visit(context.app.root + url)


@when('enters their details')
def step(context):
    form = ClaimantsDetailsForm(context.browser)
    for name, value in context.form_data.items():
        form.set_input(name, value)
    form.submit()


@then('the claimant should be sent to {url}')
def step(context, url):
    current_url = context.browser.url
    assert_that(current_url, contains_string(url))


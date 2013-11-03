from hamcrest import *

@then('the claimant should stay on {url} with title "{expected_title}"')
def step(context, url, expected_title):
    title = context.browser.title
    assert_that(title, is_(expected_title))


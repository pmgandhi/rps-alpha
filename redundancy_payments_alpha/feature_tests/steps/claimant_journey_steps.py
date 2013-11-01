from hamcrest import *
from BeautifulSoup import BeautifulSoup

@then('the claimant should stay on {url} with title "{expected_title}"')
def step(context, url, expected_title):
    page = BeautifulSoup(context.response_from_posting_data.data)
    title = page.find('title').text
    assert_that(title, is_(expected_title))
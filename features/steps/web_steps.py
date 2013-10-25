import os
import re
from behave import *
from flask import json
from hamcrest import *
from dateutil import parser
import pytz

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), '..', 'fixtures')


@when('I go to "{query}"')
def step(context, query):
    context.response = context.client.get(query)


@then('I should get back a status of "{expected_status}"')
def step(context, expected_status):
    assert_that(context.response.status_code, is_(int(expected_status)))

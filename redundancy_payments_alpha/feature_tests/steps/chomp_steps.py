from chomp.api import evaluate_forms
from hamcrest import *

@then('the chomp service should generate an xml payload containing {name}')
def step(context, name):
    xml_payload = evaluate_forms()
    assert_that(xml_payload, string_contains_in_order(name))


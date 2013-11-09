from hamcrest import assert_that, is_, has_item, none
import json
from functools import partial
from xml.dom.minidom import parseString
import xpath

# sut:
from ..chomp import generate_rp14_request

EMPLOYER_DETAILS_JSON = """
{
    "employer_details": {
        "company_name": "Scrooge McDuck Enterprises",
        "date_of_insolvency": "23/13/2013",
        "company_number": "not-in-minimum",
        "nature_of_business": "not-in-minimum",
        "type_of_insolvency": "Creditors Voluntary Liquidation",
        "insolvency_practitioner_name": "Lewis, Lewis and Lewis",
        "insolvency_practitioner_registration": "whatever",
        "insolvency_practitioner_firm": "whatever",
        "address_line_1": "whatever",
        "address_line_2": "whatever",
        "address_line_3": "whatever" ,
        "town_or_city": "whatever",
        "postcode": "whatever",
        "country": "whatever",
        "email_address" : "whatever",
        "telephone_number": "whatever"
    }
}
"""

from xml.dom.minidom import parseString
import xpath

def get_value_from_xpath(xml_doc, xpath_sel):
    """This is a test helper method which gets an attribute name and returns its
    content from an xml fragment using xpath.
    """
    # http://stackoverflow.com/questions/5572247/how-to-find-xml-elements-via-xpath-in-python-in-a-namespace-agnostic-way
    xml_dom = parseString(xml_doc)
    try:
        return xpath.findvalues(xpath_sel, xml_dom)[0]
    except IndexError:
        return None


def check_json_is_mapped_into_xml(json_attribute, xpath_location ):
    """Assertions on the xml payload to ensure that the json value has been populated
    as expected
    TODO: Use Xpath rather than find
    """
    # given
    employer_json = json.loads(EMPLOYER_DETAILS_JSON)["employer_details"]
    # when
    xml_payload = generate_rp14_request(employer_json)
    xml_value = get_value_from_xpath(xml_payload, xpath_location)
    # then
    assert_that(employer_json, has_item(json_attribute))
    assert_that(xml_value, not none() )
    assert_that(employer_json[json_attribute], is_(xml_value))

def test_claimant_information_json_is_mapped_to_valid_champ_xml():
    """Generator of unit tests for each field we currently support.
    """
    # for these fields
    field_mapping = {
        "company_name" : "//rp14:NameOfBusiness",
        "date_of_insolvency" : "//rp14:InsolvencyDate",
        "type_of_insolvency" : "//rp14:InsolvencyType",
        "insolvency_practitioner_name" : "//rp14:PayRecordsContact/rp14:Name"
    }
    # test that
    for json_attribute, xpath_location in field_mapping.iteritems():
        generated_test = partial(check_json_is_mapped_into_xml, json_attribute, xpath_location)
        generated_test.description = '%s is mapped to %s in xml payload' % (json_attribute, xpath_location)
        yield generated_test,






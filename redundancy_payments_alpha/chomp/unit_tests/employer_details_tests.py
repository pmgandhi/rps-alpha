from hamcrest import assert_that, is_, has_item, none
from bs4 import BeautifulSoup
import json

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
        "insolvency_practitioner_name": "whatever",
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

def get_xml_attribute_from(xml_fragment, attr_name):
    """This is a test helper method which gets an attribute name and returns its
    content from an xml fragment.
    """
    xml_soup = BeautifulSoup(xml_fragment, "xml")
    get_from_attr = xml_soup.find(attr_name)
    if get_from_attr:
        return get_from_attr.contents[0]
    else:
        return None

def check_json_is_mapped_into_xml(xml_attribute, json_attribute ):
    """Assertions on the xml payload to ensure that the json value has been populated
    as expected
    TODO: Use Xpath rather than find
    """
    # given
    employer_json = json.loads(EMPLOYER_DETAILS_JSON)["employer_details"]
    # when
    xml_payload = generate_rp14_request(employer_json)
    # then
    assert_that(employer_json, has_item(json_attribute) )
    assert_that(get_xml_attribute_from(xml_payload, xml_attribute), not none() )
    assert_that(employer_json[json_attribute], is_(get_xml_attribute_from(xml_payload, xml_attribute)))

def test_claimant_information_json_is_mapped_to_valid_champ_xml():
    """Generator of unit tests for each field we currently support.
    """
    # for these fields
    field_mapping = {
        "company_name" : "NameOfBusiness",
        "date_of_insolvency" : "InsolvencyDate",
        "type_of_insolvency" : "InsolvencyType",
        "insolvency_practitioner_name" : "Name"
    }
    # test that
    for json_attribute, xml_attribute in field_mapping.iteritems():
        yield check_json_is_mapped_into_xml, xml_attribute, json_attribute






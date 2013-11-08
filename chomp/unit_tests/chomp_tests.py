from hamcrest import assert_that, is_, greater_than_or_equal_to, has_item
from bs4 import BeautifulSoup
import json

# sut:
from ..chomp import generate_rp14_request

EMPLOYER_DETAILS_JSON = """
{
    "employer_details": {
        "company_name": "Scrooge McDuck Enterprises",
        "date_of_insolvency": "whatever"
    }

}
"""

def get_xml_attribute_from(xml_fragment, attr_name):
    """This is a test helper method which gets an attribute name and returns its
    content from an xml fragment.
    """
    xml_soup = BeautifulSoup(xml_fragment, "xml")
    return xml_soup.find(attr_name).contents[0]

def check_xml_is_populated_from_json(xml, xml_attribute, json_attribute, json):
    """Assertions on the xml payload to ensure that the json value has been populated
    as expected
    TODO: Use Xpath rather than find
    """
    assert_that(json, has_item(json_attribute) )
    assert_that(json[json_attribute], is_(get_xml_attribute_from(xml, xml_attribute)))

def test_claimant_information_json_is_mapped_to_valid_champ_xml():
    # given
    employer_json = json.loads(EMPLOYER_DETAILS_JSON)["employer_details"]
    # when
    xml_payload = generate_rp14_request(employer_json)
    # for
    field_mapping = {
        "NameOfBusiness" : "company_name",
        "InsolvencyDate" : "date_of_insolvency",
    }
    # then
    for xml_attribute, json_attribute in field_mapping.iteritems():
        yield check_xml_is_populated_from_json, xml_payload, xml_attribute,\
              json_attribute, employer_json






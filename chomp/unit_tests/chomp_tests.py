from hamcrest import assert_that, is_, greater_than_or_equal_to
from bs4 import BeautifulSoup
import json

# sut:
from ..chomp import generate_dms_id, generate_rp14_request

def test_law_of_excluded_middle():
    """Testing the longstanding Aristotelian axiom.
    """
    assert_that(True, is_(True))

def test_should_generate_non_conflicting_dms_id():
    """Wisdom already generates DMS ids upto 9 digits long and therefore we need to generate
    ids which are longer.
    """
    # when
    dms_id = generate_dms_id()
    # then
    assert_that(type(dms_id), is_(type(str)))
    assert_that(len(dms_id), greater_than_or_equal_to(10))


HAPPY_PATH_EMPLOYER_DETAILS_JSON = """
{
    "employer_details": {
        "company_name": "THE EGG CAME FIRST"
    }

}
"""

def get_xml_attribute_from(xml_fragment, attr_name):
    """This is a test helper method which gets an attribute name and returns its
    content from an xml fragment.
    """
    xml_soup = BeautifulSoup(xml_fragment, "xml")
    return xml_soup.find("NameOfBusiness").contents[0]

def test_happy_rp1_json_is_mapped_to_valid_champ_xml():
    # given
    employer_json = json.loads(HAPPY_PATH_EMPLOYER_DETAILS_JSON)["employer_details"]
    # when
    xml_payload = generate_rp14_request(employer_json)
    # then
    assert_that(employer_json['company_name'], is_(get_xml_attribute_from(xml_payload, "company_name")))





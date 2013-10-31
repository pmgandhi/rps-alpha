import json
from pprint import pprint
from jinja2 import Template
from random import randint

""" This code should read in a json object from a file, and an xml template from a file
    and then merge the data from the json into the xml payload.

    It should then fire the xml payload at an endpoint (configurable) and display the
    response back to the user.

    It needs to work on Windows.
"""

def read_json_from(filename):
    """This code should read in a json object from a file,
    """
    with open(JSON_FILENAME) as f:
        data = json.load(f)
    return data

def read_xml_template_from(filename):
    """This code should read in a xml template from a file,
    """
    with open(filename) as f:
        template=f.read()
    return template

def generate_dms_id():
    """This function just returns a random DMS id, while we are not integrating with Wisdom
    """
    return randint(6000000000,7000000000)


JSON_FILENAME = "rp1-data-from-week-1-webform.json"
ACCEPT_DOC_XML_FILENAME = "CHAMP_Accept_Doc.xml.template"
RP1_XML_FILENAME = "CHAMP_Submit_RP1.xml.template"

def generate_accept_doc_request(dms_id):
    xml_template = read_xml_template_from(ACCEPT_DOC_XML_FILENAME)
    template = Template(xml_template)
    return template.render(dmsid=dms_id)

def generate_rp1_request(dms_id, json_data):
    xml_template = read_xml_template_from(RP1_XML_FILENAME)
    template = Template(xml_template)
    dms_dict = {'dmsid': json_data}
    return template.render(dms_dict.update(json_data))

if __name__=="__main__":
    dms_id = generate_dms_id()
    json_data = read_json_from(JSON_FILENAME)
    # print generate_accept_doc_request(dms_id)
    print generate_rp1_request(dms_id, json_data)
    # print json_data










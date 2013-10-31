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

JSON_FILENAME = "rp1-data-from-week-1-webform.json"
ACCEPT_DOC_XML_FILENAME = "CHAMP_Accept_Doc.xml.template"
RP1_XML_FILENAME = "CHAMP_Submit_RP1.xml.template"
ACCEPT_DOC_PAYLOAD_FILENAME = "CHAMP_Accept_Doc-Payload.xml"
RP1_XML_PAYLOAD_FILENAME = "CHAMP_Submit_RP1-Payload.xml"

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

def generate_accept_doc_request(dms_id):
    """This function just takes a dms_id and returns a long string which is an accept_doc request
    """
    xml_template = read_xml_template_from(ACCEPT_DOC_XML_FILENAME)
    template = Template(xml_template)
    return template.render(dmsid=dms_id)

def generate_rp1_request(dms_id, json_data):
    """This function takes a dms_id and a json struct and returns a long string which is a rp1 request
    """
    xml_template = read_xml_template_from(RP1_XML_FILENAME)
    template = Template(xml_template)
    dms_dict = {'dmsid': dms_id}
    json_data.update(dms_dict)
    return template.render(json_data)

def write_out_to_file(payload, filename):
    """This function...
    """
    with open(filename, 'w') as f:
        f.write(payload)


if __name__=="__main__":
    dms_id = generate_dms_id()
    json_data = read_json_from(JSON_FILENAME)
    write_out_to_file(generate_accept_doc_request(dms_id), ACCEPT_DOC_PAYLOAD_FILENAME)
    write_out_to_file(generate_rp1_request(dms_id, json_data), RP1_XML_PAYLOAD_FILENAME)










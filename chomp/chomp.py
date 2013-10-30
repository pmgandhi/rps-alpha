import json
from pprint import pprint

""" This code should read in a json object from a file, and an xml template from a file
    and then merge the data from the json into the xml payload.

    It should then fire the xml payload at an endpoint (configurable) and display the
    response back to the user.

    It needs to work on Windows.
"""

def read_json_from(filename):
    """This code should read in a json object from a file,
    """
    with open(FILENAME) as f:
        data = json.load(f)
    return data

def read_xml_template_from(filename):
    """This code should read in a xml template from a file,
    """
    with open(FILENAME) as f:
        data = json.load(f)
    return data

FILENAME = "rp1-data-from-week-1-webform.json"

if __name__=="__main__":
    print pprint(read_json_from(FILENAME))




from birmingham_cabinet.api import get_rp1_form
from payload_generator import generate_claimant_information_submit_request

import json

def evaluate_forms():
    claim_json = get_rp1_form()
    claim = json.loads(claim_json)
    return generate_claimant_information_submit_request(claim)


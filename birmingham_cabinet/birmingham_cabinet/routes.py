import json

from flask import Flask, request

app = Flask(__name__)
app.debug = True

database = {}

@app.route("/claimant-contact-details/<key>", methods=["POST"])
def add_claimaint_contact_details(key):
    database[key] = request.get_json()
    return json.dumps(None), 201

@app.route("/claimant-contact-details/<key>", methods=["GET"])
def claimant_contact_details(key):
    return json.dumps(database[key])

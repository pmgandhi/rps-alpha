from flask import Flask, render_template


app = Flask(__name__)


@app.route('/_status', methods=['GET'])
def status():
    return "everything is ok"


@app.route('/claimant-contact-details', methods=['GET'])
def claimant_contact_details():
    return render_template('user_details.html')

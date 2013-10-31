import json
from flask import Flask, render_template, url_for, session
from werkzeug.utils import redirect
from forms.claimant_contact_details import ClaimantContactDetails


app = Flask(__name__)
app.secret_key = 'something_secure_and_secret'
app.debug = True


@app.route('/_status', methods=['GET'])
def status():
    return "everything is ok"


@app.route('/claimant-contact-details', methods=['GET', 'POST'])
def claimant_contact_details():
    form = ClaimantContactDetails()
    if form.validate_on_submit():
        session['user_details'] = form.data
        return redirect(url_for('done'))
    return render_template('user_details.html', form=form)


@app.route('/done', methods=['GET'])
def done():
    user_details_json = json.dumps(session.get('user_details'))
    return render_template('done.html', user_details=user_details_json)

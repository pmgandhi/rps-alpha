import json
from flask import Flask, render_template, url_for, session
from werkzeug.utils import redirect
from forms.claimant_contact_details import ClaimantContactDetails
from forms.employment_details import EmploymentDetails


app = Flask(__name__)
app.secret_key = 'something_secure_and_secret'
app.debug = True


def nav_links():
    links = [
        ('Start', url_for('start')),
        ('Personal Details', url_for('personal_details')),
        ('Employment Details', url_for('employment_details')),
        ('Wage Details', url_for('wage_details')),
        ('Summary', url_for('summary')),
        ('Wage Details', url_for('wage_details')),
    ]
    return links


@app.route('/_status', methods=['GET'])
def status():
    return "everything is ok"


@app.route('/claim-redundancy-payment/', methods=['GET'])
@app.route('/', methods=['GET'])
def claim_redundancy_payment():
    return redirect(url_for('start'))


@app.route('/claim-redundancy-payment/start/')
def start():
    return render_template('start.html', nav_links=nav_links())


@app.route('/claim-redundancy-payment/personal-details/', methods=['GET', 'POST'])
def personal_details():
    existing_form = session.get('user_details')
    
    if existing_form:
        form = ClaimantContactDetails(**existing_form)
    else:
        form = ClaimantContactDetails()

    if form.validate_on_submit():
        session['user_details'] = form.data
        return redirect(url_for('employment_details'))
    return render_template('user_details.html', form=form, nav_links=nav_links())
    

@app.route('/claim-redundancy-payment/employment-details/', methods=['GET', 'POST'])
def employment_details():
    existing_form = session.get('employment_details')

    if existing_form:
        form = EmploymentDetails(**existing_form)
    else:
        form = EmploymentDetails()

    if form.validate_on_submit():
        session['employment_details'] = form.data
        return redirect(url_for('summary'))

    return render_template('employment_details.html', form=form, nav_links=nav_links())

@app.route('/claim-redundancy-payment/wage-details/', methods=['GET'])
def wage_details():
    return render_template('wage_details.html', nav_links=nav_links())


@app.route('/claim-redundancy-payment/summary/', methods=['GET'])
def summary():
    summary = {
        'claimant_details': session.get('user_details'),
        'employment_details': session.get('employment_details')
    }
    summary_json = json.dumps(summary, indent=4)
    return render_template('summary.html', summary=summary_json, nav_links=nav_links())


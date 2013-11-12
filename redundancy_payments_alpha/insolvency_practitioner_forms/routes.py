from flask import Flask, url_for, request, render_template, session
from werkzeug.utils import redirect
from forms.employer_details_form import EmployerDetailsForm
from forms.employee_details_form import EmployeeDetailsForm
from birmingham_cabinet import api
from insolvency_practitioner_forms.mapper import mapper

app = Flask(__name__)
app.secret_key = 'i_am_a_secret'
app.debug = True


@app.route('/create-insolvency-case/employer-details/', methods=['GET', 'POST'])
def employer_details():
    form = EmployerDetailsForm()
    if form.validate_on_submit():
        return redirect(url_for('case_created'))
    else:
        return render_template('insolvency_case_form.html', form=form)


@app.route('/create-insolvency-case/case-created/', methods=['GET'])
def case_created():
    return 'ok'

import json

@app.route('/create-employee-record/employee-details/', methods=['GET','POST'])
def employee_details():
    form = EmployeeDetailsForm()
    # introduce the mapper here
    if form.validate_on_submit():
        # this method calls into the datalayer
        # the type passed in should be one the form has already mapped to match the service's contract
        #print type(form.data["employee_date_of_birth"])
        #raise Exception
        brum_cab_rp14a_create_json_request = mapper(form.data)
        api.add_rp14a_form(brum_cab_rp14a_create_json_request)
        return redirect(url_for('employee_added'))
    print form.errors
    return render_template('employee_details_form.html', form=form)


@app.route('/create-employee-record/employee-added/')
def employee_added():
    return 'ok'


if __name__ == '__main__':
    app.run()


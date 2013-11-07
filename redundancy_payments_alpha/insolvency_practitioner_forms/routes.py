from flask import Flask, url_for, request, render_template
from werkzeug.utils import redirect
from forms.employer_details_form import EmployerDetailsForm

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


if __name__ == '__main__':
    app.run()


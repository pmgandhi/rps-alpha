from flask import Flask

app = Flask(__name__)
app.secret_key = 'i_am_a_secret'
app.debug = True


@app.route('/create-insolvency-case/employer-details/', methods=['GET'])
def employer_details():
    return 'ok'

from flask import Flask

app = Flask(__name__)
app.secret_key = 'i_am_a_secret'
app.debug = True


app.route('/foo/', methods=['GET'])
def foo():
    return 'ok'


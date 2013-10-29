from flask import Flask

app = Flask(__name__)

@app.route('/_status', methods=['GET'])
def status():
    return "everything is ok"


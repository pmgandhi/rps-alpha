import datetime
import json
from os import getenv
from bson import ObjectId

from flask import Flask, jsonify, request, redirect, render_template
from flask_featureflags import FeatureFlag
import database


app = Flask(__name__)

feature_flags = FeatureFlag(app)

# Configuration
app.config.from_object(
    "claim.config.%s" % getenv("CLAIM_ENV", "development")
)

db = database.Database(
    app.config['MONGO_HOST'],
    app.config['MONGO_PORT'],
    app.config['DATABASE_NAME']
)


@app.route('/_status', methods=['GET'])
def health_check():
    if db.alive():
        return jsonify(status='ok', message='database seems fine')
    else:
        return jsonify(status='error',
                       message='cannot connect to database'), 500


@app.route('/claim')
def start_claim():
    return render_template('claim.html')


@app.route('/')
def index():
    return redirect('/claim')


def start(port):
    app.debug = True
    app.run(host='0.0.0.0', port=port)

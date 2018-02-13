from flask import Flask, jsonify
import pandas as pd

# initialize app
app = Flask(__name__)



#
@app.route("/api/v1.0")
def index():
    print('Someone has visited the index page')
    return "Welcome to the index page."

@app.route("/api/v1.0/precipitation")
def precipitation():
    print('Someone has visited the precipitation page')

@app.route("/api/v1.0/stations")
def stations():
    print('Someone has visited the stations page')

@app.route("/api/v1.0/tobs")
def tobs():
    print('Someone has visited the temperature page')

@app.route("/api/v1.0/<start>")
def start():
    print('Someone has visited the start page')

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    print("Someone has visited the start/end page")


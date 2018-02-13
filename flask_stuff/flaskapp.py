from flask import Flask, jsonify
import pandas as pd

# initialize app
app = Flask(__name__)

# outline filepath for CSVs
csv1 = ("../SurfsUp/Output/measurements_clean.csv")
csv2 = ("../SurfsUp/Output/stations_clean.csv")

# read in CSVs for later manipulation
measurements = pd.DataFrame(pd.read_csv(csv1))
stations = pd.DataFrame(pd.read_csv(csv2))

# isolate date and precipitation, convert to dict to prepare for delivery
prcp_dict = measurements[['date', 'prcp']].set_index('date').to_dict()

stat_dict = stations['']

@app.route("/api/v1.0")
def index():
    print('Someone has visited the index page')
    return "Welcome to the index page."

@app.route("/api/v1.0/precipitation")
def precipitation():
    print('Someone has visited the precipitation page')
    return jsonify(prcp_dict['prcp'])

@app.route("/api/v1.0/stations")
def stations():
    print('Someone has visited the stations page')
    return 

@app.route("/api/v1.0/tobs")
def tobs():
    print('Someone has visited the temperature page')

@app.route("/api/v1.0/<start>")
def start(start):
    print('Someone has visited the start page')

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    print("Someone has visited the start/end page")

if __name__ == "__main__":
    app.run(debug=True)


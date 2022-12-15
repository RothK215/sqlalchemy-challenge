import numpy as np
import datetime
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= '2016-08-23').\
        order_by(Measurement.date).all()
    session.close()

    rain_measurement = []
    format_data = "%Y-%m-%d"

    for date, prcp in results:
        rain_info = {}
        rain_info["date"] = datetime.datetime.strptime(date, format_data)
        rain_info["prcp"] = prcp
        rain_measurement.append(rain_info)
    return jsonify(rain_measurement)

@app.route("/api/v1.0/stations")
def station():
    session = Session(engine)
    results = session.query(Station.station)
    session.close()

    bs = []

    for station in results:
        stast = {}
        stast["station"]=station
        bs.append(stast)
    return jsonify(results)

#@app.route("/api/v1.0/tobs")
#def tobs():
#    session = Session(engine)
#   results = session.query(Measurement.date, Measurement.tobs).\
#            filter(Measurement.station >= 'USC00519281').\
#            filter(Measurement.date >= '2016-08-18').\
#            order_by(Measurement.date).all()
#    session.close()
#    temp = list(np.ravel(results))
#    return jsonify(temp)

#@app.route("/api/v1.0/<start>")

#@app.route("/api/v1.0/<start>/<end>")

if __name__ == '__main__':
    app.run(debug=True)
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:////Users/mike1/Git_Repos/sqlalchemy-challenge/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/percipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start"
    )


@app.route("/api/v1.0/percipitation")
def percipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of percipitation between specific data range"""
  
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= "2016-08-23").\
        filter(Measurement.date >= "2017-08-23").all()

    prcp_dict = []
    for tow in results:
        date_dict = {}
        date_dict[row.date] = row.prcp
        prpc_dict.append(date_dict)

    return jsonify(date_dict)



@app.route("/api/v1.0/stations")
def stations():
 
    """Return a JSON list of stations from the dataset"""
 
    results = session.query(Station.station.all()

    #results_list = ravel(results)

    #return jsonify(results)

    
 @app.route("/api/v1.0/tobs")
 def tobs():

#     """Return a JSON list of tobs from between a specific data range"""
#     # query identical to results query for percipitation

   results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2016-08-23").\
        filter(Measurement.date >= "2017-08-23").all()


    return jsonify(results)


# @app.route("/api/v1.0/start")
# def start_date():




# @app.route("/api/v1.0/<start>/<end>")
# def start_end():


#session.close()

# if __name__ == '__main__':
#     app.run(debug=True)
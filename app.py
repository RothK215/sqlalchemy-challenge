# 1. import Flask
from flask import Flask, jsonify

# 2. create an app
app = Flask(__name__)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")

@app.route("/api/v1.0/stations")

@app.route("/api/v1.0/tobs")

@app.route("/api/v1.0/<start>")

@app.route("/api/v1.0/<start>/<end>")

if __name__ == '__main__':
    app.run(debug=False)
#!/usr/bin/python3
"""
script that starts a Flask web application
Requirement:
    web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def city_state():
    """function that list the state elements"""
    cities = storage.all("City").values()
    return render_template("8-cities_by_states.html", cities=cities)


@app.teardown_appcontext
def teardown(exc):
    """method that remove the currentSQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

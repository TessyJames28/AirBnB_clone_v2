#!/usr/bin/python3
"""
script that starts a Flask web application
Requirement:
    web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """function that list the state elements"""
    state = storage.all("State")
    return render_template("7-states_list.html", state=state)


@app.teardown_appcontext
def teardown(exc):
    """method that remove the currentSQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

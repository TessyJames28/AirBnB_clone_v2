#!/usr/bin/python3
"""
script that starts a Flask web application
Requirement:
    web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state_list():
    """function that list the state elements"""
    states = storage.all("State").values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id():
    """function that list the state elements"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def teardown(exc):
    """method that remove the currentSQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

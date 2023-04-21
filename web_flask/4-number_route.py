#!/usr/bin/python3
"""
Script that starts a Flask web application
Requirement:
    web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """function that displays hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """function that returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """function that accepts variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """function that accepts variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def number_n(n):
    """function that displays if variabe is int"""
    try:
        n = int(n)
        return "{} is a number".format(n)
    except Exception:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

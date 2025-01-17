#!/usr/bin/python3
"""0. Hello Flask!"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states_list():
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_db(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""0. Hello Flask!"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models import storage


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states_list_css():
    data = {
    'states' : storage.all(State).values(),
    'amenities': storage.all(Amenity).values(),
    'places': storage.all(Place).values()
    }
    return render_template("100-hbnb.html", models=data)


@app.teardown_appcontext
def close_db(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

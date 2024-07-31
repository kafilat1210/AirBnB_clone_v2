#!/usr/bin/python3
"""Import storage module"""

from flask import Flask, render_template
from models import *
from models import storage

# Create an instance of the Flask class
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Fetch all the State objects from the database and sort them by name"""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_storage(exception):
    """Close the storage after each request"""
    storage.close()


# Run the application on 0.0.0.0 and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
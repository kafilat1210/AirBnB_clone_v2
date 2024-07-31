#!/usr/bin/python3
"""This module starts a Flask web application that displays 'Hello HBNB!',
'HBNB', 'C <text>', 'Python <text>', and a HTML page with 'Number: n'"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function returns 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function returns 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """This function returns 'C <text>' with underscores replaced by spaces"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """This function returns 'Python <text>' with underscores replaced by
    spaces"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """This function returns 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """This function returns a HTML page with 'Number: n'
    only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
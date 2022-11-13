#!/usr/bin/python3
"""
    < 3-PYTHON_ROUTE >

    This script starts a Flask web application that listen on 0.0.0.0 port 5000
    - When query with home '/hbnb' should display "HBNB!"
    - When query with '/c/<text>' should display "C <text>"
    - When query with '/python/(<text>)' should display "Python <text>" with
        default value of text is 'is cool'
    - Replace underscore _ symbols with a space.
    - Also, the option strict_slashes=False is used in route definition.

"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        < Hello >
    This function returns the string "Hello HBNB!" when '/' is requested.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
        < HBNB >
    This function returns the string "HBNB" when '/hbnb' is requested.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
        < C Route >
    This function returns the string "C <text>" when '/c/<text>' is requested.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
        < Python Route >
    This function returns the string "Python <text>" when '/python/<text>'
        is requested.
    Default value of text is 'is cool'.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


# Run the flask app on all addresses
if __name__ == "__main__":
    app.run(host='0.0.0.0')

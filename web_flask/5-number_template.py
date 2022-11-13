#!/usr/bin/python3
"""
    < 5-number_template >

    This script starts a Flask web application that listen on 0.0.0.0 port 5000
    - When query with home '/hbnb' should display "HBNB!"
    - When query with '/c/<text>' should display "C <text>"
    - When query with '/python/(<text>)' should display "Python <text>"
        - default value of text is 'is cool'
    - When query with '/number/<n>' should display "<n> is a number"
        - Only if <n> is an integer.
    - When query with '/number_template/<n>' should display a HTML page
        - Only if <n> is an integer.
        - HTML page: h1 tag--> "Number: <n>" inside the tag BODY
    - Replace underscore _ symbols with a space.
    - Also, the option strict_slashes=False is used in route definition.

"""

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """
        < Number Route >
    This function returns the string "<n> is a number" when '/number/<n>'
        is requested.
    <n> must be an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
        < Number template >
    This function display a html page with n in H1 tag inside BODY
    <n> must be an integer.
    """
    return render_template('5-number.html', n=n)


# Run the flask app on all addresses
if __name__ == "__main__":
    app.run(host='0.0.0.0')

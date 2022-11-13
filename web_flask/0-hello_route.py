#!/usr/bin/python3
"""
        < 0-HELLO_ROUTE >

    This script starts a Flask web application that listen on 0.0.0.0 port 5000
    When query with home '/' should display "Hello HBNB!"
    Also, the option strict_slashes=False is used in route definition.

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


if __name__ == "__main__":
    # Run the flask app on all addresses
    app.run(host='0.0.0.0')

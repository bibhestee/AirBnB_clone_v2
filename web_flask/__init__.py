#!/usr/bin/python3
"""
    < INIT >

This is an initialization file that runs when the web_flask package is imported

"""
from os import putenv

putenv('FLASK_APP', '0-hello_route.py')
putenv('FLASK_ENV', 'development')

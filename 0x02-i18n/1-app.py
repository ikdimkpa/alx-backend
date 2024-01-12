#!/usr/bin/env python3
"""This module sets up a basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = [ "en", "fr" ]

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index_page():
    """This function defines a route for the root URL ('/')"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run()

#!/usr/bin/env python3
"""This module sets up a basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Creates a Config class with the LANGUAGES attribute"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


    app.config.from_object(Config)


    @app.route('/')
    def index_page():
        """This function defines a route for the root URL ('/')"""
        return render_template('3-index.html')


    @babel.localeselector
    def get_locale():
        """Selects a language translation to use for request"""
        return request.accept_languages.best_match(app.config['LANGUAGES'])

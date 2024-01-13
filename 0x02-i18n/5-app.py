#!/usr/bin/env python3
from flask import Flask, render_template, g, request
from flask_babel import Babel

users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE ="UTC"


    app = Flask(__name__)
    babel = Babel(app)
    app.config.from_object(Config)

    @babel.localeselector
    def get_locale():
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
            return request.accept_languages.best_match(app.config["LANGUAGES"])


    def get_user():
        user_id = request.args.get('login_as')
        if user_id in users:
            return users.get(user_id)
        else:
            return None

    @app.before_request
    def before_request():
        g.user = get_user()



    @app.route("/")
    def index():
        return render_template('3-index.html')

if __name__ == "__main__":
    app.run(debug=True)

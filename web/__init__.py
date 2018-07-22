from flask import Flask

from .controllers import site


def create_app(debug=False):

    app = Flask(__name__)

    app.debug = debug
    app.register_blueprint(site)

    return app

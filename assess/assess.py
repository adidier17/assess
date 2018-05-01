from flask import Flask

from .frontend import frontend
from .api import api

import logging
import os

# if a package's __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered.
__all__ = ['create_app']

def create_app(test_config=None):
    """
    Create a Flask app.
    """

    app = Flask(__name__, instance_relative_config=True)
    configure_app(app, test_config)
    configure_blueprints(app)
    configure_logging(app)

    return app


def configure_app(app, test_config=None):
    """
    Configure the Flask app.
    """

    # Load the default configuration
    app.config.from_object('config.default')

    if test_config is None:
        # Load the configuration from the instance folder
        app.config.from_pyfile('config.py')
    else:
        # Load the test config if passed in
        app.config.update(test_config)

    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    #app.config.from_envvar('APP_CONFIG_FILE')


def configure_blueprints(app):
    """
    Configure blueprints in views.
    """

    for bp in [frontend, api]:
        app.register_blueprint(bp)


def configure_logging(app):
    """
    Configure file(info) and email(error) logging.
    """

    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
    info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)


# HTTP error handling
#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404

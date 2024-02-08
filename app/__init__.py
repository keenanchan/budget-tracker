'''
__init__.py

Name: Keenan Chan
Last updated: 24/02/09

Entrypoint for flask app package.
'''

from flask import Flask
# from api import bp as api_bp

# app = Flask(__name__)

# app.register_blueprint(api_bp)


def create_app():
    app = Flask(__name__)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
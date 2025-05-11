"""
The app module, containing the app factory function.
"""

from flask import Flask

from src.settings import ProdConfig


def create_app(config_object=ProdConfig) -> Flask:
    """
    An application factory.
    Args:
        config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)

    from src.routes import bp_base

    app.register_blueprint(blueprint=bp_base)

    from src.routes import bp_blog

    app.register_blueprint(blueprint=bp_blog)

    return app

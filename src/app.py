"""
The app module, containing the app factory function.
"""

from flask import (
    Flask,
    render_template,
)

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

    register_error_handlers(app)

    return app


def register_error_handlers(app):
    """
    Register error handlers.
    """

    def render_error(error):
        """Render error template."""
        error_code = getattr(error, "code", 500)
        return render_template(f"errors/{error_code}.html"), error_code

    for errcode in [404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

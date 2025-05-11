__all__ = (
    "bp_base",
    "bp_blog",
)

from flask import Blueprint

bp_base = Blueprint("base", __name__)
bp_blog = Blueprint("blog", __name__, url_prefix="/blog")

from src.routes import (
    base,
    blog,
)

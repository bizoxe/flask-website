"""
Logging module.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

root_dir = Path(__file__).absolute().parent.parent.parent


def custom_log(app):
    """
    Logging function.
    """
    log_dir = root_dir / "logs"
    log_dir.mkdir(exist_ok=True)

    formatter = logging.Formatter("[%(asctime)s]{%(pathname)s:%(lineno)d}\n%(levelname)s - %(message)s")
    handler = RotatingFileHandler("logs/makeup_website.log", maxBytes=10485760, backupCount=10)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

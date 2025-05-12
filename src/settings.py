"""
Main application settings.
"""

import os

from dotenv import load_dotenv

env_dir = os.path.abspath(os.curdir)
load_dotenv(os.path.join(env_dir, ".env"))


class Config:
    """
    Base configuration.
    """

    SECRET_KEY = os.getenv("SECRET_KEY", "very-secret-key")
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

    SMTP_SERVER_NAME = os.getenv("SMTP_SERVER_NAME", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    MAIL_SENDER = os.getenv("MAIL_SENDER")
    MAIL_RECIPIENT = os.getenv("MAIL_RECIPIENT")
    MAIL_SUBJECT = os.getenv("MAIL_SUBJECT", "Новый клиент!")


class ProdConfig(Config):
    """
    Production configuration.
    """

    ENV = "production"
    DEBUG = False


class DevConfig(Config):
    """
    Development configuration.
    """

    ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    """
    Test configuration.
    """

    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False  # for form validation

from src.app import create_app
from src.settings import (
    DevConfig,
    ProdConfig,
)


def test_prod_conf() -> None:
    app = create_app(config_object=ProdConfig)
    assert app.config["ENV"] == "production"
    assert app.config["DEBUG"] is False


def test_dev_config() -> None:
    app = create_app(config_object=DevConfig)
    assert app.config["ENV"] == "development"
    assert app.config["DEBUG"] is True

import requests
from pathlib import Path

from app import settings
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
lm = LoginManager()
lm.login_view = 'main.login'


def download(url, ofile):
    r = requests.get(url)
    opath = Path(ofile)
    opath.parent.mkdir(parents=True, exist_ok=True)
    with opath.open("w") as f:
        f.write(r.text)


def create_app():
    """Create an application instance."""
    app = Flask(__name__)

    # import configuration
    app.config["DEBUG"] = settings.DEBUG
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI

    # initialize extensions
    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)

    # import blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    if not Path(settings.DEFAULT_VOCABULARY).is_file():
        download(settings.DEFAULT_VOCABULARY_URL, settings.DEFAULT_VOCABULARY)

    return app

"""App config."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from .views import cliente_view  # pylint: disable=wrong-import-position # noqa: 401, 402

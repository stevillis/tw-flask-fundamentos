"""App config."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

csrf = CSRFProtect(app)
csrf.init_app(app)

from .views import cliente_view  # pylint: disable=wrong-import-position # noqa: 401, 402
from .models import cliente_model

"""App config."""

from flask import Flask


app = Flask(__name__)

from .views import cliente_view # pylint: disable=wrong-import-position # noqa: 401, 402

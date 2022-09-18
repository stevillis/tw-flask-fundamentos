"""App settings."""

import os

import dotenv

# Load .env file
dotenv_file = os.path.join("", ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

print(os.environ["DB_NAME"])
DB_NAME = os.environ["DB_NAME"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]

SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
SQLALCHEMY_TRACK_MODIFICATIONS = bool(
    os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
)

SECRET_KEY = os.environ["SECRET_KEY"]

BABEL_DEFAULT_LOCALE = os.environ["BABEL_DEFAULT_LOCALE"]

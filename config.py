"""Flask app configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Flask-SQLAlchemy
    PG_PROTOCOL = environ.get('PG_PROTOCOL')
    PG_USER = environ.get('PG_USER')
    PG_PASSWORD = environ.get('PG_PASSWORD')
    POSTGRES_DB = environ.get ('POSTGRES_DB')
    DB_HOST = environ.get('DB_HOST')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Redis
    REDIS_URL = environ.get('REDIS_URL')

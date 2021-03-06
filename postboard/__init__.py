"""Initialize app."""
from werkzeug.utils import import_string
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_redis import FlaskRedis


db = SQLAlchemy()
login_manager = LoginManager()
redis_client = FlaskRedis()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    cfg = import_string('config.Config')()
    app.config.from_object(cfg)

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    redis_client.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)

        return app

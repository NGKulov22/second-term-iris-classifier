from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def register_blueprints(app):
    from .main import main_bp
    from .data import data_bp
    from .predict import predict_bp
    from .results import results_bp
    from .auth import auth_bp
    from .errors import errors

    app.register_blueprint(main_bp)
    app.register_blueprint(data_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(results_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(errors)



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from . import models
    register_blueprints(app)

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    from . import models
    # Регистрация на Blueprints
    from .main import main_bp
    from .data import data_bp
    from .predict import predict_bp
    from .results import results_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(data_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(results_bp)
    app.register_blueprint(auth_bp)

    return app
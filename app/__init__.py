from flask import Flask
from .extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Инициализация на extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Регистрация на Blueprints
    from .auth import auth_bp
    from .main import main_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)

    return app
from flask import Blueprint, Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager
from flask_recaptcha import ReCaptcha
from .config import config_list
from .db import db

login_manager = LoginManager()

def create_app(config):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config_list[config])
    
    db.init_app(app)
    CORS(app)
    login_manager.init_app(app)
    
    from .main import main_bp
    app.register_blueprint(main_bp)
    
    from .user import user_bp
    app.register_blueprint(user_bp)
    
    from .dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    
    return app
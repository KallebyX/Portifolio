# backend/app.py
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from flask_migrate import Migrate
import os
from backend.utils.screenshot import capturar_screenshot
from backend.routes.main import main as main_blueprint
from backend.config import Config
from backend.models import db, Usuario
from backend.routes.formulario import form as form_blueprint
from backend.routes.contato import contato as contato_blueprint
from backend.routes.admin import admin as admin_blueprint
from backend.auth.google_auth import google_bp
from flask_session import Session
from flask_migrate import upgrade
from flask import Blueprint

load_dotenv()

mail = Mail()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    Session(app)

    mail.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "google.login"

    # Registro dos Blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(form_blueprint)
    app.register_blueprint(contato_blueprint)
    app.register_blueprint(google_bp, url_prefix="/login")
    app.register_blueprint(admin_blueprint)

    migrar_bp = Blueprint('migrar', __name__)

    @migrar_bp.route('/migrar')
    def migrar_banco():
        upgrade()
        return "Migração feita com sucesso!"

    app.register_blueprint(migrar_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    @app.route('/sitemap.xml')
    def sitemap():
        return app.send_static_file('sitemap.xml')

    @app.route('/robots.txt')
    def robots():
        return app.send_static_file('robots.txt')
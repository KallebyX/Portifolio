# backend/app.py
from flask import Flask, render_template
from backend.extensions import mail
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

    # Rotas para SEO e verificação
    @app.route('/sitemap.xml')
    def sitemap():
        return app.send_static_file('sitemap.xml')

    @app.route('/robots.txt')
    def robots():
        return app.send_static_file('robots.txt')
    
    @app.route('/offline.html')
    def offline():
        return render_template('offline.html')

    @app.route('/google8d6a10aad4e7c671.html')
    def google_verification():
        return app.send_static_file('google8d6a10aad4e7c671.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
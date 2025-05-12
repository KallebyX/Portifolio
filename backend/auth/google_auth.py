# auth/google_auth.py
from flask import Blueprint, redirect, url_for, session, request, flash
from authlib.integrations.flask_client import OAuth
from flask_login import login_user, logout_user
from backend.models import db, Usuario
from backend.config import Config

# Blueprint de autenticação
google_bp = Blueprint('google', __name__)

# Configuração OAuth
oauth = OAuth()
google = oauth.register(
    name='google',
    client_id=Config.GOOGLE_CLIENT_ID,
    client_secret=Config.GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

@google_bp.record_once
def init_oauth(setup_state):
    oauth.init_app(setup_state.app)

@google_bp.route('/')
def login():
    return google.authorize_redirect(url_for('google.callback', _external=True))

@google_bp.route('/callback')
def callback():
    token = google.authorize_access_token()
    resp = google.get('https://openidconnect.googleapis.com/v1/userinfo')
    user_info = resp.json()
    email = user_info['email']

    if email != Config.AUTHORIZED_EMAIL:
        flash("Acesso negado. Apenas o administrador pode acessar.", "danger")
        return redirect('/')

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario:
        usuario = Usuario(email=email, nome=user_info.get('name'))
        db.session.add(usuario)
        db.session.commit()

    login_user(usuario)
    flash("Login realizado com sucesso!", "success")
    return redirect(url_for('admin.painel_admin'))

@google_bp.route('/logout')
def logout():
    logout_user()
    flash("Você saiu do sistema.", "info")
    return redirect('/')
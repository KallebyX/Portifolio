import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "S3gur4K3yKalleby123!")

    # Banco de dados dinâmico
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = "filesystem"

    # Configuração do Gmail para envio de e-mails
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_DESTINATARIO = os.getenv('MAIL_DESTINATARIO')

    # OAuth com Google
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    AUTHORIZED_EMAIL = os.getenv("AUTHORIZED_EMAIL")

    # URIs de redirecionamento para OAuth2 Google
    GOOGLE_REDIRECT_URI_DEV  = os.getenv("GOOGLE_REDIRECT_URI_DEV")
    GOOGLE_REDIRECT_URI_PROD = os.getenv("GOOGLE_REDIRECT_URI_PROD")

    # Seleciona a URI correta conforme o ambiente
    if os.getenv("FLASK_ENV", "development") == "production":
        GOOGLE_REDIRECT_URI = GOOGLE_REDIRECT_URI_PROD
    else:
        GOOGLE_REDIRECT_URI = GOOGLE_REDIRECT_URI_DEV
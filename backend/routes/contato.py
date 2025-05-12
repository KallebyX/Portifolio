# routes/contato.py

from flask import Blueprint, request, redirect, url_for, current_app
from flask_mail import Message
from flask import current_app
from flask_mail import Message

contato = Blueprint('contato', __name__)

@contato.route("/enviar-contato", methods=["POST"])
def enviar_contato():
    dados = request.form

    corpo_email = f"""
    Mensagem recebida pelo site - Formulário de Contato:

    Nome: {dados.get('nome', '')}
    Email: {dados.get('email', '')}
    Mensagem: {dados.get('problema', '')}
    """

    msg = Message(
        subject="Mensagem do site - Contato",
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[current_app.config['MAIL_USERNAME']],
        body=corpo_email
    )

    try:
        mail.send(msg)
        return redirect(url_for('main.contato', sucesso=True))
    except Exception as e:
        return f"Erro ao enviar: {str(e)}"
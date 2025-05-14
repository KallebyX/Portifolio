from flask import Blueprint, request, redirect, url_for, current_app
from flask_mail import Message
from backend.extensions import mail  # 👈 IMPORTAR O MAIL CORRETAMENTE!

contato = Blueprint('contato', __name__)

@contato.route("/enviar-contato", methods=["POST"])
def enviar_contato():
    dados = request.form

    corpo_email = f"""
Nova mensagem recebida via formulário de contato do site:

Nome: {dados.get('nome', 'Não informado')}
Email: {dados.get('email', 'Não informado')}
Mensagem:

{dados.get('problema', 'Nenhuma mensagem fornecida')}

Enviado através da Página de Contato do Portfólio de Kalleby Evangelho.
"""

    msg = Message(
        subject="Nova Mensagem de Contato",
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[current_app.config['MAIL_USERNAME']],
        body=corpo_email
    )

    try:
        mail.send(msg)
        return redirect(url_for('main.contato', sucesso=True))
    except Exception as e:
        return f"Erro ao enviar: {str(e)}"
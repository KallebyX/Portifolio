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

{dados.get('mensagem', 'Nenhuma mensagem fornecida')}

Enviado através da Página de Contato do Portfólio de Kalleby Evangelho.
"""

    corpo_email_html = f"""
<h3>Nova mensagem recebida via formulário de contato do site:</h3>
<ul>
  <li><strong>Nome:</strong> {dados.get('nome', 'Não informado')}</li>
  <li><strong>Email:</strong> {dados.get('email', 'Não informado')}</li>
</ul>
<p><strong>Mensagem:</strong><br>{dados.get('mensagem', 'Nenhuma mensagem fornecida')}</p>
<hr>
<small>Enviado através da Página de Contato do Portfólio de Kalleby Evangelho.</small>
"""

    msg = Message(
        subject="Nova Mensagem de Contato",
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[current_app.config['MAIL_USERNAME']],
        body=corpo_email,
        html=corpo_email_html
    )

    try:
        mail.send(msg)
        return redirect(url_for('main.contato', sucesso=True))
    except Exception as e:
        current_app.logger.exception("Erro ao enviar mensagem de contato.")
        flash('❌ Erro ao enviar a mensagem. Tente novamente mais tarde.', 'danger')
        return redirect(url_for('main.contato'))
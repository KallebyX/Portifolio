# routes/formulario.py

import os
from flask import Blueprint, request, redirect, url_for, flash, current_app
from flask_mail import Message
from werkzeug.utils import secure_filename

form = Blueprint('form', __name__)

@form.route("/enviar-formulario", methods=["POST"])
def enviar_formulario():
    # 1. Captura os dados do formulário
    dados = request.form.to_dict()
    arquivo = request.files.get('arquivo_exemplo')

    # 2.1. Obter destinatário do .env ou config
    destinatario = current_app.config.get('MAIL_DESTINATARIO') or os.getenv('MAIL_DESTINATARIO')
    if not destinatario:
        current_app.logger.error("Variável MAIL_DESTINATARIO não encontrada.")
        flash('❌ Destinatário de e-mail não configurado. Entre em contato.', 'danger')
        return redirect(url_for('main.formulario'))

    # 2. Monta a lista de perguntas e respostas em <li>
    perguntas_respostas = ""
    for campo, resposta in dados.items():
        label = campo.replace("_", " ").capitalize()
        perguntas_respostas += f"<li><strong>{label}:</strong> {resposta}</li>"

    # 3. Constroi o template HTML do email
    corpo_email = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta charset="UTF-8">
      <title>Nova Ideia de Projeto</title>
    </head>
    <body style="font-family:Arial,sans-serif;background:#f4f6f8;padding:20px;">
      <div style="max-width:600px;margin:auto;background:#fff;padding:20px;border-radius:8px;">
        <h2 style="color:#007bff;">Nova Ideia de Projeto</h2>
        <ul style="list-style:none;padding:0;">{perguntas_respostas}</ul>
        <p style="font-size:12px;color:#666;">Enviada via Portfólio de Kalleby Evangelho</p>
      </div>
    </body>
    </html>
    """

    # 4. Prepara a mensagem
    remetente = current_app.config.get('MAIL_USERNAME') or os.getenv('MAIL_USERNAME')
    msg = Message(
        subject="🆕 Nova Ideia de Projeto Recebida",
        sender=remetente,
        recipients=[destinatario],
        html=corpo_email
    )

    # 5. Anexa arquivo, se houver
    if arquivo and arquivo.filename:
        filename = secure_filename(arquivo.filename)
        msg.attach(filename, arquivo.content_type, arquivo.read())

    # 6. Obtém a instância Mail sem importar diretamente para evitar circular import
    try:
        mail = current_app.extensions.get('mail')
        if not mail:
            raise RuntimeError("Flask-Mail não está configurado corretamente.")
        mail.send(msg)
        flash('✅ Formulário enviado com sucesso!', 'success')
    except Exception as e:
        current_app.logger.error(f"Erro ao enviar e-mail: {e}")
        flash('❌ Erro ao enviar o formulário. Tente novamente mais tarde.', 'danger')

    # 7. Redireciona de volta ao formulário
    return redirect(url_for('main.formulario'))


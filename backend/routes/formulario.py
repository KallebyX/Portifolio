# routes/formulario.py

import os
from flask import Blueprint, request, redirect, url_for, flash, current_app
from flask_mail import Message
from werkzeug.utils import secure_filename
from backend.extensions import mail

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
    <body style="font-family:Arial,sans-serif;background:#f9f9f9;padding:20px;">
      <div style="max-width:600px;margin:auto;background:#ffffff;padding:30px;border-radius:10px;box-shadow:0 2px 5px rgba(0,0,0,0.1);">
        <h2 style="color:#007bff;">💡 Nova Ideia de Projeto</h2>
        <p>Você recebeu uma nova proposta através do Portfólio de Kalleby Evangelho:</p>
        <ul style="list-style:none;padding:0;font-size:14px;color:#333;">{perguntas_respostas}</ul>
        <hr style="border:none;border-top:1px solid #eee;margin:20px 0;">
        <p style="font-size:12px;color:#999;">Mensagem enviada automaticamente pelo sistema de contato do portfólio.</p>
      </div>
    </body>
    </html>
    """

    # 4. Prepara a mensagem
    remetente = current_app.config.get('MAIL_USERNAME') or os.getenv('MAIL_USERNAME')
    msg = Message(
        subject="💡 Nova Ideia de Projeto Recebida",
        sender=remetente,
        recipients=[destinatario],
        html=corpo_email
    )

    # 5. Anexa arquivo, se houver
    if arquivo and arquivo.filename:
        filename = secure_filename(arquivo.filename)
        msg.attach(filename, arquivo.content_type, arquivo.read())

    # 6. Envia o email usando a instância importada mail
    try:
        mail.send(msg)
        flash('✅ Formulário enviado com sucesso!', 'success')
    except Exception as e:
        current_app.logger.error(f"Erro ao enviar e-mail: {e}")
        flash('❌ Erro ao enviar o formulário. Tente novamente mais tarde.', 'danger')

    # 7. Redireciona de volta ao formulário
    return redirect(url_for('main.formulario'))

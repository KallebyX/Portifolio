# routes/formulario.py
from flask import Blueprint, request, render_template_string, current_app, redirect, url_for
from flask_mail import Message
from flask import current_app

form = Blueprint('form', __name__)

@form.route("/enviar-formulario", methods=["POST"])
def enviar_formulario():
    dados = request.form
    corpo_email = f"""
    Nova ideia de projeto enviada pelo site:

    Nome: {dados.get('nome', '')}
    Email: {dados.get('email', '')}
    WhatsApp: {dados.get('whatsapp', '')}

    Problema: {dados.get('problema', '')}
    Solução: {dados.get('solucao') or dados.get('mensagem', '')}
    Referência: {dados.get('referencia', '')}
    Tipo de projeto: {dados.get('tipo_projeto', '')}
    Funcionalidades: {dados.get('funcionalidades', '')}
    Público-alvo: {dados.get('publico', '')}
    Plataforma: {dados.get('plataforma', '')}
    Prazo: {dados.get('prazo', '')}
    Orçamento: {dados.get('orcamento', '')}
    Observações adicionais: {dados.get('observacoes', '')}
    """

    # Cria a mensagem de email
    msg = Message(
        subject="Nova Ideia de Software",
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[current_app.config['MAIL_USERNAME']]
    )
    msg.body = corpo_email

    # Debug: log e print do corpo de email
    print("DEBUG - corpo_email:\n", corpo_email)
    current_app.logger.info("Enviar formulário - corpo_email:\n%s", corpo_email)

    try:
        current_app.extensions['mail'].send(msg)
        # Para teste, renderiza o corpo do email na resposta
        return render_template_string(
            """
            <h2>Email enviado com sucesso!</h2>
            <p>Veja abaixo o conteúdo que foi enviado:</p>
            <pre>{{ corpo_email }}</pre>
            <a href="{{ url_for('main.formulario') }}">Voltar ao formulário</a>
            """,
            corpo_email=corpo_email
        )
    except Exception as e:
        error_msg = f"Erro ao enviar: {str(e)}"
        current_app.logger.error(error_msg)
        return error_msg
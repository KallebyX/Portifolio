from backend.models import Projeto
from flask import Blueprint, render_template, send_from_directory, current_app, request
import os

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html", mostrar_modal_sucesso=False)

@main.route("/sobre.html")
def sobre():
    return render_template("sobre.html", mostrar_modal_sucesso=False)

@main.route("/projetos.html")
def projetos():
    projetos_db = Projeto.query.order_by(Projeto.ordem.asc(), Projeto.criado_em.desc()).all()
    return render_template("projetos.html", projetos=projetos_db, mostrar_modal_sucesso=False)

@main.route("/formulario.html")
def formulario():
    sucesso = 'sucesso' in request.args
    return render_template("formulario.html", mostrar_modal_sucesso=sucesso)

@main.route("/contato.html")
def contato():
    sucesso = 'sucesso' in request.args
    return render_template("contato.html", mostrar_modal_sucesso=sucesso)

@main.route("/pdf/<path:filename>")
def download_pdf(filename):
    return send_from_directory(os.path.join(current_app.static_folder, "pdf"), filename)

@main.app_errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404

@main.route('/download-curriculo')
def download_curriculo():
    return send_from_directory('static/pdf', 'Kalleby_EvangelhoMota_currículo.pdf', as_attachment=True)

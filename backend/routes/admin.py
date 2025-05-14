# routes/admin.py
from flask import Blueprint, render_template, redirect, request, url_for, flash, current_app, jsonify
from flask_login import login_required, current_user
from backend.utils.screenshot import capturar_screenshot
from backend.models import db, Projeto
import os
from backend.utils.s3_upload import upload_to_s3
from werkzeug.utils import secure_filename

admin = Blueprint('admin', __name__)

# Protege todas as rotas do blueprint para acesso apenas ao e-mail autorizado
@admin.before_request
def restrict_to_authorized_user():
    authorized_email = current_app.config.get("AUTHORIZED_EMAIL")
    if not current_user.is_authenticated or current_user.email != authorized_email:
        return redirect(url_for("google.login"))

# Página principal do painel
@admin.route("/admin")
@login_required
def painel_admin():
    # Ordena projetos pela posição definida (campo 'ordem'), depois por data
    projetos = Projeto.query.order_by(Projeto.ordem.asc(), Projeto.criado_em.desc()).all()
    return render_template("admin.html", projetos=projetos)

# Adicionar novo projeto
@admin.route("/admin/adicionar", methods=["POST"])
@login_required
def adicionar_projeto():
    screenshot_url = capturar_screenshot(request.form.get("site", ""), request.form["nome"])
    ordem_val = int(request.form.get("ordem", 0))
    novo = Projeto(
        nome=request.form["nome"],
        descricao=request.form["descricao"],
        categoria=request.form["categoria"],
        link=request.form["link"],
        imagem=screenshot_url,
        stack=request.form["stack"],
        site=request.form.get("site"),
        ordem=ordem_val
    )
    db.session.add(novo)
    db.session.commit()
    flash("✅ Projeto adicionado com sucesso!", "success")
    return redirect(url_for("admin.painel_admin"))

# Excluir projeto
@admin.route("/admin/excluir/<int:id>")
@login_required
def excluir_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    db.session.delete(projeto)
    db.session.commit()
    flash("❌ Projeto excluído com sucesso.", "danger")
    return redirect(url_for("admin.painel_admin"))

# Editar projeto
@admin.route("/admin/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    if request.method == "POST":
        projeto.nome = request.form["nome"]
        projeto.descricao = request.form["descricao"]
        projeto.categoria = request.form["categoria"]
        projeto.link = request.form["link"]
        projeto.stack = request.form["stack"]
        projeto.ordem = int(request.form.get("ordem", projeto.ordem))
        
        site_url = request.form.get("site", "")
        old_site = projeto.site
        projeto.site = site_url

        acao = request.form.get("acao", "")

        if acao == "gerar_screenshot":
            # Gera uma nova screenshot manualmente
            screenshot_url = capturar_screenshot(site_url, projeto.nome)
            if screenshot_url:
                projeto.imagem = screenshot_url
        else:
            imagem_arquivo = request.files.get('imagem')
            if imagem_arquivo and imagem_arquivo.filename != '':
                # Se o admin enviou nova imagem manualmente
                filename = secure_filename(imagem_arquivo.filename)
                image_url = upload_to_s3(imagem_arquivo, filename)
                projeto.imagem = image_url
            else:
                # Se não enviou imagem e mudou o site, gera nova screenshot automaticamente
                if site_url != old_site or not projeto.imagem:
                    screenshot_url = capturar_screenshot(site_url, projeto.nome)
                    if screenshot_url:
                        projeto.imagem = screenshot_url

        db.session.commit()
        flash("✏️ Projeto atualizado com sucesso!", "info")
        return redirect(url_for("admin.painel_admin"))

    return render_template("editar_projeto.html", projeto=projeto)

@admin.route("/admin/move/<int:id>/<direction>")
@login_required
def move_projeto(id, direction):
    projeto = Projeto.query.get_or_404(id)
    if direction == "up":
        vizinho = Projeto.query.filter(Projeto.ordem < projeto.ordem) \
            .order_by(Projeto.ordem.desc()).first()
    else:
        vizinho = Projeto.query.filter(Projeto.ordem > projeto.ordem) \
            .order_by(Projeto.ordem.asc()).first()
    if vizinho:
        projeto.ordem, vizinho.ordem = vizinho.ordem, projeto.ordem
        db.session.commit()
        flash("Ordem do projeto atualizada!", "success")
    return redirect(url_for("admin.painel_admin"))

@admin.route('/admin/reorder', methods=['POST'])
@login_required
def reorder_projetos():
    """
    Recebe JSON { order: [id1, id2, ...] }
    e atualiza Projeto.ordem conforme a posição.
    """
    data = request.get_json() or {}
    order = data.get('order', [])
    for idx, proj_id in enumerate(order):
        proj = Projeto.query.get(proj_id)
        if proj:
            proj.ordem = idx
    db.session.commit()
    return jsonify({'status': 'ok'}), 200
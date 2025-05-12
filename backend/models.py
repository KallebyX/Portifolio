# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

# Instância global do banco de dados
db = SQLAlchemy()

# Modelo de usuário para login via Google
class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Usuario {self.email}>"

# Modelo de projeto para exibição e gerenciamento no portfólio
class Projeto(db.Model):
    __tablename__ = 'projetos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50))
    link = db.Column(db.String(255))
    imagem = db.Column(db.String(255))  # caminho ou URL
    site = db.Column(db.String(255), nullable=True)
    ordem = db.Column(db.Integer, nullable=False, default=0)  # posição para ordenação
    stack = db.Column(db.String(255))   # tecnologias usadas
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Projeto {self.nome}>"
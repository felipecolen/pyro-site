from _md5 import md5
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

# from app import db

#
# class Usuario(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')
#
#     def __repr__(self):
#         return f'Usuário {self.username}'
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#     def avatar(self, size):
#         digest = md5(self.email.lower().encode('utf-8')).hexdigest()
#         return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'
#
#
# class Categoria(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     titulo = db.Column(db.String(20))
#     descricao = db.Column(db.Text)
#
#     def __repr__(self):
#         return f'Categoria {self.titulo}'
#
#     # def __init__(self, titulo, descricao):
#     #     self.titulo = titulo
#     #     self.descricao = descricao
#
#
# class Noticia(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     titulo = db.Column(db.String(80))
#     conteudo = db.Column(db.Text)
#     data_adicao = db.Column(db.DateTime, index=True, default=datetime.now)
#     data_atualizacao = db.Column(db.DateTime, index=True, default=datetime.now)
#     usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
#
#     def __repr__(self):
#         return f'Notícia {self.titulo} - {self.data_adicao}'
#
#     # def __init__(self, titulo, conteudo):
#     #     self.titulo = titulo
#     #     self.conteudo = conteudo

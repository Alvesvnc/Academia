from .db import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    tipo_usuario = db.Column(db.Enum('personal', 'cliente'), nullable=False)
    data_nascimento = db.Column(db.Date)
    telefone = db.Column(db.String(15))

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    peso = db.Column(db.Numeric(5,2))
    altura = db.Column(db.Numeric(3,2))
    percentual_gordura = db.Column(db.Numeric(5,2))
    massa_magra = db.Column(db.Numeric(5,2))

class Personal(db.Model):
    __tablename__ = 'personal'
    id_personal = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    CREF = db.Column(db.String(50), nullable=False)

class Treino(db.Model):
    __tablename__ = 'treinos'
    id_treino = db.Column(db.Integer, primary_key=True)
    id_personal = db.Column(db.Integer, db.ForeignKey('personal.id_personal'), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    nome_treino = db.Column(db.String(100), nullable=False)

class Exercicio(db.Model):
    __tablename__ = 'exercicios'
    id_exercicio = db.Column(db.Integer, primary_key=True)
    nome_exercicio = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    series = db.Column(db.Integer)
    repeticoes = db.Column(db.Integer)

class TreinoExercicio(db.Model):
    __tablename__ = 'treino_exercicio'
    id_treino = db.Column(db.Integer, db.ForeignKey('treinos.id_treino'), primary_key=True)
    id_exercicio = db.Column(db.Integer, db.ForeignKey('exercicios.id_exercicio'), primary_key=True)

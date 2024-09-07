from flask import Flask, render_template
from database.db import db
from database.model import Usuario, Cliente, Personal, Treino, Exercicio, TreinoExercicio

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/teste")
def teste():
    return "ola corno"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados se elas não existirem
    app.run(debug=True)

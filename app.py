from flask import Flask, render_template, request, redirect, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'seusegredo'

def criar_banco():
    with sqlite3.connect('usuarios.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                login TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                data_registro TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        login = request.form['login']
        senha = request.form['senha']
        data_registro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            with sqlite3.connect('usuarios.db') as conn:
                c = conn.cursor()
                c.execute('INSERT INTO usuarios (nome, login, senha, data_registro) VALUES (?, ?, ?, ?)',
                          (nome, login, senha, data_registro))
                conn.commit()
            return redirect('/sucesso')
        except sqlite3.IntegrityError:
            flash('⚠️ Esse login já está cadastrado. Escolha outro.', 'danger')

    return render_template('index.html')

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    criar_banco()
    app.run(debug=True)

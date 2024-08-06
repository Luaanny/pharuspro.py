from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lualinde'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

@app.route('/dicas')
def dicas():
    return render_template('dicas.html')



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario == 'admin' and senha == 'senha123':
        return 'Bem Vindo'
    else: 
        flash('Dados incorretos. Login ou senha inválidos', 'danger')
        flash('tente novamente', 'warning')
        return redirect(url_for('login'))


    

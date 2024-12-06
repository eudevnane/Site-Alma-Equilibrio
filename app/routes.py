from app import app #Está importando o objeto app do módulo app. Representa a aplicação.
from flask import render_template #Está importando a função para carregar e renderizar arquivos html.

@app.route('/') #Essa linha cria uma rota, uma url onde a página está acessível.
def home(): #Define uma função chamada ()home. Será executada quando o usuário acessar a página inicial.
    return render_template('home.html') #Diz ao flask para renderizar o arquivo home.html e enviar ao navegador do usuário. 
 
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
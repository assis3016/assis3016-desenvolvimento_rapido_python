#arrum ei o código from flask import Flask para from markupsafe import Markup


from flask import Flask
from markupsafe import Markup  # <- import correto

app = Flask(__name__)

@app.route('/')
def index():
    return Markup("Olá, seja bem-vindo! <br><a href='/resposta'>Clique aqui</a> para continuar.")

@app.route('/resposta')
def resposta():
    return "Você clicou no botão! 🎉"

if __name__ == '__main__':
    app.run(debug=False, port=5002)


   # * Running on http://127.0.0.1:5002

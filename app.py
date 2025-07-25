from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Flask com HTML Embutido</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>{{ message }}</h1>
    <form action="/resposta" method="POST">
        <button type="submit">Clique aqui</button>
    </form>
    
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, message="Olá, seja bem-vindo!")

@app.route('/resposta', methods=['POST'])
def resposta():
    return render_template_string(HTML_TEMPLATE, message="Você clicou no botão! 🎉")

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/       #esse é o link do flask


dados = [
    {"Nome": "Ana", "Idade": 28, "Cidade": "SC"},
    {"Nome": "Bruno", "Idade": 34, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 22, "Cidade": "Belo Horizonte"},
]

for pessoa in dados:
    print(f"{pessoa['Nome']} tem {pessoa['Idade']} anos e mora em {pessoa['Cidade']}.")

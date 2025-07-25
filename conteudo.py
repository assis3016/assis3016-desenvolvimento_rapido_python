  import os

# Verifica se o arquivo existe
try:
    if not os.path.exists('dados.txt'):
        # Cria o arquivo com conteúdo inicial
        with open('dados.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write("Este é o conteúdo do arquivo dados.txt.\n")

    # Agora abre o arquivo para leitura 
    with open('dados.txt', 'r', encoding='utf-8') as arquivo:
        conteúdo = arquivo.read()

    print("Tipo de conteúdo:", type(conteúdo))
    print("Conteúdo retornado pelo read:")
    print(repr(conteúdo))
except OSError as e:
    print(f"Erro ao manipular o arquivo: {e}")





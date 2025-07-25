import os

arquivo = open('de_manha_mais_energia.txt', 'w', encoding='utf-8')
print("nome do arquivo:", arquivo.name)
print("tipo de arquivo:", arquivo.mode)
print("o arquivo está fechado:", arquivo.closed)

arquivo.write("a minha vida eu preciso mudar todo dia pra escapar da rotina do meu desejo por seus beijo.\n")

arquivo.close()
print("o arquivo está fechado?", arquivo.closed)

abspath = os.path.abspath('de_manha_mais_energia.txt')
relpath = os.path.relpath('de_manha_mais_energia.txt')

print("caminho absoluto:", abspath)

print("caminho relativo:", relpath)
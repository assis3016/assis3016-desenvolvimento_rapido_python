import os

#Abrindo o arquivo no modo escrita

with open('exemplo.txt', 'w', encoding='utf-8') as arquivo:
	#exibindo os atributos do arquivo
	print("nome do arquivo:", arquivo.name)
	print("tipo do arquivo:", arquivo.mode)
	print("arquivo está fechado:", arquivo.closed)

	#escrevendo no arquivo
arquivo.write("eu vivo sempre no mundo da lua, porque sou equilibrista, meu dialogo é futurista eu sou sempre lunatico, eu vivo sempre no mundo da lua, quem quiser brincar com a gente, venha que será um barato, pegar carona.\n")
    
arquivo.close()
#verificando de o arquivo está fechado
print("arquivo está fechando agora?", arquivo.closed)


#exibindo caminhos relativos e absolutos

relpath = os.path.relpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')


#exibindo caminho  do arquivo

print("caminho relativo:", relpath)
print("caminho absoluto:", abspath)
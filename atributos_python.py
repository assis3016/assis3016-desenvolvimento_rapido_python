import os
import shutil
print(os.getcwd())

with open("meuarquivo_assis.txt", "w") as arquivo:
    arquivo.write("Este é um novo arquivo de texto.\n")


print(os.path.abspath('meuarquivo_assis.txt'))
# Define "arquivo" as an example file object
arquivo = open("meuarquivo_assis.txt", "w")
print(arquivo.name)
print(arquivo.mode)
arquivo.close()

print(arquivo.closed)

arquivo.close()
#verificando de o arquivo está fechado
print("arquivo está fechando agora?", arquivo.closed)
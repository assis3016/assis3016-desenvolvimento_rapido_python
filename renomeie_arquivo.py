import os

# Use absolute paths to avoid issues if the script is run from a different directory
nome_antigo = os.path.abspath("arquivo_antigo.txt")
nome_novo = os.path.abspath("arquivo_novo.txt")

if os.path.exists(nome_antigo):

	try:
		os.rename(nome_antigo, nome_novo)
		print(f"o arquivo antigo {nome_antigo} foi renomeado {nome_novo}.")
	except Exception as e:
		print(f"ocorreu um erro ao renomear o arquivo: {e}.")
else:
	print(f"o {nome_antigo} não foi encontrado.")	

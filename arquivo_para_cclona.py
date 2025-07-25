import matplotlib
matplotlib.use('Agg')  # Usa backend que não precisa de janela ou fontes do sistema

import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
try:
	df = pd.read_csv('dados.csv')
except FileNotFoundError:
	print("Erro: O arquivo 'dados.csv' não foi encontrado.")
	exit()

# Mostra as 5 primeiras linhas
print("Primeiras linhas do DataFrame:")
print(df.head())

# Informações gerais
print("\nInformações do DataFrame:")
print(df.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Contagem por categoria (coluna 'Categoria')
if 'Categoria' in df.columns:
	print("\nContagem por categoria:")
	print(df['Categoria'].value_counts())

	# Gera o gráfico e salva como imagem
	df['Categoria'].value_counts().plot(kind='bar', title='Contagem por Categoria')
	plt.xlabel('Categoria')
	plt.ylabel('Contagem')
	plt.tight_layout()

if 'Categoria' in df.columns:
	print("\nGráfico salvo como 'grafico.png'")
	plt.savefig('grafico.png')
else:
	print("\nNenhum gráfico foi gerado devido à ausência da coluna 'Categoria'.")

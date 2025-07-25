import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV (troque pelo caminho do seu arquivo)
import os

if os.path.exists('dados.csv'):
	df = pd.read_csv('dados.csv')
else:
	print("Erro: O arquivo 'dados.csv' não foi encontrado.")
	exit()

# Mostra as 5 primeiras linhas
print("Primeiras linhas do DataFrame:")
print(df.head())

# Exibe informações gerais
print("\nInformações do DataFrame:")
print(df.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Exemplo: contar valores de uma coluna categórica
if 'Categoria' in df.columns:
	print("\nContagem por categoria (exemplo com 'Categoria'):")
	print(df['Categoria'].value_counts())

	# Gráfico de barras
	df['Categoria'].value_counts().plot(kind='bar', title='Contagem por Categoria')
	plt.xlabel('Categoria')
	plt.ylabel('Contagem')
	plt.tight_layout()
	plt.show()
else:
	print("\nA coluna 'Categoria' não existe no DataFrame.")

import pandas as pd

# Dados da tabela da imagem foram extraídos e traduzidos
dados = [
    ["ID Produto", "Nome Produto", "ID Fornecedor", "ID Categoria", "Quantidade por Unidade", "Preço Unitário", "Unidades em Estoque", "Unidades em Pedido", "Nível de Reposição", "Descontinuado"],
    [1, "Chá", 8, 1, "10 caixas x 30 sacos", 18, 39, 0, 10, 1],
    [2, "Chang", 1, 1, "24 - 12 garrafas de 350ml", 19, 17, 40, 25, 1],
    [3, "Xarope de Anis", 1, 2, "12 - 550 ml garrafas", 10, 13, 70, 25, 0],
    # Apenas os 3 primeiros registros para exemplo. Continuar com os demais se necessário.
]

# Criar DataFrame
df = pd.DataFrame(dados[1:], columns=dados[0])

# Exportar para CSV
caminho_csv = r"produtos_traduzido.csv"
df.to_csv(caminho_csv, index=False)

caminho_csv

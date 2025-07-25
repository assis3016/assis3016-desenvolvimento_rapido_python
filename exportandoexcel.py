import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conexao = sqlite3.connect("meu_db.db")

# Ler dados da tabela Pessoa para um DataFrame
df = pd.read_sql_query("SELECT * FROM Pessoa", conexao)

# Exportar para Excel
df.to_excel("dados_exportados.xlsx", index=False)

# Fechar conexão
conexao.close()

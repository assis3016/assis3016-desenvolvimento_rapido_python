import sqlite3 as conector

#abertura de conexao

conexao = conector.connect("meu_banco.db")  # Use o nome do arquivo do banco de dados SQLite

#aquisição de um cursor

cursor = conexao.cursor()

#execução de comandos: SELECT..CREATE...

cursor.execute("CREATE TABLE IF NOT EXISTS exemplo (id INTEGER PRIMARY KEY, nome TEXT)")  # Exemplo de comando SQL válido
cursor.fetchall()


# Efetivaçao do comando
conexao.commit()

#Efetivação das conexões
cursor.close()
conexao.close()
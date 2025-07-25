import sqlite3
from datetime import datetime

# Conversor para BOOLEAN
def conv_bool(dado):
    return True if dado == 1 else False

# Conversor para DATE
def conv_date(dado):
    # dado vem como bytes, ex: b'2012-05-11'
    return datetime.strptime(dado.decode(), "%Y-%m-%d").date()

# Registrar conversores antes de conectar
sqlite3.register_converter("BOOLEAN", conv_bool)
sqlite3.register_converter("DATE", conv_date)

# Criar conexão com parse types ativado
conexao = sqlite3.connect("meu_db.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cursor = conexao.cursor()

# Criar tabela (apaga se já existir)
cursor.execute("DROP TABLE IF EXISTS Pessoa;")
cursor.execute("""
CREATE TABLE Pessoa (
    cpf INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    oculos BOOLEAN NOT NULL
);
""")

# Inserir dados
cursor.execute("""
INSERT INTO Pessoa (cpf, nome, data_nascimento, oculos) VALUES (?, ?, ?, ?)
""", (123459654, 'Carlos', '2012-05-11', 0))

conexao.commit()

# Consultar dados e mostrar tipos
cursor.execute("SELECT * FROM Pessoa")
registros = cursor.fetchall()

for registro in registros:
    print("Registro:", registro)
    print("cpf:", type(registro[0]), registro[0])
    print("nome:", type(registro[1]), registro[1])
    print("nascimento:", type(registro[2]), registro[2])
    print("usa_oculos:", type(registro[3]), registro[3])
    print('---')

cursor.close()
conexao.close()

import sqlite3 as conector
from modelo import Pessoa

# Conexão com o banco
conexao = conector.connect("meu_db.db", detect_types=conector.PARSE_DECLTYPES | conector.PARSE_COLNAMES)
cursor = conexao.cursor()

# Função conversora de boolean
def conv_bool(dado):
    return True if dado == 1 else False

# Registro do conversor
conector.register_converter("BOOLEAN", conv_bool)

# Tenta adicionar a coluna 'profissao' se não existir
try:
    cursor.execute("ALTER TABLE Pessoa ADD COLUMN profissao TEXT;")
    print("Coluna 'profissao' adicionada.")
except conector.OperationalError as e:
    if "duplicate column name" in str(e).lower():
        print("Coluna 'profissao' já existe.")
    else:
        raise

# Atualiza os valores da coluna 'profissao' (só onde estiver NULL)
cursor.execute("UPDATE Pessoa SET profissao = 'Desconhecida' WHERE profissao IS NULL;")
conexao.commit()

# SELECT com filtro
comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
cursor.execute(comando, {"usa_oculos": True})

# Pega os registros
registros = cursor.fetchall()

# Processa os dados
for registro in registros:
    pessoa = Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)
    print("profissao:", type(pessoa.profissao), pessoa.profissao)

# Fecha a conexão
cursor.close()
conexao.close()

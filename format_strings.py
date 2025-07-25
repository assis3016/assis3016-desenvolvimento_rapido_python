'''

#
# Exemplo de método de formatação de string

# ------------------------------------------------------
# Formatação de Strings com .format()
mensagem1 = "Olá, sou {}, tenho {} anos e {} meses.".format("Lucas", 40, 7)
print(mensagem1)

# Encerra o programa aqui
exit()
'''
# ------------------------------------------------------
# O código abaixo não será executado por causa do exit()

# Formatação de Strings com .format() usando variáveis
nome = "Jorge"
idade = 21
meses = 6

mensagem2 = "Olá, meu nome é {}, eu tenho {} anos e {} meses.".format(nome, idade, meses)
print(mensagem2)

exit()

# F-Strings
mensagem3 = f"Olá, meu nome é {nome}, eu tenho {idade} anos e {meses} meses."
print(mensagem3)

# Precisão numérica com .format()
valor = 3.14159
print("Pi com duas casas decimais: {:.2f}".format(valor))

# Precisão numérica com F-String
print(f"Pi com duas casas decimais: {valor:.2f}")

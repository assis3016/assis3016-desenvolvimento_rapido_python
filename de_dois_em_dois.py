'''
def contar_de_dois_em_dois():
    """
    imprime números de 2 a 100, aumentando 2 a cada vez.
    """
    n = 2
    while n <= 100:
        print(n)
        n += 2

if __name__ == "__main__":
    # Chama a função para contar de 2 em 2.
    contar_de_dois_em_dois()
    

   '''
'''
def contar_de_dois_em_dois():
    n = 2
    while n <= 100:
        print(n)
        n += 2

if __name__ == "__main__":


    contar_de_dois_em_dois()

'''
'''
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)

# Teste
print(contar_vogais("Python é divertido"))  # Deve imprimir 6

'''
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)

if __name__ == "__main__":
    print(contar_vogais("Online C++ Compiler "
                        "Code, Compile, Run and Debug C++ program online. "
                        "Write your code in this editor and press 'Run' b"))


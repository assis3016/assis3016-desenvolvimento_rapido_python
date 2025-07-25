def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
print(f"O fatorial de 5 é: {fatorial(5)}")

# Corrige a função fatorial duplicada e remove redundâncias
def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Solicita ao usuário um número inteiro
n = int(input("Digite um número inteiro para calcular o fatorial: "))

# Exibe o resultado
print(f"O fatorial de {n} é: {fatorial(n)}")


def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Solicita ao usuário um número inteiro
n = int(input("Digite um número inteiro para calcular o fatorial: "))

# Exibe o resultado
print(f"O fatorial de {n} é: {fatorial(n)}")

def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado = fatorial * i
    return resultado

n = int(input("digite um número inteiro para calcular o fatorial: "))

import matplotlib.pyplot as plt

def plotar_grafico(dados):
    """Plota um gráfico simples com os dados fornecidos."""
    plt.plot(dados)
    plt.title("Gráfico de Dados")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.show()

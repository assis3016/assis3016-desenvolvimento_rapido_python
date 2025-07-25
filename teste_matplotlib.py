import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot([1, 2, 3], [4, 5, 6], label="Linha de Teste")
plt.legend()
plt.title("Gráfico de Teste")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.show()

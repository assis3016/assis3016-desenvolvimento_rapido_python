import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Minha Janela")
root.geometry("300x150")

# Função chamada ao clicar no botão
def clique():
    print("Você clicou no botão!")

# Botão "Clique aqui"
botao_clique = tk.Button(root, text="Clique aqui", command=clique)
botao_clique.pack(pady=10)

# Botão "Quit" que fecha a janela
botao_sair = tk.Button(root, text="Quit", command=root.quit)
botao_sair.pack(pady=10)

# Mantém a janela rodando
root.mainloop()

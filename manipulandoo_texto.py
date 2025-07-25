def main():
    print("Escolha uma opção:")
    print("1. Criar novo arquivo (sobrescreve)")
    print("2. Adicionar nova frase ao arquivo")

    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        print("Digite seu texto. Digite 'sair' sozinho em uma linha para terminar.")
        linhas = []
        while True:
            linha = input()
            if linha.strip().lower() == "sair":
                break
            linhas.append(linha)
        with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("\n".join(linhas))
        print("Arquivo criado com sucesso.")

    elif opcao == "2":
        print("Digite a nova frase. Digite 'sair' sozinho em uma linha para terminar.")
        linhas = []
        while True:
            linha = input()
            if linha.strip().lower() == "sair":
                break
            linhas.append(linha)
        with open("meu_arquivo.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write("\n".join(linhas) + "\n")
        print("Frase(s) adicionada(s) com sucesso.")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()

#verificando se o arquivo está fechado não é necessário, pois o 'with' já fecha automaticamente.2 estou aqui de novo

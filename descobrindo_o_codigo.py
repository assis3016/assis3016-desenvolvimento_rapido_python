def aplicar_zenit_polar(texto):
    # Mapeamento ZENIT <-> POLAR
    zenit = "zenitZENIT"
    polar = "polarPOLAR"

    # Gera dicionário bidirecional
    tabela = str.maketrans(zenit + polar, polar + zenit)

    # Substituição direta
    return texto.translate(tabela)

def main():
    while True:
        print("\nDigite uma frase codificada ou original (ou 'sair' para encerrar):")
        frase = input("> ")

        if frase.lower() == "sair":
            break

        resultado = aplicar_zenit_polar(frase)
        print("Resultado:", resultado)

if __name__ == "__main__":
    main()

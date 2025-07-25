def aplicar_zenit_polar(texto):
    # Letras da cifra ZENIT ↔ POLAR
    zenit = "zenitZENIT"
    polar = "polarPOLAR"
    
    # Tradução bidirecional
    tabela = str.maketrans(zenit + polar, polar + zenit)
    
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

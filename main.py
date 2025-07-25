import os
import sys

# Adiciona a pasta 'utilidades' no caminho de importação
sys.path.append(os.path.join(os.path.dirname(__file__), 'utilidades'))

from contador import contar_vogais

frases = [
    "Python é maravilhoso",
    "Vamos contar as vogais",
    "12345!?",
    "",
]

for frase in frases:
    print(f'"{frase}" → {contar_vogais(frase)} vogais')

    main.py
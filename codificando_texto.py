import os

def zenit_polar_replace(text):
	# Aplicará a codificação Z-E-N-I-T P-O-L-A-R utilizando o método replace
	replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
					('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
	for old, new in replacements:
		text = text.replace(old, new)
	return text

def main():

#entrada da frase de aplicação  da codificação

	phrase = "the quick brown fox jumps over the lazy dog"
	phrase_title = phrase.title()#a primeira letra de cada palavra em maiuscula
def main():
	# entrada da frase de aplicação da codificação
	phrase = "the quick brown fox jumps over the lazy dog"
	phrase_title = phrase.title()  # a primeira letra de cada palavra em maiúscula

	# dividir a frase em palavras
	words = phrase_title.split()

	# processar cada palavra na lista usando ZENIT POLAR
	coded_words = [zenit_polar_replace(word) for word in words]

	# Juntar todas palavras codificadas em uma frase
	coded_phrase = " ".join(coded_words)
	print("original:", phrase)
	print("title: ", phrase_title)
	print("coded:", coded_phrase)
if __name__ == "__main__":
	main()
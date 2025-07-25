from PIL import Image
import numpy as np

def main():
	# Carregar a imagem original
	try:
		img = Image.open("inserir_imagem_no_python.jpg")
	except FileNotFoundError:
		print("Erro: O arquivo 'inserir_imagem_no_python.jpg' não foi encontrado.")
		return

	# Converter a imagem em dados binários
	img_data = np.array(img)
	binary_data = img_data.tobytes()

	print("\n", img_data.shape, "\n")

	# Salvar os dados binários em um arquivo
	with open("original_img.bin", "wb") as file:
		file.write(binary_data)

if __name__ == "__main__":
	main()
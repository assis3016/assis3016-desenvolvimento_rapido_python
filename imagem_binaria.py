import cv2

# 1. Carregar a imagem original (em escala de cinza)
imagem_cinza = cv2.imread(r'repositorio_imagem\IMG-20230922-WA0014.jpg', cv2.IMREAD_GRAYSCALE)  # Certifique-se de que o arquivo 'raqqqel.png' existe no diretório correto

# Verificar se a imagem foi carregada corretamente
if imagem_cinza is None:
	raise FileNotFoundError(r"repositorio_imagem\\666ac145-a811-4295-80d1-72f57b053146.jpeg não foi encontrada ou não pôde ser carregada.")

# 2. Aplicar limiar (threshold) para binarizar
_, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# 3. Salvar ou exibir o resultado
cv2.imwrite(r'repositorio_imagem\IMG-20230922-WA0014.jpg', imagem_binaria)  # Salva a imagem binária
cv2.imshow('Binária', imagem_binaria)              # Mostra na tela
cv2.waitKey(0)
cv2.destroyAllWindows()

# Removido porque 'arquivo' não foi definido

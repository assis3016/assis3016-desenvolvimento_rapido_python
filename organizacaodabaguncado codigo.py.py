import os
import shutil

EXTENSOES_DESTINO = {
    ".png": "png",
    ".dll": "dll",
    ".svg": "svg",
    ".mp4": "mp4",
    ".avi": "videos",
    ".ts": "ts",
    "md": "markdown",
    ".json": "json",
    ".txt": "textos",
    ".docx": "documentos",
    ".doc": "documentos",
    ".xls": "documentos",
    ".xlsx": "documentos",
    ".jpg": "jpg",
    ".php": "php",
    
}

def mover_arquivos(diretorio_base):
    for pasta_atual, _, arquivos in os.walk(diretorio_base):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_atual, arquivo)

            if os.path.isfile(caminho_arquivo):
                extensao = os.path.splitext(arquivo)[1].lower()

                if extensao in EXTENSOES_DESTINO:
                    nome_pasta = EXTENSOES_DESTINO[extensao]
                    pasta_destino = os.path.join(diretorio_base, nome_pasta)

                    # Criar pasta de destino se não existir
                    os.makedirs(pasta_destino, exist_ok=True)

                    try:
                        destino_final = os.path.join(pasta_destino, arquivo)

                        # Evita mover se já estiver na pasta correta
                        if os.path.abspath(pasta_atual) != os.path.abspath(pasta_destino):
                            shutil.move(caminho_arquivo, destino_final)
                            print(f"✅ Movido: {arquivo} → {nome_pasta}")
                    except Exception as e:
                        print(f"❌ Erro ao mover {arquivo}: {e}")

def main():
    diretorio = r"D:\Users\assis\perdidos"
    mover_arquivos(diretorio)

if __name__ == "__main__":
    main()
